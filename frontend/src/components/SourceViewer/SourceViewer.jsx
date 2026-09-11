import React from 'react';
import { useApp } from '../../context/AppContext';
import SourcePassage from './SourcePassage';
import { FileText, ArrowLeft, ExternalLink } from 'lucide-react';

export default function SourceViewer() {
  const { selectedDoc, setSelectedDoc, setActiveTab } = useApp();

  if (!selectedDoc) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center text-slate-400">
        <FileText className="w-10 h-10 mx-auto mb-2 text-slate-300" />
        <p className="text-sm">Select a legal document from the Document Library to view its complete text.</p>
        <button
          onClick={() => setActiveTab('documents')}
          className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg text-xs font-semibold hover:bg-blue-700 transition"
        >
          Browse Documents
        </button>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-4">
      <div className="flex items-center justify-between pb-4 border-b border-slate-100">
        <button
          onClick={() => setSelectedDoc(null)}
          className="inline-flex items-center text-xs font-medium text-slate-600 hover:text-blue-600 transition"
        >
          <ArrowLeft className="w-4 h-4 mr-1" />
          Back to List
        </button>
        <span className="text-xs px-2 py-0.5 rounded bg-slate-100 font-semibold text-slate-600 uppercase">
          {selectedDoc.doc_type}
        </span>
      </div>

      <div>
        <h2 className="text-lg font-bold text-slate-900">{selectedDoc.title}</h2>
        <div className="text-xs text-slate-500 mt-1 flex flex-wrap gap-x-4 gap-y-1">
          {selectedDoc.court_authority && <span>Authority: {selectedDoc.court_authority}</span>}
          {selectedDoc.citation_ref && <span>Citation: {selectedDoc.citation_ref}</span>}
          {selectedDoc.date && <span>Date: {selectedDoc.date}</span>}
          <span>Indexed Chunks: {selectedDoc.total_chunks}</span>
        </div>
      </div>

      <div>
        <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
          Full Document Text
        </h3>
        <SourcePassage text={selectedDoc.full_text || selectedDoc.content || 'Content not loaded'} />
      </div>
    </div>
  );
}
