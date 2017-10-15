from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key bold_message is the same as {{ bold_message }} in the
    # template!
    context_dict = {'bold_message': "Crunchy, cream, cookie, candy, cupcake!"}

    # Return the rendered response to send to the client.
    # We make use of the render shortcut function to make our lives easier.
    # Note that the first parameter after the request object is the template
    # we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'author_name': "Adam Joyce"}
    return render(request, 'rango/about.html', context=context_dict)
