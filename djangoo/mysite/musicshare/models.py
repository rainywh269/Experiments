from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime
from django.db.models import signals

def create_profile_for_user(sender, **kwargs):
    if kwargs['created']:
        p = user() # 'Profile' is my custom User model
        p.__dict__.update(kwargs['instance'].__dict__)
        p.save()

signals.post_save.connect(create_profile_for_user, sender=User)

class user( User ):
    objects=UserManager()
    img=models.ImageField(upload_to="gravatar",default="no-cover.png")
    def __unicode__(self):
        return self.username

class artist(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="images",default="no-cover.png")
    def __unicode__(self):
        return self.name
    
class album(models.Model):
    artist=models.ForeignKey(artist)
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="covers",default="no-cover.png")
    def __unicode__(self):
        return self.name

class song(models.Model):
    album=models.ForeignKey(album)
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class record(models.Model):
    user=models.ForeignKey(user)
    song=models.ForeignKey(song)
    date=models.DateTimeField('date listened')
    def __unicode__(self):
        return self.date.isoformat(' ')[0:16]
