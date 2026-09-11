import React, { useState, useEffect } from 'react';
import { useApp } from '../../context/AppContext';
import DocumentSearch from './DocumentSearch';
import DocumentFilters from './DocumentFilters';
import DocumentList from './DocumentList';
import { apiService } from '../../services/api';
import { Upload, Plus, RefreshCw } from 'lucide-react';

export default function DocumentBrowser() {
  const { documents, loadDocuments } = useApp();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedType, setSelectedType] = useState('');
  const [uploading, setUploading] = useState(false);

  useEffect(() => {
    loadDocuments({ doc_type: selectedType, search: searchTerm });
  }, [selectedType, searchTerm]);

  const handleFileUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    formData.append('title', file.name.replace(/\.[^/.]+$/, ''));
    formData.append('doc_type', 'judgment');

    setUploading(true);
    try {
      await apiService.uploadDocument(formData);
      await loadDocuments();
      alert('Document uploaded and indexed successfully!');
    } catch (err) {
      alert('Upload failed: ' + err.message);
    } finally {
      setUploading(false);
      e.target.value = '';
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center pb-4 border-b border-slate-100 gap-3">
        <div>
          <h2 className="text-base font-bold text-slate-900">Legal Document Repository</h2>
          <p className="text-xs text-slate-500">Curated judgments, statutes, and acts supporting citation verification.</p>
        </div>

        <div className="flex items-center gap-2">
          <label className="inline-flex items-center px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-semibold cursor-pointer shadow-sm transition">
            <Upload className="w-3.5 h-3.5 mr-1.5" />
            {uploading ? 'Indexing...' : 'Upload Document'}
            <input
              type="file"
              accept=".txt,.pdf,.md"
              onChange={handleFileUpload}
              className="hidden"
              disabled={uploading}
            />
          </label>
          <button
            onClick={() => loadDocuments()}
            className="p-1.5 text-slate-400 hover:text-slate-700 border border-slate-200 rounded-lg hover:bg-slate-50 transition"
            title="Refresh repository"
          >
            <RefreshCw className="w-4 h-4" />
          </button>
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-3">
        <DocumentSearch searchTerm={searchTerm} onSearchChange={setSearchTerm} />
        <DocumentFilters selectedType={selectedType} onTypeChange={setSelectedType} />
      </div>

      <DocumentList documents={documents} onRefresh={() => loadDocuments()} />
    </div>
  );
}
