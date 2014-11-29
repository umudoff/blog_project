from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
     fk_CreatedBy = models.ForeignKey(User, null=False, blank=False,
                                      editable=True, auto_created=User)
     title = models.CharField(max_length=128)
     body = models.TextField(max_length=999)
     created = models.DateField(auto_now_add=True)
     # url = models.CharField(max_length=256)
     
                                     
     def post_save(self, request, extra_command="", *args, **kwargs):
         self.fk_CreatedBy = request.user
         self.save()
                                             
     def __unicode__(self):
         return self.title.lower()



class Comment(models.Model):
     postID = models.ForeignKey('Post',null=False, blank=False)
     description = models.TextField(max_length=999)
     dateTimeCreated = models.DateField(auto_now_add=True, editable=False)
     # url = models.CharField(max_length=256)
    
     fk_UserID = models.ForeignKey(User, null=True, blank=True,
                                        editable=True)
  
    
     def __unicode__(self):
        return self.description.lower()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username