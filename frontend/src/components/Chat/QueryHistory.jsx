import React from 'react';
import { useApp } from '../../context/AppContext';
import { History, ChevronRight } from 'lucide-react';

export default function QueryHistory() {
  const { queryHistory, setQuery, handleQuerySubmit } = useApp();

  if (!queryHistory || queryHistory.length === 0) return null;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-4">
      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center">
        <History className="w-3.5 h-3.5 mr-1.5 text-blue-600" />
        Recent Queries
      </h3>
      <div className="space-y-1.5">
        {queryHistory.map((q, idx) => (
          <button
            key={idx}
            onClick={() => {
              setQuery(q);
              handleQuerySubmit(q);
            }}
            className="w-full text-left p-2 rounded-lg hover:bg-slate-50 text-xs text-slate-700 flex items-center justify-between transition group"
          >
            <span className="truncate flex-1 pr-2">{q}</span>
            <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-blue-600 transition" />
          </button>
        ))}
      </div>
    </div>
  );
}
