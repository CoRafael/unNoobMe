from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import *

@login_required
def latest_rating(request):
    try:
        offers = JobOffer.objects.all()
        ratings = Rating.objects.filter(offer__in=offers)

        context = {'ratings': ratings}

    except IndexError:
        context = {}

    return render(request, 'ratings.html', context)