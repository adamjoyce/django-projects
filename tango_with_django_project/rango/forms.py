from django import forms

from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category's name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and the Model.
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=128,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and the Model.
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some field may allow NULL values, so we may wish to exclude them.
        # Here we are hiding the ForeignKey.
        exclude = ('category',)
        # Alternatively be could specific the fields to input
        # i.e. fields = ('title', 'url', 'views',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and does not begin with 'http://'
        # prepend 'http://'
        if url and not url.startswith('http://'):
            url = "http://" + url
            cleaned_data['url'] = url

            return cleaned_data
