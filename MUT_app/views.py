from django.shortcuts import render


def home(request):
    return render(request, 'MUT_app/index.html')


def about(request):
    return render(request, 'MUT_app/about.html')


def goods(request):
    return render(request, 'MUT_app/goods.html')

