from django.urls import path
from . import views

urlpatterns = [
    # path('produk' , views.produk, name='produk'),
    # path('kategori' , views.kategori, name='kategori'),
    path('home' , views.home, name='home'),
    path("produk/", views.produk_data, name="produk"),
    path("produk/detail/<int:id>", views.detail_produk, name="detail_produk"),
    path("contact/", views.contact, name = "contact"),
    path("about/", views.contact, name = "about"),
    path("hapus_data/<data_id>", views.hapus_data, name="hapus-data")
]