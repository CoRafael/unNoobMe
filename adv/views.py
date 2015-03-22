from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import *



# return the latest 10 ACTIVE advertisments of the database
@login_required
def advertisement(request, id):
    adv = Advertisement.objects.filter(id=id)[0]
    context = {'user': request.user, 'advertisement': adv}
    return render(request, 'advertisement/advertisement.html', context)