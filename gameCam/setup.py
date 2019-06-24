print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="gameCam",
      version='1.0',
      packages=['gameCam'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      license="MIT",
      description="A wrapper for PyGame's camera so I can take USB webcam photos.",
      download_url="https://github.com/family-richards/zeroPizzaPi/tree/master/gameCam",
      url="https://github.com/family-richards/zeroPizzaPi/tree/master/gameCam")
print("Package installed!")
