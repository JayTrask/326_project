<<<<<<< HEAD
import textwrap
import datetime

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from HiveList.models import Genre, Song, Artist, Playlist, Contributors, SongInstance

fake = Faker()

# Create Genres
genres = [
    Genre(genre_name="Pop"),
    Genre(genre_name="Hip Hop"),
    Genre(genre_name="Country"),
    Genre(genre_name="Afro"),
    Genre(genre_name="Latin"),
    Genre(genre_name="Electro/EDM"),
    Genre(genre_name="R&B"),
    Genre(genre_name="Rock"),
    Genre(genre_name="Indie"),
    Genre(genre_name="Folk/Acoustic"),
    Genre(genre_name="Classical"),
    Genre(genre_name="Jazz"),
    Genre(genre_name="Party"),
    Genre(genre_name="Christian"),
    Genre(genre_name="Comedy"),
    Genre(genre_name="K-Pop"),
    Genre(genre_name="Reggae"),
    Genre(genre_name="Metal"),
    Genre(genre_name="Soul"),
    Genre(genre_name="Blues"),
    Genre(genre_name="Punk")
]

# Save Genres
for genre in genres:
    genre.save()

# Create Artists
artists = []
for i in range(1, 100):
    a_name = fake.first_name() +" "+ fake.last_name()
    a_id = fake.uuid4()
    artist = Artist(artist_name = a_name, artist_id = a_id)
    artist.save()
    artists.append(artist)


# Create Songs
songs = []
for i in range(1, 500):
    s_title = fake.text(20)
    s_genre = genres[fake.random_int(0, len(genres)) - 1]
    s_id = fake.uuid4()
    s_artist = artists[fake.random_int(0, len(genres)) - 1]
    song = Song(title = s_title, genre = s_genre, song_id = s_id, artist = s_artist)
    song.save()
    songs.append(song)

# Create Playlists
playlists = []
for i in range(1, 200):
    p_name = fake.text(20)
    p_private = fake.boolean()
    p_creation_date = fake.date()
    p_description = fake.text(100)
    #p_vote_time = fake.date_time()
    p_ranking = fake.random_int(0, 100000)
    p_voting_threshold = fake.random_int(1, 101)
    p_id = fake.uuid4()
    playlist = Playlist(playlist_id = p_id, playlist_name = p_name, playlist_creation_date = p_creation_date, playlist_description = p_description, playlist_is_private = p_private, playlist_ranking = p_ranking, playlist_votingthreshold = p_voting_threshold)
    playlist.save()
    playlists.append(playlist)
 
# Create Contributors
contributors = []
for i in range(1, 200):
    playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    contributor = Contributors(playlist_id = playlist_id)
    contributor.save()
    contributors.append(contributor)


# Create SongInstances
song_instances = []
for i in range(1, 1000):
    si_id = songs[fake.random_int(0, len(songs)) - 1]
    si_playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    si_number_yes_votes = fake.random_int(0, 500)
    si_number_no_votes = fake.random_int(0, 500)
    si_siid = fake.uuid4()
    song_instance = SongInstance(song_instance_id = si_siid, song_id = si_id, playlist_id = si_playlist_id, number_yes_votes = si_number_yes_votes, number_no_votes = si_number_no_votes)
    song_instance.save()
    song_instances.append(song_instance)
"""
# Create VoteInstances
vote_instances = []
for i in range(1, 100):
    vi_contributor_id = contributors[fake.random_int(0, len(contributors)) - 1]
    vi_song_id = song_instances[fake.random_int(0, len(song_instances)) - 1]
    vi_vote = "y"
    vi_pid = playlists[fake.random_int(0, len(playlists)) - 1]
    vi_viid = fake.uuid4()
    vote_instance = VoteInstance(vote_instance_id = vi_viid, playlist_id = vi_pid, song_id = vi_song_id, contributor_id = vi_contributor_id, vote = vi_vote)
    vote_instance.save()
    vote_instances.append(vote_instance)
"""

#Create SuperUser
username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

username: {username}
password: {password}
email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

$ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)

# NEW 17
#ct = ContentType.objects.get_for_model(Playlist)
#permission = Permission.objects.get(
            #codename="can_mark_returned", name="Set book as returned", content_type=ct
            #)
  

# Create and add users
users = []
print("Generated users:")
for a in range(0, 50):
    firstName = fake.first_name()
    lastName = fake.last_name()
    username = firstName.lower()[0] + lastName.lower()
    email = f"{username}@326.edu"
    password = lastName
    user = User.objects.create_user(username, email, password)
    user.first_name = firstName
    user.last_name = lastName
    #user.last_name = a.last_name
    #user.user_permissions.add(permission)
    user.save()
    users.append(user)
    print(f"  username: {username}, password: {password}")

print("\nUsers who have a playlist:")
for i in range(0, 5):
    a_playlist = playlists[fake.random_int(0, len(playlists)) - 1]
    a_user = users[fake.random_int(0, len(users)) - 1]
    a_playlist.playlist_creator_id = a_user
    a_playlist.save()
    print(f"  {a_user.username}")














