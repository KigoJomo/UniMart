from django.urls import path
from .import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("shop/", views.shop, name="shop"),
    path("products/<str:category>/", views.get_products, name="get_products"),
    path('search/', views.search_products, name='search_products'),
]

