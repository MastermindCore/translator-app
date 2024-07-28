import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


LANGUAGES = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'italian': 'it',
    'japanese': 'ja',
    'korean': 'ko',
    'portuguese': 'pt',
    'russian': 'ru',
    'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW',
    'dutch': 'nl',
    'arabic': 'ar',
    'hindi': 'hi',
    'bengali': 'bn',
    'greek': 'el',
    'hebrew': 'he',
    'turkish': 'tr',
    'swedish': 'sv',
    'norwegian': 'no',
    'danish': 'da',
    'finnish': 'fi',
    'polish': 'pl',
    'czech': 'cs',
    'hungarian': 'hu',
    'thai': 'th',
    'indonesian': 'id',
    'vietnamese': 'vi'
}

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")
        self.root.geometry("600x400")
        self.root.config(bg="lightblue")

        # Input Text
        self.input_label = tk.Label(root, text="Enter text:", bg="lightblue", font=("Arial", 12))
        self.input_label.pack(pady=10)
        self.input_text = tk.Text(root, height=10, width=60)
        self.input_text.pack(pady=10)


        self.src_lang_label = tk.Label(root, text="Source Language:", bg="lightblue", font=("Arial", 12))
        self.src_lang_label.pack(pady=5)
        self.src_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.keys()), width=30)
        self.src_lang_combobox.set("english")
        self.src_lang_combobox.pack(pady=5)


        self.dest_lang_label = tk.Label(root, text="Target Language:", bg="lightblue", font=("Arial", 12))
        self.dest_lang_label.pack(pady=5)
        self.dest_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.keys()), width=30)
        self.dest_lang_combobox.set("spanish")
        self.dest_lang_combobox.pack(pady=5)

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text, bg="white", font=("Arial", 12))
        self.translate_button.pack(pady=10)


        self.output_label = tk.Label(root, text="Translated text:", bg="lightblue", font=("Arial", 12))
        self.output_label.pack(pady=10)
        self.output_text = tk.Text(root, height=10, width=60)
        self.output_text.pack(pady=10)

    def translate_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        src_lang = self.src_lang_combobox.get()
        dest_lang = self.dest_lang_combobox.get()

        if input_text and src_lang and dest_lang:
            try:
                src_lang_code = LANGUAGES.get(src_lang.lower())
                dest_lang_code = LANGUAGES.get(dest_lang.lower())
                translated_text = GoogleTranslator(source=src_lang_code, target=dest_lang_code).translate(input_text)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, translated_text)
            except Exception as e:
                messagebox.showerror("Translation Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill all the fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
