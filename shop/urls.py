from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="ShopHome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="Trackingstatus"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.ProductView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('products/', views.product_list, name='product_list'),

]
