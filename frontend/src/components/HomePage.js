import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Donations from './Donations';
import Users from './Users';
import Announcements from './Announcements';
import './HomePage.css';

function HomePage() {
  const [activeTab, setActiveTab] = useState('home'); // State for active tab

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };

  return (
    <Router> {/* Wrap with Router */}
      <div className="home-page">
        <div className="tabs">
          <Link
            to="/"
            className={`tab ${activeTab === 'home' ? 'active' : ''}`}
            onClick={() => handleTabClick('home')}
          >
            Home
          </Link>
          <Link
            to="/donations"
            className={`tab ${activeTab === 'donations' ? 'active' : ''}`}
            onClick={() => handleTabClick('donations')}
          >
            Donations
          </Link>
          <Link
            to="/users"
            className={`tab ${activeTab === 'users' ? 'active' : ''}`}
            onClick={() => handleTabClick('users')}
          >
            Users
          </Link>
          <Link
            to="/announcements"
            className={`tab ${activeTab === 'announcements' ? 'active' : ''}`}
            onClick={() => handleTabClick('announcements')}
          >
            Announcements
          </Link>
        </div>

        <Routes> {/* Use Routes instead of Switch */}
          <Route path="/donations" element={<Donations />} />
          <Route path="/users" element={<Users />} />
          <Route path="/announcements" element={<Announcements />} />
          <Route path="/" element={<h1>Welcome to the Community Hub!</h1>} /> {/* Home content */}
        </Routes>
      </div>
    </Router>
  );
}

export default HomePage;