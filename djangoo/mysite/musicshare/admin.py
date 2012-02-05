from django.contrib import admin
from musicshare.models import user,song,record,artist,album

class recordAdmin(admin.StackedInline):
    model = record
    extra=0

class UserAdmin(admin.ModelAdmin):
    '''
    fieldsets = [
            (None,{'fields':['username']}),
            ('password',{'fields':['password'],'classes':['collapse']}),
            ('gravatar',{'fields':['img']}),
            ]
    '''
    inlines = [recordAdmin]
class songAdmin(admin.ModelAdmin):
    inlines=[recordAdmin]

admin.site.register(user,UserAdmin)
admin.site.register(song,songAdmin)
admin.site.register(record)
admin.site.register(artist)
admin.site.register(album)


