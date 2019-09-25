from django.conf.urls import url, include

from .views import WorkList


urlpatterns = [
    url(r'^$', WorkList.as_view(), name='work-list'),
]
