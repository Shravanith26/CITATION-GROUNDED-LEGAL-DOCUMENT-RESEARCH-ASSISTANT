import React from 'react';

export default function SourcePassage({ text, highlightTerm }) {
  if (!text) return null;

  return (
    <div className="p-4 bg-amber-50/70 border border-amber-200/90 rounded-lg text-xs leading-relaxed text-slate-900 font-serif whitespace-pre-wrap">
      {text}
    </div>
  );
}
