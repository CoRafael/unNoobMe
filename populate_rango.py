import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unNoobMe.settings')
django.setup()

from random import randrange
from base.models import *
import datetime



def populate():
    print 'Creating Interests...'

    interestslist = create_interests()

    User.objects._create_user('admin', 'a@a.a', 'admin', True, True)

    print 'Done'
    print 'Creating Users...'

    userdata = '''Orla;Alvarez;erat@utodio.edu
Tobias;Randall;nulla.ante.iaculis@velsapien.co.uk
Vivien;Roberts;Suspendisse@non.net
Xander;Mitchell;amet.massa@vulputatemauris.ca
Stone;Fitzgerald;a.feugiat.tellus@mienimcondimentum.co.uk
Eleanor;Lambert;vitae@DuisgravidaPraesent.org
Angela;Olson;ut.aliquam@netus.edu
Macy;Freeman;justo@quam.ca
Gail;Parks;lacus.Cras.interdum@interdumligula.ca
Kirby;Robles;Cras@Quisque.edu
Marsden;Edwards;egestas.hendrerit@Aliquam.net
Flynn;Newton;Donec@odio.org
Jermaine;Chapman;vel@mollislectus.ca
Desiree;Sandoval;eu.tempor.erat@accumsan.org
Hector;Macias;montes.nascetur.ridiculus@aaliquet.ca
Tasha;Good;urna.convallis.erat@Vestibulumaccumsanneque.com
Levi;Wyatt;euismod.est@erosNam.edu
Thane;Bennett;lectus@Crassed.ca
Zahir;Mcfadden;egestas.a.dui@nequesed.edu
Wynter;Jefferson;a.sollicitudin.orci@Quisquevarius.ca
Rafael;Reyes;neque.Sed.eget@semperauctorMauris.org
Levi;Serrano;elementum.sem@Maecenasmalesuada.edu
Stone;Cote;ac.libero.nec@feugiatmetus.ca
Valentine;Berry;mauris@nunc.ca
Dorian;Mcmahon;magnis.dis@metus.ca
Winter;Thompson;non.dapibus@elitEtiam.com
Barrett;West;nibh.dolor.nonummy@lobortisnisinibh.com
Ignacia;Sanders;ut.erat.Sed@aptent.edu
Kennedy;Padilla;odio.Phasellus.at@malesuadaiderat.com
Rebekah;Williams;ante@velitSedmalesuada.org
Tad;Ramirez;odio@euismodenim.co.uk
Tara;Trevino;nascetur@egetdictum.edu
Trevor;Whitaker;vulputate.eu@conubianostraper.net
Ralph;Bowman;est.Nunc@Ut.ca
Libby;Sharp;lobortis@euismodestarcu.ca
Jaquelyn;Peters;tempus.risus@accumsaninterdum.org
Beatrice;Benson;tellus.lorem.eu@necimperdiet.edu
Raja;Hartman;neque.vitae.semper@aliquet.edu
Leila;Page;lacus@seddictumeleifend.org
Quon;Foreman;metus.facilisis@velmauris.ca
Judith;Frye;auctor.vitae.aliquet@ornare.com
Stuart;Thompson;lobortis.mauris.Suspendisse@cubilia.net
Rowan;Boone;vehicula@semper.edu
Darius;Bolton;augue@nonhendreritid.org
Danielle;Battle;parturient.montes@scelerisquemollis.edu
Willow;Medina;Nullam.suscipit.est@eu.co.uk
Denise;Myers;Fusce@suscipitestac.edu
Xanthus;Pruitt;eget.dictum@risusvariusorci.org
Shelly;Knowles;elit@Integerurna.ca'''

    userlist = []
    index = 1

    for x in userdata.split('\n'):
        f = x.split(';')

        user = add_user(f[0].lower() + str(index), f[0], f[1], f[2], '1234')
        user_profile = add_user_profile(user, 'Glasgow', index % (len(interestslist) - 1) + 1)
        index += 1

        userlist.append(user_profile)

    print 'Done'

    advertismentlist = []
    mtypeslist = create_meeting_types()
    courseslist = create_courses()

    print 'Creating advertisments'

    for x in range(0, 30, 1):
        day = randrange(1, 28)
        advertismentlist.append(add_advertisment(randrange(1, 4),
                                                 mtypeslist[randrange(0, len(mtypeslist) - 1)],
                                                 datetime.datetime(2015, 8, day, 6, 51, 1, 804000, None),
                                                 courseslist[0][randrange(1, len(courseslist[0]) - 1)],
                                                 interestslist[0], userlist[randrange(1, len(userlist) - 1)]))
        day = randrange(1, 28)
        advertismentlist.append(add_advertisment(randrange(1, 4),
                                                 mtypeslist[randrange(0, len(mtypeslist) - 1)],
                                                 datetime.datetime(2015, 8, day, 6, 51, 1, 804000, None),
                                                 courseslist[1][randrange(1, len(courseslist[1]) - 1)],
                                                 interestslist[6], userlist[randrange(1, len(userlist) - 1)]))
        day = randrange(1, 28)
        advertismentlist.append(add_advertisment(randrange(1, 4),
                                                 mtypeslist[randrange(0, len(mtypeslist) - 1)],
                                                 datetime.datetime(2015, 8, day, 6, 51, 1, 804000, None),
                                                 courseslist[2][randrange(1, len(courseslist[2]) - 1)],
                                                 interestslist[6], userlist[randrange(1, len(userlist) - 1)]))

    print 'Done'


def add_advertisment(duration, mtype, date, lesson, interest, user):
    adv = Advertisement.objects.get_or_create(duration=duration, type_of_meeting=mtype,
                                              date=date, lesson=lesson, advInterest=interest[0], user=user)
    return adv


def add_user(username, firstname, last_name, email, password):
    user = User.objects._create_user(username, email, password, False, False)
    user.first_name = firstname
    user.last_name = last_name
    user.save()
    return user


def add_user_profile(user, city, interest):
    profile = UserProfile.objects.get_or_create(user=user, city=city)[0]
    profile.userInterest.add(interest)
    profile.save()
    return profile


def create_interests():
    interests = [Interest.objects.get_or_create(category='Computer Science'),
                 Interest.objects.get_or_create(category='Biology'),
                 Interest.objects.get_or_create(category='Psychology'),
                 Interest.objects.get_or_create(category='Arts'),
                 Interest.objects.get_or_create(category='Physics'),
                 Interest.objects.get_or_create(category='History'),
                 Interest.objects.get_or_create(category='Mathematics'),
                 Interest.objects.get_or_create(category='Chemistry'),
                 Interest.objects.get_or_create(category='Biology'),
                 Interest.objects.get_or_create(category='Sex Education'),
                 Interest.objects.get_or_create(category='Medicine')]
    return interests


def create_courses():
    cs_courses = ['Python programming', 'MATLAB programming', 'C++ programming', 'Data Structures',
                  'Web Design', 'Django', 'Machine Learning', 'Networking', 'Operating systems']

    chem_courses = ['General Chemistry', 'Analytical Chemistry', 'Inorganic Chemistry', 'Nuclear Chemistry',
                    'Organic Chemistry', 'Theoretical Chemistry']

    math_courses = ['Trigonometry', 'Algebra', 'Probability theory', 'Calculus', 'Sequences', 'Series',
                    'Vector analysis', 'Number theory']

    return cs_courses, chem_courses, math_courses


def create_meeting_types():
    types = ['Skype meeting', 'Cafe meeting', 'Library meeting', 'Home meeting']
    return types


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()