

PERTANYAAN

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Pertama, permintaan yang masuk ke dalam server Django akan diproses melalui urls untuk diteruskan ke views yang didefinisikan oleh pengembang untuk memproses permintaan tersebut.

Views ini berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk.

Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya views akan memanggil query ke models dan database akan mengembalikan hasil dari query tersebut ke views.

Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai respons.


    # urls.py untuk melakukan routing terhadap fungsi views yang telah kita buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser.

    # Menampilkan data ke dalam HTML dari database Django lokal maupun data atau variabel yang kita definisikan ke dalam berkas views.py

    # Pada fungsi views yang telah kita buat, import models yang sudah dibuat sebelumnya ke dalam file views.py. Kita menggunakan class tersebut untuk melakukan pengambilan data dari database. Models.py ini file yang berhubungan langsung dengan database.



2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Virtual environment merupakan sebuah ruang lingkup virtual yang terisolasi dari dependencies utama. Virtual environment sangat berguna ketika kita membutuhkan depedencies yang beda-beda antara satu project dengan project yang lainnya berjalan pada 1 sistem yang sama.

    Ketika kita menginstal modul atau library menggunakan "pip", maka modulnya akan terinstal secara global. Mungkin bisa, jika kita membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, akan menjadi masalah. Misalnya pada hari ini kita membuat proyek aplikasi menggunakan django 1.2. Lalu aplikasi berjalan dengan sempurna menggunakan modul versi 1.2. Beberapa saat kemudian, django merilis versi terbarunya anggap saja versi 4.0. Selanjutnya kita mengupgrade modul. tetapi, aplikasi yang telah kita buat tidak bisa berjalan dengan modul versi terbaru ini, karena adanya perbedaan atau perubahan fungsi dan lainnya.Sementara itu, ada proyek lainnya yang harus menggunakan modul versi itu. Disinilah kita membutuhkan virtualenv, agar masing-masing aplikasi memiliki modulnya sendiri.





3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!
    # Pada file views.py di folder katalog membuat fungsi yang menerima parameter request dan mengembalikan render :  
    
    def show_katalog(request):
        return render(request, "katalog.html", context).

    # Pada folder katalog terdapat folder templates yang di dalamnya terdapat file katalog.html beserta isinya. Pada template isi tersebut terdapat code   
    
    <h5>Name: </h5> dan <h5>Student ID: 
    </h5> diubah menjadi <h5>Name: </h5> dan <h5>Student ID: </h5>
                    <p>Fill me!</p>     <p>Fill me!</p>                     <p>{{nama}}</p>     <p>{{NPM}}</p>

    Selain itu juga menambahkan {% for katalog in list_katalog_barang %}
                                    <tr>
                                        <th>{{katalog.item_name}}</th>
                                        <th>{{katalog.item_price}}</th>
                                        <th>{{katalog.item_stock}}</th>
                                        <th>{{katalog.rating}}</th>
                                        <th>{{katalog.description}}</th>
                                        <th>{{katalog.item_url}}</th>
                                    </tr>
                                {% endfor %}
                                </table>.



    # Pada folder katalog dengan file urls.py ditambahkan code from django.urls import path
        from katalog.views import show_katalog
        
        app_name = 'katalog'
        
        urlpatterns = [
        path('', show_katalog, name='show_katalog'),
                                                            ]
    yang berguna untuk melakukan routing terhadap fungsi views.py sehingga halaman HTML dapat dapat ditampilkan pada browser.

    # Pada folder project_django terdapat file urls.py dimana ditambahkan code path('katalog/', include('katalog.urls')).