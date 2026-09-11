import os
import glob
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.config.config import settings
from app.database.database import init_db, SessionLocal
from app.database.models import DocumentModel
from app.services.document_service import DocumentService
from app.utils.logging import setup_logger
from app.utils.error_handler import LegalAssistantException, global_exception_handler

# Import API routers
from app.api.documents import router as documents_router
from app.api.query import router as query_router
from app.api.chunks import router as chunks_router
from app.api.logs import router as logs_router

logger = setup_logger("app", "query.log")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event to initialize DB and auto-index legal corpus if empty."""
    logger.info("Initializing database tables...")
    init_db()

    # Check if raw documents should be indexed on startup
    db = SessionLocal()
    try:
        count = db.query(DocumentModel).count()
        if count == 0:
            logger.info("Database empty. Auto-ingesting legal documents from raw directory...")
            doc_service = DocumentService()
            raw_files = glob.glob(os.path.join(settings.RAW_DOCUMENTS_DIR, "*.*"))
            for fpath in raw_files:
                try:
                    doc_service.ingest_document_file(file_path=fpath, db=db)
                except Exception as e:
                    logger.error(f"Failed to auto-index {fpath}: {e}")
            logger.info("Initial legal corpus auto-indexing complete.")
        else:
            logger.info(f"Database ready with {count} indexed legal documents.")
    finally:
        db.close()

    yield
    logger.info("Shutting down application...")

app = FastAPI(
    title=settings.APP_NAME,
    description="Precision legal research assistant using Retrieval-Augmented Generation (RAG) with verifiable inline citations.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware for React frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount exception handlers
app.add_exception_handler(LegalAssistantException, global_exception_handler)

# Include API routes
app.include_router(query_router)
app.include_router(documents_router)
app.include_router(chunks_router)
app.include_router(logs_router)

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "embedding_model": settings.EMBEDDING_MODEL_NAME,
        "llm_model": settings.OLLAMA_MODEL
    }

# Interactive web dashboard served directly at root /
@app.get("/", response_class=HTMLResponse)
def root_dashboard():
    """Embedded interactive Single-Page Application interface for demo/evaluation."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Citation-Grounded Legal Document Research Assistant</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .citation-badge {
            background-color: #1e3a8a;
            color: #ffffff;
            font-size: 0.75rem;
            padding: 2px 6px;
            border-radius: 9999px;
            cursor: pointer;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            margin: 0 2px;
            transition: all 0.2s;
        }
        .citation-badge:hover {
            background-color: #2563eb;
            transform: translateY(-1px);
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col font-sans">
    <!-- Header -->
    <header class="bg-slate-900 border-b border-slate-800 text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-lg bg-blue-600 flex items-center justify-center text-white text-xl shadow">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight">LexisGrounded</h1>
                    <p class="text-xs text-slate-400">Citation-Grounded Legal Document Research Assistant (RAG)</p>
                </div>
            </div>
            <div class="flex items-center space-x-3">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-950 text-emerald-300 border border-emerald-800">
                    <i class="fa-solid fa-circle text-[8px] mr-1.5 text-emerald-400"></i> Zero Hallucination Mode
                </span>
                <a href="/docs" target="_blank" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-md border border-slate-700 transition">
                    <i class="fa-solid fa-book mr-1"></i> API Docs
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Left: Query & Answer Panel -->
        <div class="lg:col-span-8 flex flex-col space-y-6">
            <!-- Search / Query Box -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
                <label for="queryInput" class="block text-sm font-semibold text-slate-700 mb-2">
                    <i class="fa-solid fa-magnifying-glass mr-1.5 text-blue-600"></i> Ask a Legal Research Question
                </label>
                <div class="relative">
                    <textarea id="queryInput" rows="3" class="w-full rounded-lg border border-slate-300 p-3 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition shadow-inner" placeholder="e.g., What factors are considered while granting anticipatory bail?"></textarea>
                    <div class="flex justify-between items-center mt-3">
                        <div class="flex flex-wrap gap-2 text-xs text-slate-500">
                            <span>Sample queries:</span>
                            <button onclick="setQuery('What factors are considered while granting anticipatory bail?')" class="text-blue-600 hover:underline">Anticipatory Bail Grounds</button> •
                            <button onclick="setQuery('Can anticipatory bail be limited to a fixed time period till charge sheet is filed?')" class="text-blue-600 hover:underline">Duration of Bail</button> •
                            <button onclick="setQuery('What guidelines were issued regarding arrest in Arnesh Kumar?')" class="text-blue-600 hover:underline">Arrest Guidelines</button>
                        </div>
                        <button id="submitBtn" onclick="submitQuery()" class="inline-flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg shadow-sm transition">
                            <span>Analyze Context</span>
                            <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Answer Section -->
            <div id="answerCard" class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex-1 hidden">
                <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
                    <div class="flex items-center space-x-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
                        <h2 class="text-base font-semibold text-slate-800">Grounded Legal Synthesis</h2>
                    </div>
                    <div id="confidenceBadge" class="text-xs px-2.5 py-1 rounded-full font-medium bg-blue-50 text-blue-700 border border-blue-200">
                        Grounded
                    </div>
                </div>

                <div id="loadingIndicator" class="hidden py-8 text-center text-slate-500">
                    <i class="fa-solid fa-circle-notch fa-spin text-2xl text-blue-600 mb-2"></i>
                    <p class="text-sm">Retrieving verified precedents & generating citation-grounded answer...</p>
                </div>

                <div id="answerContent" class="prose max-w-none text-slate-700 text-sm leading-relaxed whitespace-pre-wrap"></div>

                <!-- Citations Bar -->
                <div id="citationsSection" class="mt-6 pt-4 border-t border-slate-100">
                    <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center">
                        <i class="fa-solid fa-link mr-1.5 text-blue-600"></i> Supporting Statutory & Judicial Citations
                    </h3>
                    <div id="citationsList" class="grid grid-cols-1 sm:grid-cols-2 gap-3"></div>
                </div>
            </div>
        </div>

        <!-- Right: Source Document & Passage Inspector -->
        <div class="lg:col-span-4 flex flex-col space-y-6">
            <!-- Inspection Panel -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 sticky top-6">
                <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-3">
                    <h2 class="text-sm font-semibold text-slate-800">
                        <i class="fa-solid fa-file-contract mr-1.5 text-blue-600"></i> Source Passage Inspector
                    </h2>
                    <span id="inspectBadge" class="text-[10px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">No Selection</span>
                </div>

                <div id="inspectorEmptyState" class="py-12 text-center text-slate-400 text-xs">
                    <i class="fa-solid fa-magnifying-glass-arrow-right text-3xl mb-2 text-slate-300"></i>
                    <p>Click on any citation badge <span class="bg-slate-200 text-slate-700 px-1 py-0.5 rounded font-bold">[1]</span> or source card to inspect the exact passage from the original legal document.</p>
                </div>

                <div id="inspectorContent" class="hidden space-y-3">
                    <div class="bg-slate-50 p-3 rounded-lg border border-slate-200 text-xs space-y-1">
                        <div><strong class="text-slate-700">Document:</strong> <span id="inspDocTitle" class="text-slate-900 font-medium"></span></div>
                        <div><strong class="text-slate-700">Reference:</strong> <span id="inspSecRef" class="text-blue-700 font-semibold"></span></div>
                        <div><strong class="text-slate-700">Relevance Score:</strong> <span id="inspScore" class="text-emerald-700 font-mono"></span></div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">Verifiable Passage Text:</label>
                        <div id="inspPassageText" class="p-3 bg-amber-50/60 border border-amber-200/80 rounded-lg text-xs leading-relaxed text-slate-800 max-h-64 overflow-y-auto font-serif"></div>
                    </div>
                </div>
            </div>

            <!-- Pre-loaded Legal Corpus -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
                <h3 class="text-sm font-semibold text-slate-800 mb-3 flex items-center">
                    <i class="fa-solid fa-landmark mr-1.5 text-blue-600"></i> Indexed Legal Repository
                </h3>
                <div id="corpusList" class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg border border-slate-100 bg-slate-50 hover:bg-slate-100 transition cursor-pointer" onclick="setQuery('What principles were laid down in Gurbaksh Singh Sibbia regarding anticipatory bail?')">
                        <div class="font-medium text-slate-800">Gurbaksh Singh Sibbia v. State of Punjab</div>
                        <div class="text-[11px] text-slate-500">(1980) 2 SCC 565 • Constitution Bench</div>
                    </div>
                    <div class="p-2.5 rounded-lg border border-slate-100 bg-slate-50 hover:bg-slate-100 transition cursor-pointer" onclick="setQuery('Can anticipatory bail be limited to a fixed time period according to Sushila Aggarwal?')">
                        <div class="font-medium text-slate-800">Sushila Aggarwal v. State (NCT of Delhi)</div>
                        <div class="text-[11px] text-slate-500">(2020) 5 SCC 1 • Duration & Charge sheet</div>
                    </div>
                    <div class="p-2.5 rounded-lg border border-slate-100 bg-slate-50 hover:bg-slate-100 transition cursor-pointer" onclick="setQuery('What directions were given in Arnesh Kumar for arrest under Section 498A?')">
                        <div class="font-medium text-slate-800">Arnesh Kumar v. State of Bihar</div>
                        <div class="text-[11px] text-slate-500">(2014) 8 SCC 273 • Arrest Guidelines</div>
                    </div>
                    <div class="p-2.5 rounded-lg border border-slate-100 bg-slate-50 hover:bg-slate-100 transition cursor-pointer" onclick="setQuery('What are the statutory grounds and conditions under Section 438 of CrPC?')">
                        <div class="font-medium text-slate-800">Section 438, Code of Criminal Procedure, 1973</div>
                        <div class="text-[11px] text-slate-500">Statutory Provision • Pre-arrest bail</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 py-3 text-center text-xs text-slate-500">
        Legal Document Research Assistant • Powered by RAG with Verifiable Citations • For Academic Evaluation & Research
    </footer>

    <script>
        let currentCitations = [];

        function setQuery(text) {
            document.getElementById('queryInput').value = text;
            submitQuery();
        }

        async function submitQuery() {
            const query = document.getElementById('queryInput').value.trim();
            if (!query) return;

            const card = document.getElementById('answerCard');
            const loading = document.getElementById('loadingIndicator');
            const content = document.getElementById('answerContent');
            const citationsList = document.getElementById('citationsList');
            const submitBtn = document.getElementById('submitBtn');

            card.classList.remove('hidden');
            loading.classList.remove('hidden');
            content.textContent = '';
            citationsList.innerHTML = '';
            submitBtn.disabled = true;

            try {
                const response = await fetch('/api/query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query, top_k: 5 })
                });
                const data = await response.json();

                loading.classList.add('hidden');
                submitBtn.disabled = false;

                // Format inline citations [1], [2] as interactive badges
                let formattedText = data.answer.replace(/\\[([0-9]+)\\]/g, (match, p1) => {
                    return `<span class="citation-badge" onclick="inspectCitation(${p1})">[${p1}]</span>`;
                });
                content.innerHTML = formattedText;

                // Update Confidence badge
                const badge = document.getElementById('confidenceBadge');
                if (data.confidence === 'grounded') {
                    badge.className = 'text-xs px-2.5 py-1 rounded-full font-medium bg-emerald-50 text-emerald-700 border border-emerald-200';
                    badge.innerHTML = '<i class="fa-solid fa-shield-check mr-1"></i> Fully Grounded';
                } else {
                    badge.className = 'text-xs px-2.5 py-1 rounded-full font-medium bg-amber-50 text-amber-700 border border-amber-200';
                    badge.innerHTML = '<i class="fa-solid fa-triangle-exclamation mr-1"></i> ' + data.confidence;
                }

                // Render Citations
                currentCitations = data.citations || [];
                if (currentCitations.length === 0) {
                    citationsList.innerHTML = '<div class="text-xs text-slate-400 col-span-2">No direct source passages cited for this query.</div>';
                } else {
                    citationsList.innerHTML = currentCitations.map(c => `
                        <div class="p-3 bg-slate-50 hover:bg-blue-50/50 border border-slate-200 rounded-lg cursor-pointer transition text-xs" onclick="inspectCitation(${c.marker_index})">
                            <div class="flex items-center justify-between mb-1">
                                <span class="font-bold text-blue-800">[${c.marker_index}] ${c.document}</span>
                                <span class="text-[10px] text-slate-500 font-semibold">${c.section || ''}</span>
                            </div>
                            <p class="text-slate-600 line-clamp-2 italic text-[11px] font-serif">"${c.snippet}"</p>
                        </div>
                    `).join('');
                    
                    // Auto inspect the first citation
                    if (currentCitations[0]) {
                        inspectCitation(currentCitations[0].marker_index);
                    }
                }
            } catch (err) {
                loading.classList.add('hidden');
                submitBtn.disabled = false;
                content.innerHTML = `<div class="p-3 bg-red-50 text-red-700 rounded border border-red-200 text-xs">Error submitting query: ${err.message}</div>`;
            }
        }

        async function inspectCitation(markerIndex) {
            const cit = currentCitations.find(c => c.marker_index === markerIndex);
            if (!cit) return;

            document.getElementById('inspectorEmptyState').classList.add('hidden');
            document.getElementById('inspectorContent').classList.remove('hidden');

            document.getElementById('inspectBadge').textContent = `Citation [${markerIndex}]`;
            document.getElementById('inspDocTitle').textContent = cit.document;
            document.getElementById('inspSecRef').textContent = cit.section || 'Paragraph';
            document.getElementById('inspScore').textContent = `${((cit.confidence_score || 1.0) * 100).toFixed(1)}% match`;

            // If chunk_id exists, fetch full chunk detail
            if (cit.chunk_id) {
                try {
                    const res = await fetch(`/api/chunks/${cit.chunk_id}`);
                    if (res.ok) {
                        const chunkData = await res.json();
                        document.getElementById('inspPassageText').textContent = chunkData.text;
                        return;
                    }
                } catch(e) {}
            }
            document.getElementById('inspPassageText').textContent = cit.snippet;
        }
    </script>
</body>
</html>
    """
