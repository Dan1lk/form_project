from .views import index, done, update_feedback
from django.urls import path

urlpatterns = [
    path('done', done),
    path('', index),
    path('<int:id_feedback>', update_feedback),
]