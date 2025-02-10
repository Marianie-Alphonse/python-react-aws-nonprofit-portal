import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App';
import reportWebVitals from './components/reportWebVitals';

// ReactDOM.createRoot
const root = ReactDOM.createRoot(document.getElementById('root'));

// ReactDOM.render
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Measuring performance in web applications
reportWebVitals();
