from django.test import TestCase
from django.utils.timezone import now
from django.db.models import F
from api.models import User, Continent, Country, City


class UserTestCase(TestCase):

    def setUp(self):
        self.continent = Continent.objects.create(name="Europe")
        self.country = Country.objects.create(name="Finland", continent=self.continent)
        self.city = City.objects.create(name="Oulu", country=self.country)
        self.user = User.objects.create(username="username", password="password",
                                   name="Name", surname="Surname",
                                   birth_date=now(), email="email", city=self.city)

    def test_get_user_by_username(self):
        """
            Getting user by username
        """
        user_db = User.objects.get(username=self.user.username)
        self.assertEqual(self.user.password, user_db.password)

    def test_update_user_karma(self):
        """
            Updating user karma
        """
        User.objects.filter(username=self.user.username).update(karma=F('karma') + 1)
        user_db = User.objects.get(username=self.user.username)
        self.assertEqual(self.user.karma + 1, user_db.karma)

    def test_delete_user(self):
        """
            Deleting user
        """
        User.objects.filter(username=self.user.username).delete()
        user_db = User.objects.filter(username=self.user.username).first()
        self.assertIsNone(user_db)

    def test_update_user_surname(self):
        """
            Updating user surname
        """
        self.user.surname = 'NewSurname'
        self.user.save(update_fields=['surname'])
        user_db = User.objects.get(username=self.user.username)
        self.assertEqual('NewSurname', user_db.surname)

    def test_get_highest_karma_top_2_users(self):
        """
            Getting top 2 users with highest karma
        """
        User.objects.create(username="username2", password="password",
                            name="Name", surname="Surname", karma=10,
                            birth_date=now(), email="email", city=self.city)
        User.objects.create(username="username3", password="password",
                            name="Name", surname="Surname", karma=20,
                            birth_date=now(), email="email", city=self.city)

        users = User.objects.filter().order_by('-karma')[:2]

        self.assertEqual(2, users.__len__())
        self.assertEqual(20, users[0].karma)
        self.assertEqual(10, users[1].karma)


