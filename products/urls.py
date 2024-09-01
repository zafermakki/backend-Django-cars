from django.urls import path
from . import views

urlpatterns = [
    path('categories/', view= views.getCategories),
    path('<int:id>/', view= views.getProductsByCatId),
    path('', view= views.getProducts)
    
]
