from django.contrib import admin
from .models import produk, kategori

# Register your models here.

class produkBuku(admin.ModelAdmin):
    list_display = ("namaproduk", "harga",)

admin.site.register(produk, produkBuku)
admin.site.register(kategori)