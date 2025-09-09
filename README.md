# Syllable Splitter and Speaker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/OS-Windows_11-blue" alt="Operating System">
  <img src="https://img.shields.io/badge/Built_with-AI-green" alt="Built with AI">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

This project is an educational tool, built with Python, that demonstrates how to create a simple desktop application from the ground up. The application takes an English word, splits it into its phonetic syllables, and reads the result aloud using a Text-to-Speech (TTS ) engine.

The development of this project was iterative, starting with a basic command-line script and evolving into a full-featured graphical application. It serves as a practical case study for learners interested in GUI development, code organization, and integrating external tools.

<img width="442" height="427" alt="image" src="https://github.com/user-attachments/assets/fe56fe03-0f22-4504-bcf5-ffab88ba1f64" />  


---

### Index

1.  [Features](#features)
2.  [System Requirements](#system-requirements)
3.  [Project Structure](#project-structure)
4.  [How to Run the Project](#how-to-run-the-project)
5.  [Known Limitations](#known-limitations)
6.  [Future Implementations Under Review](#future-implementations-under-review)
7.  [A Note for Linux Users](#a-note-for-linux-users)
8.  [AI Transparency: A Note on Collaboration](#ai-transparency-a-note-on-collaboration)
9.  [About Me & Contact](#about-me--contact)  

---

### Features

*   **Syllable Splitting:** Accurately splits English words into phonetic syllables (e.g., "beautiful" -> `beau, ti, ful`) using the `pyphen` library.
*   **Graphical User Interface (GUI):** A clean and user-friendly interface built with Python's standard `Tkinter` library.
*   **Text-to-Speech (TTS):** Reads the syllabified word aloud using native OS voices.
*   **Voice Selection:** Allows the user to choose between the English (US) voices "David" (Male) and "Zira" (Female).
*   **Robust Architecture:** Uses a multi-process model to ensure the GUI remains responsive and stable during TTS playback.

---

### System Requirements

This application is designed to run on **Windows 11** and relies on specific Text-to-Speech voices that are pre-installed on most editions of the OS.

*   **Operating System:** Windows 11.
*   **Required Voices:**
    *   `Microsoft David Desktop - English (United States)`
    *   `Microsoft Zira Desktop - English (United States)`

#### How to Verify Your Installed Voices

Some specialized editions of Windows (like LTSC or N editions) may not include these voices by default. You can easily check if you have them installed:

1.  Press the **Windows Key** and type "Text-to-speech settings" and press Enter.
2.  In the settings window that opens, look for the "Voices" dropdown menu.
3.  Click the dropdown and check if "Microsoft David Desktop" and "Microsoft Zira Desktop" appear in the list.

If they are not present, you may need to install the English (United States) language pack via "Language settings" to get them.

---

### Project Structure

The code is organized into separate files for clarity and maintainability.

```
Syllable-Splitter-and-Speaker/
├── gui.py              # The main GUI application script.
├── speak.py            # A dedicated, separate script for handling TTS.
├── main.py             # The original command-line version of the app.
├── README.md           # This file
└── requirements.txt    # A list of Python libraries needed for the project.
```

---

### How to Run the Project

1.  **Clone the repository (or download the files) to your local machine.**

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the GUI application:**
    ```bash
    python gui.py
    ```

---

### Known Limitations

The primary limitation of this application lies with the standard, non-AI Text-to-Speech engines built into Windows.

**Syllable Pronunciation:**
The TTS engine interprets comma-separated text as a phrase. For a word like "correctly," which we split into `"cor, rect, ly"`, the engine may not recognize "cor" as a phonetic sound. Instead, it might default to "spelling mode" and read it as "C-O-R," followed by the sounds for "rect" and "ly."

This happens because the TTS engine is designed to pronounce whole words, not isolated phonetic fragments. This discovery was a key part of our development journey and led us to explore more advanced AI-based solutions.

---

### Future Implementations Under Review

To overcome the limitations of native TTS and to explore modern AI development, we are currently reviewing three advanced architectural approaches:

1.  **The Gradio API Model:** The local desktop app would call an API for a Hugging Face (HF) Space that hosts a powerful AI TTS model (like `suno/bark`). This would provide extremely high-quality audio while keeping the local app lightweight.
2.  **The Full Local Model:** The AI TTS model would be downloaded and run directly on the user's machine. This would allow for offline use but would require powerful hardware and a large initial download.
3.  **The Full Hugging Face Model:** The entire application, including the syllable-splitting logic, would be moved into a single Gradio web app on Hugging Face. This would make the tool instantly accessible to anyone with a web browser, with zero installation required.

---

### A Note for Linux Users

This application was primarily developed and tested on Windows 11. The `pyttsx3` library relies on TTS engines provided by the operating system.

*   **Installation:** Linux users may need to install a TTS engine manually, such as `espeak`, for `pyttsx3` to function:
    ```bash
    sudo apt-get install espeak
    ```
*   **AI Version as an Alternative:** Given the potential for configuration issues and the limitations of older TTS engines, Linux users might find a better experience using the web-based AI version of the TTS, which can be accessed here: [HF Space TTS Project](https://huggingface.co/spaces/ThiSecur/tts2-project ). This provides higher-quality audio and requires no local setup.

---

### AI Transparency: A Note on Collaboration

This project was developed collaboratively between a human developer and **Manus**, an AI agent from the Manus team. The process was iterative and conversational:

*   The user provided the initial goal and context.
*   Manus generated the initial code, suggested libraries (`pyphen`, `tkinter`, `pyttsx3`), and explained core programming concepts.
*   The user tested the code, provided critical feedback, and suggested new features.
*   When we encountered bugs, such as the TTS engine freezing the GUI or only playing once, we worked through the problem together. Manus proposed solutions (threading, subprocesses), and the user's clear testing and feedback helped us arrive at the final, stable architecture.

This README file itself was co-created, with the user defining its structure and requesting the inclusion of this transparency section. This project serves as a practical example of human-AI partnership, where the AI acts as a programming assistant and knowledge base, while the human guides the project's vision, goals, and quality assurance.

## About Me & Contact

**Thiago Maria - From Brazil to the World 🌎**  
*Senior Security Information Professional | Passionate Programmer | AI Developer*

With a professional background in security analysis and a deep passion for programming, I created this Github acc to share some knowledge about security information, cybersecurity, Python and AI development practices. Most of my work here focuses on implementing security-first at companies while maintaining usability and productivity.

Let's Connect:  

👇🏽 Click on the badges below:  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/thiago-cequeira-99202239/)  
[![Hugging Face](https://img.shields.io/badge/🤗Hugging_Face-AI_projects-yellow)](https://huggingface.co/ThiSecur)  
 
## Ways to Contribute:   
 Want to see more upgrades? Help me keep it updated!    
 [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT) 
