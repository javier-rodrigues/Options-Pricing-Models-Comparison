import React, { useState } from 'react';
import axios from 'axios';

// Main Home Component
const Home = () => {
  const [message, setMessage] = useState('');
  const [activeComponent, setActiveComponent] = useState('');
  const [showOtherOptions, setShowOtherOptions] = useState(false);

  // API Call Handlers
  const runBlackScholes = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_black_scholes');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Black-Scholes function');
    }
  };

  const runBinomialTree = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_binomial');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Binomial Tree function');
    }
  };

  const runMonteCarlo_CV = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_monte_carlo_control');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Monte Carlo Control Variate function');
    }
  };

  const runMonteCarlo_AV = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_monte_carlo_antithetic');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Monte Carlo Antithetic Variate function');
    }
  };

  const runGetSimilarHistoricalOptions = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_historical_options_screener');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Get Similar Historical Options');
    }
  };

  const runBacktest = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_backtest');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Backtest');
    }
  };

  const runCalculateImpliedVolatility = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_implied_volatility');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Implied Volatility');
    }
  };

  const runFetchOptionChain = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/test_option_chain');
      setMessage(response.data.msg);
    } catch (error) {
      setMessage('Error running Option Chain fetch');
    }
  };

  return (
    <div>
      <h1>Welcome to the Options Pricing App</h1>
      <p>Select a feature:</p>

      {/* Main Feature Buttons */}
      <button onClick={() => setActiveComponent('pricing')}>Pricing</button>
      <button onClick={runGetSimilarHistoricalOptions}>Run Get Similar Historical Options</button>
      <button onClick={runBacktest}>Run Backtest</button>
      <button onClick={() => setShowOtherOptions(!showOtherOptions)}>Other</button>

      {/* Pricing Sub-Options */}
      {activeComponent === 'pricing' && (
        <div>
          <button onClick={runBlackScholes}>Run Black-Scholes</button>
          <button onClick={runBinomialTree}>Run Binomial Tree</button>
          <button onClick={runMonteCarlo_CV}>Run Monte Carlo Control Variate</button>
          <button onClick={runMonteCarlo_AV}>Run Monte Carlo Antithetic Variate</button>
        </div>
      )}

      {/* Other Sub-Options */}
      {showOtherOptions && (
        <div>
          <button onClick={runCalculateImpliedVolatility}>Run Implied Volatility</button>
          <button onClick={runFetchOptionChain}>Run Option Chain Fetch</button>
        </div>
      )}

      {/* Display API Response Message */}
      <p>{message}</p>
    </div>
  );
};

export default Home;
