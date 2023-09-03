import tkinter as tk

# Create the main window
root = tk.Tk()

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate dimensions for the container
container_width = int(screen_width * 0.25)
container_height = int(screen_height * 0.25)

# Create a container frame
container_frame = tk.Frame(root, width=container_width, height=container_height)
container_frame.pack_propagate(False)  # Prevent the frame from adjusting to its content
container_frame.pack()

# Add the phrase label and center it
phrase_label = tk.Label(container_frame, text="Scan your RFID", font=("Helvetica", 16))
phrase_label.pack(fill=tk.BOTH, expand=True)
phrase_label.pack_propagate(False)  # Prevent the label from adjusting to its content
phrase_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the GUI main loop
root.mainloop()

# import tkinter as tk
# from tkinter import Entry
# from mfrc522 import SimpleMFRC522  # Import the MFRC522 library
# import threading

# # Create the main window
# root = tk.Tk()

# # Get screen dimensions
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate dimensions for the container
# container_width = int(screen_width * 0.25)
# container_height = int(screen_height * 0.25)

# # Create a container frame
# container_frame = tk.Frame(root, width=container_width, height=container_height)
# container_frame.pack_propagate(False)  # Prevent the frame from adjusting to its content
# container_frame.pack()

# # Create a label and entry for RFID input
# rfid_label = tk.Label(container_frame, text="Scan your RFID", font=("Helvetica", 16))
# rfid_label.pack(fill=tk.BOTH, expand=True)
# rfid_label.pack_propagate(False)  # Prevent the label from adjusting to its content

# rfid_entry = Entry(container_frame, font=("Helvetica", 16))
# rfid_entry.pack(fill=tk.BOTH, expand=True)
# rfid_entry.pack_propagate(False)  # Prevent the entry from adjusting to its content

# # Function to handle RFID scanning in a separate thread
# def scan_rfid():
#     try:
#         rfid_reader = SimpleMFRC522()
#         rfid_label.config(text="Scan your RFID")

#         while True:
#             rfid_id, rfid_text = rfid_reader.read()
#             rfid_label.config(text="Enter RFID Pass")
#             rfid_entry.delete(0, tk.END)
            
#     except Exception as e:
#         print("Error reading RFID:", e)

# # Create a thread to handle RFID scanning
# rfid_thread = threading.Thread(target=scan_rfid)
# rfid_thread.daemon = True  # Set as a daemon thread to exit when the main program exits
# rfid_thread.start()

# # Start the GUI main loop
# root.mainloop()
