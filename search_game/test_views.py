from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from search_game.test.factories import UserFactory, CityFactory, BalanceFactory


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user',
            password='test-pw'
        )
        test_user = UserFactory()
        test_city = CityFactory()
        test_balance = BalanceFactory()

        print test_user + ' ' + test_balance + ' ' + test_city

    def test_home_page(self):
        # Tests to see if home page is rendered if user is not logged in
        response = self.client.get(reverse('home'))
        self.assertIn('<a href="{}">Login</a>'.format(reverse('login')), response.content)

    def test_home_page_authenticated(self):
        # Tests to see if home page is rendered if user is logged in

        user = User.objects.create_user(username='profile-user', email='test@test.com', password='profile-pw')
        self.client.login(
            username='profile-user',
            password='profile-pw'
        )
        response = self.client.get(reverse('home'))
        self.assertInHTML('<p>Please carry on to your profile.</p>', response.content)
        self.assertEqual(response.context['user'].username, user.username)

    def tet_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(User.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))
