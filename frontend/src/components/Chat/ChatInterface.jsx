import React from 'react';
import QueryInput from './QueryInput';
import AnswerDisplay from './AnswerDisplay';

export default function ChatInterface() {
  return (
    <div className="flex flex-col space-y-6">
      <QueryInput />
      <AnswerDisplay />
    </div>
  );
}
