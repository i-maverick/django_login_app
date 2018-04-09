from django import forms


class MainForm(forms.Form):
    check = forms.BooleanField()
