from django.shortcuts import render
from nsetools import Nse

from django.http import HttpResponse


def stock_list(request):
    # nse = Nse()
    # top_50 = nse.get_top_gainers()[:50]  # Get top 50 gainers from nsetools
    #
    # context = {
    #     'stocks': top_50
    # }
    # return render(request, 'stock_data/stock_list.html', context)
    # return HttpResponse("<h1>Hi User </h1>")
    return render(request, 'stock_list.html')


def manu(request):
        return HttpResponse('<h1> I mhere </h1')