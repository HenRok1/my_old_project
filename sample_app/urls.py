from django.conf.urls import url

from sample_app.models import DiaryDay
from sample_app.views import DiaryDayView, DiaryRedirectView


urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        DiaryDayView.as_view(), name='diaryday'),

    url(r'^$', DiaryRedirectView.as_view(permanent=False), name='diary'),
]
