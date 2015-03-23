from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from base.models import *


@login_required
def latest_rating(request):
    try:
        offers = JobOffer.objects.all()
        ratings = Rating.objects.filter(offer__in=offers).order_by('-added')[:10]

        context = {'ratings': ratings}

    except IndexError:
        context = {}

    return render(request, 'ratings.html', context)


@login_required
def rate_offer(request):
    if request.method == 'POST' and request.POST.get('type') == 'rateoffer':
        try:
            offer_id = request.POST.get('offer_id')
            offer = JobOffer.objects.get_or_create(id=offer_id)[0]
            ratings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            context = {'offer': offer, 'ratings': ratings}
        except IndexError:
            context = {}
        return render(request, 'rate_offer.html', context)
    elif request.method == 'POST' and request.POST.get('type') == 'save_rate':
        offer_id = request.POST.get('offer_id')
        rate = request.POST.get('rate')
        comment = request.POST.get('comment')
        author = UserProfile.objects.get_or_create(user=request.user)[0]
        offer = JobOffer.objects.get_or_create(id=offer_id)[0]
        Rating.objects.get_or_create(rate=rate, comment=comment, author=author, offer=offer)
        return HttpResponseRedirect('/')
