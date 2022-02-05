from django import forms


class FormName(forms.Form):
    bond = forms.CharField()
    amount = forms.IntegerField()
