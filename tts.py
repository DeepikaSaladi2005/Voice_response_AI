from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file="output.mp3"):
    """
    Converts text to speech and saves it as an audio file.
    
    :param text: The text to convert to speech.
    :param language: The language for speech synthesis (default is 'en' for English).
    :param output_file: The name of the output MP3 file.
    """
    try:
        if not text.strip():  # Check if text is empty
            print("Error: No text provided for speech conversion!")
            return

        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)  # Save as an MP3 file

        # Play the generated speech
        os.system(f"start {output_file}")  
        print(f"Speech saved as {output_file} and played successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    user_text = input("Enter the text you want to convert to speech: ")  
    text_to_speech(user_text)
