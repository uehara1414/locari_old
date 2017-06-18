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
