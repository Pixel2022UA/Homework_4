from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.generate, name="generate-student"),
    path("generate-students/", views.generate_set_students, name="generate-students")
]