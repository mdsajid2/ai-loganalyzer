import React from 'react';
import { createRoot } from 'react-dom/client'; // Updated import
import App from './App';

// Use the new React 18 API
const container = document.getElementById('root');
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);