from django.conf.urls import url

from . import views

app_name = 'classify'
urlpatterns = [
    url(r'^$', views.multi2, name='multi'),
    url(r'^hot/$', views.tea, name='tea'),
    url(r'^tea/$', views.tea, name='tea'),
    #url(r'^(?P<question_id>[0-9]+)/ans/$', views.tea, name='tea'),
]