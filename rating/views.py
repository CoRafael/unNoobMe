from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import *

@login_required
def latest_rating(request):
    latest_rating_list = Rating.objects.order_by('id')[:10]
    context = {'latest_rating': latest_rating_list}
    return render(request, 'ratings.html', context)