from django.test import TestCase
from base.models import Advertisement
from django.core.urlresolvers import reverse


class AdvertMethodTests(TestCase):

    def test_ensure_duration_is_positive(self):
        ad = Advertisement(active=True, duration=-1, type_of_meeting='Skype', date='2012-09-04 06:00', advInterest_id=2, user_id=4)
        ad.save()  # Save method converts the ad.duration to the absolute value i.e. from negative to positive
        self.assertEqual((ad.duration >= 0), True)

    def test_ensure_active_is_boolean(self):
        ad = Advertisement(active=True, duration=-1, type_of_meeting='Skype', date='2012-09-04 06:00', advInterest_id=2, user_id=4)
        ad.save()
        self.assertIsInstance(ad.active, bool)


class IndexViewTests(TestCase):

    def test_index_view_with_no_interests(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)