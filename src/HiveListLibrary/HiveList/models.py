from django.db import models

# Create your models here.


class Playlist(models.Model):
    """
    Model representing a playlist
    """
    playlist_id = models.IntegerField(max_length=100, primary_key=True)
    playlist_name = models.CharField(max_length=200, help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    playlist_creator_id = models.ForeignKey(User)
    playlist_creation_date = models.DateField()
    playlist_description = models.TextField(max_length=1000, help_text="Enter description for playlist")
    playlist_creation_date = models.DateField()
    playlist_contributors = models.ManyToManyField(Contributor, help_text="Select a contributor for this playlist")

    def __str__(self):
        """
        Description: String for representing the model object (in Admin site etc.)
        :return: the playlist name
        """
        return self.playlist_name


class Contributors(models.Model):
    """
    Model representing all the contributors for a playlist. This will use a playlist ID as a key to the playlists table, and a user ID
    that is a key to the users table
    """
    playlist_id = models.ForeignKey(playlist_id, ondelete=cascade)
    contributor_id = contributor_id = models.ForeignKey(User, ondelete=models.cascade)

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.contributor_id


class Artist(models.Model):
    """
    Model representing a Song
    """
    artist_id = models.IntegerField(max_length=100, primary_key=True)
    artist_name = models.CharField(max_length=200)

    def __str__(self):
        """
        Description:
        :return:
        """
        return f'{artist_id}, {artist_name}'

class Song(models.Model):
    """
    Model representing a Song
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)
    
    """Not positive how we want to represent this ID"""
    song_id = models.UUIDField(
                               primary_key=True,
                               default=uuid.uuid4,
                               help_text="Unique ID for this particular book across whole library",
                               )

    def __str__(self):
        """
        Description:
        :return:
        """
        return f'{self.title}, {self.artist}'


class Genre(models.Model):
    """
    Model representing a Song
    """

	#not sure if that works for genre id 

    genre_id = models.ForeignKey('Genre.genre_id', on_delete=models.SET_NULL, null=True)
    genre_name = models.CharField(max_length=200, help_text="Enter a genre for the song (e.g. Swedish Heavy Metal)")

    def __str__(self):
        """
        Description: 
        :return: 
        """
        return genre_name;


class SongInstance(models.Model):
    """
    Model representing a Song Instance
    """
    song_id = models.ForeignKey('Song.song_id', on_delete=models.SET_NULL, null=True)
    playlist_id = models.ForeignKey('Playlist.playlist_id', on_delete=models.SET_NULL, null=True)
    contrib = models.ManyToManyField(Contributors, help_text="Select a genre for this book")
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
    contributor_id = models.ForeignKey(User, ondelete=models.cascade)
    song_id = models.ForeignKey('SongInstance', ondelete=models.cascade)

    VOTE_STATUS = (
    	('y', 'yes'),
    	('n', 'no')
    	)

    vote = models.CharField(max_length=1, choices=VOTE_STATUS, blank=true)

    def __str__(self):
        """
        Description:
        :return:
        """
        return contributor_id




