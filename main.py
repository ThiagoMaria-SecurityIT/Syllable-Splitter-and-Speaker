import pyphen
import re # Import the regular expressions module

def split_word_into_syllables(word):
    """
    Splits a single word into syllables using the Pyphen library.
    """
    try:
        dic = pyphen.Pyphen(lang='en_US')
        hyphenated_word = dic.inserted(word)
        return hyphenated_word.split('-')
    except Exception as e:
        return [f"Could not process the word '{word}'. Error: {e}"]

def is_valid_word(word):
    """
    Checks if the input string is a valid word (contains only letters).
    Returns True if valid, False otherwise.
    """
    # The isalpha() method returns True if all characters in the string are alphabetic.
    return word.isalpha()

def main():
    """
    Main function to run the interactive syllable splitter.
    """
    print("--- Syllable Splitter ---")
    print("Enter a word to see it split into syllables. Type 'quit' to exit.")
    
    while True:
        user_input = input("\nPlease enter a word: ").strip() # Use .strip() to remove leading/trailing whitespace
        
        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
            
        if not user_input:
            print("Input is empty. Please enter a word.")
            continue

        # --- NEW: Add validation check ---
        if not is_valid_word(user_input):
            print(f"Invalid input: '{user_input}'. Please enter a word containing only letters.")
            continue

        syllables = split_word_into_syllables(user_input)
        print(f"The syllables for '{user_input}' are: {syllables}")

if __name__ == "__main__":
    main()
