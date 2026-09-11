import React from 'react';
import CitationItem from './CitationItem';
import { BookmarkCheck } from 'lucide-react';

export default function CitationList({ citations }) {
  if (!citations || citations.length === 0) return null;

  return (
    <div className="pt-4 border-t border-slate-100">
      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center">
        <BookmarkCheck className="w-3.5 h-3.5 mr-1.5 text-blue-600" />
        Supporting Legal Citations & Sources ({citations.length})
      </h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {citations.map((citation, index) => (
          <CitationItem key={index} citation={citation} />
        ))}
      </div>
    </div>
  );
}
