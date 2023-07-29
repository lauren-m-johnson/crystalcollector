from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crystals/<int:crystal_id>/add_aquired/', views.add_aquired, name='add_aquired'),
    path('props/', views.PropList.as_view(), name='props_index'),
    path('props/<int:pk>/', views.PropDetail.as_view(), name='props_detail'),
    path('props/create/', views.PropCreate.as_view(), name='props_create'),
    path('props/<int:pk>/update/', views.PropUpdate.as_view(), name='props_update'),
    path('props/<int:pk>/delete/', views.PropDelete.as_view(), name='props_delete'),
]