import React from 'react';

export default function DocumentFilters({ selectedType, onTypeChange }) {
  const types = [
    { label: 'All Types', value: '' },
    { label: 'Judgments', value: 'judgment' },
    { label: 'Statutes & Acts', value: 'statute' },
  ];

  return (
    <div className="flex gap-2">
      {types.map((t) => (
        <button
          key={t.value}
          onClick={() => onTypeChange(t.value)}
          className={`px-3 py-1.5 text-xs font-semibold rounded-lg transition ${
            selectedType === t.value
              ? 'bg-blue-600 text-white'
              : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
          }`}
        >
          {t.label}
        </button>
      ))}
    </div>
  );
}
