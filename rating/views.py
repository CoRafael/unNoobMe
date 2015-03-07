from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import User
from base.models import *

@login_required
def latest_rating(request, username):
    try:
        user = UserProfile.objects.filter(user=User.objects.filter(username=username)[0])[0]

        offers = JobOffer.objects.all()
        advertisement = Advertisement.objects.all()
        ratings = Rating.objects.filter(offer__in=offers)

        context = {'userprofile': user, 'offers': offers, 'ratings': ratings, 'advertisement': advertisement}

    except IndexError:
        context = {}

    return render(request, 'ratings.html', context)