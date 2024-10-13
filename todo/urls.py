from django.urls import path
from . import views
urlpatterns=[
    path('edit/',views.edit,name='edit'),
    path('',views.whattodo,name='whattodo'),
    path('<int:id>/',views.delete,name='delete'),
]