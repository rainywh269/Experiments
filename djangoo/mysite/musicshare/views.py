from django.template import Context,loader, RequestContext
from musicshare.models import user, record, artist, song, album
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response, get_object_or_404
from musicshare.forms import  userForm
from musicshare.user import newUser,editUser
from musicshare.music import newArtist,newAlbum,newSong,newRecord
import datetime


def home(request):
    s=request.GET.get('pk','1')
    userR=get_object_or_404(user,pk=int(s))
    return render_to_response('musicshare/index.html',{'user':userR,'strin':s})

#http://127.0.0.1:8000/submit/?title=testTitle&pk=1&artist=testArtist&album=testAlbum
def submit(request):
    artistN=request.GET.get('artist',None)
    albumN=request.GET.get('album',None)
    titleN=request.GET.get('title',None)
    userR=get_object_or_404(user,pk=int(request.GET.get('pk','0')))
    record.objects.create(
            user=userR,
            song=song.objects.get_or_create(
                name=titleN,
                album=album.objects.get_or_create(
                    artist=artist.objects.get_or_create(name=artistN)[0],
                    name=albumN)[0]
                )[0],
            date=datetime.datetime.now())
    return HttpResponse("Ok") 

def artistView(request):
    s=request.GET.get('pk','1')
    artistR=get_object_or_404(artist,pk=int(s))
    return render_to_response('musicshare/artist.html',{'artist':artistR})

