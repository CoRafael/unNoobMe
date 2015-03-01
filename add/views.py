from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import Advertisement


# return the latest 10 ACTIVE advertisments of the database
@login_required
def latest_advertisement(request):
    latest_advertisement_list = Advertisement.objects.filter(active=True).order_by('-date')[:10]
    context = {'latest_advertisement': latest_advertisement_list}
    return render(request, 'base/dummy_latest.html', context)


# return the latest 10 ACTIVE advertisments for specific interests of the user
@login_required
def latest_interest(request):
    interest_list = Advertisement.objects.filter(active=True, advInterest=1).order_by('-date')[:10]
    context = {'latest_interest': interest_list}
    return render(request, 'base/dummy_interest.html', context)