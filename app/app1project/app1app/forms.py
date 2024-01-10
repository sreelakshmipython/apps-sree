from django import forms
from.models import Song
class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=['song_name','movie_name','singer','year','img']
