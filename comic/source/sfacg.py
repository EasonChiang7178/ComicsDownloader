from comic.source.abstract import AbstractComicSource
from comic import utils

from urllib.request import urlretrieve
# from urllib.error import ContentTooShortError, HTTPError
# from http.client import RemoteDisconnected
import os

class Sfacg(AbstractComicSource):
  """ The online comics named sfacg """

  baseUrl = "http://comic.sfacg.com/HTML/"

  def __init__(self, browser, comicName):
    """ Return a sfacg comic source object for crawling """
    self.browser = self.browserInit(browser)
    self.comicName = comicName
    self.isAtEnd = False
    self.j = ""

  def isCrawlAtEnd(self):
    """ Return a bool indicating the end of the crawling """
    return self.isAtEnd

  def crawler(self, volumeNum, downloadDir):
    """ The main logic for crawling this comic source """

    # To check whether the volume exists, try 2 times
    for i in range(2):
      volumeStr = utils.paddingLeftStr(str(volumeNum), "0", 3) + self.j + "/"
      self.browser.get(self.baseUrl + self.comicName + "/" + volumeStr)
      if self.__isVolumeNotFound(volumeStr) == True:
        # After 2 tries, the volume may not be existed
        if i == 1:
          print("ERROR: volume " + str(volumeNum) + " of the " + self.comicName + " is not exist!")
          return False
        # If not found, find it's j of volume again
        if self.j == "":
          self.j = "j"
        else:
          self.j = ""
      else:
        break

    storePath = downloadDir + self.comicName + "/" + volumeStr
    self.__createVolumeDirectory(storePath)

    # Retrieve the comics!
    print(">\t", end="")

    curVolTotalPage = int(self.browser.find_element_by_id("TotalPage").text) - 1
    for page in range(1, curVolTotalPage):
      curPicElement = self.browser.find_element_by_id("curPic")
      curPicSrc = curPicElement.get_attribute("src")

      picFileName = volumeStr[:-1] + "_" + utils.paddingLeftStr(str(page), "0", 3) + curPicSrc[-4:]

      # Try 3 times if the retrieve was failed
      for i in range(3):
        try:
          urlretrieve(curPicSrc, storePath + picFileName)
          print(picFileName + (", " if page != (curVolTotalPage - 1) else ""), end="", flush=True)
          break
        except Exception as e:
          if i == 2:
            print("\nERROR: retrieve fail at " + picFileName + " with " + e.__class__.__name__, end=("" if i < 2 else "\n"))
            with open("RetrieveError" + self.comicName + ".txt", "a", encoding="UTF-8") as file:
              file.write("Failed at " + picFileName[:-4] + ": " + curPicSrc + "\n")
          else:
            print("\nWARNING: retrieve fail at " + picFileName + " with " + e.__class__.__name__, end=("" if i < 2 else "\n"))
            print("\nINFO: try again...")
          print(">\t", end="")

      curPicElement.click()

    print("\nINFO: volume " + volumeStr[:-1] + " end\n")

    # Check whether entering the end of the comic
    if 'javascript' not in self.browser.execute_script("return nextVolume;"):
      self.browser.find_element_by_css_selector('a[href="javascript:NextVolume();"]').click()
    else:
      self.isAtEnd = True

    return True

  def __isVolumeNotFound(self, volumeStr):
    """ Check whether browser enter the not found page """
    if 'LOLI' in self.browser.find_elements_by_tag_name('img')[1].get_attribute('src'):
      print("INFO: volume " + volumeStr[:-1] + " not found, try to find volume " + (volumeStr[:-1] + "j" if len(volumeStr) == 4 else volumeStr[:-2]))
      return True
    else:
      return False

  def __createVolumeDirectory(self, storePath):
    """ Create the direcotory to store the volume of the comic """
    os.makedirs(storePath, exist_ok=True)
