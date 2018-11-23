from django.shortcuts import render

from HiveList.models import Playlist, Contributors, Artist, Song, Genre, SongInstance\

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = {
        "test": 5,
        "test2": 13,
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "index.html", context=context)

@login_required(login_url='/accounts/login/')
def currentPlaylist(request):
    playlist = Playlist.objects.order_by("?").first()
    all_songInstances = SongInstance.objects.filter(playlist_id__exact=playlist.playlist_id).values('song_id')
    all_songs = Song.objects.filter(song_id__in=all_songInstances)
    # Render the HTML tmeplate index.html with the data in the context variable
    context = {
        "songs": all_songs,
        "current_playlist": playlist
    }
    return render(request, "currentPlaylist.html", context=context)

@login_required(login_url='/accounts/login/')
def Explore(request):
    playlists = Playlist.objects.all()[:10]
    playlist_ids = Playlist.objects.all()[:10].values('playlist_id')
    all_songInstances = SongInstance.objects.filter(playlist_id__in=playlist_ids).values('song_id')
    songs = Song.objects.filter(song_id__in=all_songInstances)
    context = {
        "popular_playlists": playlists,
        "popular_songs": songs,
    }
    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Explore.html", context=context)


def Home(request):
    # IP_playlists = pass
    top_10_playlists = Playlist.objects.all()[0:10]
    public_playlists_var = Playlist.objects.filter(playlist_is_private__exact=False)[0:5]  # TODO: make pages
    # profile_information = pass
    # playlist_export = pass

    context = {
        # "IP_playlists": IP_playlists
        "top_10": top_10_playlists,
        "public_playlists": public_playlists_var,
        # "profile_information": profile_information
        # "playlist_export": playlist_export
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Home.html", context=context)

@login_required(login_url='/accounts/login/')
def myLists(request):
    IP_playlists = Playlist.objects.all()[:10]
    My_playlists = Playlist.objects.all()[11:21]

    context = {
        "My_IP_Playlists": IP_playlists,
        "My_Finished_Playlists": My_playlists,
    }
    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "myLists.html", context=context)

@login_required(login_url='/accounts/login/')
def playlistSettings(request):
    playlist = Playlist.objects.order_by("?").first()
    all_songInstances = SongInstance.objects.filter(playlist_id__exact=playlist.playlist_id).count()

    context = {
        "song_count": all_songInstances,
        "playlist": playlist,
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "playlistSettings.html", context=context)

@login_required(login_url='/accounts/login/')
def profile(request):
    userPlaylists = Playlist.objects.filter(playlist_creator_id=request.user)
    #all_songInstances = SongInstance.objects.filter(playlist_id__exact=playlist.playlist_id).values('song_id')
    #all_songs = Song.objects.filter(song_id__in=all_songInstances)
    context = {
        "playlists": userPlaylists,
    }
    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "profile.html", context=context)
