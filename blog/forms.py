from django import forms
from pagedown.widgets import PagedownWidget

class BlogPostSaveForm(forms.Form):
    title = forms.CharField(
        # label = 'Title',
        widget = forms.TextInput(attrs={'size': 128}))
    body = forms.CharField(
        # label='Post', 
        # widget=forms.Textarea())
        widget=PagedownWidget())
    tags = forms.CharField(
        # label='Tags',
        required = True,
        widget = forms.TextInput(attrs={'rows': 3}))

class SearchForm(forms.Form):
    query = forms.CharField(
        label=u'Search for',
        widget=forms.TextInput(attrs={'size':32})
        )
