import React, { useEffect, useState } from 'react';
import { fetchPricingData } from '../services/api';

const Pricing = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    (async () => {
      const response = await fetchPricingData();
      setData(response);
    })();
  }, []);

  return (
    <div>
      <h1>Pricing</h1>
      <p>{data ? data.msg : 'Loading...'}</p>
    </div>
  );
};

export default Pricing;
