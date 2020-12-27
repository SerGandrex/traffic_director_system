from django import forms
from .models import RedirectLink, LandingPage


class RedirectLinkCreateForm(forms.ModelForm):
    class Meta:
        model = RedirectLink
        fields = '__all__'


class LandingPageCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = LandingPage
        fields = ['url', 'country', 'weight']
