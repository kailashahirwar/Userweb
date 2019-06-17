from django import forms

from app.models import Interest, Content


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ('name',)


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('content',)
