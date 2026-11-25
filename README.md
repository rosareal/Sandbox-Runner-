# 🛡️ Rancang Bangun Mini Sandbox Runner Berbasis Isolasi Proses dan Pembatasan Sumber Daya (*Resource Limit*) pada Sistem Operasi Linux

Proyek Kelompok Mata Kuliah **Sistem Operasi (TIK103)**  
Program Studi **D4 Rekayasa Keamanan Siber – Politeknik Negeri Jakarta**

---

## 📌 Deskripsi Proyek
**Mini Sandbox Runner** adalah utilitas berbasis CLI (*Command Line Interface*) di lingkungan Linux untuk mengeksekusi skrip Python yang tidak sepenuhnya dipercaya secara terisolasi. Program ini membatasi waktu eksekusi, penggunaan memori (RAM), jumlah proses anak, serta membersihkan direktori kerja pasca-eksekusi guna mencegah serangan *resource exhaustion* atau gangguan pada sistem utama (*host*).

## 👥 Anggota Kelompok & Pembagian Fokus Kerja

| Nama Mahasiswa | Fokus Peran | Tanggung Jawab Utama |
| :--- | :--- | :--- |
| **Tristan Birendra Rozi** | Ketua Kelompok & Arsitek Sistem | Inisialisasi repositori Git, manajemen jadwal, penyusunan `README.md`, & integrasi sistem |
| **Cello Gemayel Aswan** | Pengembang Inti (*Resource & Isolation*) | Implementasi pembatasan sumber daya (`setrlimit`: CPU, RAM, NPROC) & isolasi direktori sementara |
| **Muhammad Farrelivo Kafka Herdian** | Pengembang Inti (*Process & Execution*) | Implementasi eksekusi *child process* (`subprocess`), penanganan *timeout*, & tangkapan output |
| **Rosa Salsabillah Putri Wardoyo** | Penguji (QA) & Dokumentator | Penyusunan skrip uji berbahaya (`tests/`), dokumen proposal (`docs/PROPOSAL.md`), & `CHANGELOG.md` |

## 🧠 Pemetaan Konsep Sistem Operasi

| Konsep Sistem Operasi | Implementasi Teknis dalam Proyek |
| :--- | :--- |
| **Manajemen Proses (`fork` & `exec`)** | Pembuatan *child process* terpisah menggunakan `subprocess` serta terminasi paksa (`SIGKILL`) saat melebihi batas waktu. |
| **Pembatasan Sumber Daya (`setrlimit`)** | Penerapan batas kuota CPU time (`RLIMIT_CPU`), kapasitas RAM (`RLIMIT_AS`), dan jumlah proses (`RLIMIT_NPROC`) di kernel Linux. |
| **Isolasi Lingkungan & Berkas** | Menjalankan eksekusi di dalam direktori sementara terisolasi (`tempfile.mkdtemp`), membatasi variabel lingkungan (`env`), serta menghapus jejak direktori setelah selesai. |

## 🎯 Daftar Fitur (Prioritas MVP)
* **Must Have (Target Pertemuan 12 – Selesai):**
  * Menjalankan skrip target di dalam *child process* terisolasi.
  * Pembatasan waktu eksekusi (*Timeout*) otomatis.
  * Pembatasan kapasitas memori (RAM) dan pencegahan *fork bomb* (`RLIMIT_NPROC`).
  * Pembersihan direktori sementara otomatis pasca-eksekusi.
* **Should Have (Target Pertemuan 13–14):**
  * Pencatatan log eksekusi (`execution.log`) beserta status keluar (*exit code*).
  * Isolasi jaringan menggunakan *Linux Network Namespace* (`unshare -n`).
* **Could Have (Opsional):**
  * Dukungan eksekusi multi-bahasa (C/Bash) dan ringkasan statistik penggunaan CPU/RAM.

## 🚀 Cara Instalasi dan Menjalankan (Linux VM)
1. **Clone repositori:**
   ```bash
   git clone https://github.com
   cd Sandbox-Runner
   ```
2. **Pastikan Python 3 terpasang di VM Linux:**
   ```bash
   python3 --version
   ```
3. **Jalankan prototipe MVP dengan skrip uji:**
   ```bash
   python3 src/sandbox.py tests/test_normal.py
   ```

## 🧪 Skenario Pengujian Keamanan
1. **Uji Eksekusi Normal (`tests/test_normal.py`):** Skrip berjalan normal dan menampilkan output standar dengan status `Exit Code: 0`.
2. **Uji Infinite Loop (`tests/test_loop.py`):** Skrip melakukan perulangan tanpa henti; sistem otomatis menghentikan proses setelah 3 detik dengan pesan `ALERT`.
3. **Uji Kelebihan Memori (`tests/test_memory.py`):** Skrip mencoba mengalokasikan RAM > 64 MB; kernel menghentikan proses dengan `MemoryError` / `Killed`.

## ⚠️ Etika & Batasan Keamanan
Seluruh pengujian skrip berbahaya **wajib dilakukan di dalam Mesin Virtual (VM) Linux terisolasi** milik kelompok dan tidak menyimpan kredensial sensitif di dalam repositori ini.
