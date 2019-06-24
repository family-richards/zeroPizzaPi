print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="simpleMicSpeechRecog",
      version='1.0',
      packages=['simpleMicSpeechRecog'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      license="MIT",
      description="A simple wrapper for SpeechRecognition so I can easily hear speech.",
      download_url="https://github.com/family-richards/zeroPizzaPi/tree/master/simpleMicSpeechRecog",
      url="https://github.com/family-richards/zeroPizzaPi/tree/master/simpleMicSpeechRecog")
print("Package installed!")
