import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unNoobMe.settings')
django.setup()

from base.models import *


def populate():
    print 'Creating Interests'
    # user_interest=create_interests()
    for x in range(0, 10):
        print 'Creating user_%d' % x
        user = add_user(username='user_%d' % x, firstname='user_%d' % x, last_name='user_%d' % x,
                        email='user_%d@paparies.com' % x, password='user_%d' % x)
        user_profile = add_user_profile(user=user, city='Nicosia')


def add_user(username, firstname, last_name, email, password):
    user = User.objects._create_user(username=username, email=email, password=password, is_staff=False,
                                     is_superuser=False)
    user.first_name = firstname
    user.last_name = last_name

    user.save()
    return user


def add_user_profile(user, city):
    user = UserProfile(user=user, city=city)
    get = Interest(category='Computer Science')
    user.save()
    get.save()
    user.userInterest.add(get)
    return user


def create_interests():
    to_return = [Interest.objects.get_or_create(category='Computer Science'),
                 Interest.objects.get_or_create(category='Biology'),
                 Interest.objects.get_or_create(category='Pyschology'),
                 Interest.objects.get_or_create(category='Ksisimo Arxidiwn'),
                 Interest.objects.get_or_create(category='Education'),
                 Interest.objects.get_or_create(category='Sex Education')]
    return to_return


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()