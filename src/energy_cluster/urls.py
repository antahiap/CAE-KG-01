from django.urls import path
from . import views

app_name = 'dataviewer'

# path('', views.get_runs, name='index'),
urlpatterns = [
    path(
        '<str:run_name>/',
        views.ClusterOrder.as_view(), name='energy_cluster'
        ),
        ]
