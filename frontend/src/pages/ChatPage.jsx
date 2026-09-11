import React from 'react';
import ChatInterface from '../components/Chat/ChatInterface';
import CitationPanel from '../components/Citations/CitationPanel';
import QueryHistory from '../components/Chat/QueryHistory';

export default function ChatPage() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
      {/* Left 8 columns: Query and Grounded Answer */}
      <div className="lg:col-span-8">
        <ChatInterface />
      </div>

      {/* Right 4 columns: Passage Inspector and History */}
      <div className="lg:col-span-4 space-y-6">
        <CitationPanel />
        <QueryHistory />
      </div>
    </div>
  );
}
