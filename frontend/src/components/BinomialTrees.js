import React, { useState } from "react";
import axios from "axios";

const BinomialTree = () => {
  const [output, setOutput] = useState("");

  const runBinomialTreeTest = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/options/pricing",
        { params: { model: "binomial_tree" } }
      );
      setOutput(response.data.msg);
    } catch (error) {
      setOutput("Error running Binomial Tree test: " + error.message);
    }
  };

  return (
    <div>
      <h2>Binomial Tree Model</h2>
      <button onClick={runBinomialTreeTest}>Run Binomial Tree Test</button>
      <p>{output}</p>
    </div>
  );
};

export default BinomialTree;
