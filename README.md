Dashboard
https://cough-aiot-project.onrender.com/dashboard/page1

Video Demo 1:
https://drive.google.com/file/d/1noJH2Ndz4vxkh7ScD9HAB0aqgefARQ1u/view?usp=sharing

# 🏥 Sistem Pemantau Kesehatan Berbasis IoT (AIoT Cough & Sneeze Detection)

**Proyek IoT Pemantauan Suhu dan Klasifikasi Batuk/Bersin Real-Time Menggunakan Edge AI & Node-RED**

---

## 📌 Ringkasan Proyek
Proyek ini merupakan sistem pemantau kesehatan jarak jauh berbasis IoT (*Internet of Things*) yang mengintegrasikan kecerdasan buatan di tingkat lokal (*Edge AI*) menggunakan platform Edge Impulse. Perangkat berfungsi untuk memantau suhu tubuh pasien dan mendeteksi frekuensi batuk serta bersin secara *real-time* langsung di mikrokontroler ESP32.

---

## 🎯 Fitur Utama
* 🌡️ **Pemantauan Suhu Real-Time:** Mengukur suhu tubuh pasien menggunakan sensor presisi tinggi DS18B20.
* 🎙️ **Edge AI Audio Classification:** Mendeteksi dan mengklasifikasikan suara batuk, bersin, dan *noise* menggunakan model *Convolutional Neural Network* (1D CNN) MFCC yang terkuantisasi INT8.
* 🔐 **Komunikasi Aman (MQTT over TLS):** Pengiriman data telemetri berformat JSON secara efisien dan aman ke EMQX Cloud Broker.
* 📊 **Dashboard Interaktif Node-RED:** Visualisasi langsung untuk grafik tren suhu, akumulasi batuk/bersin harian, serta tabel histori log mentah pasien.
* 🚨 **Sistem Peringatan & Eskalasi Darurat:** Menghasilkan notifikasi UI otomatis untuk indikasi suhu tinggi (*fever*), rekomendasi obat, serta peringatan eskalasi 3 hari yang menghubungkan pasien ke fasilitas kesehatan/dokter.

---

## 🛠️️ Komponen & Spesifikasi Hardware
* **Mikrokontroler:** ESP32 WROOM-32D (Tensilica Dual-Core 32-bit LX6, 240 MHz, 520 KB SRAM, Wi-Fi & BLE)
* **Sensor Suhu:** DS18B20 Waterproof Temperature Sensor Probe
* **Sensor Mikrofon:** INMP441 Omnidirectional I2S MEMS Microphone Module
* **Aksesori:** Kabel Data USB Type-C, Kabel Jumper (Male-to-Male), Breadboard 400 *tie-points*

---

## 💻 Arsitektur Perangkat Lunak & Cloud
* 🧠 **Edge Impulse AI Pipeline:** Ekstraksi fitur MFCC & pelatihan model 1D CNN (Akurasi $\ge$ 85%, Kuantisasi INT8 untuk efisiensi RAM ESP32).
* ☁️ **MQTT Broker:** EMQX Cloud (`mqtts://va00e289.ala.asia-southeast1.emqxsl.com:8883`)
* 🗄️ **Database Cloud:** InfluxDB Cloud (Bucket: `patient_data`, Org ID: `35a50f0f8db3c242`)
* 🌐 **Backend & Dashboard:** Node-RED Engine

---

## ⚡ Format Payload Data (MQTT JSON)
Data dikirim dari ESP32 ke cloud dalam format JSON berikut:

```json
{
  "device_id": "patient_01",
  "temperature_c": 37.8,
  "symptom": "cough",
  "confidence": 0.95
}
## 🔗 Tautan Penting
* 🖥️ **Live Dashboard UI:** [Buka Node-RED Dashboard](https://cough-aiot-project.onrender.com/dashboard/page2)
* ⚙️ **Node-RED Flow Editor:** [Buka Flow Editor](https://cough-aiot-project.onrender.com/#flow/cea766101cfe7747)
* 🎥 **Video Demo:** [Tonton di Google Drive](#) *(Ganti tanda # dengan link asli video Anda)*

---

## 👥 Anggota Kelompok (Group 10 - LA08)

| Nama | NIM |
| :--- | :--- |
| **Tandri Wibowo** | 2702261681 |
| **Kenneth Andrew Lukita** | 2702247310 |
| **Leonard Vanderson Gani** | 2702264563 |

