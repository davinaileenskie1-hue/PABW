# -*- coding: utf-8 -*-
"""Generate Laporan Praktikum Modul 3 - Blade Template Laravel (.docx)."""
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = r"D:\xampp\htdocs\PABW\Praktikum_3\PRK_3"
IMG = os.path.join(BASE, "laporan", "img", "01-halaman-students.png")
OUT = os.path.join(BASE, "laporan", "707012500135_Davin Aileenskie Sofiandy_Modul_03.docx")

doc = Document()

# ---------- basic document styling ----------
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

for lvl in (1, 2, 3):
    st = doc.styles["Heading %d" % lvl]
    st.font.name = "Calibri"
    st.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
    st.font.size = Pt({1: 15, 2: 13, 3: 12}[lvl])


def add_code(code, lang_comment=None):
    """Insert a shaded, bordered monospace code block."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(4)
    pf.space_after = Pt(8)
    pf.left_indent = Inches(0.1)
    pf.line_spacing = 1.0
    run = p.add_run(code)
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    rf.set(qn("w:ascii"), "Consolas")
    rf.set(qn("w:hAnsi"), "Consolas")
    rf.set(qn("w:cs"), "Consolas")
    ppr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F4F4F4")
    ppr.append(shd)
    borders = OxmlElement("w:pBdr")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "4")
        e.set(qn("w:color"), "CCCCCC")
        borders.append(e)
    ppr.append(borders)
    return p


def para(text="", bold=False, italic=False, align=None, size=None, space_after=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    if align is not None:
        p.alignment = align
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    return p


def bullet(text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_lead:
        p.add_run(bold_lead).bold = True
    p.add_run(text)
    return p


def numbered(text, bold_lead=None):
    p = doc.add_paragraph(style="List Number")
    if bold_lead:
        p.add_run(bold_lead).bold = True
    p.add_run(text)
    return p


def caption(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(10)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def fill_table(rows, col_widths=None, header=True):
    t = doc.add_table(rows=0, cols=len(rows[0]))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for ci, val in enumerate(row):
            cp = cells[ci].paragraphs[0]
            cr = cp.add_run(str(val))
            cr.font.size = Pt(11)
            if header and ri == 0:
                cr.bold = True
        if header and ri == 0:
            for c in cells:
                tcpr = c._tc.get_or_add_tcPr()
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:fill"), "DCE6F1")
                tcpr.append(shd)
    if col_widths:
        for row in t.rows:
            for ci, w in enumerate(col_widths):
                row.cells[ci].width = Inches(w)
    return t


# ================= COVER =================
sp = doc.add_paragraph()
sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
sp.add_run("\n[ Tempatkan Logo Institusi di Sini ]\n").font.size = Pt(11)

para("LAPORAN PRAKTIKUM", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=20, space_after=0)
para("PENGEMBANGAN APLIKASI BERBASIS WEB", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=16, space_after=6)
para("Modul 3: Blade Template Laravel", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=24)

para("Disusun Oleh:", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=4)
for line in [
    "Nama\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0: Davin Aileenskie Sofiandy",
    "NIM\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0: 707012500135",
    "Kelas\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0: D4SIKC-49-04",
    "Mata Kuliah\u00a0\u00a0\u00a0\u00a0: Pengembangan Aplikasi Berbasis Web",
    "Dosen Pengampu: ........................................................",
]:
    para(line, align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=2)

for _ in range(4):
    doc.add_paragraph()
para("TELKOM UNIVERSITY", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=0)
para("FAKULTAS ILMU TERAPAN", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0)
para("JURUSAN S1 TERAPAN SISTEM INFORMASI KOTA CERDAS", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0)
para("TAHUN AJARAN 2026", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0)
doc.add_page_break()

# ================= 1. TUJUAN =================
doc.add_heading("1. Tujuan Praktikum", level=1)
para("Adapun tujuan yang ingin dicapai pada praktikum Modul 3 ini adalah sebagai berikut.")
numbered("sebagai template engine bawaan Laravel beserta alur kompilasinya menjadi kode PHP.", "Memahami konsep Blade ")
numbered("terutama penulisan ekspresi {{ }} untuk menampilkan data dan direktif @if, @elseif, @else, @foreach, serta @forelse.", "Menguasai sintaks dasar Blade, ")
numbered("menggunakan @extends, @section, dan @yield sehingga tampilan antarhalaman menjadi konsisten dan bagian yang berulang cukup ditulis satu kali.", "Menerapkan layouting ")
numbered("melalui reusable component berbasis tag <x-...> dan partial menggunakan direktif @include.", "Membuat tampilan modular ")
numbered("sehingga data dapat dikirim dari controller dan ditampilkan secara dinamis di dalam view.", "Menghubungkan route, controller, dan view dengan pola MVC ")

# ================= 2. ALAT DAN BAHAN =================
doc.add_heading("2. Alat dan Bahan", level=1)
doc.add_heading("2.1 Perangkat Keras", level=2)
fill_table([
    ["Komponen", "Spesifikasi"],
    ["Perangkat", "Laptop"],
    ["Prosesor", "13th Gen Intel(R) Core(TM) i7-13650HX"],
    ["RAM", "16 GB (15,6 GB terdeteksi)"],
    ["Penyimpanan", "SSD, ruang kosong lebih dari 2 GB"],
    ["Sistem Operasi", "Microsoft Windows 11 Pro"],
], col_widths=[1.8, 4.4])

doc.add_heading("2.2 Perangkat Lunak", level=2)
fill_table([
    ["Perangkat Lunak", "Versi / Keterangan"],
    ["XAMPP (Apache & MySQL)", "Terpasang pada D:\\xampp"],
    ["PHP", "8.2.12 (ZTS Visual C++ 2019 x64)"],
    ["Composer", "2.10.3"],
    ["Laravel Framework", "12.69.2"],
    ["Visual Studio Code", "Terpasang pada D:\\Microsoft VS Code"],
    ["Git", "2.53.0.windows.1"],
    ["Google Chrome", "Untuk menjalankan dan menguji aplikasi"],
], col_widths=[2.1, 4.1])

# ================= 3. LANGKAH-LANGKAH =================
doc.add_heading("3. Langkah-Langkah Praktikum", level=1)
para("Praktikum dikerjakan dengan pola MVC (Model-View-Controller). Route menentukan alamat URL, "
     "controller menyiapkan data mahasiswa dalam bentuk array, dan view menampilkan data tersebut "
     "sebagai halaman HTML. Berikut tahapan yang dikerjakan pada Subbab 3.4.2 sampai 3.4.4.")

doc.add_heading("3.1 Sintaks Dasar Blade dan Layout Utama (Subbab 3.4.2)", level=2)
para("Langkah pertama adalah membuat controller sebagai penyedia data. Perintah yang dijalankan:")
add_code("php artisan make:controller StudentController")
para("Perintah tersebut menghasilkan berkas app/Http/Controllers/StudentController.php. Isi berkas "
     "kemudian diubah menjadi seperti berikut.")
add_code(r"""<?php

