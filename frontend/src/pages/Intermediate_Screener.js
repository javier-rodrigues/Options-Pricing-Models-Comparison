import React from "react";
import { Container, Button } from "react-bootstrap";
import { Link } from "react-router-dom";

const IntermediateScreener = () => {
  return (
    <Container className="text-center mt-5">
      <h1>Option Screener</h1>
      <div className="d-flex flex-column align-items-center mt-4">
        <Link to="/manual-screener">
          <Button variant="primary" className="m-2">Manual Screener</Button>
        </Link>
        <Link to="/browse-options">
          <Button variant="primary" className="m-2">Browse Options</Button>
        </Link>
      </div>
    </Container>
  );
};

export default IntermediateScreener;
