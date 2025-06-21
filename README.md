# 📷 Live QR Code Scanner

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=google-chrome)](https://rizz0311.github.io/QR-SCANNER-APP/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A simple, fast, and responsive QR code scanner that runs entirely in your web browser. This application uses your device's camera to detect and decode QR codes in real-time.

# 🐍 Python QR Code Scanner with Webcam & Flask

This project is a web-based QR code scanner that uses your computer's webcam. It's built with Python using the Flask framework to serve the video stream to a web page and OpenCV to process the video feed.



![image](https://github.com/user-attachments/assets/86d32efa-79e7-40ab-8875-35072b855d22)


## 📜 Description

This application starts a local web server that:
1.  Accesses your default webcam.
2.  Streams the video feed live to a web page at `http://127.0.0.1:5000`.
3.  Continuously scans the video feed for QR codes using the `pyzbar` library.
4.  When a QR code is detected, it draws a green bounding box around it.
5.  If the QR code contains a valid URL, it automatically opens the URL in a new browser tab.

## ✨ Features

-   **Live Video Streaming:** Real-time video from your webcam displayed in the browser.
-   **Real-Time QR Detection:** Scans for QR codes on every frame.
-   **Visual Feedback:** Highlights detected QR codes with a green box and displays the decoded data.
-   **Automatic URL Opening:** Seamlessly opens web links found in QR codes.
-   **Duplicate Prevention:** Includes a delay to prevent opening the same URL multiple times in a row.

## 🛠️ Technology Stack

-   **Backend:** Python
-   **Web Framework:** Flask
-   **Computer Vision:** OpenCV (`opencv-python`)
-   **QR Code Decoding:** pyzbar (`pyzbar`)
-   **Array Manipulation:** NumPy
-   **Frontend:** HTML

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 and `pip` installed on your system. You can download them from [python.org](https://www.python.org/).

### Installation & Setup

1.  **Clone the repository:**
    Replace `your-username/your-repository-name` with your actual GitHub repo details.
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd qr_scanner_app
    ```

3.  **Install the required Python libraries:**
    All the necessary packages can be installed with a single command.
    ```bash
    pip install opencv-python pyzbar numpy Flask
    ```
    *(Alternatively, if a `requirements.txt` file is provided, you can use `pip install -r requirements.txt`)*


### Running the Application

1.  **Start the Flask server:**
    From within the project directory, run the following command in your terminal:
    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Once the server is running, you will see output in your terminal indicating it's active. Open your web browser and navigate to:
    [**http://127.0.0.1:5000**](http://127.0.0.1:5000)

3.  **Grant Camera Access:**
    Your browser will likely prompt you for permission to access your webcam. You must **Allow** it for the application to work.

4.  **Scan QR Codes:**
    Point a QR code at your webcam. You should see it highlighted, and if it's a URL, it will open automatically.

5.  **To stop the application:**
    Go back to your terminal and press `Ctrl+C`.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving this project, feel free to fork the repository and submit a pull request.

## 📝 Details

<details>
  <summary>A Note on the Original Python Version</summary>
  
  This project was initially developed using a Python backend with Flask and OpenCV. While powerful, that version required a server environment capable of running Python, making it unsuitable for simple static hosting like GitHub Pages. The project was then re-imagined as a pure client-side JavaScript application to ensure easy access, deployment, and enhanced user privacy.
</details>






