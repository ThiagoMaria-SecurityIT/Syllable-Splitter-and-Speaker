import tkinter as tk
from tkinter import font as tkFont
import pyphen
import subprocess
import sys

# --- Core Logic (remains the same) ---
def split_word_into_syllables(word):
    dic = pyphen.Pyphen(lang='en_US')
    hyphenated_word = dic.inserted(word)
    return hyphenated_word.split('-')

def is_valid_word(word):
    return word.isalpha()

# --- GUI Application ---
class SyllableSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Syllable Splitter")
        self.root.geometry("450x400") # Increased height for voice options

        # --- Style Configuration ---
        self.BG_COLOR = "#f0f0f0"
        self.BUTTON_COLOR = "#0078D4"
        self.SPEAK_BUTTON_COLOR = "#28a745"
        self.BUTTON_TEXT_COLOR = "#ffffff"
        self.TEXT_COLOR = "#1f1f1f"
        self.ERROR_COLOR = "#d9534f"
        
        self.root.configure(bg=self.BG_COLOR)

        # --- Font Configuration ---
        self.default_font = tkFont.Font(family="Segoe UI", size=10)
        self.entry_font = tkFont.Font(family="Segoe UI", size=11)
        self.result_font = tkFont.Font(family="Segoe UI", size=12)
        self.instruction_font = tkFont.Font(family="Segoe UI", size=9)

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        content_frame = tk.Frame(self.root, padx=20, pady=20, bg=self.BG_COLOR)
        content_frame.pack(expand=True, fill="both")

        # ... (Input and instruction labels are the same) ...
        input_label = tk.Label(content_frame, text="Enter a word:", font=self.default_font, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        input_label.pack(anchor="w")
        self.word_entry = tk.Entry(content_frame, font=self.entry_font, width=40, relief="solid", bd=1)
        self.word_entry.pack(pady=5, ipady=4, anchor="w")
        self.word_entry.focus_set()
        instruction_label = tk.Label(content_frame, text="Please enter only one word containing only letters.", font=self.instruction_font, bg=self.BG_COLOR, fg="grey")
        instruction_label.pack(anchor="w", pady=(0, 10))

        # --- NEW: Voice Selection Frame ---
        voice_frame = tk.LabelFrame(content_frame, text="Select Voice", font=self.default_font, bg=self.BG_COLOR, fg=self.TEXT_COLOR, padx=10, pady=5)
        voice_frame.pack(pady=10, fill="x")

        self.selected_voice = tk.StringVar(value="Zira") # Default to Zira

        zira_radio = tk.Radiobutton(voice_frame, text="Zira (Female)", variable=self.selected_voice, value="Zira", font=self.default_font, bg=self.BG_COLOR)
        zira_radio.pack(side="left", padx=10)

        david_radio = tk.Radiobutton(voice_frame, text="David (Male)", variable=self.selected_voice, value="David", font=self.default_font, bg=self.BG_COLOR)
        david_radio.pack(side="left", padx=10)

        # --- Button Frame ---
        button_frame = tk.Frame(content_frame, bg=self.BG_COLOR)
        button_frame.pack(pady=5)
        
        # ... (Button creation is the same) ...
        button_style = {"font": self.default_font, "fg": self.BUTTON_TEXT_COLOR, "relief": "flat", "padx": 10, "pady": 5}
        split_button = tk.Button(button_frame, text="Split Word", command=self.on_split_button_click, bg=self.BUTTON_COLOR, **button_style)
        split_button.pack(side="left", padx=5)
        clear_button = tk.Button(button_frame, text="Clear", command=self.on_clear_button_click, bg=self.BUTTON_COLOR, **button_style)
        clear_button.pack(side="left", padx=5)
        self.speak_button = tk.Button(button_frame, text="Speak", command=self.on_speak_button_click, bg=self.SPEAK_BUTTON_COLOR, state="disabled", **button_style)
        self.speak_button.pack(side="left", padx=5)

        # ... (Result display is the same) ...
        self.root.bind('<Return>', lambda event: self.on_split_button_click())
        result_label = tk.Label(content_frame, text="Result:", font=self.default_font, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        result_label.pack(anchor="w", pady=(10, 0))
        self.result_text = tk.StringVar()
        self.result_display_label = tk.Label(content_frame, textvariable=self.result_text, font=self.result_font, wraplength=380, justify="left", bg="white", relief="solid", bd=1, anchor="nw")
        self.result_display_label.pack(fill="x", ipady=8, ipadx=5)

    # --- MODIFIED: on_speak_button_click now sends the selected voice ---
    def on_speak_button_click(self):
        """Calls the speak.py script with the text and the selected voice."""
        text_to_speak = self.result_text.get()
        voice_choice = self.selected_voice.get() # Get the user's voice choice

        if text_to_speak and not text_to_speak.lower().startswith("error"):
            python_executable = sys.executable
            # Pass the voice choice as a second argument
            subprocess.Popen([python_executable, "speak.py", text_to_speak, voice_choice])

    # --- (Other methods are unchanged) ---
    def on_split_button_click(self):
        user_input = self.word_entry.get().strip()
        self.result_display_label.config(fg=self.TEXT_COLOR)
        self.speak_button.config(state="disabled")
        if not user_input: self.result_text.set("Error: Input is empty. Please enter a word."); self.result_display_label.config(fg=self.ERROR_COLOR); return
        if not is_valid_word(user_input): self.result_text.set(f"Invalid input: '{user_input}'. Please enter only one word containing only letters."); self.result_display_label.config(fg=self.ERROR_COLOR); return
        try:
            syllables = split_word_into_syllables(user_input)
            clean_output = "-".join(syllables)
            self.result_text.set(clean_output)
            self.speak_button.config(state="normal")
        except Exception as e: self.result_text.set(f"An error occurred: {e}"); self.result_display_label.config(fg=self.ERROR_COLOR)
    def on_clear_button_click(self):
        self.word_entry.delete(0, tk.END); self.result_text.set(""); self.result_display_label.config(fg=self.TEXT_COLOR); self.speak_button.config(state="disabled"); self.word_entry.focus_set()
    def on_closing(self): self.root.destroy()

def main():
    root = tk.Tk()
    app = SyllableSplitterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