namespace App\Http\Controllers;
use Illuminate\\Http\\Request;
class StudentController extends Controller
{
    public function index()
    {
        $students = [[
            'name' => 'Davin Aileenskie S',
            'major' => 'sistem informasi kota cerdas',
            'age' => 19,
            'courses' => [
                'Pemrograman Web Lanjut',
                'Pemrograman Mobile',
                'Pemrograman Berbasis Framework',
                'Pemrograman Berbasis Framework Lanjut'],
        ],
        [
            'name' => 'siti',
            'major' => 'sistem informasi',
            'age' => 21,
            'courses' => [
                'UI/UX Design',
                'Pemrograman Mobile',
                'Pemrograman Berbasis Framework',
                'Manajemen Proyek'],
        ],
    ];
        return view('students.index', compact('students'));
        }
}""")
para("Method index() berisi array multidimensi $students yang menyimpan nama, jurusan, umur, dan daftar "
     "mata kuliah. Fungsi compact('students') setara dengan ['students' => $students], sehingga data dapat "
     "diakses pada view melalui variabel $students.")

para("Selanjutnya ditambahkan route pada berkas routes/web.php agar URL /students memanggil controller di atas.")
add_code("""<?php

use Illuminate\\Support\\Facades\\Route;
use App\\Http\\Controllers\\StudentController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/students', [StudentController::class, 'index'])-> name('students.index');""")
para("Route diberi nama students.index melalui ->name('students.index') agar dapat dipanggil sebagai "
     "route('students.index') pada navigasi di layout.")

