import React from 'react';
import { useApp } from '../../context/AppContext';
import { ShieldCheck, AlertTriangle, Clock, Cpu } from 'lucide-react';
import CitationList from '../Citations/CitationList';

export default function AnswerDisplay() {
  const { answerData, loading, inspectCitation } = useApp();

  if (loading) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center">
        <div className="inline-block animate-spin rounded-full h-8 w-8 border-4 border-blue-600 border-t-transparent mb-3"></div>
        <p className="text-sm font-medium text-slate-700">Retrieving authentic legal passages & generating grounded response...</p>
        <p className="text-xs text-slate-400 mt-1">Cross-referencing statutory provisions and Supreme Court precedents</p>
      </div>
    );
  }

  if (!answerData) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center text-slate-400">
        <p className="text-sm">Submit a question above to retrieve cited legal rulings and statutory provisions.</p>
      </div>
    );
  }

  const { answer, citations, confidence, model_used, latency_ms } = answerData;

  // Format text to highlight inline citations [1], [2]
  const renderFormattedAnswer = () => {
    const parts = answer.split(/(\[[0-9]+\])/g);
    return parts.map((part, index) => {
      const match = part.match(/^\[([0-9]+)\]$/);
      if (match) {
        const markerIdx = parseInt(match[1], 10);
        const cit = citations?.find((c) => c.marker_index === markerIdx);
        return (
          <button
            key={index}
            onClick={() => cit && inspectCitation(cit)}
            className="inline-flex items-center px-2 py-0.5 mx-1 text-xs font-bold rounded-full bg-blue-900 hover:bg-blue-700 text-white shadow-sm transition"
            title={cit ? `${cit.document} (${cit.section})` : 'Citation'}
          >
            [{markerIdx}]
          </button>
        );
      }
      return <span key={index}>{part}</span>;
    });
  };

  const isGrounded = confidence === 'grounded';

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col space-y-6">
      {/* Header Bar */}
      <div className="flex flex-wrap items-center justify-between pb-3 border-b border-slate-100 gap-2">
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
          <h2 className="text-base font-semibold text-slate-800">Citation-Grounded Answer</h2>
        </div>

        <div className="flex items-center space-x-3 text-xs">
          {latency_ms && (
            <span className="flex items-center text-slate-500">
              <Clock className="w-3.5 h-3.5 mr-1" />
              {latency_ms} ms
            </span>
          )}
          {model_used && (
            <span className="flex items-center text-slate-500">
              <Cpu className="w-3.5 h-3.5 mr-1" />
              {model_used}
            </span>
          )}
          <span
            className={`inline-flex items-center px-2.5 py-1 rounded-full font-medium ${
              isGrounded
                ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                : 'bg-amber-50 text-amber-700 border border-amber-200'
            }`}
          >
            {isGrounded ? (
              <>
                <ShieldCheck className="w-3.5 h-3.5 mr-1 text-emerald-600" />
                Fully Grounded
              </>
            ) : (
              <>
                <AlertTriangle className="w-3.5 h-3.5 mr-1 text-amber-600" />
                {confidence}
              </>
            )}
          </span>
        </div>
      </div>

      {/* Answer Body */}
      <div className="text-slate-800 text-sm leading-relaxed whitespace-pre-wrap font-sans">
        {renderFormattedAnswer()}
      </div>

      {/* Citations List Component */}
      <CitationList citations={citations} />
    </div>
  );
}
