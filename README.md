# 🏥 Sistem Pemantau Kesehatan Berbasis IoT (AIoT Cough & Sneeze Detection)

**Proyek IoT Pemantauan Suhu dan Klasifikasi Batuk/Bersin Real-Time Menggunakan Edge AI & Node-RED**

---

## 📌 Ringkasan Proyek
Proyek ini merupakan sistem pemantau kesehatan jarak jauh berbasis IoT (*Internet of Things*) yang kini telah ditingkatkan menjadi purwarupa siap-AI (*AIoT-Ready Prototype*). Perangkat berfungsi untuk memantau suhu tubuh pasien, mendeteksi frekuensi batuk serta bersin secara *real-time* langsung di mikrokontroler ESP32 (*Edge AI*), sekaligus memantau suhu dan kelembapan ruangan pasien secara kontinu. Proyek ini juga berfokus pada otomasi pengambilan keputusan (*rule-based automation*) dan pengumpulan deret waktu (*time-series data logging*) hingga mencapai lebih dari 1.000 *records* untuk analitik cerdas di masa mendatang.

---

## 🎯 Fitur Utama
- 🌡️ **Pemantauan Suhu Real-Time:** Mengukur suhu tubuh pasien menggunakan sensor presisi tinggi DS18B20.
- 🌬️ **Pemantauan Lingkungan Kamar:** Memantau suhu dan kelembapan udara ruangan pasien menggunakan sensor DHT22 untuk mengidentifikasi apakah gejala dipicu oleh infeksi atau udara ruangan yang buruk.
- 🎙️ **Edge AI Audio Classification:** Mendeteksi dan mengklasifikasikan suara batuk, bersin, dan *noise* menggunakan model *Convolutional Neural Network* (1D CNN) MFCC yang terkuantisasi INT8 di platform Edge Impulse.
- 🔐 **Komunikasi Aman (MQTT over TLS):** Pengiriman data telemetri berformat JSON secara kontinu (tiap 5 detik) ke EMQX Cloud Broker dengan pengaman deteksi gangguan sensor (*fallback logic*).
- 🗄️ **Continuous Data Logging:** Penyimpanan data historis multi-field secara kontinu ke InfluxDB Cloud yang mampu merekam ribuan data berformat *time-series*.
- 📊 **Dashboard Interaktif Node-RED:** Visualisasi langsung untuk grafik tren suhu, akumulasi batuk/bersin harian, serta tabel histori log mentah (*Raw Patient Log*) yang memuat riwayat kondisi pasien dan ruangan.
- 🚨 **Sistem Peringatan & Eskalasi Otomatis (4 Aturan Utama):**
  1.  **Fever Alert:** Peringatan UI otomatis untuk indikasi suhu tinggi $\ge 37,5^\circ\text{C}$ beserta rekomendasi obat.
  2.  **Room Environment Alert:** Peringatan UI untuk menghidupkan *Humidifier* (jika kelembapan $\le 40\%$) atau *Dehumidifier* (jika kelembapan $\ge 70\%$).
  3.  **Daily Symptom Triage:** Menentukan status *Occurrence* atau *In-Sick* jika frekuensi batuk/bersin harian $\ge 5$ kali.
  4.  **3-Day Urgent Escalation:** Eskalasi darurat yang menghubungkan pasien ke rumah sakit atau dokter jika gejala terdeteksi berlanjut melewati batas aman (3 hari).

---

## 🛠 Komponen & Spesifikasi Hardware
- **Mikrokontroler:** ESP32 WROOM-32D (Tensilica Dual-Core 32-bit LX6, 240 MHz, 520 KB SRAM, Wi-Fi & BLE)
- **Sensor 1 (Suhu Tubuh):** DS18B20 Waterproof Temperature Sensor Probe (Antarmuka 1-Wire di Pin D4)
- **Sensor 2 (Gejala Medis):** INMP441 Omnidirectional I2S MEMS Microphone Module (Antarmuka I2S di Pin D14, D15, D32)
- **Sensor 3 (Lingkungan):** DHT22 / AM2302 Room Temperature & Humidity Module (Antarmuka Single-Bus di Pin D5)
- **Aksesori:** Kabel Data USB Type-C, Kabel Jumper, Breadboard 400 *tie-points* (Menggunakan distribusi daya paralel 3,3V).

---

## 💻 Arsitektur Perangkat Lunak & Cloud
- 🧠 **Edge Impulse AI Pipeline:** Ekstraksi fitur MFCC & pelatihan model 1D CNN yang diseimbangkan melalui 400 sampel audio gabungan dari dataset COUGHVID & ESC-50.
- ☁️ **MQTT Broker:** EMQX Cloud (`mqtts://va00e289.ala.asia-southeast1.emqxsl.com:8883`)
- 🗄️ **Database Cloud:** InfluxDB Cloud AWS (Bucket: `patient_data`, Org ID: `35a50f0f8db3c242`)
- 🌐 **Backend & Dashboard:** Node-RED Engine yang di-*deploy* persisten di platform cloud Render.

---

## ⚡ Format Payload Data (MQTT JSON)
Data dikirim dari ESP32 ke cloud dalam format JSON 4-*field* berikut:

```json
{
  "device_id": "patient_01",
  "temperature_c": 37.8,
  "room_temp_c": 24.5,
  "humidity_pct": 75.0,
  "symptom": "sneeze",
  "confidence": 0.99
}

```
## 🔗 Tautan Penting
- 🖥️ **Live Dashboard UI:** [Buka Node-RED Dashboard](https://cough-aiot-project.onrender.com/dashboard/page2)
- ⚙️ **Node-RED Flow Editor:** [Buka Flow Editor](https://cough-aiot-project.onrender.com/#flow/64ab3de8b366f712)
- 📁 **1.000+ Records Dataset InfluxDB (CSV):** [Lihat Dataset CSV](https://github.com/leonardvanderson/Cough-AIoT-Project/blob/main/Dataset%20MQTT%20Real%20Time%20influxdata%202026-11-06T08%2049%2053Z.csv)
- 💾 **Source Code Arduino:** [Lihat Kode ESP32](https://github.com/leonardvanderson/Cough-AIoT-Project/blob/main/Source%20Code%20Arduino%202.txt)
- 📜 **Flowchart & Pseudocodes:** [Lihat Dokumentasi Algoritma](https://github.com/leonardvanderson/Cough-AIoT-Project/blob/main/Pseudocodes.txt)
- 🎥 **Video Demo:** [Tonton di Google Drive]([https://drive.google.com/file/d/1uvlVrptck8dT_ZKZyWGNqyluf0FuleyM/view?usp=sharing](https://drive.google.com/file/d/12Xwy_EdF0_ZLHQW8k1ztuyqKJ6aKZRLl/view?usp=sharing))

---

## 👥 Anggota Kelompok (Group 10 - LA08)

| Nama | NIM |
| :--- | :--- |
| **Tandri Wibowo** | 2702261681 |
| **Kenneth Andrew Lukita** | 2702247310 |
| **Leonard Vanderson Gani** | 2702264563 |

