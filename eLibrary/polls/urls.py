from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('reqmember', views.reqmember, name='reqmember'),
    path('updateinfo', views.updateinfo, name='updateinfo'),
    path('requpdate', views.requpdate, name='requpdate'),
]
