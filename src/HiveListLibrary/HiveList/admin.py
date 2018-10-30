from django.contrib import admin

from HiveList.models import Playlist, Contributors, Artist, Song, Genre, SongInstance, VoteInstance

# Register your models here.

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    #displays
    list_display = {'id', 'name', 'creator_id', 'creation_date', 'description', 'ranking', 'vote_time', 'voting_threshold'}


@admin.register(Contributors)
class ContributorAdmin(admin.ModelAdmin):
    #displays
    list_display = {'playlist_id', 'contributor_id'}


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    #displays
    list_display = {'artist_id', 'artist_name'}


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    #displays
    list_display = {'song_id', 'title', 'artist_id'}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    #displays
    list_display = {'genre_id', 'genre_name'}


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    #displays
    list_display = {'song_instance_id', 'song_id', 'playlist_id', 'contributor_id', 'number_votes', 'yes_votes', 'no_votes'}


@admin.register(VoteInstance)
class VoteInstanceAdmin(admin.ModelAdmin):
    #displays
    list_display = {'contrubutor_id', 'song_id', 'vote_status'}
