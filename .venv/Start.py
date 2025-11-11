import tkinter as tk
from tkinter import filedialog
import pandas as PD


def open_file():
    file_path = filedialog.askopenfilename(
        title="1st File",
        filetypes=(("Text files", "*.*"), ("All files", "*.*"))
    )
    file_path = filedialog.askopenfilename(
        title="2nd File",
        filetypes=(("Text files", "*.*"), ("All files", "*.*"))
    )
    if file_path:
        print(f"File selected: {file_path}")
        df = PD.read_excel(file_path)
        print(df.head())





root = tk.Tk()
root.withdraw()  # Hide the main window
open_file()