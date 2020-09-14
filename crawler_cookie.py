#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #建立一個 Request物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie":"over18=1", #新增cookie 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") #根據觀察，取得的資料是 JSON 格式

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") #讓BeautifulSuop 協助我們解析 HTML 格式文件
    titles=root.findAll("div", class_="title")  #尋找所有 class = "title" 的 div標籤
    for title in titles:
        if title.a != None: #   如果標題包含 a標籤 (沒有被刪除)，print
            print(title.a.string)
    # titles=root.find_all("div", class_="title") #尋找所有 class_"title"的 div文件
    # for title in titles:
    #     if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
    #         print(title.a.string)

    #抓取下一頁的連結
    nextLink=root.find("a", string="‹ 上頁") #找到內文是 < 上頁 的 a標籤
    # print(nextLink["href"])
    return nextLink["href"]
# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" 
pageURL="https://www.ptt.cc"+getData(pageURL) 
print(pageURL)
count=0
while count <3:  #抓三頁
    pageURL="https://www.ptt.cc"+getData(pageURL) # 進入迴圈跑getData，抓到第一頁後得到上一頁的網址，上一頁的網址會return pageURL
    count+=1
