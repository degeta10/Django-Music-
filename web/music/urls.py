from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^rock',views.rock,name='rock'),
]