import React from 'react';
import { useApp } from '../../context/AppContext';
import { apiService } from '../../services/api';
import { FileText, Eye, Trash2 } from 'lucide-react';

export default function DocumentList({ documents, onRefresh }) {
  const { setSelectedDoc, setActiveTab } = useApp();

  const handleView = async (doc) => {
    try {
      const fullDoc = await apiService.fetchDocumentDetail(doc.id);
      setSelectedDoc(fullDoc);
      setActiveTab('source');
    } catch (err) {
      setSelectedDoc(doc);
      setActiveTab('source');
    }
  };

  const handleDelete = async (docId, e) => {
    e.stopPropagation();
    if (window.confirm('Are you sure you want to delete this document from the repository?')) {
      try {
        await apiService.deleteDocument(docId);
        if (onRefresh) onRefresh();
      } catch (err) {
        alert('Failed to delete document: ' + err.message);
      }
    }
  };

  if (!documents || documents.length === 0) {
    return (
      <div className="p-8 text-center text-slate-400 text-xs bg-slate-50 rounded-lg border border-dashed border-slate-200">
        No documents match the current filters.
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {documents.map((doc) => (
        <div
          key={doc.id}
          onClick={() => handleView(doc)}
          className="p-4 bg-white hover:bg-slate-50 border border-slate-200 rounded-xl cursor-pointer transition shadow-sm flex flex-col justify-between"
        >
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-200">
                {doc.doc_type}
              </span>
              <span className="text-xs text-slate-400 font-mono">
                {doc.total_chunks} chunks
              </span>
            </div>

            <h3 className="text-sm font-bold text-slate-900 line-clamp-2">
              {doc.title}
            </h3>

            <div className="text-xs text-slate-500 mt-2 space-y-0.5">
              {doc.court_authority && <div>Court: {doc.court_authority}</div>}
              {doc.citation_ref && <div>Citation: {doc.citation_ref}</div>}
              {doc.date && <div>Date: {doc.date}</div>}
            </div>
          </div>

          <div className="flex items-center justify-between pt-3 mt-3 border-t border-slate-100 text-xs">
            <span className="text-blue-600 font-medium flex items-center hover:underline">
              <Eye className="w-3.5 h-3.5 mr-1" />
              View full text
            </span>
            <button
              onClick={(e) => handleDelete(doc.id, e)}
              className="text-slate-400 hover:text-red-600 transition"
              title="Delete Document"
            >
              <Trash2 className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}
