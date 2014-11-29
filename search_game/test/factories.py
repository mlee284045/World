import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Sequence(lambda i: 'User{}'.format(i))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'search_game.City'

    name = factory.Sequence(lambda i: 'country{}'.format(i))
    # well created factories can populate a database pretty easily


class BalanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'search_game.Balance'
