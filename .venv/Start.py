import tkinter as tk
import pandas as PD
from tkinter import filedialog
from rapidfuzz import fuzz, process



def open_file():
    file_path_1 = filedialog.askopenfilename(title="1st File",  filetypes=(("Text files", "*.*"), ("All files", "*.*")) )
    file_path_2 = filedialog.askopenfilename(title="2nd File",  filetypes=(("Text files", "*.*"), ("All files", "*.*")) )
    output_file = filedialog.asksaveasfilename(
        title="Save Results",
        defaultextension=".xlsx",  # automatically add .xlsx if user doesn't
        initialfile="fuzzy_results.xlsx",  # proposed filename
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )




    if file_path_1:
        df1 = PD.read_excel(file_path_1)
        df_data_1 = PD.DataFrame(df1)

    if file_path_2:
        df2 = PD.read_excel(file_path_2)
        df_data_2= PD.DataFrame(df2)

    def get_best_match(row_value):
        best_match = process.extractOne(row_value, df_data_2['Nazov'].tolist(), scorer=fuzz.ratio)
        matched_string = best_match[0]  # best matching string
        score = best_match[1]  # similarity score
        return PD.Series([matched_string, f"{int(score)} %"])

    df_data_1[['Best_Match', 'Fuzzy_Match']] = df_data_1['Nazov'].apply(get_best_match)

    if output_file:  # user did not cancel
        df_data_1.to_excel(output_file, index=False)

    print(f"Saved to {output_file}")


root = tk.Tk()
root.withdraw()  # Hide the main window
open_file()