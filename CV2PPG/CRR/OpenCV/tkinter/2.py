import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoCaptureApp:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Video Capture App")

        # Open video source
        self.video_capture = cv2.VideoCapture(video_source)

        # Create canvas for video display
        self.canvas = tk.Canvas(window, width=self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Create buttons for selecting display mode
        self.mode = tk.StringVar()
        self.mode.set("Normal")
        self.normal_button = tk.Radiobutton(window, text="Normal", variable=self.mode, value="Normal")
        self.normal_button.pack(side=tk.LEFT, padx=5)
        self.grayscale_button = tk.Radiobutton(window, text="Grayscale", variable=self.mode, value="Grayscale")
        self.grayscale_button.pack(side=tk.LEFT, padx=5)
        self.flip_button = tk.Radiobutton(window, text="Flip", variable=self.mode, value="Flip")
        self.flip_button.pack(side=tk.LEFT, padx=5)
        self.negative_button = tk.Radiobutton(window, text="Negative", variable=self.mode, value="Negative")
        self.negative_button.pack(side=tk.LEFT, padx=5)

        # Create button for saving frame to file
        self.save_button = tk.Button(window, text="Save Frame", command=self.save_frame)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Create button for detecting faces
        self.detect_button = tk.Button(window, text="Detect Faces", command=self.detect_faces)
        self.detect_button.pack(side=tk.LEFT, padx=5)

        # Load face detection cascade
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Start video capture
        self.capture_video()

    def capture_video(self):
        # Capture frame-by-frame
        ret, frame = self.video_capture.read()

        if ret:
            # Apply selected display mode
            if self.mode.get() == "Grayscale":
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            elif self.mode.get() == "Flip":
                frame = cv2.flip(frame, 0)
            elif self.mode.get() == "Negative":
                frame = cv2.bitwise_not(frame)

            # Detect faces (if enabled)
            if self.detect_button["text"] == "Detecting Faces...":
                faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Convert frame to PIL image format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)

            # Convert PIL image to ImageTk format and display on canvas
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Schedule next frame capture
        self.window.after(15, self.capture_video)

    def save_frame(self):
        # Capture current frame and save to file
        ret, frame = self.video_capture.read()
        if ret:
            filename = "frame.png"
            cv2.imwrite(filename, frame)

    def detect_faces(self):
        # Toggle face detection mode
        if self.detect_button["text"] == "Detect Faces":
            self.detect_button["text"] = "Detecting Faces..."
        else:
            self.detect_button["text"] = "Detect Faces"

    def __del__(self):
        # Release video source and close window
        self.video_capture.release()
        self.window.destroy()

# Create window and video capture app instance
window = tk.Tk()
app = VideoCaptureApp(window)

# Run event loop
window.mainloop()
