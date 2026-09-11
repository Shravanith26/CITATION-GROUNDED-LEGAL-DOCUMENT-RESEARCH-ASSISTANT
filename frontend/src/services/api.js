const API_BASE = '/api';

export const apiService = {
  async submitQuery(query, topK = 5, sessionId = 'default-session') {
    const response = await fetch(`${API_BASE}/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, top_k: topK, session_id: sessionId }),
    });
    if (!response.ok) {
      const err = await response.json().catch(() => ({ message: 'Query request failed' }));
      throw new Error(err.message || 'Error executing legal query');
    }
    return response.json();
  },

  async fetchDocuments(filters = {}) {
    const params = new URLSearchParams();
    if (filters.doc_type) params.append('doc_type', filters.doc_type);
    if (filters.court) params.append('court', filters.court);
    if (filters.search) params.append('search', filters.search);

    const response = await fetch(`${API_BASE}/documents?${params.toString()}`);
    if (!response.ok) throw new Error('Failed to fetch legal documents');
    return response.json();
  },

  async fetchDocumentDetail(docId) {
    const response = await fetch(`${API_BASE}/documents/${docId}`);
    if (!response.ok) throw new Error('Failed to fetch document detail');
    return response.json();
  },

  async deleteDocument(docId) {
    const response = await fetch(`${API_BASE}/documents/${docId}`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete document');
    return response.json();
  },

  async uploadDocument(formData) {
    const response = await fetch(`${API_BASE}/documents`, {
      method: 'POST',
      body: formData,
    });
    if (!response.ok) {
      const err = await response.json().catch(() => ({ message: 'Upload failed' }));
      throw new Error(err.message || 'Failed to upload document');
    }
    return response.json();
  },

  async fetchChunkDetail(chunkId) {
    const response = await fetch(`${API_BASE}/chunks/${chunkId}`);
    if (!response.ok) throw new Error('Failed to fetch passage detail');
    return response.json();
  },

  async fetchLogs(limit = 50) {
    const response = await fetch(`${API_BASE}/logs?limit=${limit}`);
    if (!response.ok) throw new Error('Failed to fetch audit logs');
    return response.json();
  }
};
