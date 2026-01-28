# ESP32-CAM OpenCV Stream Capture

![ESP32-CAM](https://img.shields.io/badge/ESP32-blue?logo=espressif)
![OpenCV](https://img.shields.io/badge/OpenCV-Python-orange?logo=opencv)
![IoT](https://img.shields.io/badge/IoT-green?logo=iot)

This project demonstrates how to use an **ESP32-CAM (AI Thinker)** as a lightweight HTTP camera server and access single-frame JPEG images from a Python script.

It is designed for **computer vision** and **image processing** applications where all processing is performed on the PC, not on the **ESP32**.

<p float="left">
  <img src="Example.gif" width="400"/>
</p>

## Features
- ESP32-CAM HTTP server
- `/capture` endpoint for a single JPEG frame
- Compatible with **OpenCV (Python)**
- Ideal for:
  - OpenCV image processing
  - Object detection
  - Face / QR / motion detection
  - AI & ML experiments on PC

## How It Works
1. **ESP32-CAM** runs an HTTP server on port **80**
2. Each request to `/capture`:
   - Captures a single frame from the camera
   - Sends it as a JPEG image
3. Python script:
   - Requests `/capture` repeatedly
   - Decodes the image using OpenCV
   - Processes frames in real time

This approach avoids ESP32 performance limits and lets the PC handle all heavy processing.

## ESP32-CAM Endpoints
| Endpoint   | Method | Description |
|-----------|--------|-------------|
| `/`        | GET    | Web interface with MJPEG stream |
| `/stream`  | GET    | Live MJPEG video stream |
| `/capture` | GET    | Single JPEG frame for OpenCV / image processing |

## Hardware Requirements
- ESP32-CAM (AI Thinker)
- USB-to-TTL adapter (FTDI, CP2102, etc.)
- Jumper wires

## Libraries Used
These libraries are included with the **ESP32 Arduino Core**:

- `esp_camera.h`
- `esp_wifi.h`
- `WiFi.h`
- `esp_http_server.h`
- `esp_timer.h`
- `img_converters.h`

## Installation
### Programming ESP32-CAM
The ESP32-CAM does not include an integrated USB-to-serial programmer so an external FTDI (USB-to-TTL) programmer is used for uploading code. (You can also use an Arduino Uno as a USB-to-serial adapter. For more information, refer to tutorial videos on YouTube.)
<p float="left">
  <img src="FTDI Programmer Pinout.png" width="500" />
</p>

### Uploading the Code to ESP32-CAM
1. Install **VS Code** and the **PlatformIO IDE** extension
2. Create a new project in **PlatformIO IDE**
3. Make sure `platformio.ini` contains the correct configuration:
```ini
[env:esp32cam]
platform = espressif32
board = esp32cam
framework = arduino
monitor_speed = 115200
```
4. Connect the ESP32-CAM to the FTDI programmer (see [Programming ESP32-CAM](#programming-esp32-cam))
5. Get the code from [src/main.cpp](https://github.com/Mali03/ESP32-CAM-OpenCV-Stream/blob/main/src/main.cpp) and set your WiFi credentials:
```cpp
const char *ssid = "******";
const char *password = "******";
```
6. Build and upload the code to the ESP32-CAM
7. Open Serial Monitor to get the IP address

Example:
```cpp
Camera Ready! Use 'http://192.168.1.131' to connect
```

### Running the Python OpenCV Script
Once the **ESP32-CAM** is running and connected to WiFi, you can capture frames on your computer using Python and OpenCV.

1. Install required Python dependencies:
```
pip install opencv-python numpy
```
2. Open the Python script located at:
```
src/StreamCapture.py
```
3. Update the ESP32-CAM IP address in the script:
```py
url = "http://192.168.1.131/capture"
```
4. Run the script:
```
python StreamCapture.py
```
5. A window will open showing live frames from the ESP32-CAM. Press 'q' to exit.

## License
This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/Mali03/ESP32-CAM-OpenCV-Stream/blob/main/LICENSE) file for details.

## Need Help
If you need any help contact me on [LinkedIn](https://www.linkedin.com/in/mali03/).

⭐ If you like this project, don’t forget to give it a star on GitHub!
