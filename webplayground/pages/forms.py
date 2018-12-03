from  django import forms
from pages.models import Page

class PagesForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','content','order']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'titulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }

        labels= {
            'title':'',
            'order':'',
            'content': '',
        }