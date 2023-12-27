from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import kategori, produk
from .form import FormProduk
from django.shortcuts import redirect

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def hapus_data(request, data_id):
    data = produk.objects.get(id=data_id)
    data.delete()
    return redirect("produk")

def produk_data(request):
    submitted = False
    if request.method == "POST":
        form = FormProduk(request.POST, request.FILES)
        if form.is_valid():
            simpanData = produk.objects.create(
                namaproduk = form.cleaned_data.get("namaproduk"),
                harga=form.cleaned_data.get("harga"),
                kategori=form.cleaned_data.get("kategori"),
            )
            simpanData.save()
            return HttpResponseRedirect("/produk?submitted=True")
    else:
        form = FormProduk
        if "submitted" in request.GET:
            submitted = True

    data = produk.objects.all()
    form = FormProduk
    contenxt = {
       "Judul":"Selamat Datang",
       "subjudul":"Toko Buku",
       "data": data,
       "form": form,
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(contenxt, request))

def detail_produk(request, id):
    produk = produk.objrcts.get(id==id)
    template = loader.get_template("detikProduk.html")
    context={
        "produk": produk,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("produk.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())
