from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    #path(r'^currentPlaylist/(?P<playlist_id>[0-9]+)?$', views.currentPlaylist, name="currentPlaylist"),
    path("currentPlaylist/<uuid:playlist_id>", views.currentPlaylist, name="currentPlaylist"),
    #path(r'^currentPlaylist/?$', views.currentPlaylist, name="currentPlaylist"),
    path("home/", views.Home, name="home"),
    path("explore/", views.Explore, name="explore"),
    path("mylists/", views.myLists, name="mylists"),
    path("profile/", views.profile, name="profile"),
    path("playlistSettings/", views.playlistSettings, name="playlistSettings"),
    path("signup/", views.signup, name="signup"),
    path("mylists/create_playlist/", views.playlist_create, name="Create")
    #path("songs/", views.SongListView.as_view(), name="songs"),
    #path("song/<int:pk>", views.SongDetailView.as_view(), name="song-detail"),
]

