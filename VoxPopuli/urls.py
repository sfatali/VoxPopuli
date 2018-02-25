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
from api.models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

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

class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem

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
        model = Idea

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
        model = Event

        fields = ('user', \
                'idea',\
                'event_date', \
                'created_date', \
                'updated_date', \
                'title', \
                'body', \
                'status')

class UserEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvent

        fields = ('user', \
                'event',\
                'created_date')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvent

        fields = ('post_id', \
                'user',\
                'comment',\
                'created_date')

class ReportHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvent

        fields = ('post_id', \
                'user',\
                'reason',\
                'created_date')

class UserSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvent

        fields = ('post_id', \
                'user',\
                'created_date')


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        #using [] instead of () because it needs to be a tuple or list explicitly
        fields = ['name']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country

        fields = ('name','continent')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City

        fields = ('name','country')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserEventViewSet(viewsets.ModelViewSet):
    queryset = UserEvent.objects.all()
    serializer_class = EventSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = EventSerializer

class ReportHistoryViewSet(viewsets.ModelViewSet):
    queryset = ReportHistory.objects.all()
    serializer_class = EventSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = EventSerializer

class ContinentViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'problems', ProblemViewSet)
router.register(r'ideas', IdeaViewSet)
router.register(r'events', EventViewSet)
router.register(r'userevents', UserEventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reporthistory', ReportHistoryViewSet)
router.register(r'usersubscriptions', UserSubscriptionViewSet)
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


