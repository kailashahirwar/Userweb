from django import forms

from app.models import Interest


class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ('name', )