para("Setelah itu dibuat layout utama resources/views/layouts/main.blade.php. Berkas ini berperan sebagai "
     "\u201ccetakan\u201d halaman yang memuat head, CSS, navigasi, dan footer.")
add_code("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title') | Praktikum </title>
    <style>
        body {font-family: arial, sans-serif; margin: 20px;}
        header, footer {background: #f5f5f5; padding: 10px; text-align: center;}
        nav a {margin: 0 10 px; text-decoration: none;}
        .card {border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 6px;}
        .course {background: #eef; margin: 3px; padding: 5px; display: inline-block; border-radius: 4px;}
    </style>
</head>
<body>
    <header>
        <h1>Praktikum Laravel</h1>
        <nav>
            <a href="{{ route('students.index') }}">Mahasiswa</a>
        </nav>
    </header>

    <main>
        @yield('content')
    </main>
    <footer>
        <p>&copy; 2026 Praktikum Laravel - Davin A.S</p>
    </footer>
</body>
</html>""")
para("Direktif @yield('title') dan @yield('content') adalah placeholder yang akan diisi oleh view turunan. "
     "Tautan navigasi menggunakan named route route('students.index').")

para("Langkah berikutnya adalah membuat view resources/views/students/index.blade.php yang mewarisi layout utama.")
add_code("""@extends('layouts.main')

@section('title', 'Daftar Mahasiswa')

@section('content')
<h2>Daftar Mahasiswa</h2>

    <x-alert type="success" message="Data mahasiswa berhasil dimuat." />



@foreach ($students as $student)
    @include('partials.student-card', ['student' => $student])
@endforeach
@endsection""")
para("Direktif @extends('layouts.main') membuat view ini mewarisi layout utama, @section('title', ...) mengisi "
     "@yield('title'), dan @section('content') mengisi @yield('content'). Perulangan @foreach menampilkan setiap "
     "mahasiswa melalui partial student-card. Setiap direktif wajib ditutup, misalnya @foreach dengan @endforeach.")

doc.add_heading("3.2 Reusable Component (Subbab 3.4.3)", level=2)
para("Komponen Blade diletakkan pada folder resources/views/components dan dipanggil menggunakan tag berawalan "
     "x-. Pada langkah ini dibuat komponen alert pada berkas resources/views/components/alert.blade.php.")
add_code("""    @if ($type === 'error')
        <div style="padding: 10px; border: 1px solid red; margin: 10px 0;">
    @else
        <div style="padding: 10px; border: 1px solid green; margin: 10px 0;">
    @endif
            <strong>{{ ucfirst($type) }}</strong> {{ $message }}
        </div>""")
para("Nilai $type dan $message diterima dari atribut saat komponen dipanggil. Fungsi ucfirst($type) mengubah "
     "huruf pertama menjadi kapital (error menjadi Error), sedangkan percabangan @if menentukan warna border: "
     "merah untuk type=\"error\" dan hijau untuk type lainnya. Komponen kemudian dipanggil pada view index "
     "dengan kode berikut.")
add_code("""<x-alert type="success" message="Data mahasiswa berhasil dimuat." />""")
para("Satu komponen cukup dibuat sekali, lalu dapat dipanggil berkali-kali dengan atribut berbeda. Jika desain "
     "alert ingin diubah, cukup mengubah satu berkas alert.blade.php dan seluruh halaman yang memakainya akan "
     "ikut berubah.")

doc.add_heading("3.3 Partial Sederhana (Subbab 3.4.4)", level=2)
para("Partial digunakan untuk memecah view yang panjang menjadi bagian kecil dengan direktif @include. Tampilan "
     "satu kartu mahasiswa dipisahkan ke berkas resources/views/partials/student-card.blade.php.")
add_code("""<div class="card">
    <h3>{{ $student['name'] }}</h3>
    <p><strong>Jurusan: </strong> {{ $student['major'] }}</p>
    <p><strong>Umur: </strong> {{ $student['age'] }} Tahun</p>

    @if ($student['age'] >= 22)
    <p>Status: <span style="color:green;">Senior</span></p>
    @else
    <p>Status: <span style="color:blue;">Junior</span></p>
    @endif

    <h4>Mata Kuliah:</h4>
    @forelse ($student['courses'] as $course)
    <span class="course">{{ $course }}</span>
    @empty
    <p>Tidak ada mata kuliah terdaftar.</p>
@endforelse
</div>""")
para("Partial ini hanya berfokus pada tampilan satu mahasiswa. Variabel $student dikirim dari view pemanggil "
     "melalui @include. Di dalamnya digunakan direktif @if untuk menentukan status Senior (umur \u2265 22) atau "
     "Junior, serta @forelse untuk menampilkan daftar mata kuliah dan @empty sebagai penanganan bila daftar kosong.")

para("Berkas students/index.blade.php kemudian diubah agar memanggil partial tersebut, sehingga view utama "
     "menjadi ringkas karena tidak lagi memuat detail kartu mahasiswa secara langsung.")
add_code("""@foreach ($students as $student)
    @include('partials.student-card', ['student' => $student])
@endforeach""")
para("Perbedaan dengan <x-alert> adalah @include tidak memiliki konsep props/atribut, melainkan langsung "
     "mengirim variabel. Komponen (<x-...>) cocok untuk elemen antarmuka kecil yang dipakai di banyak halaman, "
     "sedangkan partial (@include) cocok untuk memecah bagian halaman yang besar.")

doc.add_heading("3.4 Menjalankan dan Menguji Aplikasi", level=2)
para("Server pengembangan dijalankan melalui terminal dengan perintah berikut, lalu alamat "
     "http://127.0.0.1:8000/students dibuka pada browser.")
add_code("php artisan serve")
para("Halaman yang tampil memuat alert hijau sebagai tanda data berhasil dimuat, serta dua kartu mahasiswa "
     "beserta status dan daftar mata kuliahnya. Hasil pengujian ditampilkan pada bagian berikut.")

# ================= 4. HASIL DAN DOKUMENTASI =================
doc.add_heading("4. Hasil dan Dokumentasi Program", level=1)
para("Aplikasi berhasil dijalankan dan seluruh komponen Blade yang dibuat pada Subbab 3.4.2 sampai 3.4.4 "
     "tampil sesuai rancangan. Halaman daftar mahasiswa dapat dilihat pada gambar berikut.")
doc.add_picture(IMG, width=Inches(6.2))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption("Gambar 1. Halaman daftar mahasiswa pada URL /students yang menampilkan komponen alert dan kartu mahasiswa.")
para("Dari Gambar 1 terlihat bahwa layout utama (header, navigasi \u201cMahasiswa\u201d, dan footer) berhasil "
     "diwariskan. Komponen <x-alert type=\"success\"> tampil sebagai kotak hijau berisi pesan \u201cData mahasiswa "
     "berhasil dimuat.\u201d. Setiap kartu mahasiswa merupakan hasil pemanggilan partial student-card, lengkap "
     "dengan nama, jurusan, umur, status (Junior karena umur kurang dari 22 tahun), serta daftar mata kuliah "
     "berbentuk label. Data ditampilkan dari array pada controller, bukan data statis di dalam view.")

# ================= 5. ANALISIS DAN PEMBAHASAN =================
doc.add_heading("5. Analisis dan Pembahasan", level=1)
para("1. Pembagian layout, komponen, dan partial.", bold=True)
para("Layout utama resources/views/layouts/main.blade.php dipisahkan karena bagian head, CSS, navigasi, dan "
     "footer selalu sama di setiap halaman. Dengan @extends, @section, dan @yield, bagian yang berulang cukup "
     "ditulis satu kali sehingga perubahan menu atau warna cukup dilakukan pada satu berkas. Komponen "
     "<x-alert> dibuat terpisah karena merupakan elemen antarmuka kecil yang dipakai berulang dengan atribut "
     "berbeda (success maupun error). Partial student-card dipisahkan agar view utama tidak terlalu panjang "
     "dan bagian yang berfokus pada satu mahasiswa mudah dirawat. Pembagian ini membuat kode lebih terstruktur, "
     "mudah dibaca, dan mengurangi pengulangan.")
para("2. Perbedaan sebelum dan sesudah menggunakan Blade.", bold=True)
para("Sebelum menggunakan Blade, setiap halaman harus menuliskan ulang struktur HTML, CSS, dan navigasi, serta "
     "menyisipkan kode PHP dengan sintaks <?php ?> yang bercampur dengan HTML sehingga sulit dibaca. Setelah "
     "menggunakan Blade, penulisan menjadi lebih ringkas melalui {{ }} dan direktif seperti @if, @foreach, dan "
     "@forelse. Pewarisan layout menghilangkan duplikasi struktur halaman, sedangkan komponen dan partial "
     "membuat tampilan dapat digunakan kembali. Blade juga otomatis meng-escape data yang ditampilkan sehingga "
     "lebih aman terhadap penyisipan HTML.")
para("3. Kendala dan penyelesaian.", bold=True)
bullet("Nilai $type dan $message sempat tidak terbaca karena atribut tidak dikirim saat memanggil komponen. "
       "Masalah diselesaikan dengan memastikan pemanggilan menyertakan atribut, misalnya "
       "<x-alert type=\"success\" message=\"...\" />.", "Komponen alert: ")
bullet("Halaman sempat tidak memuat CSS karena @yield('content') tertulis di luar tag <main> atau nama section "
       "tidak sama dengan nama yield. Masalah diselesaikan dengan mencocokkan kembali nama @section pada view "
       "turunan dengan @yield pada layout.", "Layout tidak muncul: ")
bullet("Daftar mata kuliah tidak tampil karena variabel $student tidak dikirim ke partial. Hal ini diperbaiki "
       "dengan menambahkan parameter kedua pada @include, yaitu ['student' => $student].", "Partial tidak menerima data: ")
bullet("Perubahan berulang kali tidak terlihat karena view lama masih tersimpan di cache. Masalah diatasi "
       "dengan menjalankan php artisan view:clear.", "Cache view: ")

# ================= 6. KESIMPULAN =================
doc.add_heading("6. Kesimpulan", level=1)
para("Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Blade Template mempermudah penyusunan "
     "tampilan Laravel melalui sintaks yang ringkas dan mudah dibaca. Penggunaan {{ }} dan direktif @if, @else, "
     "@foreach, serta @forelse memungkinkan data dari controller ditampilkan secara dinamis. Fitur layouting "
     "@extends, @section, dan @yield berhasil menghilangkan duplikasi struktur halaman sehingga tampilan menjadi "
     "seragam dan mudah dirawat. Komponen <x-alert> dan partial @include membuktikan bahwa tampilan dapat "
     "dipecah menjadi bagian kecil yang dapat dipakai ulang. Secara keseluruhan, alur MVC yang menghubungkan "
     "route, controller, dan view berjalan dengan baik, dan seluruh tujuan praktikum dapat tercapai.")

# ================= 7. LINK GITHUB =================
doc.add_heading("7. Link GitHub", level=1)
para("Kode program lengkap praktikum ini dapat diakses pada repositori berikut.")
add_code("https://github.com/.................../PABW")
para("Catatan: ganti tautan di atas dengan alamat repositori GitHub milik Saudara sebelum laporan dikumpulkan.",
     italic=True)

doc.save(OUT)
print("SAVED:", OUT)
