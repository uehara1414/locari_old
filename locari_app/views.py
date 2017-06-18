from django.shortcuts import render


def index(request):
    return render(request, 'locari_app/index.html')


def mypage(request):
    return render(request, 'locari_app/mypage.html')


def search(request):
    return render(request, 'locari_app/search.html')


def signup(request):
    return render(request, 'locari_app/signup.html')


def signin(request):
    return render(request, 'locari_app/signin.html')


def wish(request):
    return render(request, 'locari_app/wish.html')


def onsale(request):
    return render(request, 'locari_app/onsale.html')


def confirming(request):
    return render(request, 'locari_app/confirming.html')


def sale_request(request):
    return render(request, 'locari_app/sale_request.html')


def sale_request_submitted(request):
    return render(request, 'locari_app/sale_request_submitted.html')


def buy_request(request):
    return render(request, 'locari_app/buy_request.html')


def buy_request_submitted(request):
    return render(request, 'locari_app/buy_request_submitted.html')
