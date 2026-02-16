from PyPDF2 import PdfReader
from gtts import gTTS

# Load PDF
reader = PdfReader("sample.pdf")

text = ""

# Extract text from all pages
for page in reader.pages:
    text += page.extract_text()

# Convert to speech
tts = gTTS(text)

# Save as MP3
tts.save("audiobook.mp3")

print("✅ Audiobook created!")