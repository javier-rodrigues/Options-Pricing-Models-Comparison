import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';

const HowToUse = () => {
  return (
    <Container className="py-5">
      <Row className="text-center mb-4">
        <Col>
          <h2>How to Use the Dashboard</h2>
          <p>Explore the options below to get started.</p>
        </Col>
      </Row>
      <Row>
        <Col md={6} className="mb-3">
          <Card>
            <Card.Body>
              <Card.Title>Tutorial</Card.Title>
              <Card.Text>Learn how to screen for options, view metrics, and run simulations.</Card.Text>
              <Button variant="primary" href="/tutorial">
                View Tutorial
              </Button>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6} className="mb-3">
          <Card>
            <Card.Body>
              <Card.Title>Common Questions & Fixes</Card.Title>
              <Card.Text>Find answers to frequently asked questions or report a bug.</Card.Text>
              <Button variant="secondary" href="/FAQ">
                View FAQ
              </Button>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default HowToUse;
