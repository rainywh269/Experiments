from django import forms
from django.forms import ModelForm 
from musicshare.models import user, record, artist, song, album


class userForm( ModelForm ):
    class Meta:
        model=user
        fields = ("username","img","password")

class artistForm( ModelForm ):
    class Meta:
        model=artist

class songForm( ModelForm ):
    class Meta:
        model=song

class albumForm( ModelForm ):
    class Meta:
        model=album

class recordForm( ModelForm ):
    class Meta:
        model=record
