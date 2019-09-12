# cambridge-dictionary-crawler
My first web crawler. This project let you use command line to look up Cambridge dictionary instead of using browser yourself.
## !! New features
After looking up to the dictionary, you can store the word to the excel file. When next time you want to review it, it's handy. 
### steps
* new an vocabulary file 
* refer the cell position with your code to personalize your vocabulary list.
* attachment excel file is a sample.
## Tools used in the project
``requests``, ``lxml``, ``xpath``
## Run in the command line
For example, we want to look `spider` up in the Cambridge dictionary.
```
python3 CambridgeDic.py spider
```
Then the result is
```
Definition:
 a small creature with eight thin legs that catches insects in a web (= a net made from sticky threads)
 蜘蛛
Sentence:
 We watched the spider spin its web.
 我們看著蜘蛛織網。
 ```
 ## Personalization
This is the result of the first definition and sentence in the Cambridge dictionary page. If you want to personalize the result, you can change the content in `xpath` to scratch what you want.


