from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

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

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Could provide a confirmation message but for this project
            # the category will be added to the index page.
            # Redirect the user to the index page.
            return index(request)
        else:
            # The supplied form contains errors.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages if any.
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
