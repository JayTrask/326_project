from django.db import models

# Create your models here.


class Playlist(models.Model):
    """
    Model representing a playlist
    """
    playlist_id = models.IntegerField(max_length=100, primary_key=True)
    playlist_name = models.CharField(max_length=200, help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    playlist_description = models.TextField(max_length=1000, help_text="Enter description for playlist")
    playlist_creation_date = models.DateField()
    playlist_contributors = models.ManyToManyField(Contributor, help_text="Select a contributor for this playlist")

    def __str__(self):
        """
        Description: String for representing the model object (in Admin site etc.)
        :return: the playlist name
        """
        return self.playlist_name


class Contributor(models.Model):
    """
    Model representing a Contributor
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class Artist(models.Model):
    """
    Model representing a Song
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class Song(models.Model):
    """
    Model representing a Song
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class Genre(models.Model):
    """
    Model representing a Song
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class SongInstance(models.Model):
    """
    Model representing a Song Instance
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class VoteInstance(models.Model):
    """
    Model representing a Vote Instance
    """

    def __str__(self):
        """
        Description:
        :return:
        """
        pass




