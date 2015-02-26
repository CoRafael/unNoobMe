from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # We are going to use the User predefined table
    # info : https://docs.djangoproject.com/en/1.7/ref/contrib/auth/#django.contrib.auth.models.User.username
    # basic info: {username,firstname,last_name.email,password, last_login??, date_joined?? -> we will discuss this!}
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    city = models.CharField(max_length=100, default='Glasgow')
    points = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='avatar_pictures', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    def username(self):
        return self.user.username

    def firstname(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def last_login(self):
        return self.user.last_login

    def date_joined(self):
        return self.user.date_joined
