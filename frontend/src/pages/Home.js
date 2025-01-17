import React, { useState } from 'react';
import Screener from '../components/Screener';
import Pricing from '../components/Pricing';
import Backtest from '../components/Backtest';

const Home = () => {
  const [activeComponent, setActiveComponent] = useState(''); // Tracks which component to display

  return (
    <div>
      <h1>Welcome to the Options Pricing App</h1>
      <p>Select a feature:</p>
      
      {/* Buttons to select a feature */}
      <button onClick={() => setActiveComponent('screener')}>Screener</button>
      <button onClick={() => setActiveComponent('pricing')}>Pricing</button>
      <button onClick={() => setActiveComponent('backtest')}>Backtest</button>

      {/* Render the selected component */}
      <div>
        {activeComponent === 'screener' && <Screener />}
        {activeComponent === 'pricing' && <Pricing />}
        {activeComponent === 'backtest' && <Backtest />}
      </div>
    </div>
  );
};

export default Home;
