from django import forms
from .models import kategori


class FormProduk(forms.Form):
    kategori = forms.ModelChoiceField(queryset=kategori.objects.all())
    namaproduk = forms.CharField()
    harga = forms.IntegerField()