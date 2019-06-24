from pygame.image import save
import pygame.camera as gamecam
gamecam.init()
class gameCam:
  def __init__(self, location, width, height):
    self.cammy = gamecam.Camera(location, (width, height))
    self.cammy.start()
  def start(self):
    self.cammy.start()
  def stop(self):
    self.cammy.stop()
  def takePicture(self):
    return self.cammy.get_image()
  def savePicture(self, filename):
    save(self.cammy.get_image(), filename)
