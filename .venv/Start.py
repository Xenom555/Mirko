import tkinter as tk
from tkinter import filedialog
import pandas as PD
from rapidfuzz import fuzz

def open_file():
    file_path_1 = filedialog.askopenfilename(
        title="1st File",
        filetypes=(("Text files", "*.*"), ("All files", "*.*"))
    )
    file_path_2 = filedialog.askopenfilename(
        title="2nd File",
        filetypes=(("Text files", "*.*"), ("All files", "*.*"))
    )
    if file_path_1:
        print(f"File selected: {file_path_1}")
        df1 = PD.read_excel(file_path_1)
        print(df1.head())

    if file_path_2:
        print(f"File selected: {file_path_2}")
        df2 = PD.read_excel(file_path_2)
        print(df2.head())

root = tk.Tk()
root.withdraw()  # Hide the main window
open_file()