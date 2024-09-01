from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddSale),
    path('<int:id>/', view= views.getByUser)
]
