from django.contrib import admin
from django.urls import path
from omop_viewer.views import patViewer
from omop_viewer.views import search
import omop_viewer.views as views


urlpatterns = [
    path('', patViewer),
    path('search/', search),
    path('encounter/<int:visit_occurrence_id>/', views.encounter, name='encounter'),
]
