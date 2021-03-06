from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Interest(models.Model):
    category = models.CharField(max_length=100, default='Computer Science')

    def __unicode__(self):
        return self.category


class UserProfile(models.Model):
    # The additional attributes we wish to include.
    city = models.CharField(max_length=100, default='Glasgow')
    points = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='avatar_pictures', blank=True)
    # other relationships
    # We are going to use the User predefined table
    # info : https://docs.djangoproject.com/en/1.7/ref/contrib/auth/#django.contrib.auth.models.User.username
    # basic info: {username,firstname,last_name.email,password, last_login??, date_joined?? -> we will discuss this!}
    user = models.OneToOneField(User)
    userInterest = models.ManyToManyField(Interest)

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

    def get_interests(self):
        return ", ".join([i.category for i in self.userInterest.all()])


class Advertisement(models.Model):
    active = models.BooleanField(default=True)
    duration = models.IntegerField()  # lets say hours
    type_of_meeting = models.CharField(max_length=150)
    date = models.DateTimeField()
    lesson = models.CharField(max_length=150)
    # other relationships
    advInterest = models.ForeignKey(Interest)
    user = models.ForeignKey(UserProfile)
    added = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return ", ".join([self.user.user.username, self.date.strftime("%d-%m-%y"), self.advInterest.category])

    def get_interest(self):
        return self.advInterest.category

    def get_user(self):
        return self.user.username()
    # def save(self, *args, **kwargs):
    #     self.duration = abs(self.duration)
    #     super(Advertisement, self).save(*args, **kwargs)

class JobOffer(models.Model):
    accepted = models.BooleanField(default=False)
    # other relationship
    user = models.ForeignKey(UserProfile)
    advertisement = models.ForeignKey(Advertisement)

    def get_user(self):
        return self.user.username()

    def get_add_id(self):
        return self.advertisement.id


class Rating(models.Model):
    rate = models.IntegerField(default=0)
    comment = models.CharField(max_length=250, default='')
    # other relationship
    author = models.ForeignKey(UserProfile)
    offer = models.ForeignKey(JobOffer)
    added = models.DateTimeField(auto_now_add=True)

    def get_author(self):
        return self.author.username()

    def get_offer_id(self):
        return self.offer.id