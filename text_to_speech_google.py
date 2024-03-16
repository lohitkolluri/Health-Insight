# from google.cloud import texttospeech

# import pyttsx3
# import tempfile
# import os


def save_to_audio_file(audio_content):
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(audio_content)
        print('Audio content written to file "output.mp3"')


# def synthesize(text):
#     print("[gcp tts] rendering", text)
#     client = texttospeech.TextToSpeechClient()
#     # Set the text input to be synthesized
#     synthesis_input = texttospeech.SynthesisInput(text=text)

#     # Build the voice request, select the language code ("en-US") and the ssml
#     # voice gender ("neutral")
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="hi-IN",
#         name="hi-IN-Neural2-B",
#     )

#     # Select the type of audio file you want returned
#     audio_config = texttospeech.AudioConfig(
#         speaking_rate=0.9, audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     # Perform the text-to-speech request on the text input with the selected
#     # voice parameters and audio file type
#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )
#     return response.audio_content


# def synthesize(text):
#     print("[local TTS] rendering", text)
#     engine = pyttsx3.init()
#     engine.setProperty("rate", 150)  # Adjust the speaking rate as needed
#     engine.setProperty("volume", 1.0)  # Adjust the volume as needed

#     # Set language and voice (if available)
#     voices = engine.getProperty("voices")
#     for voice in voices:
#         if "hi" in voice.languages:  # Check if voice supports Hindi language
#             engine.setProperty("voice", voice.id)
#             break

#     # Save synthesized speech to a temporary audio file
#     temp_audio_file = "temp_audio.mp3"
#     engine.save_to_file(text, temp_audio_file)
#     engine.runAndWait()

#     # Read the generated audio file and return its content
#     audio_content = b""
#     with open(temp_audio_file, "rb") as audio_file:
#         audio_content = audio_file.read()

#     # Clean up temporary audio file
#     os.remove(temp_audio_file)

#     return audio_content


def synthesize(text):
    # Placeholder function, does nothing
    print("[gcp tts] rendering is disabled")
    return None
