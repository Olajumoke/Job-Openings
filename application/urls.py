from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^display/(?P<pk>[0-9]+)/$', views.QuestionnaireDisplay, name='display'),
	url(r'^process/(?P<pk>[0-9]+)/$', views.QuestionnaireProcess, name = 'process'),
	url(r'^results/', views.QuestionnaireResults, name ='results'),
	url(r'^form/(?P<pk>[0-9]+)/$', views.new_form, name='new_form'),
	url(r'^rsa/(?P<pk>[0-9]+)/$', views.rsa, name='rsa'),
]
