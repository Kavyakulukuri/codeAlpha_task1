import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Translator instance
        self.translator = Translator()

        # Title Label
        title_label = tk.Label(root, text="Language Translator", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)

        # Input Text
        self.input_label = tk.Label(root, text="Enter Text:", font=("Helvetica", 12))
        self.input_label.pack(pady=5)
        self.input_text = tk.Text(root, height=6, width=60, wrap=tk.WORD, font=("Helvetica", 12))
        self.input_text.pack(pady=5)

        # Language Selection
        lang_frame = tk.Frame(root)
        lang_frame.pack(pady=10)

        tk.Label(lang_frame, text="From:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
        self.src_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), width=20, state="readonly")
        self.src_lang.grid(row=0, column=1, padx=5)
        self.src_lang.set("english")  # Use lowercase matching LANGUAGES values

        tk.Label(lang_frame, text="To:", font=("Helvetica", 12)).grid(row=0, column=2, padx=5)
        self.dest_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), width=20, state="readonly")
        self.dest_lang.grid(row=0, column=3, padx=5)
        self.dest_lang.set("french")  # Use lowercase matching LANGUAGES values

        # Translate Button
        translate_button = tk.Button(root, text="Translate", command=self.translate, font=("Helvetica", 12), bg="#007BFF", fg="white")
        translate_button.pack(pady=10)

        # Output Text
        self.output_label = tk.Label(root, text="Translated Text:", font=("Helvetica", 12))
        self.output_label.pack(pady=5)
        self.output_text = tk.Text(root, height=6, width=60, wrap=tk.WORD, font=("Helvetica", 12))
        self.output_text.pack(pady=5)

    def translate(self):
        try:
            # Get input text and languages
            input_text = self.input_text.get("1.0", tk.END).strip()
            if not input_text:
                messagebox.showwarning("Input Error", "Please enter text to translate.")
                return

            src_lang_name = self.src_lang.get().lower()  # Convert to lowercase for compatibility
            dest_lang_name = self.dest_lang.get().lower()

            if not src_lang_name or not dest_lang_name:
                messagebox.showwarning("Language Selection Error", "Please select both source and target languages.")
                return

            # Get language codes
            src_lang_code_list = [key for key, val in LANGUAGES.items() if val.lower() == src_lang_name]
            dest_lang_code_list = [key for key, val in LANGUAGES.items() if val.lower() == dest_lang_name]

            if not src_lang_code_list or not dest_lang_code_list:
                messagebox.showerror("Language Error", "Selected language is not supported!")
                return

            src_lang_code = src_lang_code_list[0]
            dest_lang_code = dest_lang_code_list[0]

            # Translate
            translated = self.translator.translate(input_text, src=src_lang_code, dest=dest_lang_code)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
