# 📡 A9G GPS to SMS MicroPython Script

This MicroPython script retrieves **GPS coordinates** from the **Ai-Thinker A9G module** and **sends them via SMS** every 1 minute. The SMS contains a **Google Maps link** for easy location tracking.

---

## 🚀 Features
✅ **Retrieves GPS location** (latitude, longitude, altitude)  
✅ **Formats location as a Google Maps URL**  
✅ **Sends SMS every 1 minute** to a specified phone number  
✅ **Error handling for missing GPS data**  
✅ **Works on Ai-Thinker A9G (GSM + GPS module)**  

---

## 🛠️ Hardware Requirements
- Ai-Thinker **A9G** GSM/GPS module
- Microcontroller supporting **MicroPython** (ESP32, STM32, etc.)
- SIM card with **SMS capability**
- GPS antenna for better signal reception
- Power source (USB or battery)

---

## 📥 Installation & Setup

### 1️⃣ **Install MicroPython on A9G**
1. Flash **MicroPython firmware** onto the A9G module.
2. Use a **serial terminal** (like `Thonny`, `uPyCraft`, or `picocom`) to connect.

### 2️⃣ **Upload Required Modules**
Ensure that `gps` and `cellular` modules are available in MicroPython.

### 3️⃣ **Modify the Script**
Update the **destination phone number** inside `phone_number` in `main.py`:

```python
phone_number = "XXXXXXX"  # Change to your recipient number
