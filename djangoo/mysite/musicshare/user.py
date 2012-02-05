from django.core.urlresolvers import reverse
from django.template import RequestContext
from musicshare.models import user
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from musicshare.forms import userForm

def newUser(request):
    if request.method=="POST":
        form=userForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('musicshare/newUser.html',
                    {'form':"OK",'action':"/user/new"},
                    context_instance=RequestContext(request))
        else:
            return render_to_response('musicshare/newUser.html',
                    {'form':"BAD",'action':"/user/new"},
                    context_instance=RequestContext(request))
    else:
        form=userForm()
    return render_to_response('musicshare/newUser.html',{'form':form,'action':"/user/new"},context_instance=RequestContext(request))

def editUser(request,pk):
    userO=user.objects.get(pk=int(pk))
    if request.method=="POST":
        form=userForm(request.POST,request.FILES,instance=userO)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('musicshare.views.editUser', args=(userO.pk,)))
        else:
            return HttpResponse("BAD")
    form = userForm(instance=userO)
    return render_to_response('musicshare/editUser.html',{'form':form},context_instance=RequestContext(request))
