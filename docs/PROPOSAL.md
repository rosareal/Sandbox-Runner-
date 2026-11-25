# 📄 Proposal Proyek: Rancang Bangun Mini Sandbox Runner Berbasis Isolasi Proses dan Pembatasan Sumber Daya (*Resource Limit*) pada Sistem Operasi Linux

**Mata Kuliah:** Sistem Operasi (TIK103)  
**Program Studi:** D4 Rekayasa Keamanan Siber – Politeknik Negeri Jakarta  

**Anggota Kelompok:**
1. Tristan Birendra Rozi
2. Cello Gemayel Aswan
3. Muhammad Farrelivo Kafka Herdian
4. Rosa Salsabillah Putri Wardoyo

## 1. Latar Belakang & Rumusan Masalah
Eksekusi kode dari sumber tidak tepercaya secara langsung pada sistem utama (*host*) berisiko menyebabkan *resource exhaustion*, *infinite loop*, maupun *fork bomb*. Proyek ini merancang utilitas *sandbox* ringan berbasis CLI di Linux untuk mengisolasi proses eksekusi skrip dan membatasi penggunaan sumber daya secara otomatis.

## 2. Tujuan & Batasan
- **Tujuan:** Membangun prototipe *Mini Sandbox Runner* di Linux dengan pembatasan waktu CPU, memori (RAM), jumlah proses, dan isolasi direktori sementara.
- **Batasan:** Fokus pada eksekusi skrip Python (`.py`) pada lingkungan VM Linux menggunakan pendekatan *process-level sandboxing*.

## 3. Pemetaan Konsep Sistem Operasi
- **Manajemen Proses (`fork` & `exec`):** Menjalankan skrip target sebagai *child process* terpisah menggunakan `subprocess` dan menghentikannya (`SIGKILL`) jika melebihi batas waktu.
- **Pembatasan Sumber Daya (`setrlimit`):** Mengatur kuota waktu prosesor (`RLIMIT_CPU`), kapasitas RAM (`RLIMIT_AS`), dan batas proses anak (`RLIMIT_NPROC`).
- **Isolasi Lingkungan & Berkas:** Menggunakan direktori sementara terisolasi (`tempfile.mkdtemp`) yang otomatis dihapus setelah proses selesai.

## 4. Jadwal Kerja 3 Minggu
- **Minggu 1 (Pertemuan 12):** Penyusunan proposal, setup repositori Git, dan pembuatan prototipe awal (*MVP*).
- **Minggu 2 (Pertemuan 13):** Pengembangan fitur pencatatan log eksekusi dan isolasi jaringan (`unshare`).
- **Minggu 3 (Pertemuan 14–15):** Pengujian menyeluruh, penyusunan laporan akhir, dan presentasi demo.
