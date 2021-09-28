from django.urls import path

from . import views



urlpatterns=[
    path('list', views.list, name='list'),
    path('crud_new', views.crud_new, name='crud_new'),
    path('crud_create', views.crud_create, name='crud_create'),
    path('list2', views.list2, name='list2'),
    path('import/', views.csvimport, name='csvimport'),
    path('export/', views.csvexport, name='csvexport'),
    path('data', views.ChemicalList.as_view(), name= 'data'),
    path('top', views.top, name='top'),
    path('test', views.test, name='test'),
    path('test2', views.test2, name='test2')
    
]

