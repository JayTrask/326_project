from django.contrib import admin

from HiveList.models import Playlist, Contributor, Artist, Song, Genre, SongInstance, VoteInstance

# Register your models here.

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    #displays


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    #displays


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    #displays


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    #displays


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    #displays


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    #displays


@admin.register(VoteInstance)
class VoteInstanceAdmin(admin.ModelAdmin):
    #displays
