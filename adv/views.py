from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import *


@login_required
def advertisement(request, id):
    adv = Advertisement.objects.filter(id=id)[0]
    offers = JobOffer.objects.filter(advertisement=id)
    context = {'user': request.user, 'advertisement': adv, 'offers': offers}
    return render(request, 'advertisement/advertisement.html', context)