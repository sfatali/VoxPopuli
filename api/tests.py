from django.test import TestCase
from django.utils.timezone import now
from api.models import User, Continent, Country, City, Problem


class UserTestCase(TestCase):
    def setUp(self):
        print("test set up!")

        continent = Continent.objects.create(name="Europe")
        country = Country.objects.create(name="Finland", continent=continent)
        city = City.objects.create(name="Oulu", country=country)
        user = User.objects.create(username="username", password="password",
                            name="Name", surname="Surname",
                            birth_date=now(), email="email",
                            country=country, city=city)
        #problem = Problem.objects.create(user=user, title="meh title", body="body",
                               #country=country, city=city, tags=['sadness', 'meh'])

    def test_user_create(self):
        user_db = User.objects.get(id=1)
        self.assertEqual("username", user_db.username)

