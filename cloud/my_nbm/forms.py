from django import forms

class CreateNewAnalysis(forms.Form):
    nodes = forms.CharField(required = True,help_text="Enter the array.")
    elements = forms.CharField(help_text="Enter the array.")