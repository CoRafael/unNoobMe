from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from base.models import *


@login_required
def advertisement(request, id):
    adv = Advertisement.objects.filter(id=id)[0]
    offers = JobOffer.objects.filter(advertisement=id)
    context = {'user': request.user.userprofile, 'advertisement': adv, 'offers': offers}
    return render(request, 'advertisement/advertisement.html', context)


@login_required
def add_offer(request):
    print request.user
    if request.method == 'POST' and request.POST.get('type') == 'addoffer':
        get_user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        get_id_add = request.POST.get('advertisement')
        add = Advertisement.objects.get_or_create(id=get_id_add)[0]
        JobOffer.objects.get_or_create(user=get_user_profile, advertisement=add)
        return HttpResponseRedirect('/')
    elif request.method == 'POST' and request.POST.get('type') == 'chooseoffer':
        get_offer_id = request.POST.get('offer_id')
        get_add_id = request.POST.get('advertisement_id')
        offer = JobOffer.objects.get_or_create(id=get_offer_id)[0]
        add = Advertisement.objects.get_or_create(id=get_add_id)[0]
        offer.accepted = True
        add.active = False
        offer.save()
        add.save()
        return HttpResponseRedirect('/')
