from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index.html$', views.index,name='index'),
    url(r'^impressum.html',views.impressum,name='impressum'),
    url(r'^howto.html',views.howto,name='howto'),
    url(r'^createtodo.html','todoapp.views.createtodo',name='createtodo'),
    url(r'^delete/([0-9]*)/$',views.delete),
    url(r'^edit/([0-9]*)/$',views.edit)

]