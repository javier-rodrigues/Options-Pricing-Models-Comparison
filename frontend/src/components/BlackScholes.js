import React, { useState } from "react";
import axios from "axios";

const BlackScholes = () => {
  const [output, setOutput] = useState("");

  const runBlackScholesTest = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/options/pricing",
        { params: { model: "black_scholes" } }
      );
      setOutput(response.data.msg);
    } catch (error) {
      setOutput("Error running Black-Scholes test: " + error.message);
    }
  };

  return (
    <div>
      <h2>Black-Scholes Model</h2>
      <button onClick={runBlackScholesTest}>Run Black-Scholes Test</button>
      <p>{output}</p>
    </div>
  );
};

export default BlackScholes;
