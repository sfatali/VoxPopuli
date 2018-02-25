from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Problem)
admin.site.register(Idea)
admin.site.register(Event)
admin.site.register(UserEvent)
admin.site.register(Comment)
admin.site.register(ReportHistory)
admin.site.register(UserSubscription)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)