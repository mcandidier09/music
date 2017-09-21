from django import forms

from playlist.models import Song, Playlist


class PlaylistForm(forms.ModelForm):
    """Form for creating playlist
    """

    class Meta:
        model = Playlist
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        """ playlist needs user
        """
        self.user = kwargs.pop('user', None)

        return super(PlaylistForm, self).__init__(*args, **kwargs)

    def save(self):
        """playlist creation
        """
        playlist = Playlist.objects.create(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            user=self.user
        )
        return playlist


class SongForm(forms.ModelForm):
    """Form for adding song on a playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']

    def __init__(self, *args, **kwargs):
        """ User and playlist are used for creation of song
        """
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)

        return super(SongForm, self).__init__(*args, **kwargs)

    def save(self):
        """ Song creation needs user and playlist 
        """
        song = Song.objects.create(
            title=self.cleaned_data['title'],
            link=self.cleaned_data['link'],
            user=self.user,
            playlist=self.playlist
        )
        return song


class UpdateSongForm(forms.ModelForm):
    """ Form for editing a song from a playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']