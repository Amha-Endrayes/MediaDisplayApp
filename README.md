# Media Display App

A Flask-based web application designed to display images (and optionally videos) over Wi-Fi on smart TVs via their built-in web browsers. The application includes an admin dashboard for uploading, managing, and adjusting slideshow settings (such as delay and pause/resume) and a display page that shows the media as a fullscreen slideshow.

## Features

- **Admin Dashboard:**
  - **Connected Devices:** View a list of devices (tracked by IP address and last seen time).
  - **Media Management:** Upload new media via an enhanced drag-and-drop interface with image preview, remove media, or update/replace an existing image.
  - **Slideshow Settings:** Configure the delay (in seconds) and pause/resume slideshow functionality.
  - **Scrollable Media View:** When there are many files, media are displayed inside a scrollable container for easy navigation.

- **Display Page:**
  - Fullscreen, borderless view with a black background (ideal for smart TVs).
  - Automatic slideshow of images that updates in near real-time without manual page refresh.
  - Polls for new media and updated settings.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)
- Flask

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/MediaDisplayApp.git
   cd MediaDisplayApp
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   ```
   # On macOS/Linux:
   ```
   source venv/bin/activate
   ```
   # On Windows:
   ```
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install Flask
   ```

## File Structure

```plaintext
MediaDisplayApp/
├── app.py
├── README.md
├── static/
│   ├── css/
│   │   └── style.css        # Custom CSS styles.
│   └── media/               # Folder for uploaded images/videos.
└── templates/
    ├── base.html            # Base template with Bootstrap.
    ├── dashboard.html       # Admin dashboard.
    ├── display.html         # Display page for TVs.
    ├── upload.html          # Enhanced upload page with drag-and-drop.
    └── update.html          # Update/replace media form.
```

## Running the Application

1. **Start the Flask Server:**

   ```bash
   python app.py
   ```

   The application will run on your local network (default port 5000).

2. **Access the Admin Dashboard:**

   Open your web browser and navigate to:
   
   ```
   http://<your_server_ip>:5000/dashboard
   ```
   
   From here you can:
   - View connected devices.
   - Upload new media at `/admin/upload`.
   - Remove or update existing media files.
   - Adjust slideshow settings.

3. **Access the Display Page on Your Smart TV or Device:**

   On your smart TV or device, open a web browser and go to:
   
   ```
   http://<your_server_ip>:5000/display
   ```
   
   The display page shows a fullscreen slideshow of your uploaded images that updates automatically when new media is added or when settings change.

## Customization & Next Steps

- **Real-Time Updates:**  
  The display page polls for new media every 5 seconds. You can adjust this interval in the JavaScript (`setInterval(updateSlides, 5000)`) within `templates/display.html`.

- **Video Integration:**  
  Currently, the slideshow is set up for images. Videos are supported in the admin dashboard and can be integrated into the slideshow with additional JavaScript logic.

- **UI Enhancements:**  
  Further customize the look and feel by editing `static/css/style.css` and making adjustments to the HTML templates.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) and [Bootstrap](https://getbootstrap.com/).
- Inspired by modern web design principles to provide a sleek and professional media display experience.


