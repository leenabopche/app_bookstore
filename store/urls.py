from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # 👈 root URL goes to login view
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show_cart'),
]

