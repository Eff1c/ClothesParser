from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.IndexView.as_view(), name='default_index'),
    path('sex=<slug:sex>', views.index, name='index'),
    path('clothing_type=<slug:clothing_type>', views.index, name='index'),
    path('sex=<slug:sex>/clothing_type=<slug:clothing_type>', views.index, name='index'),

    path('about/', views.About.as_view(), name='about'),
    path('search', views.search, name='search'),
]
