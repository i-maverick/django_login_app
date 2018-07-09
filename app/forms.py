from django import forms


class MainForm(forms.Form):
    select1 = forms.ChoiceField(
        choices=[(1, 'one'), (2, 'two'), (3, 'three')],
        widget=forms.Select(),
        required=False
    )
    select2 = forms.ChoiceField(
        choices=[(1, 'one'), (2, 'two'), (3, 'three')],
        widget=forms.Select(),
        required=False
    )
    select3 = forms.ChoiceField(
        choices=[(1, 'one'), (2, 'two'), (3, 'three')],
        widget=forms.Select(),
        required=False
    )
    check1 = forms.BooleanField(required=False)
    check2 = forms.BooleanField(required=False)
    check3 = forms.BooleanField(required=False)
