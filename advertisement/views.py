from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import *


# return the latest 10 ACTIVE advertisments of the database
@login_required
def latest_advertisement(request):
    latest_advertisement_list = Advertisement.objects.filter(active=True).order_by('-date')[:10]
    context = {'latest_advertisement': latest_advertisement_list}
    return render(request, 'advertisement/latest.html', context)


# return the latest 10 ACTIVE advertisments for specific interests of the user
@login_required
def latest_interest(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user)[0]
    interestedads = Advertisement.objects.filter(active=True, advInterest=user_profile.userInterest.all()).order_by(
        '-date')[:10]
    context = {'latest_interest': interestedads}
    return render(request, 'advertisement/interest.html', context)
