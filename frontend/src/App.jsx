import React from 'react';
import { useApp } from './context/AppContext';
import ChatPage from './pages/ChatPage';
import DocumentsPage from './pages/DocumentsPage';
import SourcePage from './pages/SourcePage';
import { Scale, BookOpen, FileText, ExternalLink, ShieldCheck } from 'lucide-react';

export default function App() {
  const { activeTab, setActiveTab } = useApp();

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans">
      {/* Header */}
      <header className="bg-slate-900 text-white shadow-md border-b border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center space-x-3">
            <div className="w-9 h-9 rounded-lg bg-blue-600 flex items-center justify-center text-white shadow">
              <Scale className="w-5 h-5" />
            </div>
            <div>
              <h1 className="text-base font-bold tracking-tight">LexisGrounded</h1>
              <p className="text-[11px] text-slate-400">Citation-Grounded Legal Document Research Assistant</p>
            </div>
          </div>

          {/* Tab Navigation */}
          <nav className="flex space-x-1 bg-slate-800 p-1 rounded-lg text-xs font-semibold">
            <button
              onClick={() => setActiveTab('chat')}
              className={`px-3 py-1.5 rounded-md transition flex items-center ${
                activeTab === 'chat'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'text-slate-300 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <Scale className="w-3.5 h-3.5 mr-1.5" />
              Research Assistant
            </button>
            <button
              onClick={() => setActiveTab('documents')}
              className={`px-3 py-1.5 rounded-md transition flex items-center ${
                activeTab === 'documents'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'text-slate-300 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5 mr-1.5" />
              Document Library
            </button>
            <button
              onClick={() => setActiveTab('source')}
              className={`px-3 py-1.5 rounded-md transition flex items-center ${
                activeTab === 'source'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'text-slate-300 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <FileText className="w-3.5 h-3.5 mr-1.5" />
              Source Viewer
            </button>
          </nav>

          <div className="flex items-center space-x-2 text-xs">
            <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-medium bg-emerald-950 text-emerald-300 border border-emerald-800">
              <ShieldCheck className="w-3 h-3 mr-1 text-emerald-400" />
              Grounded RAG
            </span>
            <a
              href="http://127.0.0.1:8000/docs"
              target="_blank"
              rel="noreferrer"
              className="text-slate-300 hover:text-white px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 border border-slate-700 transition flex items-center"
            >
              API Docs
              <ExternalLink className="w-3 h-3 ml-1" />
            </a>
          </div>
        </div>
      </header>

      {/* Main Content View */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full">
        {activeTab === 'chat' && <ChatPage />}
        {activeTab === 'documents' && <DocumentsPage />}
        {activeTab === 'source' && <SourcePage />}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-slate-200 py-3 text-center text-xs text-slate-500">
        Citation-Grounded Legal Document Research Assistant • College Project Evaluation • Verifiable Precedents & Bare Acts
      </footer>
    </div>
  );
}
