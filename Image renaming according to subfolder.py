# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:33:02 2024

@author: Anas Odeh 
"""

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
from tkinter.ttk import Progressbar
import os
import shutil
import easygui
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Home\Desktop\Anas Odeh\computional biology\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_progress(value):
    # Update the progress bar's value
    progress_bar['value'] = value
    # Update the text above the progress bar to show current progress percentage
    progress_text = f"Progress: {int(value)}%"
    canvas.itemconfig(progress_label, text=progress_text)
    window.update_idletasks()

def complete_progress():
    messagebox.showinfo("Success", "Images have been successfully renamed and pooled.")
    # Reset progress bar and label when done
    progress_bar['value'] = 0
    canvas.itemconfig(progress_label, text="Progress: 0%")

def process_images():
    base_directory = input_folder
    output_directory = os.path.join(base_directory, 'pooled_images')

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    items = [item for item in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, item)) and item != 'pooled_images']
    total_items = len(items)

    for index, item in enumerate(items, start=1):
        item_path = os.path.join(base_directory, item)
        for file in os.listdir(item_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
                old_file_path = os.path.join(item_path, file)
                new_file_name = f"{item}{os.path.splitext(file)[1]}"
                new_file_path_in_subfolder = os.path.join(item_path, new_file_name)
                new_file_path_in_output = os.path.join(output_directory, new_file_name)

                # Rename within the subfolder
                if not os.path.exists(new_file_path_in_subfolder):
                    shutil.move(old_file_path, new_file_path_in_subfolder)

                # Copy to the pooled_images directory
                if not os.path.exists(new_file_path_in_output):
                    shutil.copy2(new_file_path_in_subfolder, new_file_path_in_output)
                break
        
        progress = (index / total_items) * 100
        window.after(100, update_progress, progress)

    window.after(100, complete_progress)

def start_image_processing_thread():
    if 'input_folder' not in globals():
        messagebox.showerror("Error", "Please select your input folder first!")
        return
    
    # Start the image processing in a separate thread to avoid UI freezing
    threading.Thread(target=process_images, daemon=True).start()

def select_input_folder():
    folder = easygui.diropenbox()
    if folder:
        global input_folder
        input_folder = folder

window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(719.0, 512.0, image=image_image_1)

canvas.create_text(60.0, 964.0, anchor="nw", text="©️By using this application, you must cite the name of the app developer, Anas Odeh", fill="#FFFFFF", font=("Inter Bold", 32 * -1))

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(735.0, 55.0, image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=select_input_folder, relief="flat")
button_1.place(x=446.0, y=236.0, width=603.0, height=45.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=start_image_processing_thread, relief="flat")
button_2.place(x=594.0, y=317.0, width=283.0, height=41.0)

# Create and place the progress label and bar
progress_label = canvas.create_text(720, 400, text="Progress: 0%", fill="white", font=("Helvetica", 24))
progress_bar = Progressbar(canvas, orient='horizontal', length=1000, mode='determinate')
progress_bar.place(x=220, y=425)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(712.0, 150.0, image=image_image_3)

window.resizable(False, False)
window.mainloop()
