# 🌐 Nexus Core: Home Lab Management Portal

Nexus Core is a lightweight, single-page, responsive dashboard built specifically for self-hosted server environments. It bridges the gap between home network resource administration and day-to-day informational awareness by aggregating personalized external data feeds right alongside internal service routing links.

Built entirely using **Flask**, **Tailwind CSS**, and browser-native geolocation APIs, it requires no external API tokens, heavy container overhead, or complex enterprise server configurations (like Apache or Nginx).

---

## ✨ Features

* **🗂️ Dual-Tab Interface:** Instantly toggle between real-time curated information feeds and your internal home lab network directory shortcuts.
* **⚙️ JSON-Driven Configurations:** Seamlessly toggle, add, or swap news categories and data providers instantly by editing a simple local `feeds.json` text config file.
* **🌍 Real-Time Regional News Engine:** Dynamically parses live upstream headlines for curated subsets, including U.S. breaking news, regional updates from Latin America, and global soccer tournament statistics.
* **🌤️ Zero-Token Geolocation Weather:** Leverages browser-side location requests to pull instant ambient metrics directly from the free, no-authentication Open-Meteo API.
* **📱 Tailwind Fluid Adaptive Grid:** Layout scales gracefully across all physical viewports—optimized for wall-mounted control tablets, mobile configurations via Tailscale, and wide desktop administration monitors.

---

## 🛠️ Quick Installation Guide

Ensure you have Python 3 installed on your host system, then execute the following steps:

### 1. Set Up the Project Files
Clone or place the directory on your host machine, ensuring the following layout structure:
```text
homelab-dashboard/
├── app.py
├── feeds.json
├── requirements.txt
└── templates/
    └── index.html

