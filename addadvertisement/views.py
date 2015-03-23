from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from base.models import Interest, Advertisement,UserProfile

@login_required
def add_advertisement(request):

    if request.method == 'GET':
        try:
            interests = Interest.objects.all()
            types = ['Skype meeting', 'Cafe meeting', 'Library meeting', 'Home meeting']
            context = {"interests": interests, "types": types}
        except IndexError:
            context = {}
        return render(request, 'addadvertisement.html', context)
    else:
        typeofmeeting = request.POST.get("typeofmeeting", "Skype Meeting")
        interest = request.POST.get("interest", "Computer Science")
        lesson = request.POST.get("lesson", "C/C++")
        duration = request.POST.get("duration", "1")
        date = request.POST.get("date", "2016-02-23 15:00")
        date = date.replace("/","-",3)
        get_user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        get_type_interest = Interest.objects.get_or_create(id=interest)[0]
        Advertisement.objects.get_or_create(duration=duration, type_of_meeting=typeofmeeting, date=date, lesson=lesson,
                                            advInterest=get_type_interest, user=get_user_profile)
        return HttpResponseRedirect('/')