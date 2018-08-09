from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details')
    # path(r'^details/(?P<id>\d+)/$', views.details, name='details')
]


