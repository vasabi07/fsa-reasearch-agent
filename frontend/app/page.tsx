"use client";
import React, { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (event:React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const result = await axios.post('http://localhost:8000/chat', { message });
      setResponse(result.data.message);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter your message"
        />
        <button type="submit">Send</button>
      </form>
      {response && <div className='p-2 bg-slate-800 text-white'>AI: {response}</div>}
    </div>
  );
}
