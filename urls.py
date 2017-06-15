from django.conf.urls import url
from Portal import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^listing/(?P<code>[A-Z]{3}[0-9]{3})/$', views.view_listing, name='view_listing'),
  url(r'^post-an-ad/$', views.post_an_ad, name='post_an_ad'),
  url(r'^post-an-ad/success/(?P<code>[A-Z]{3}[0-9]{3})/$', views.post_an_ad_success, name='post_an_ad_success'),
  url(r'^help/$', views.help, name='help'),
  url(r'^admin-tools/prune/(?P<pin>[0-9]{8})/$', views.prune, name='prune'),
]