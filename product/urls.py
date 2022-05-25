from django.urls import path,include
from . import views
from .views import ProductListView,ProductDetailView


urlpatterns = [
    #path('',views.home,name='blog-home'),
    path('',ProductListView.as_view(),name='product-home'),#class based view
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
]