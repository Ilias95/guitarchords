from django.contrib.auth.models import User

from chords.models import Artist, Song, Bookmark


def create_artist(name='Some Artist'):
    artist = Artist(name=name)
    artist.save()
    return artist

def create_song(title='Random Song', artist=None, user=None, published=True):
    song = Song(title=title, artist=artist, user=user, published=published)
    song.save()
    return song

def create_user(username='username', password='password'):
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return user

def create_bookmark(user, published_song=True):
    bookmark = Bookmark(user=user, song=create_song(published=published_song))
    bookmark.save()
    return bookmark

def valid_song_data(title='Title', artist_txt='artist_txt', genre=Song.POP,
                    video='http://www.example.com', tabs=True, content='content'):
    return {
        'title' : title, 'artist_txt' : artist_txt, 'genre' : genre,
        'video' : video, 'tabs' : tabs, 'content' : content
    }