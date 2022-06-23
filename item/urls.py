from django.urls import path
from item import views

urlpatterns = [
    path('post/', views.CaretgoryView.as_view()),
    path("post/<int:categroy_id>/", views.CaretgoryView.as_view()),
]