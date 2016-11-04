from abc import ABCMeta, abstractmethod
from selenium import webdriver

class AbstractComicSource(object):
  """ AbstractComicSource for base class of the comic source object

  Attributes:
    browser: the name of the browser used to choose the which webdriver use
    comicName: the name or url code of the comic you interested
  """

  __metaclass__ = ABCMeta

  baseUrl = ""

  def __init__(self, browser, comicName):
    """ Return a comic source object for crawling """
    self.browser = self.browserInit(browser)
    self.comicName = comicName

  def browserInit(self, browser):
    """ Initialize the webdriver for crawler"""
    if browser.lower() == "firefox":
      browser = webdriver.Firefox()
    elif browser.lower() == "chrome":
      browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    elif browser.lower() == "ie":
      browser = webdriver.Ie()
    elif browser.lower() == "opera":
      browser = webdriver.Opera()
    else:
      browser = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')

    browser.implicitly_wait(.5)
    return browser

  def quit(self):
    self.browser.quit()

  def getComicName(self):
    """ Return the comic name which you want to crawl """
    return self.comicName

  @abstractmethod
  def isCrawlAtEnd(self):
    """ Return a bool indicating the end of the crawling """
    pass

  @abstractmethod
  def crawler(self, volumeNum):
    """ The main logic for crawling this comic source """
    pass