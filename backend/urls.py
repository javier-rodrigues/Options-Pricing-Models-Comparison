"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (
    test_black_scholes,
    test_binomial,
    test_monte,
    test_historical_options_screener,
    test_backtest,
    test_implied_volatility,
    test_option_chain,
)

urlpatterns = [
    path('api/test_black_scholes', test_black_scholes, name='test_black_scholes'),
    path('api/test_binomial', test_binomial, name='test_binomial'),
    path('api/test_monte', test_monte, name='test_monte_carlo'),
    path('api/test_historical_options_screener', test_historical_options_screener, name='test_historical_options_screener'),
    path('api/test_backtest', test_backtest, name='test_backtest'),
    path('api/test_implied_volatility', test_implied_volatility, name='test_implied_volatility'),
    path('api/test_option_chain', test_option_chain, name='test_option_chain'),
]