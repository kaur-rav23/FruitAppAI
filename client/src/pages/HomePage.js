import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Link to an external CSS file

function HomePage() {
  return (
    <div className="home-container">
      <div className="header">
        <h1>Fruit.AI</h1>
        <p>"Be Healthy!"</p>
      </div>
      <div className="services-grid">
        <Link to="/chatbot" className="service-item chatbot">
          <span>Chat.</span>
        </Link>
        <Link to="/translator" className="service-item translator">
          <span>Translator</span>
        </Link>
        <Link to="/faq" className="service-item faq">
          <span>FAQs</span>
        </Link>
        <Link to="/about" className="service-item about">
          <span>About</span>
        </Link>
      </div>
    </div>
  );
}

export default HomePage;
