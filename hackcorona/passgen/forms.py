
from django import forms
from django.forms import ModelForm
from .models import PassModel

class PassForm(ModelForm):
    class Meta:
        model= PassModel
        fields='__all__'
        exclude=['issuedate','uniquenumber','checked']

class DownloadForm(ModelForm):
    class Meta:
        model=PassModel
        fields=['aadharcardnumber']