=======
import textwrap
import datetime

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from HiveList.models import Genre, Song, Artist, Playlist, Contributors, SongInstance

fake = Faker()

# Create Genres
genres = [
    Genre(genre_name="Pop"),
    Genre(genre_name="Hip Hop"),
    Genre(genre_name="Country"),
    Genre(genre_name="Afro"),
    Genre(genre_name="Latin"),
    Genre(genre_name="Electro/EDM"),
    Genre(genre_name="R&B"),
    Genre(genre_name="Rock"),
    Genre(genre_name="Indie"),
    Genre(genre_name="Folk/Acoustic"),
    Genre(genre_name="Classical"),
    Genre(genre_name="Jazz"),
    Genre(genre_name="Party"),
    Genre(genre_name="Christian"),
    Genre(genre_name="Comedy"),
    Genre(genre_name="K-Pop"),
    Genre(genre_name="Reggae"),
    Genre(genre_name="Metal"),
    Genre(genre_name="Soul"),
    Genre(genre_name="Blues"),
    Genre(genre_name="Punk")
]

# Save Genres
for genre in genres:
    genre.save()

# Create Artists
artists = []
for i in range(1, 100):
    a_name = fake.first_name() +" "+ fake.last_name()
    a_id = fake.uuid4()
    artist = Artist(artist_name = a_name, artist_id = a_id)
    artist.save()
    artists.append(artist)


# Create Songs
songs = []
for i in range(1, 500):
    s_title = fake.text(20)
    s_genre = genres[fake.random_int(0, len(genres)) - 1]
    s_id = fake.uuid4()
    s_artist = artists[fake.random_int(0, len(genres)) - 1]
    song = Song(title = s_title, genre = s_genre, song_id = s_id, artist = s_artist)
    song.save()
    songs.append(song)

# Create Playlists
playlists = []
for i in range(1, 200):
    p_name = fake.text(20)
    p_private = fake.boolean()
    p_creation_date = fake.date()
    p_description = fake.text(100)
    #p_vote_time = fake.date_time()
    p_ranking = fake.random_int(0, 100000)
    p_voting_threshold = fake.random_int(1, 101)
    p_id = fake.uuid4()
    playlist = Playlist(playlist_id = p_id, playlist_name = p_name, playlist_creation_date = p_creation_date, playlist_description = p_description, playlist_is_private = p_private, playlist_ranking = p_ranking, playlist_votingthreshold = p_voting_threshold)
    playlist.save()
    playlists.append(playlist)
 
# Create Contributors
contributors = []
for i in range(1, 200):
    playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    contributor = Contributors(playlist_id = playlist_id)
    contributor.save()
    contributors.append(contributor)


# Create SongInstances
song_instances = []
for i in range(1, 1000):
    si_id = songs[fake.random_int(0, len(songs)) - 1]
    si_playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    si_number_yes_votes = fake.random_int(0, 500)
    si_number_no_votes = fake.random_int(0, 500)
    si_siid = fake.uuid4()
    song_instance = SongInstance(song_instance_id = si_siid, song_id = si_id, playlist_id = si_playlist_id, number_yes_votes = si_number_yes_votes, number_no_votes = si_number_no_votes)
    song_instance.save()
    song_instances.append(song_instance)
"""
# Create VoteInstances
vote_instances = []
for i in range(1, 100):
    vi_contributor_id = contributors[fake.random_int(0, len(contributors)) - 1]
    vi_song_id = song_instances[fake.random_int(0, len(song_instances)) - 1]
    vi_vote = "y"
    vi_pid = playlists[fake.random_int(0, len(playlists)) - 1]
    vi_viid = fake.uuid4()
    vote_instance = VoteInstance(vote_instance_id = vi_viid, playlist_id = vi_pid, song_id = vi_song_id, contributor_id = vi_contributor_id, vote = vi_vote)
    vote_instance.save()
    vote_instances.append(vote_instance)
"""

#Create SuperUser
username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

username: {username}
password: {password}
email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

$ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)

# NEW 17
#ct = ContentType.objects.get_for_model(Playlist)
#permission = Permission.objects.get(
            #codename="can_mark_returned", name="Set book as returned", content_type=ct
            #)
  

# Create and add users
users = []
print("Generated users:")
for a in range(0, 50):
    firstName = fake.first_name()
    lastName = fake.last_name()
    username = firstName.lower()[0] + lastName.lower() + str(a)
    email = f"{username}@326.edu"
    password = lastName
    user = User.objects.create_user(username, email, password)
    user.first_name = firstName
    user.last_name = lastName
    #user.last_name = a.last_name
    #user.user_permissions.add(permission)
    user.save()
    users.append(user)
    print(f"  username: {username}, password: {password}")

print("\nUsers who have a playlist:")
for i in range(0, 5):
    a_playlist = playlists[fake.random_int(0, len(playlists)) - 1]
    a_user = users[fake.random_int(0, len(users)) - 1]
    a_playlist.playlist_creator_id = a_user
    a_playlist.save()
    print(f"  {a_user.username}")














>>>>>>> f1dceea70a1d3d772ed9a8adfbe6bc3907973e7e
