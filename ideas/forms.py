from django import forms


class IdeaEdit(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(max_length=20)
    content = forms.CharField(max_length=2000)
