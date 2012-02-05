from django.core.urlresolvers import reverse
from django.template import RequestContext
from musicshare.models import song, album, artist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from musicshare.forms import artistForm, albumForm, songForm, recordForm

mapping={
        "newArtist":[artistForm,"/artist/new"],
        "newAlbum":[albumForm,"/album/new"],
        "newSong":[songForm,"/song/new"],
        "newRecord":[recordForm,"/record/new"],
        }
def newAction(func):
    def func_wrapper(request):
        if request.method=="POST":
            form= mapping[func.__name__][0](request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return render_to_response('musicshare/newUser.html',
                        {'form':"OK",'action':mapping[func.__name__][1]},
                        context_instance=RequestContext(request))
            else:
                return render_to_response('musicshare/newUser.html',
                        {'form':"BAD",'action':mapping[func.__name__][1]},
                        context_instance=RequestContext(request))
        else:
            form= mapping[func.__name__][0]()
        return render_to_response('musicshare/newUser.html',{'form':form,'action':mapping[func.__name__][1]},context_instance=RequestContext(request))
    return func_wrapper
    
@newAction
def newArtist(request):
    pass
@newAction
def newAlbum(request):
    pass
@newAction
def newSong(request):
    pass
@newAction
def newRecord(request):
    pass
