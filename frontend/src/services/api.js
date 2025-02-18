import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/';

export const fetchScreenerData = async () => {
    const response = await axios.get(`${API_BASE_URL}options/screener`);
    return response.data;
};

export const fetchPricingData = async (model, symbol) => {
    const response = await axios.get(`${API_BASE_URL}options/pricing`, {
        params: { model, symbol },
    });
    return response.data;
};

export const runBlackScholes = async () => {
    const response = await axios.get(`${API_BASE_URL}test_black_scholes`);
    return response.data;
};

export const runBinomialTree = async () => {
    const response = await axios.get(`${API_BASE_URL}test_binomial_tree`);
    return response.data;
};

export const runMonteCarlo = async () => {
    const response = await axios.get(`${API_BASE_URL}test_monte_carlo`);
    return response.data;
};

export const runBacktest = async () => {
    const response = await axios.get(`${API_BASE_URL}test_run_backtest`);
    return response.data;
};

export const runGetSimilarHistoricalOptions = async () => {
    const response = await axios.get(`${API_BASE_URL}test_similar_historical_options`);
    return response.data;
};

export const runImpliedVolatility = async () => {
    const response = await axios.get(`${API_BASE_URL}test_implied_volatility`);
    return response.data;
};

export const runOptionChain = async () => {
    const response = await axios.get(`${API_BASE_URL}test_option_chain`);
    return response.data;
};

export const runRiskFreeRate = async () => {
    const response = await axios.get(`${API_BASE_URL}test_risk_free_rate`);
    return response.data;
};

export const fetchSimilarHistoricalOptions = async (params) => {
  const response = await axios.post(`${API_BASE_URL}/get-similar-historical-options`, params);
  return response.data;
};

