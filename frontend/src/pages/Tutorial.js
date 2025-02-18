import React from "react";
import { Container, Button } from "react-bootstrap";
import { Link } from "react-router-dom";

const Tutorial = () => {
  return (
    <Container className="text-center mt-5">
      <h1>Tutorial</h1>
      <div className="d-flex flex-column align-items-center mt-4">
        <Link to="/tutorial/screening">
          <Button variant="primary" className="m-2">Screening for Options</Button>
        </Link>
        <Link to="/tutorial/metrics">
          <Button variant="primary" className="m-2">Viewing Option Metrics</Button>
        </Link>
        <Link to="/tutorial/simulations">
          <Button variant="primary" className="m-2">Running Simulations</Button>
        </Link>
      </div>
    </Container>
  );
};

export default Tutorial;
