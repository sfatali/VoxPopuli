from django.test import TestCase
from django.utils.timezone import now
import uuid
from api.models import User, Continent, Country, City, Problem, Comment
import datetime
from django.db.models import Q


class UserTestCase(TestCase):

    def setUp(self):
        self.continent = Continent.objects.create(name="Europe")
        self.country = Country.objects.create(name="Finland", continent=self.continent)
        self.country2 = Country.objects.create(name="Sweden", continent=self.continent)
        self.city = City.objects.create(name="Oulu", country=self.country)
        self.city2 = City.objects.create(name="Helsinki", country=self.country)
        self.city3 = City.objects.create(name="Malmo", country=self.country2)
        self.user = User.objects.create(username="username", password="password",
                                   name="Name", surname="Surname",
                                   birth_date=now(), email="email", city=self.city)
        self.problem1 = Problem.objects.create(id=uuid.uuid4(), user=self.user, title="Mega problem in Oulu",
                                              body="Description of the mega problem. Sad.",
                                              city = self.city, tags=["mega", "hyper"],
                                                created_date=datetime.datetime(2016, 3, 23, 16, 38, 46, 271475))
        Problem.objects.create(id=uuid.uuid4(), user=self.user, title="Mega problem in Helsinki",
                                              body="Description of the mega problem",
                                              city=self.city2, tags=["hyper", "sad"], score=20,
                                                created_date=datetime.datetime(2017, 3, 23, 16, 38, 46, 271475))
        Problem.objects.create(id=uuid.uuid4(), user=self.user, title="Mega problem in Malmo. Sad.",
                               body="Description of the mega problem",
                               city=self.city3, tags=["magic"], score=50,
                               created_date=datetime.datetime(2018, 3, 23, 16, 38, 46, 271475))

    def test_get_user_problems(self):
        """
            Problems of a certain user
        """
        user_problems = Problem.objects.filter(user=self.user).order_by('-created_date')
        self.assertEqual(3, user_problems.__len__())

    def test_get_10_most_voted_problems_in_country(self):
        """
            Top 10 problems in a certain country
        """
        problems = Problem.objects.prefetch_related('city__country').\
            filter(city__country=self.country).\
            order_by('-score')[:10]

        self.assertEqual(2, problems.__len__())
        self.assertEqual(20, problems[0].score)

    def test_get_10_most_voted_problems_in_continent(self):
        """
            Top 10 problems in a certain continent
        """
        problems = Problem.objects.prefetch_related('city__country__continent').\
            filter(city__country__continent=self.continent).\
            order_by('-score')[:10]

        self.assertEqual(3, problems.__len__())
        self.assertEqual(50, problems[0].score)

    def test_filter_problems_by_tag_overlap(self):
        """
            Getting problems, where at least 1 tag from a set is present
        """
        problems = Problem.objects.filter(tags__overlap=['hyper', 'magic']).order_by('-created_date')
        self.assertEqual(3, problems.__len__())

    def test_filter_problems_by_tag_contains(self):
        """
            Getting problems, where at all tags from a set is present
        """
        problems = Problem.objects.filter(tags__contains=['hyper', 'mega']).order_by('-created_date')
        self.assertEqual(1, problems.__len__())
        self.assertEqual(self.problem1.title, problems[0].title)

    def test_get_problems_by_year(self):
        """
            Getting problems from a certain year
        """
        problems = Problem.objects.filter(created_date__year=2018)
        self.assertEqual(1, problems.__len__())

    def test_problem_contains_string(self):
        """
            Search problems containing a string (in title, body, tags)
        """
        search_string = "sad"
        problems = Problem.objects.filter(Q(title__icontains=search_string)
                                          | Q(body__icontains=search_string)
                                          | Q(tags__overlap=[search_string]))
        self.assertEqual(3, problems.__len__())

