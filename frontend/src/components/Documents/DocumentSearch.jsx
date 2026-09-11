import React from 'react';
import { Search } from 'lucide-react';

export default function DocumentSearch({ searchTerm, onSearchChange }) {
  return (
    <div className="relative flex-1">
      <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => onSearchChange(e.target.value)}
        placeholder="Filter by case name, act, or section..."
        className="w-full pl-9 pr-3 py-2 text-xs border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:border-blue-600 transition"
      />
    </div>
  );
}
