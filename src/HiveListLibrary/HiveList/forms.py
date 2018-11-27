from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from HiveList.models import Playlist


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class PlaylistCreationForm(forms.Form):

	#playlist_is_private = forms.ChoiceField(choices = {'yes', 'no'}, label="", initial='', widget=forms.Select(), required=True)
	playlist_votingthreshold: forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'min':'0', 'max':'100'}), required=True)

	class Meta:
		model = Playlist
		fields = [
			'playlist_name',
			'playlist_description',
			'playlist_votingthreshold',
			'playlist_is_private'
		]





