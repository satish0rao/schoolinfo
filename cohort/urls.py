from django.conf.urls import patterns, url

from cohort import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'berkeley/', views.berkeley, name='detail'),
    url(r'd3/', views.d3_chart, name='d3_chart'),
    url(r'data/(?P<data_id>\d+)/$', views.data, name='d3_chart'),
    url(r'catch/(?P<filename>\w+.\w+)$', views.catch, name='catch'),
)
