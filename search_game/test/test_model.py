from datetime import timedelta, datetime
from django.contrib.auth.models import User
from django.test import TestCase
from search_game.models import City, Balance


class CityModelTest(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            name='test-city',
            country='TC',
            latitude=100,
            longitude=100,
        )

    def test_arrive(self):
        # check to see if the created city should have default values of False in city.current and city.visited
        self.assertFalse(self.city.current)
        self.assertFalse(self.city.visited)
        # method Arrive changes the current attr and visited attr from default False to True
        self.city.arrive()

        # Check to see if city.current and city.visited is True after arriving at the city
        self.assertTrue(self.city.current)
        self.assertTrue(self.city.visited)

    def test_leave(self):
        self.city.arrive()
        self.assertTrue(self.city.current)
        self.city.leave()
        self.assertFalse(self.city.current)


class BalanceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test-user')
        self.balance = Balance.objects.create(
            user=self.user,
            start=self.user.date_joined,
            end=(self.user.date_joined + timedelta(days=14))
        )

    def test_add_money(self):
        self.assertEqual(self.balance.money, 5000.00)
        self.assertEqual(self.balance.add_money(545.45), 5545.45)
        self.assertEqual(self.balance.money, 5545.45)

    def test_minus_money(self):
        self.assertEqual(self.balance.money, 5000.00)
        self.assertEqual(self.balance.minus_money(545.45), 4454.55)
        self.assertEqual(self.balance.money, 4454.55)

    def test_update_time(self):
        new_time = datetime.date
        self.assertEqual(self.balance.update_time(new_time), new_time)

    def test_get_time_left_hours(self):
        self.assertEqual(self.balance.get_time_left_hours(), 14 * 24)

    def test_get_time_left_days(self):
        self.assertEqual(self.balance.get_time_left_days(), 14)
