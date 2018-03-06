"""VoxPopuli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
import events.models
import util.models
import ideas.models
import problems.models
import profiles.models
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = profiles.models.Profile

        """
        fields = ('username', \
                 'password', \
                 'name', \
                 'surname', \
                 'birth_date', \
                 'email', \
                 'registered_date', \
                 'karma', \
                 'country', \
                 'city')
        """
        fields = ('birth_date', \
                 'about', \
                 'karma', \
                 'city')


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = problems.models.Problem

        fields = ('user', \
                'created_date', \
                'updated_date', \
                'title', \
                'body', \
                'image', \
                'score', \
                'status', \
                'country', \
                'city', \
                'tags')


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ideas.models.Idea

        fields = ('user', \
                'created_date', \
                'updated_date', \
                'title', \
                'body', \
                'image', \
                'score', \
                'status', \
                'tags')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = events.models.Event

        fields = ('user', \
                'idea',\
                'event_date', \
                'created_date', \
                'updated_date', \
                'title', \
                'body', \
                'status')


class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = events.models.Attendance

        fields = ('user', \
                'event',\
                'created_date')


class EventCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = events.models.EventComment

        fields = ('event', \
                'user',\
                'comment',\
                'created_date')


class IdeaCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ideas.models.IdeaComment

        fields = ('idea', \
                'user',\
                'comment',\
                'created_date')


class ProblemCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = problems.models.ProblemComment

        fields = ('problem', \
                'user',\
                'comment',\
                'created_date')

"""
class EventReportHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = events.models.ReportHistory

        fields = ('post_id', \
                'user',\
                'reason',\
                'created_date')


class IdeaReportHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ideas.models.ReportHistory

        fields = ('post_id', \
                'user',\
                'reason',\
                'created_date')


class ProblemReportHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = problems.models.ReportHistory

        fields = ('post_id', \
                'user',\
                'reason',\
                'created_date')
"""


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'util.Continent'
        #using [] instead of () because it needs to be a tuple or list explicitly
        fields = ['name']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'util.Country'

        fields = ('name','continent')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'util.City'

        fields = ('name','country')


# ViewSets define the view behavior.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = profiles.models.Profile.objects.all()
    serializer_class = ProfileSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = problems.models.Problem.objects.all()
    serializer_class = ProblemSerializer


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = ideas.models.Idea.objects.all()
    serializer_class = IdeaSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = events.models.Event.objects.all()
    serializer_class = EventSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = events.models.Attendance.objects.all()
    serializer_class = EventSerializer


"""
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = EventSerializer

class ReportHistoryViewSet(viewsets.ModelViewSet):
    queryset = ReportHistory.objects.all()
    serializer_class = EventSerializer
"""


class ContinentViewSet(viewsets.ModelViewSet):
    queryset = util.models.Continent.objects.all()
    serializer_class = ContinentSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = util.models.Country.objects.all()
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = util.models.City.objects.all()
    serializer_class = CitySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet)
router.register(r'problems', ProblemViewSet)
router.register(r'ideas', IdeaViewSet)
router.register(r'events', EventViewSet)
router.register(r'userevents', AttendanceViewSet)
"""
router.register(r'comments', CommentViewSet)
router.register(r'reporthistory', ReportHistoryViewSet)
"""
router.register(r'continents', ContinentViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]


