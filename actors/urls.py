from . import views
from django.urls import path

urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
