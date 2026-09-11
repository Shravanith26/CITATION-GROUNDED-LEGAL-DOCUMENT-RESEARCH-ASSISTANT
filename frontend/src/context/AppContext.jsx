import React, { createContext, useContext, useState, useEffect } from 'react';
import { apiService } from '../services/api';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [activeTab, setActiveTab] = useState('chat'); // 'chat' | 'documents' | 'source'
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [answerData, setAnswerData] = useState(null);
  const [queryHistory, setQueryHistory] = useState([
    'What factors are considered while granting anticipatory bail?',
    'What did the Supreme Court hold in Sushila Aggarwal regarding bail duration?',
    'What guidelines were issued regarding arrest in Arnesh Kumar?'
  ]);
  const [activeCitation, setActiveCitation] = useState(null);
  const [inspectedChunk, setInspectedChunk] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(null);

  const loadDocuments = async (filters = {}) => {
    try {
      const data = await apiService.fetchDocuments(filters);
      setDocuments(data);
    } catch (err) {
      console.error('Error fetching documents:', err);
    }
  };

  useEffect(() => {
    loadDocuments();
  }, []);

  const handleQuerySubmit = async (queryText) => {
    const textToSubmit = queryText || query;
    if (!textToSubmit.trim()) return;

    setLoading(true);
    setError(null);
    try {
      const result = await apiService.submitQuery(textToSubmit);
      setAnswerData(result);
      if (!queryHistory.includes(textToSubmit)) {
        setQueryHistory((prev) => [textToSubmit, ...prev.slice(0, 19)]);
      }
      if (result.citations && result.citations.length > 0) {
        inspectCitation(result.citations[0]);
      }
    } catch (err) {
      setError(err.message || 'Error communicating with legal research backend');
    } finally {
      setLoading(false);
    }
  };

  const inspectCitation = async (citation) => {
    setActiveCitation(citation);
    if (citation?.chunk_id) {
      try {
        const chunk = await apiService.fetchChunkDetail(citation.chunk_id);
        setInspectedChunk(chunk);
      } catch (err) {
        setInspectedChunk({
          text: citation.snippet,
          document_title: citation.document,
          section_ref: citation.section,
        });
      }
    } else {
      setInspectedChunk({
        text: citation.snippet,
        document_title: citation.document,
        section_ref: citation.section,
      });
    }
  };

  return (
    <AppContext.Provider
      value={{
        activeTab,
        setActiveTab,
        query,
        setQuery,
        loading,
        error,
        answerData,
        queryHistory,
        activeCitation,
        inspectedChunk,
        documents,
        selectedDoc,
        setSelectedDoc,
        loadDocuments,
        handleQuerySubmit,
        inspectCitation,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => useContext(AppContext);
