from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    category = models.CharField(max_length=100, default='Computer Science')


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
        return "\n".join([i.category for i in self.userInterest.all()])


class Advertisement(models.Model):
    active = models.BooleanField(default=True)
    duration = models.IntegerField()
    type_of_meeting = models.CharField(max_length=150)
    date = models.DateField()
    lesson = models.CharField(max_length=150)
    # other relationships
    advInterest = models.OneToOneField(Interest)
    user = models.OneToOneField(UserProfile)

    def get_interest(self):
        return self.advInterest.category

    def get_user(self):
        return self.user.username()


class JobOffer(models.Model):
    accepted = models.BooleanField(default=True)
    # other relationship
    user = models.OneToOneField(UserProfile)
    advertisement = models.OneToOneField(Advertisement)

    def get_user(self):
        return self.user.username()

    def get_add_id(self):
        return self.advertisement.advID


class Rating(models.Model):
    rate = models.IntegerField(default=0)
    comment = models.CharField(max_length=250, default='')
    # other relationship
    author = models.OneToOneField(UserProfile)
    offer = models.OneToOneField(JobOffer)

    def get_author(self):
        return self.author.username()

    def get_offer_id(self):
        return self.offer.offerID


class MenuItem(models.Model):
    name = models.CharField(max_length=50, default='menu item')
    url = models.CharField(max_length=250)
    parent = models.ForeignKey(MenuItem)
