
# import cv2
# import tkinter as tk
# from PIL import Image, ImageTk
# from mfrc522 import SimpleMFRC522  # Make sure to install the mfrc522 library


# # Create a Tkinter window
# root = tk.Tk()
# root.title("Reversed Vending Machine")

# # Create left and right frames
# left_frame = tk.Frame(root)
# left_frame.pack(side="left", padx=10, pady=10)

# right_frame = tk.Frame(root)
# right_frame.pack(side="left", padx=10, pady=10)

# # Create labels and button in the right frame
# label = tk.Label(right_frame, text="Place your RFID Card", font=("Helvetica", 16))
# label.pack(pady=10)

# button = tk.Button(right_frame, text="Enter", font=("Helvetica", 12), padx=10, pady=5)
# button.pack()

# # Create a label to display the button press message
# message_label = tk.Label(right_frame, text="", font=("Helvetica", 16))
# message_label.pack(pady=10)

# # Open the camera using OpenCV
# cap = cv2.VideoCapture(0)

# # Define a function to capture video frames and perform face detection
# def detect_faces():
#     ret, frame = cap.read()
#     if ret:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         # Convert the OpenCV image to Tkinter format
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(img)
#         img = ImageTk.PhotoImage(image=img)
        
#         # Update the left frame with the captured frame
#         panel.img = img
#         panel.config(image=img)
#         panel.after(10, detect_faces)  # Repeat the detection every 10 milliseconds

# def on_button_click():
#     label.config(text="You have pressed the button")
    
#     # Schedule resetting the message_label text back to "Place your RFID Card" after 10 seconds
#     root.after(10000, reset_message_label)

# # Define a function to reset the message_label text
# def reset_message_label():
#     label.config(text="Place your RFID Card")

# # Bind the button click event to the function
# button.config(command=on_button_click)

# panel = tk.Label(left_frame)
# panel.pack()

# # Start face detection
# detect_faces()

# # Start the Tkinter main loop
# root.mainloop()

# # Release the camera
# cap.release()
# cv2.destroyAllWindows()


import cv2
import tkinter as tk
from PIL import Image, ImageTk
# from mfrc522 import SimpleMFRC522  # Make sure to install the mfrc522 library

root = tk.Tk()
root.title("RFID-Based Face Detection System")

left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side="left", padx=10, pady=10)

message_label = tk.Label(right_frame, text="Place your RFID Card", font=("Helvetica", 16))
message_label.pack(pady=10)

rfid_confirmation_label = tk.Label(right_frame, text="", font=("Helvetica", 16))

tag_entry = tk.Entry(right_frame, font=("Helvetica", 12))
tag_entry_label = tk.Label(right_frame, text="Enter confirmation tag number:", font=("Helvetica", 12))

cap = cv2.VideoCapture(0)

# reader = SimpleMFRC522()
def detect_faces():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        
        panel.img = img
        panel.config(image=img)
        panel.after(10, detect_faces)  

def read_rfid_card():
    try:
        tag_id, _ = reader.read()
        # Check the tag_id against the database
        if is_valid_tag(tag_id):
            points = get_points_for_tag(tag_id)
            message_label.config(text=f"Congrats! You have {points} points")
            root.after(10000, resume_reading_rfid)
        else:
            show_tag_entry()
    except Exception as e:
        print("Error reading RFID card:", e)

def is_valid_tag(tag_id):
    # Implement your logic to check if tag_id is in the database
    # Return True if valid, False otherwise
    return False

def get_points_for_tag(tag_id):
    # Implement your logic to retrieve points for the tag from the database
    # Return the points as an integer
    return 0

def show_tag_entry():
    message_label.pack_forget()
    rfid_confirmation_label.pack()
    tag_entry_label.pack()
    tag_entry.pack()
    enter_button.pack()

def on_enter_button_click():
    entered_tag_id = tag_entry.get()
    if is_valid_tag(entered_tag_id):
        points = get_points_for_tag(entered_tag_id)
        rfid_confirmation_label.config(text=f"Congrats! You have {points} points")

        root.after(10000, resume_reading_rfid)
    else:
        rfid_confirmation_label.config(text="Invalid tag number. Try again.")

def hide_tag_entry():
    rfid_confirmation_label.pack_forget()
    tag_entry_label.pack_forget()
    tag_entry.pack_forget()
    enter_button.pack_forget()
    message_label.config(text="Place your RFID Card")
    message_label.pack()

def resume_reading_rfid():
    hide_tag_entry()
    # read_rfid_card()

enter_button = tk.Button(right_frame, text="Enter", font=("Helvetica", 12), padx=10, pady=5, command=on_enter_button_click)

panel = tk.Label(left_frame)
panel.pack()

detect_faces()

# read_rfid_card()

root.mainloop()

cap.release()
cv2.destroyAllWindows()
