from django import forms


class MakeFund(forms.Form):
    idea_id = forms.IntegerField()
    amount = forms.IntegerField()
    comment = forms.CharField(max_length=100)
