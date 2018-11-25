from django import forms


class RestapiForm(forms.Form):
    post = forms.CharField()