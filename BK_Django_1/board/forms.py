from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={'required': 'Input Title.'},
        max_length=128,
        label="Title")
    content = forms.CharField(
        error_messages={'required': 'Input Content.'},
        widget=forms.Textarea,
        label="Content")
    tags = forms.CharField(
        required=False,
        label="Tag")


