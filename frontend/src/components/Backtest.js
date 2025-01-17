import React, { useState } from 'react';
import { runBacktest } from '../services/api';

const Backtest = () => {
  const [data, setData] = useState(null);

  const handleBacktest = async () => {
    const response = await runBacktest({}); // Send an empty object for testing
    setData(response);
  };

  return (
    <div>
      <h1>Backtest</h1>
      <button onClick={handleBacktest}>Run Backtest</button>
      <p>{data ? data.msg : 'Click the button to run backtest.'}</p>
    </div>
  );
};

export default Backtest;
