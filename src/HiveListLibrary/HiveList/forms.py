from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from HiveList.models import Playlist, Song, SongInstance

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        help_texts = {
                'username': ''
                }


class PlaylistCreationForm(forms.ModelForm):
    playlist_name = forms.CharField(max_length=200, help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    playlist_description = forms.CharField(max_length=1000, help_text="Enter description for playlist")
    playlist_vote_time = forms.DateTimeField()
    playlist_votingthreshold = forms.IntegerField()
    playlist_is_private = forms.BooleanField(required=False)

    class Meta:
        model = Playlist
        fields = [
            'playlist_name',
            'playlist_description',
            'playlist_vote_time',
            'playlist_votingthreshold',
            'playlist_is_private'
            ]


class NamesChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
                    return '{title} by {artist}'.format(title=obj.title, artist=obj.artist)


class AddSongForm(forms.ModelForm):
    song_id = NamesChoiceField(label="Song", queryset=Song.objects.all())

    class Meta:
        model = SongInstance
        exclude = ['song_instance_id', 'playlist_id', 'number_yes_votes', 'number_no_votes', 'adder_id']


class VoteForm(forms.ModelForm):
    number_yes_votes = forms.IntegerField()
    number_no_votes = forms.IntegerField()

    class Meta:
        model = SongInstance
        fields = ['number_yes_votes','number_no_votes']

