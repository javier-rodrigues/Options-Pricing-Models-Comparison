import React, { useEffect, useState } from 'react';
import { fetchScreenerData } from '../services/api';

const Screener = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    (async () => {
      const response = await fetchScreenerData();
      setData(response);
    })();
  }, []);

  return (
    <div>
      <h1>Screener</h1>
      <p>{data ? data.msg : 'Loading...'}</p>
    </div>
  );
};

export default Screener;
