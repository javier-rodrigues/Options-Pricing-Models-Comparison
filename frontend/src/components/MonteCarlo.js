import React, { useState } from "react";
import axios from "axios";

const MonteCarlo = () => {
  const [output, setOutput] = useState("");

  const runMonteCarloTest = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/options/pricing",
        { params: { model: "monte_carlo" } }
      );
      setOutput(response.data.msg);
    } catch (error) {
      setOutput("Error running Monte Carlo test: " + error.message);
    }
  };

  return (
    <div>
      <h2>Monte Carlo Model</h2>
      <button onClick={runMonteCarloTest}>Run Monte Carlo Test</button>
      <p>{output}</p>
    </div>
  );
};

export default MonteCarlo;
