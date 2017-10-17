from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
    # Query the database for a list of all categories stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve up to the top five categories.
    # Place the list in our context dictionary that will be passed to our
    # template engine.
    context_dict = {}
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # Render the response and send it back.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'author_name': "Adam Joyce"}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    # Context dictionary to pass to the template render engine.
    context_dict = {}

    try:
        # Is there a category name slug with the given name?
        # If not, the .get() method raises a DoesNotExist exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all associated pages.
        pages = Page.objects.filter(category=category)

        # Add the results to the template context under the name 'pages'.
        context_dict['pages'] = pages

        # Add the category object to the context for use in the template.
        # It will determine if the category exits.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # The template will display no catgeory.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
