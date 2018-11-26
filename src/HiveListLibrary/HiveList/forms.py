from django import forms


class ProfileForm(forms.Form):
    post = forms.CharField(label="Current Password", max_length=100)
