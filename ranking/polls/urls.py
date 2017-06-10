from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^new/$', views.index, name='new'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^about/$', views.about, name='about'),
    url(r'^brand/$', views.brand, name='brand'),
    url(r'^find/$', views.find, name='find'),
    url(r'^(?P<question_id>[0-9]+)/rankboard/$', views.rankboard, name='rankboard'),
    url(r'^(?P<question_id>[0-9]+)/information/$', views.information, name='information'),
    url(r'^(?P<question_id>[0-9]+)/store1/$', views.store1, name='store1'),
    url(r'^(?P<question_id>[0-9]+)/store2/$', views.store2, name='store2'),
    url(r'^(?P<question_id>[0-9]+)/store3/$', views.store3, name='store3'),
    url(r'^(?P<question_id>[0-9]+)/store4/$', views.store4, name='store4'),
    url(r'^(?P<question_id>[0-9]+)/store5/$', views.store5, name='store5'),
    url(r'^(?P<question_id>[0-9]+)/store6/$', views.store6, name='store6'),
    url(r'^(?P<question_id>[0-9]+)/store7/$', views.store7, name='store7'),
    url(r'^(?P<question_id>[0-9]+)/store8/$', views.store8, name='store8'),
    url(r'^(?P<question_id>[0-9]+)/store9/$', views.store9, name='store9'),
    url(r'^(?P<question_id>[0-9]+)/store10/$', views.store10, name='store10'),
	url(r'^multi/$', views.multi, name='multi'),
    # url(r'^tea/$', views.tea, name='tea'),
]

