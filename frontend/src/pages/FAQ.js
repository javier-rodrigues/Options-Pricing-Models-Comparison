import React from 'react';
import { Container, Accordion, Button } from 'react-bootstrap';

const CommonQuestions = () => {
  return (
    <Container className="py-5">
      <h2 className="text-center mb-4">Common Questions & Fixes</h2>
      <Accordion>
        <Accordion.Item eventKey="0">
          <Accordion.Header>What models are available for option pricing?</Accordion.Header>
          <Accordion.Body>
            The app supports Black-Scholes, Binomial, and Monte Carlo simulations. Select your preferred model in the settings panel.
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>How do I conduct an options screening?</Accordion.Header>
          <Accordion.Body>
            Use our advanced screener to filter options based on criteria like expiration dates, strike prices, and implied volatility.
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Is there a feature for real-time data updates?</Accordion.Header>
          <Accordion.Body>
            Yes! The app provides real-time data feeds for options markets to help you make informed decisions.
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      <div className="text-center mt-4">
        <Button variant="danger">Submit Bug Report</Button>
      </div>
    </Container>
  );
};

export default CommonQuestions;
