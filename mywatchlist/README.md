LINK : https://tugas2pbpjessica.herokuapp.com/mywatchlist/html/




1. Jelaskan perbedaan antara JSON, XML, dan HTML!

// JSON merupakan singkatan dari JavaScript Object Notation, yang didesain menjadi self-describing sehingga mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile. JSON dapat digunakan untuk menyimpan dan mengirimkan data. JSON memiliki format berupa text kode sehingga JSON banyak terdapat di banyak bahasa pemrograman.


// XML merupakan singkatan dari eXtensible Markup Language, yang didesain menjadi self-descriptive sehingga dengan membaca XML dapat mengerti informasi apa yang ingin disampaikan dari data tertulis. XML merupakan sebuah informasi yang dibungkus di dalam tag dengan struktur tree. Struktur tersebut dimulai dari root, branch, hingga berakhir pada leaves sehingga XML seringkali digunakan sebagai tempat untuk menyimpan dan mengirimkan data. 

// HTML merupakan singkatan dari HyperText Markup Language, yaitu bahasa markup language untuk membuat serta menyusun halaman dan aplikasi web. HTML digunakan untuk mendeskripsikan struktur dan layout pada web. HTML tidak dianggap sebagai bahasa pemrograman karena tak bisa memberikan fungsi yang dinamis. Umumnya, fungsi HTML menampilkan data dan mendeskripsikan struktur dari sebuah webpage namun, HTML merupakan sebuah bahasa yang telah ditentukan dengan implikasinya sendiri.


2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?


Data delivery merupakan sebuah proses mentransfer data dari suatu platform menuju ke suatu profil atau platform lainnya. Dalam Django, dimungkinkan bagi kita untuk mengirimkan data dari suatu stack ke stack lainnya, data-data tersebut dapat berbentuk dalam berbagai format, seperti JSON, XML, HTML, dan lainnya sehingga data delivery sangat diperlukan dalam mengimplementasikan sebuah platform.


3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.


- Diawali dengan mengaktifkan environment pada command prompt direktori yang dituju lalu menjalankan perintah startapp untuk membuat aplikasi baru bernama mywatchlist dan memasukkannya pada “INSTALLED APPS” yang ada pada settings.py django-app.

- Pada file settings.py di folder project_djanggo menambahkan ‘mywatchlist’, di dalam variable INSTALLED-APP.

- Pada file models.py di folder mywatchlist menambahkan potongan kode :
from django.db import models

class MyWatchList(models.Model):
    Watched = models.CharField(max_length=50)
    Title = models.TextField()
    Rating = models.IntegerField()
    Release_date = models.TextField()
    Review = models.TextField()

- Selanjutnya menjalankan perintah python manage.py makemigrations dilanjut dengan python manage.py migrate di cmd.

- Pada folder fixtures di folder mywatchlist membuat file bernama initial_mywatchlist_data.json dengan isi potongan kode :

//Berisikan data yang diminta
{
        "model":"mywatchlist.MyWatchList",
        "pk":1,
        "fields":{
            "Watched":"sudah ditonton",
            "Title":"Miracle in Cell No.7",
            "Rating": 4,
            "Release_date": "8 September 2022.",
            "Review": "Miracle in Cell No.7 film yang mengandung bawang dan membuat penonton kangen dengan sosok ayahnya "
        }

- Menjalankan sebuah perintah di cmd yaitu python manage.py loaddata initial_mywatchlist_data.json.

- Pada file views.py di folder mywatchlist menambahkan kode : 

def show_mywatchlist(request):
    return render(request, "mywatchlist.html",context)
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



- Pada folder templates di folder mywatchlist membuat sebuah file mywatchlist.html dengan isi :

<!-- {% extends 'base.html' %}

{% block content %}
<h1>Tugas 3 PBP</h1>

<h5>Nama: </h5>
<p>{{Nama}}</p>
<h5>NPM: </h5>
<p>{{NPM}}</p>

<table>
    <tr>
    <th>Watched</th>
    <th>Title</th>
    <th>Rating</th>
    <th>Release_date</th>
    <th>Review</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for datawishlist in list_barang %}
    <tr>
        <th>{{datawishlist.Watched}}</th>
        <th>{{datawishlist.Title}}</th>
        <th>{{datawishlist.Rating}}</th>
        <th>{{datawishlist.Release_date}}</th>
        <th>{{datawishlist.Review}}</th>
    </tr>
{% endfor %}
</table> -->


- Selanjutnya folder mywatchlist terdapat file bernama urls.py berisi kode :

from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml 
from mywatchlist.views import show_json 

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name= "show_xml"),
    path('json/', show_json, name="show_json"),
]


- Menambahkan kode path('wishlist/', include('wishlist.urls')), ke dalam urls.py di folder project_django.

- Pada file views.py di folder mywatchlist ditambahkan :

from django.shortcuts import render
from mywatchlist.models import MyWatchlist 


- Menambahkan potongan kode di fungsi show_mywatchlist yaitu :

data_mywatchlist = MyWatchList.objects.all()
context = {
    'list_barang': data_mywatchlist,
    'Nama': 'Jessica Aulia',
    'NPM' : '2106633512'}


- Terakhir adalah melakukan deployment aplikasi pada heroku dengan memasukkan API key dan nama aplikasi pada secret repositori github yang digunakan.






"Hasil Screenshot"

![postman html](https://user-images.githubusercontent.com/112611451/191648356-a926ddf6-468b-422e-997f-120424c8bde2.jpg)

![postman json](https://user-images.githubusercontent.com/112611451/191648365-90af2e45-bf1f-4f77-bc30-824d3e8c35ff.jpg)

![postman xml](https://user-images.githubusercontent.com/112611451/191648385-a3d9ed0e-8011-459f-8d03-923a84f53a7c.jpg)
