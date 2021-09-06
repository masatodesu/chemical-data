from django.urls import path

from . import views

#app_name = 'main'

urlpatterns=[
   
    #path('import/', views.PostImport.as_view(), name='import'),
    #path('', views.PostIndex.as_view(), name='index'),
    #path('export/', views.post_export, name='export'),
    path('list', views.list, name='list'),
    path('form_input', views.form_input, name='form_input'),
    path('form_process', views.form_process, name='form_process'),
    path('crud_new', views.crud_new, name='crud_new'),
    path('crud_create', views.crud_create, name='crud_create'),
    path('', views.list2, name='list2'),
    path('import/', views.csvimport, name='csvimport'),
    path('export/', views.csvexport, name='csvexport'),
]

