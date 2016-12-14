from django.conf.urls import url

from projects import views

app_name = 'projects'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
