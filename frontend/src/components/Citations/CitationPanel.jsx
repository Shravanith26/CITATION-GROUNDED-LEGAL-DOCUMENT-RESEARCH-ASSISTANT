import React from 'react';
import { useApp } from '../../context/AppContext';
import { FileText, ShieldAlert } from 'lucide-react';

export default function CitationPanel() {
  const { activeCitation, inspectedChunk } = useApp();

  if (!activeCitation) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 text-center text-slate-400 text-xs">
        <FileText className="w-8 h-8 mx-auto mb-2 text-slate-300" />
        <p>Click any citation badge [1] to inspect the source paragraph here.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 space-y-4">
      <div className="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 className="text-sm font-semibold text-slate-800 flex items-center">
          <FileText className="w-4 h-4 mr-2 text-blue-600" />
          Citation [{activeCitation.marker_index}]
        </h3>
        <span className="text-[11px] font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
          {activeCitation.confidence_score ? `${(activeCitation.confidence_score * 100).toFixed(0)}% relevance` : 'Verified'}
        </span>
      </div>

      <div className="bg-slate-50 p-3 rounded-lg border border-slate-100 text-xs space-y-1">
        <div><strong className="text-slate-600">Document:</strong> <span className="font-medium text-slate-900">{activeCitation.document}</span></div>
        <div><strong className="text-slate-600">Section/Para:</strong> <span className="font-semibold text-blue-700">{activeCitation.section}</span></div>
      </div>

      <div>
        <label className="block text-xs font-bold text-slate-700 mb-1">Full Source Passage:</label>
        <div className="p-3 bg-amber-50/50 border border-amber-200 rounded-lg text-xs leading-relaxed text-slate-800 max-h-60 overflow-y-auto font-serif">
          {inspectedChunk?.text || activeCitation.snippet}
        </div>
      </div>
    </div>
  );
}
