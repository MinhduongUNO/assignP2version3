from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('portfolio.urls', namespace='portfolio')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^password-change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', views.password_reset_confirm,
       name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
       views.password_reset_complete,
       name='password_reset_complete'),
]
