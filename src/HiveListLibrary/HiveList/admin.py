from django.contrib import admin

from HiveList.models import Genre, Playlist, Contributors, Artist, Song, Genre, SongInstance

# Register your models here.

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("playlist_id", "playlist_name", "playlist_creation_date", "playlist_vote_time", "playlist_is_private")
    


@admin.register(Contributors)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ("playlist_id", "playlist_id")
    


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("artist_id", "artist_name")
    


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title","artist","genre")
    


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_name", "genre_name")


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    list_display = ("song_instance_id", "song_id", "playlist_id", "number_yes_votes", "number_no_votes")
    

"""
@admin.register(VoteInstance)
class VoteInstanceAdmin(admin.ModelAdmin):
    list_display = ("contributor_id","vote")
"""

