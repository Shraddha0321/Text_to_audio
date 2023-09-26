from gtts import gTTS

#Read text from a file
with open("book.txt", "r") as file:
    book_text = file.read()
    
sections = book_text.split("\n\n")

#Convert each section to audio
for i ,section in enumerate(sections):
    tts = gTTS(section)
    audio_filename = f"chapter_{i + 1}.mp3"
    tts.save(audio_filename)
    print(f"Chapter {i+1} converted to {audio_filename}")
    
print("Audiobook creation complete.")