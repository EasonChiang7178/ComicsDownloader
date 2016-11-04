from comic.crawler import Crawler
from comic.source.sfacg import Sfacg

import sys
import getopt


# =============== Declare default value =============== #
browser = "phantomjs"

downloadDirectory = "downloaded/"

comicName = ""
volumeNum = 1
onlyGetCurVol = False

# =============== END declare default value =============== #


opts, args = getopt.getopt(sys.argv[2:], "v:b:c")

for op, value in opts:
  if op == "-v":      # download from which volume
    volumeNum = int(value)
  elif op == "-b":      # the name of the browser to use
    browser = valuse
  elif op == "-c":      # download only current volume
   onlyGetCurVol = True
  else:
    sys.exit()

# Check whether user input which comic to download
if len(sys.argv) > 1 and sys.argv[1] and '-' not in sys.argv[1]:
  comicName = sys.argv[1]

if comicName == "":
  print("ERROR: Please enter the comic name")
  sys.exit()


comicCrawler = Crawler(
  Sfacg(browser, comicName),
  volumeNum,
  onlyGetCurVol,
  downloadDirectory
)

comicCrawler.run()
