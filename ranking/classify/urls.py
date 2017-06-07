from django.conf.urls import url

from . import views

app_name = 'classify'
urlpatterns = [
    url(r'^$', views.multi2, name='multi'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^tea/$', views.tea, name='tea'),
    url(r'^chew/$', views.chew, name='chew'),
    #url(r'^(?P<question_id>[0-9]+)/ans/$', views.tea, name='tea'),
]