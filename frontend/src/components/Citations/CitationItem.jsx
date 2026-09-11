import React from 'react';
import { useApp } from '../../context/AppContext';
import { BookOpen } from 'lucide-react';

export default function CitationItem({ citation }) {
  const { inspectCitation, activeCitation } = useApp();
  const isActive = activeCitation?.marker_index === citation.marker_index;

  return (
    <div
      onClick={() => inspectCitation(citation)}
      className={`p-3 rounded-lg border cursor-pointer transition text-xs flex flex-col justify-between ${
        isActive
          ? 'bg-blue-50 border-blue-400 shadow-sm'
          : 'bg-slate-50 hover:bg-slate-100 border-slate-200'
      }`}
    >
      <div className="flex items-center justify-between mb-1.5">
        <span className="font-bold text-blue-900 flex items-center">
          <span className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-blue-900 text-white font-bold text-[10px] mr-1.5">
            {citation.marker_index}
          </span>
          <span className="truncate max-w-[180px]">{citation.document}</span>
        </span>
        <span className="text-[10px] text-slate-500 font-semibold px-1.5 py-0.5 bg-slate-200/60 rounded">
          {citation.section || 'Passage'}
        </span>
      </div>
      <p className="text-slate-600 line-clamp-2 italic text-[11px] font-serif">
        "{citation.snippet}"
      </p>
      <div className="mt-2 flex items-center text-[10px] text-blue-600 font-medium">
        <BookOpen className="w-3 h-3 mr-1" />
        Inspect source passage
      </div>
    </div>
  );
}
