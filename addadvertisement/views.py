from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from base.models import Interest, Advertisement,UserProfile


def add_advertisement(request):
    interests = Interest.objects.all()
    types = ['Skype meeting', 'Cafe meeting', 'Library meeting', 'Home meeting']
    context = {"interests": interests, "types": types}

    return render(request, 'addadvertisement.html', context)


@login_required
def test(request):
    if request.method == 'POST':
        typeofmeeting = request.POST.get("typeofmeeting", "Skype Meeting")
        interest = request.POST.get("interest", "Computer Science")
        lesson = request.POST.get("lesson", "C/C++")
        date = "2016-02-20 15:00"

        get_user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        get_type_interest = Interest.objects.get_or_create(id=interest)[0]
        Advertisement.objects.get_or_create(duration="2", type_of_meeting=typeofmeeting, date=date, lesson=lesson,
                                            advInterest=get_type_interest, user=get_user_profile)
        print typeofmeeting
        print interest
        print lesson

    return HttpResponseRedirect('/')