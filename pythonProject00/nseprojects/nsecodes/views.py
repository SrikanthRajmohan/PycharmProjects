from django.shortcuts import render

from django.shortcuts import render


def bhavcopy(request):
    date = "26/06/2023"  # Replace with the actual date
    stocks = [
        {"symbol": "AAPL", "open": 100, "high": 110, "low": 95, "close": 105},
        {"symbol": "GOOG", "open": 2000, "high": 2050, "low": 1980, "close": 2020},
        # Add more stocks here
    ]

    return render(request, 'bhavcopy.html', {'date': date, 'stocks': stocks})

# Create your views here.
