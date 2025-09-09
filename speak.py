import pyttsx3
import sys

def find_voice_id(engine, name):
    """Finds a voice ID by a name contained within the voice's name."""
    voices = engine.getProperty('voices')
    for voice in voices:
        if name.lower() in voice.name.lower():
            return voice.id
    return None

def speak(text, voice_name=None):
    """
    Initializes a TTS engine, sets a specific voice if requested,
    speaks the given text, and exits.
    """
    try:
        engine = pyttsx3.init()

        if voice_name:
            voice_id = find_voice_id(engine, voice_name)
            if voice_id:
                engine.setProperty('voice', voice_id)
            # If voice not found, it will use the default, which is fine.

        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        with open("tts_error.log", "a") as f:
            f.write(f"Error speaking '{text}' with voice '{voice_name}': {e}\n")

if __name__ == "__main__":
    # The script now expects two arguments: the text and an optional voice name.
    if len(sys.argv) > 1:
        text_to_speak = sys.argv[1]
        voice_to_use = None
        if len(sys.argv) > 2:
            voice_to_use = sys.argv[2]
        
        speak(text_to_speak, voice_to_use)
