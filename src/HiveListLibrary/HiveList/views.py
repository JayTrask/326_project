from django.shortcuts import render

from HiveList.models import Playlist, Contributor, Artist, Song, Genre, SongInstance, VoteInstance

# Create your views here.
def index(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "index.html", context=context)


def currentPlaylist(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "currentPlaylist.html", context=context)

def Explore(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Explore.html", context=context)

def Home(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Home.html", context=context)

def myLists(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "myLists.html", context=context)

def playlistSettings(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "playlistSettings.html", context=context)

def profile(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "profile.html", context=context)
