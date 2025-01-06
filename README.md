# Live Image Broker  

The **Live Image Broker** is designed to resolve connectivity issues between an image source (e.g., `ffmpeg`) and an image sink (e.g., `live_visualization`) during live video streaming.  

![Architecture](../../doc/export/architecture.svg "Architecture")  

---

## Overview  

When transferring raw video data via TCP/IP, one application must act as a server while the other acts as a client. However, this setup introduces a significant drawback:  
- If either application crashes or disconnects, the other application will also fail due to the lost connection.  
- In particular, this can negatively impact `ffmpeg` because the DJI Goggles may require a manual plug-out and plug-in to function properly again.  

The **Live Image Broker** solves this issue by acting as a broker between the two applications:  
- It serves as a **server** for both the image source and the image sink.  
- The **image source** (e.g., `ffmpeg`) connects on **port 50000**, while the **image sink** (e.g., `live_visualization`) connects on **port 50001**.  
- The broker passes all received image data from the source to the sink and handles reconnections if either application goes down.  

This ensures that both applications can keep running independently, as long as the **Live Image Broker** remains active.  

![Live Image Broker Schema](../../doc/export/live_image_broker_schema.svg "Live Image Broker Schema")  

---

## Environment Setup  

To set up a development environment and install all required dependencies, run the following commands (example for Windows):  

```bash
python -m venv venv
venv/Scripts/activate
python -m pip install -r requirements.txt
```

---

## How to Run  

Execute the following command to start the **Live Image Broker**:  

```bash
python live_image_broker/main.py
```
