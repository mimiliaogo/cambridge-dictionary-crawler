import requests, sys
from lxml import etree

def Dic(word):
    r = requests.get('https://dictionary.cambridge.org/dictionary/english-chinese-traditional/' + word, headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
    
    # parse html
    html = r.text
    page = etree.HTML(html)
    # eng def
    endefs = page.xpath('//b[@class="def"]')
    endef = endefs[0].xpath('string(.)')
    # chi def
    # xpath will return a list
    chdef = page.xpath('//*[@id="english-chinese-traditional-1-1-1"]/div/div[1]/span/span')
    chdefstr = chdef[0].xpath('string(.)')
    print('Definition:\n',endef.strip(), '\n',chdefstr.strip())

    # eng sentence
    enstc = page.xpath('//*[@id="english-chinese-traditional-1-1-1"]/div/div[1]/span/div[1]/span[1]')
    enstcstr = enstc[0].xpath('string(.)')
    # chi sentence
    chstc = page.xpath('//*[@id="english-chinese-traditional-1-1-1"]/div/div[1]/span/div[1]/span[2]')
    chstcstr = chstc[0].xpath('string(.)')

    print('Sentence:\n', enstcstr.strip(),'\n', chstcstr.strip())

if len(sys.argv) > 1:
    word = sys.argv[1]
    Dic(word)
else:
    print('No word!')
