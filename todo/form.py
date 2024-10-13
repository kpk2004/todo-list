from django import forms
class Myform(forms.Form):
    task=forms.CharField(max_length=100)