from speech_recognition import Microphone as mic
from speech_recognition import Recognizer as recog
class MicSpeechHearer:
  def __init__(self):
    self.mic = mic()
    self.hearer = recog()
  def adjustForNoise(self, duration=1):
    with self.mic as micy:
      self.hearer.adjust_for_ambient_noise(micy, duration=duration)
  def listenAndHear(self, adjustForNoise=False, adjustDuration=1, runWhenAdjustedForNoise=""):
    if adjustForNoise:
      self.adjustForNoise(duration=adjustDuration)
      if runWhenAdjustedForNoise != "":
        runWhenAdjustedForNoise()
    with self.mic as micy:
      audio = self.hearer.listen(micy)
      try:
        return self.hearer.recognize_google(audio)
      except Exception as e:
        print("Exception:")
        print(e)
        return ""
