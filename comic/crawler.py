class Crawler(object):
  """ The comic crawler that walk though the online comic repository
  and download the comics!

  Attributes:
    comicSource: The AbstractComicSource object defining the source to crawler
    volumeNum: The specified volume that start downloading to end
    onlyGetCurVol: Whether download the current volume only
    downloadDir: The directory to store the downloaded contents
  """

  def __init__(self, comicSource, volumeNum, onlyGetCurVol, downloadDir):
    """ Return the Crawler object to manipulate the comic download"""
    self.comicSource = comicSource
    self.volumeNum = volumeNum
    self.onlyGetCurVol = onlyGetCurVol
    self.downloadDir = downloadDir

  def run(self):
    """ Start to the crawling """
    print("INFO: Start crawling comic, " + self.comicSource.getComicName())

    if not self.onlyGetCurVol:
      pageNotFoundCounter = 0
      while self.comicSource.isCrawlAtEnd() == False:
        print("INFO: Crawling Volume " + str(self.volumeNum) + "...")

        if self.comicSource.crawler(self.volumeNum, self.downloadDir) == False:
          pageNotFoundCounter += 1
        else:
          pageNotFoundCounter = 0

        if pageNotFoundCounter >= 500:
          print("ERROR: Comic " + self.comicSource.getComicName() + " not found, exit")
          break

        self.volumeNum += 1
    else:
      print("INFO: Crawling Volume " + str(self.volumeNum) + "...")
      self.comicSource.crawl(self.volumeNum)

    print("INFO: Retrieve comic end!")
    self.comicSource.quit()
