from django.db import models

# Create your models here.
class kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama}"
    
class  produk(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    namaproduk = models.CharField(max_length=100)
    harga = models.IntegerField()

    def __str__(self):
        return f"{self.namaproduk} {self.harga}"