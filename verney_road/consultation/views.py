from django.shortcuts import render

def index(request):
    return render(request, 'consultation/index.html')

def who_are_we(request):
    return render(request, 'consultation/who_are_we.html')

def project_information(request):
    return render(request, 'consultation/project_information.html')
