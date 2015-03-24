from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import *

# return the latest 10 ACTIVE advertisments of the database
@login_required
def latest_advertisement(request):
    latest_advertisement_list = Advertisement.objects.filter(active=True).order_by('-added')[:10]
    context = {'latest_advertisement': latest_advertisement_list}
    return render(request, 'advertisement/latest.html', context)


# return the latest 10 ACTIVE advertisments for specific interests of the user
@login_required
def latest_interest(request):
    try:
        user = request.user
        user_profile = UserProfile.objects.filter(user=user)[0]
        interestedads = Advertisement.objects.filter(active=True, advInterest=user_profile.userInterest.all()).order_by('-added')[:10]
        context = {'latest_interest': interestedads}
    except IndexError:
        context = {}
    return render(request, 'advertisement/interest.html', context)

@login_required
def my_adds(request):
    try:
        user = request.user
        user_profile = UserProfile.objects.filter(user=user)[0]
        my_actadds = Advertisement.objects.filter(user=user_profile, active=True).order_by('-added')[:10]
        my_inactadds = Advertisement.objects.filter(user=user_profile, active=False).order_by('-added')[:10]
        context = {'my_actadds': my_actadds, 'my_inactadds': my_inactadds}
    except IndexError:
        context = {}
    return render(request, 'advertisement/my_adds.html', context)

@login_required
def my_offers(request):
    try:
        user = request.user
        user_profile = UserProfile.objects.filter(user=user)[0]

        accepted = JobOffer.objects.filter(user=user_profile, accepted=True)
        declined = JobOffer.objects.filter(user=user_profile, accepted=False)

        my_actadds = []
        my_inactadds = []

        for f in accepted:
            my_actadds.append(f.advertisement)

        for f in declined:
            my_inactadds.append(f.advertisement)

        my_actadds.sort(key=lambda x: x.added, reverse=True)
        my_inactadds.sort(key=lambda x: x.added, reverse=True)

        context = {'my_actadds': my_actadds, 'my_inactadds': my_inactadds}
    except IndexError:
        context = {}
    return render(request, 'advertisement/my_offers.html', context)