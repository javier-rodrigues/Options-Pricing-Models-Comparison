from django.http import JsonResponse
from rest_framework.decorators import api_view

# Import your testing functions
from app.pricing.testing.test_option_price import test_option_price
from app.pricing.testing.test_binomial_tree import test_binomial_tree
from app.pricing.testing.test_monte_carlo import test_monte_carlo
from app.analytics.testing.test_get_similar_historical_options import test_get_similar_historical_options
from app.analytics.testing.test_run_backtest import test_run_backtest
from app.analytics.testing.test_calculate_implied_volatility import test_calculate_implied_volatility
from app.data.testing.test_fetch_option_chain import test_fetch_option_chain
from app.data.fetch_risk_free_rate import fetch_risk_free_rate

@api_view(['GET'])
def test_black_scholes(request):
    try:
        test_option_price()
        return JsonResponse({"msg": "Black-Scholes function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Black-Scholes: {str(e)}"}, status=500)

@api_view(['GET'])
def test_binomial(request):
    try:
        test_binomial_tree()  # Utility function, does not handle `request`
        return JsonResponse({"msg": "Binomial Tree function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Binomial Tree: {str(e)}"}, status=500)


@api_view(['GET'])
def test_monte(request):
    try:
        test_monte_carlo()
        return JsonResponse({"msg": "Monte Carlo function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Monte Carlo: {str(e)}"}, status=500)

@api_view(['GET'])
def test_historical_options_screener(request):
    try:
        test_get_similar_historical_options()
        return JsonResponse({"msg": "Get Similar Historical Options function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Similar Historical Options: {str(e)}"}, status=500)

@api_view(['GET'])
def test_backtest(request):
    try:
        test_run_backtest()
        return JsonResponse({"msg": "Backtest function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Backtest: {str(e)}"}, status=500)

@api_view(['GET'])
def test_implied_volatility(request):
    try:
        test_calculate_implied_volatility()
        return JsonResponse({"msg": "Implied Volatility function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Implied Volatility: {str(e)}"}, status=500)

@api_view(['GET'])
def test_option_chain(request):
    try:
        test_fetch_option_chain()
        return JsonResponse({"msg": "Option Chain function ran successfully!"})
    except Exception as e:
        return JsonResponse({"msg": f"Error in Option Chain: {str(e)}"}, status=500)

