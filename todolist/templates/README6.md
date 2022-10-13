## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan programming untuk sebuah aplikasi atau sistem yang tidak bisa diubah saat sedang proses. Hal ini dikarenakan metode pemanggilan function atau request yang hanya bisa dilakukan satu-satu (synchronous). Asynchronous programming adalah paradigma untuk sebuah sistem yang bisa update atau berubah tanpa harus dijalankan ulang. Hal ini dikarenakan sistem bisa multitasking dan menjalankan banyak hal sekaligus (sambil jalan sambil update)

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan program yang bergantung pada 'event' yang terjadi pada sistem atau aplikasi. Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dll.

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
AJAX (Asynchronous JavaScript And XML) memiliki kemampuan untuk mengubah isi html / tampilan page tanpa harus mengubah file/data yang tentunya membutuhkan refresh. AJAX juga mampu membuat HTTP POST dan GET request sendirinya. Dengan ajax, kita bisa mensubmit atau mengambil data dan langsung menampilkannya di web.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya memulai dengan membuat perubahan pada views.py sesuai dengan persyaratan yang dituliskan pada soal, yakni membuat fungsi bernama todolist_json yang berfungsi untuk mengembalikan seluruh data task dalam bentuk json lalu pengembalikan data task tersebut akan diambil menggunakan AJAX GET. Lalu membentuk file baru bernama todolist_add pada views.py serta membuat perubahan pada todolist.html untuk menyambungkan AJAX.