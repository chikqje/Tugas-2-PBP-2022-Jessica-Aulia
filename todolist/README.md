link HEROKU
https://tugas2pbpjessica.herokuapp.com/todolist/


### 1. Apa kegunaan {% csrf_token %} pada elemen ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?

CSRF (Cross Site Request Forgery) adalah serangan eksploitasi web yang memaksa pengguna tanpa sadar mengirimkan/melakukan sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu.

Aplikasi web akan mengeksekusi dan menanggapi request tersebut yang sebenarnya bukan keinginan dari pengguna. Dengan begitu, jika website tersebut menerima request tanpa CSRF token yang tepat, maka request tersebut akan ditolak.

Dengan tidak adanya {% csrf_token %} maka form tersebut tidak adanya sebuah csrf_token sehingga penyerang/hacker dapat melakukan CSRF terhadap request yang berhubungan dengan form tersebut.


### 2. Apakah kita dapat membuat elemen "< form >" secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.

Pembuatan suatu form secara manual dapat dilakukan tanpa harus  menggunakan {{ form.as_table }}. Kita dapat menggunakan elemen < form >, kemudian menentukan request dari suatu form, dan mengatur kemana form akan dikirim dengan mengatur attribute action. Kemudian kita harus mengisi form tersebut dengan input field yang bisa digunakan di html, serta pastikan juga terdapat < input type="submit" > untuk meng-submit form tersebut . Terakhir kita bisa mengatur routing dan function akan memproses data yang dikirimkan form tersebut.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1.) Pengguna akan mengisi form
2.) Setelah itu data mereka yang sudah diisi akan disimpan pada browser/internet pengguna. 
3.) Setelah pengguna menekan tombol submit, form akan terkirim sebagai HTTP request POST. 
4.) Data akan diterima oleh server saat user mengisi form tersebut
5.) Data yang telah diisi pada form akan disimpan terlebih dahulu oleh browser user.
6.)Setelah user tekan tombol submit, maka form tersebut akan terkirim sebagai HTTP request dengan method dan url yang sudah ditentukan oleh attribute dari form tersebut. 
7.) Data tersebut kemudian akan diterima oleh server yang dituju url form tersebut. 
8.) Data tersebut akan disimpan ke dalam database.
9.) Jika data ingin ditampilkan, kita dapat menampilkan data tersebut di template HTML. 



### 4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Menjalankan environment pada cmd lalu membuat aplikasi baru dengan manage.py startapp bernama todolist serta menambahkan app tersebut pada INSTALLED_APP yang ada pada settings.py. Membuat sebuah class pada models.py yang berisikan empat variabel, yakni usernames, date, title, dan description dengan fieldtype masing-masing yang berbeda. Membuat sebuah file baru bernama forms.py yang akan meng-import class dari models.py, lalu membentuk class baru dengan ModelForm yang tersambung pada class models.py.

Buat sebuah fungsi baru pada views.py untuk me-return render dari sebuah parameter request dengan bentuk html, lalu membuat folder templates yang akan berisikan code html dengan menambahkan beberapa fitur (salah satunya button yang akan tersambung pada fungsi di views.py). Membentuk beberapa fungsi baru pada views.py, seperti fungsi register, login, logout, hingga fungsi untuk membuat form. Bentuk file html register, login sesuai dengan template yang telah diberikan dan file html createtask yang akan berisikan tabel form untuk meminta input user. Sambungkan setiap fungsi pada views.py dengan file html melalui render.

Merestriksi halaman utama todolist dengan menambahkan @login_required(login_url='') agar halaman hanya dapat diakses setelah user login serta membuat atau menambahkan cookie dengan menambahkan data last_login dan menampilkannya ke halaman utama todolist.

Pada urls.py, import setiap fungsi pada views.py, lalu masukan path pada urlpatterns sesuai dengan fungsinya masing-masing. Untuk dapat mengakses django admin, lakukan perintah createsuperstar pada commandprompt dan buatlah akun, kemudian pada file admin.py masukkan admin.site.register(Task) agar form yang diinput user dapat masuk pada django admin.
