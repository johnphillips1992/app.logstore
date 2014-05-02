from django.conf.urls.defaults import patterns, url

from tamu.coa.app.logstore.views import LogView


urlpatterns = patterns('',
    url('^/$', LogView.as_view(), name='log-view'))
