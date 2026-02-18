import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def process_file(input_path):
    try:
        file_extension = os.path.splitext(input_path)[1].lower()
        df = pd.read_csv(input_path) if file_extension == '.csv' else pd.read_excel(input_path)

        # Clean column names
        df.columns = df.columns.str.strip()

        if 'Sub-category' not in df.columns:
            messagebox.showerror("Error", f"Could not find 'Sub-category'. found: {list(df.columns)}")
            return

        # 1. SET THE DEFAULT
        # This fills the whole column with 'N' first, so nothing stays blank
        df['Visible to Guest'] = 'N'

        # 2. DEFINE KEYWORDS
        # If the cell CONTAINS any of these words, it gets marked 'Y'
        show_keywords = ["Electronics", "Fans", "Appearance", "Maintenance", "Venting", "Glass"]

        # 3. APPLY "SHOW" LOGIC (Keyword search)
        # We search for any row where 'Sub-category' contains a word from our show_list
        pattern = '|'.join(show_keywords) # Creates a search like "Electronics|Fans|Venting"
        
        # This finds matches regardless of upper/lower case
        mask = df['Sub-category'].astype(str).str.contains(pattern, case=False, na=False)
        df.loc[mask, 'Visible to Guest'] = 'Y'

        # Save result
        output_path = os.path.join(os.path.dirname(input_path), "updated_parts_list.csv")
        df.to_csv(output_path, index=False)
        
        messagebox.showinfo("Success", "Logic applied! Anything not matching your 'Show' list was set to 'N'.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# --- GUI Boilerplate ---
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Spreadsheets", "*.csv *.xlsx *.xls")])
    if file_path: process_file(file_path)

root = tk.Tk()
root.title("Parts Visibility Updater")
root.geometry("400x200")
tk.Label(root, text="Select a CSV or Excel file", pady=20).pack()
tk.Button(root, text="Select Spreadsheet", command=select_file, bg="#0078D7", fg="white", padx=20, pady=10).pack()
root.mainloop()