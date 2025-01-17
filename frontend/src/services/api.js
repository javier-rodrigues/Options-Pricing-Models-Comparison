import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const fetchScreenerData = async () => {
  const response = await axios.get(`${API_BASE_URL}/options/screener`);
  return response.data;
};

export const fetchPricingData = async (model, symbol) => {
  const response = await axios.get(`${API_BASE_URL}/options/pricing`, {
    params: { model, symbol },
  });
  return response.data;
};

export const runBacktest = async (backtestParams) => {
  const response = await axios.post(`${API_BASE_URL}/options/backtest`, backtestParams);
  return response.data;
};