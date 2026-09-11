import React from 'react';
import { useApp } from '../../context/AppContext';
import { Search, ArrowRight, Loader2 } from 'lucide-react';

export default function QueryInput() {
  const { query, setQuery, loading, handleQuerySubmit } = useApp();

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleQuerySubmit();
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-4">
      <label htmlFor="legalQuery" className="block text-sm font-semibold text-slate-700 mb-2 flex items-center">
        <Search className="w-4 h-4 mr-2 text-blue-600" />
        Ask a Legal Research Question
      </label>
      <div className="relative">
        <textarea
          id="legalQuery"
          rows={3}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="e.g., What factors are considered while granting anticipatory bail under Section 438?"
          className="w-full rounded-lg border border-slate-300 p-3 text-sm focus:ring-2 focus:ring-blue-600 focus:border-blue-600 transition shadow-inner resize-none text-slate-800"
          disabled={loading}
        />
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mt-3 gap-2">
          <div className="flex flex-wrap gap-1.5 text-xs text-slate-500">
            <span className="font-medium">Quick Queries:</span>
            <button
              onClick={() => {
                setQuery('What factors are considered while granting anticipatory bail?');
                handleQuerySubmit('What factors are considered while granting anticipatory bail?');
              }}
              className="text-blue-600 hover:underline"
            >
              Anticipatory Bail
            </button>
            <span>•</span>
            <button
              onClick={() => {
                setQuery('What is the duration of anticipatory bail according to Sushila Aggarwal?');
                handleQuerySubmit('What is the duration of anticipatory bail according to Sushila Aggarwal?');
              }}
              className="text-blue-600 hover:underline"
            >
              Bail Duration
            </button>
            <span>•</span>
            <button
              onClick={() => {
                setQuery('What directions did the Supreme Court issue in Arnesh Kumar regarding arrest?');
                handleQuerySubmit('What directions did the Supreme Court issue in Arnesh Kumar regarding arrest?');
              }}
              className="text-blue-600 hover:underline"
            >
              Arrest Rules
            </button>
          </div>

          <button
            onClick={() => handleQuerySubmit()}
            disabled={loading || !query.trim()}
            className="inline-flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-slate-300 text-white text-xs font-semibold rounded-lg shadow-sm transition"
          >
            {loading ? (
              <>
                <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" />
                Analyzing...
              </>
            ) : (
              <>
                Analyze Context
                <ArrowRight className="w-3.5 h-3.5 ml-1.5" />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
