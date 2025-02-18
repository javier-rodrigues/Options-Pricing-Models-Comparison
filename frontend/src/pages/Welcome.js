import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';

const Welcome = () => {
  return (
    <Container fluid className="text-center bg-dark text-light vh-100 d-flex align-items-center justify-content-center">
      <Row>
        <Col>
          <h1>Welcome to the Option Analysis Dashboard!</h1>
          <p>Click below to get started.</p>
          <Button variant="primary" className="mt-3" href="/how_to">
            How to Use
          </Button>
          <Button variant="secondary" className="mt-3 ms-3" href="/intermediate_screener">
            Enter Dashboard
          </Button>
        </Col>
      </Row>
    </Container>
  );
};

export default Welcome;
