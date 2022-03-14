from django.conf.urls import include, url
from django.contrib import admin
from crudapp import views



urlpatterns =[
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/$', views.retrieve, name= "retrieve"),
    url(r'^add/$', views.AddDetail, name= "add"),
    url(r'^delete/(?P<id>[0-9]+)$', views.deleteview, name='delete'),
    url(r'^update/(?P<id>[0-9]+)$', views.updateview, name='update'),
    url(r'^addlist/$', views.Add_Marklist),
    url(r'^alltable/$', views.all_table),
    url(r'^marklist/$', views.Stu_Marklist),
    url(r'^subwise/$', views.Sub_wise_marks),
    url(r'^hlmark/$', views.high_lower_submark),
    url(r'^delmarklist/(?P<id>[0-9]+)$', views.deletemark)
   ]