from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'search_game.views.home', name='home'),
    url(r'^register/$', 'search_game.views.register', name='register'),
    url(r'^profile/$', 'search_game.views.profile', name='profile'),
    url(r'^map/$', 'search_game.views.map', name='map'),
    url(r'^city/(?P<city_id>\d+)/$', 'search_game.views.city_view', name='city_view'),
    url(r'^profile/reset/$', 'search_game.views.reset', name='reset'),
    url(r'^profile/success/$', 'search_game.views.success', name='success'),
    url(r'^profile/failure/$', 'search_game.views.failure', name='failure'),
    url(r'^profile/work/$', 'search_game.views.work_start', name='work_start'),
    url(r'^profile/work/(?P<time>\d+)/$', 'search_game.views.work_complete', name='work_complete'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)
