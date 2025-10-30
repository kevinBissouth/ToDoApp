from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("work/", views.work, name='work'),
    path("add_tache/", views.add_tache, name='add_tache'),
    path("delete_tache/<int:id>/", views.delete_tache, name='delete_tache'),
    path('modifie_tache/<int:id>/', views.modifie_tache, name='modifie_tache'),
    # path("formulaire/", views.formulaire, name="formulaire"),
]