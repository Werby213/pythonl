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

        # Start video capture
        self.capture_video()

    def capture_video(self):
        # Capture frame-by-frame
        ret, frame = self.video_capture.read()

        if ret:
            # Convert frame to PIL image format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)

            # Update canvas with new image
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Repeat every 'interval' ms
        self.window.after(10, self.capture_video)

    def __del__(self):
        if self.video_capture.isOpened():
            self.video_capture.release()

# Create main window and run app
root = tk.Tk()
app = VideoCaptureApp(root)
root.mainloop()
