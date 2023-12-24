from django.http import HttpResponse


def index(request):
    return HttpResponse("lixo")


def detail(request, stock_id):
    return HttpResponse(f"stock id: {stock_id}")


def results(request, stock_id):
    response = "stocks"
    return HttpResponse(response)



