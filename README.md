# Comics Downloader

The python program that retrieves the comics from comic website.

(Currently support for [comic.sfacg.com](http://comic.sfacg.com) only)



## Required Module

Since this project using [Selenium](http://docs.seleniumhq.org) to crawl the comic website, the ```selenium```  module and a web browser (default is using [PhantomJS](http://phantomjs.org)) is required. 

```selenium``` can be download from its website or be installed through a third-party installer such as pip.

 And don't forget to check whether the webdriver installer is needed for your favorite browser.

(For Chrome, its webdrivre could be download from [here](https://sites.google.com/a/chromium.org/chromedriver/))

## Usage

```python
python main.py comicname [-v volumenum] [-b browsername] [-c]
```

**comicname**, the subpath of url followed by ```/HTML/``` to direct to the comic you interested.

For example, the case of [comic.sfacg.com](http://comic.sfacg.com) 

```http://comic.sfacg.com/HTML/Naruto/``` 

the comicname to input is the *Naruto*

#### Options

* **-v volumenum**, the volume number start to download from. default value is 1.
* **-b browsername**, the name of the browser this program to drive. default uses the PhantomJS. The driver path could be edited in the ```comic/source/abstract.py``` if your webdriver is installed in the other path.


* **-c**, the flag indicating to download the current volume only. If this flag is not set, the program will download the comic to the latest volume in the comic website.

  ​