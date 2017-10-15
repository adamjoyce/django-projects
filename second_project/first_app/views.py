from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.\
def index(request):
    html = "<html><body><h1>Index Page</h1></body></html>"
    return HttpResponse(html)

def help(request):
    my_dict = {'insert_text':"This is the help page... Please help..."}
    return render(request, 'first_app/help.html', context=my_dict)
