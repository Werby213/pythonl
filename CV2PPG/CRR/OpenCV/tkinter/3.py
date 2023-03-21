import cv2
import tkinter as tk
from PIL import Image, ImageTk

class VideoCaptureApp:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Video Capture App")
        self.video_source = video_source

        # Create video capture object and start capturing frames
        self.video_capture = cv2.VideoCapture(video_source)
        if not self.video_capture.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Initialize GUI elements
        self.canvas = tk.Canvas(window, width=self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.save_button = tk.Button(window, text="Save Frame", command=self.save_frame)
        self.save_button.pack()

        self.detect_button = tk.Button(window, text="Detect Faces", command=self.detect_faces)
        self.detect_button.pack()

        self.triggered_button = tk.Button(window, text="Triggered", command=self.triggered_mode)
        self.triggered_button.pack()

        # Initialize face detection classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Initialize mode flags
        self.detect_mode = False
        self.triggered_mode = False

        # Start capturing video frames
        self.capture_video()

    def capture_video(self):
        # Capture frame-by-frame
        ret, frame = self.video_capture.read()
        if ret:
            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            if self.detect_mode:
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # Draw rectangles around detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Apply triggered mode if enabled
            if self.triggered_mode and len(faces) > 0:
                # Resize face to window size
                (x, y, w, h) = faces[0]
                face = cv2.resize(gray[y:y+h, x:x+w], (self.window.winfo_width(), self.window.winfo_height()))

                # Add triggered message to bottom of window
                triggered_text = "TRIGGERED"
                cv2.rectangle(frame, (0, self.window.winfo_height()-40), (self.window.winfo_width(), self.window.winfo_height()), (0, 0, 255), -1)
                cv2.putText(frame, triggered_text, (int(self.window.winfo_width()/2)-50, self.window.winfo_height()-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Replace frame with resized face
                frame = face

                # Convert frame to PIL image format
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)

                # Convert PIL image to Tkinter PhotoImage format and display on canvas
                self.photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

                # Schedule next capture
            self.window.after(15, self.capture_video)

            def save_frame(self):
                # Save current frame as JPEG image file
                ret, frame = self.video_capture.read()
                if ret:
                    cv2.imwrite("frame.jpg", frame)
                    print("Frame saved as frame.jpg")

            def detect_faces(self):
                # Toggle face detection mode
                self.detect_mode = not self.detect_mode

            def triggered_mode(self):
                # Toggle triggered mode
                self.triggered_mode = not self.triggered_mode

        # Create main window and video capture object
        window = tk.Tk()
        app = VideoCaptureApp(window)

        # Start the GUI
        window.mainloop()

        # Release video capture object and close all windows
        app.video_capture.release()
        cv2.destroyAllWindows()
