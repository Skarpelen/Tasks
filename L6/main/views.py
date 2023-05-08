from django.shortcuts import render


def index(request):
    return render(request, 'main/list_emps.html')


def add_emp(request):
    return render(request, 'main/add_emp.html')


def best_emp(request):
    return render(request, 'main/best_emp.html')