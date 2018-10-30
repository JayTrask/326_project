import uuid
from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


now = datetime.datetime.now()


# Create your models here.

class Playlist(models.Model):
    """
    Model representing a playlist
    """
    playlist_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular Playlist across entire site",
    )
    playlist_name = models.CharField(max_length=200,
                                     help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    playlist_creator_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    playlist_creation_date = models.DateField(auto_now_add=True, blank=True)
    playlist_description = models.TextField(max_length=1000, help_text="Enter description for playlist")
    playlist_ranking = models.IntegerField(default=0)
    playlist_vote_time = models.DateTimeField(default=now.strftime("%Y-%m-%d %H:%M"), blank=True)
    playlist_votingthreshold = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        """
        Description: String for representing the model object (in Admin site etc.)
        :return: the playlist name
        """
        return self.playlist_id


class Contributors(models.Model):
    """
    Model representing all the contributors for a playlist. This will use a playlist ID as a key to the playlists table, and a user ID
    that is a key to the users table
    """
    playlist_id = models.ForeignKey('Playlist', on_delete=models.SET_NULL, null=True)
    contributor_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.playlist_id


class Artist(models.Model):
    """
    Model representing a Song
    """
    artist_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular Song across entire site",
    )
    artist_name = models.CharField(max_length=200)

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.artist_id


class Song(models.Model):
    """
    Model representing a Song
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)

    song_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular Song across entire site",
    )

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.song_id


class Genre(models.Model):
    """
    Model representing a Song
    """

    # not sure if that works for genre id

    genre_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular Genre across entire site",
    )
    genre_name = models.CharField(max_length=200, help_text="Enter a genre for the song (e.g. Swedish Heavy Metal)")

    def __str__(self):
        """
        Description: 
        :return: 
        """
        return self.genre_name


class SongInstance(models.Model):
    """
    Model representing a Song Instance
    """
    song = models.ForeignKey('Song.song_id', on_delete=models.SET_NULL, null=True)
    song_instance_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular Song Instance",
    )
    playlist_id = models.ForeignKey('Playlist.playlist_id', on_delete=models.SET_NULL, null=True)
    contributor_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    number_votes = models.IntegerField(default=0)
    number_yes_votes = models.IntegerField(default=0)
    number_no_votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Description:
        :return:
        """
        return f'{self.song_id}, {self.playist_id}'


class VoteInstance(models.Model):
    """
    Model representing a vote
    """
    contributor_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    song_id = models.ForeignKey('SongInstance', on_delete=models.SET_NULL, null=True)

    VOTE_STATUS = (
        ('y', 'yes'),
        ('n', 'no')
    )

    vote = models.CharField(max_length=1, choices=VOTE_STATUS, blank=True)

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.contributor_id
