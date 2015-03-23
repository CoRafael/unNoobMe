from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import User, UserProfile, Rating, JobOffer


@login_required
def userprofile(request, username):
    try:
        user = UserProfile.objects.filter(user=User.objects.filter(username=username)[0])[0]
        interests = user.userInterest.all()

        offers = JobOffer.objects.filter(user=user).order_by('-advertisement_id')[:10]
        # have to filter selected = true too with real data

        ratings = Rating.objects.filter(offer__in=offers)

        context = {'username': username, 'userrequest': request.user.userprofile.username(), 'userprofile': user,
                   'interests': interests,
                   'ratings': ratings}

    except IndexError:
        context = {}

    return render(request, 'userprofile/userprofile.html', context)
