from django.conf.urls import url
from . import views
from login.views import hiw,cform

urlpatterns = [
    url(r'^$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^login/profile/$', views.profile, name='oh'),
    url(r'^send/$', views.send, name='send'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^display$', views.Display, name='display'),
    url(r'^search/$', views.search, name='search'),
    url(r'^hiw/$', hiw.as_view(), name='hiw'),
    url(r'^cform/$', cform.as_view(), name='cform')

]
