import React, { useState } from 'react';
import BlackScholes from './BlackScholes';
import BinomialTree from './BinomialTree';
import MonteCarlo from './MonteCarlo';

const Pricing = () => {
   const [pricingModel, setPricingModel] = useState(''); // Tracks which pricing model is selected

   return (
      <div>
         <h2>Pricing</h2>
         <p>Select a pricing model:</p>

         {/* Buttons to select pricing models */}
         <button onClick={() => setPricingModel('black-scholes')}>Black-Scholes</button>
         <button onClick={() => setPricingModel('binomial-tree')}>Binomial Tree</button>
         <button onClick={() => setPricingModel('monte-carlo')}>Monte Carlo</button>

         {/* Render the selected pricing model's component */}
         <div>
            {pricingModel === 'black-scholes' && <BlackScholes />}
            {pricingModel === 'binomial-tree' && <BinomialTree />}
            {pricingModel === 'monte-carlo' && <MonteCarlo />}
         </div>
      </div>
   );
};

export default Pricing;
