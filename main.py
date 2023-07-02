
# This is a sample Python script.
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def getTitle(url):
    try:
        response = requests.get(myurl)
    except HTTPError as e:
        return None
    except URLError as e:
        return None

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.svdMainGrid1)
        trlist = soup.find('div', attrs={"id": "svdMainGrid1"})
    except AttributeError as e:
        return None
    return trlist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import requests
    from bs4 import BeautifulSoup

    stocklist = list()
    betalist = list()

    f = open('D:/MyML/GomuTool/code.txt', 'r')
    # 파일에 텍스트 쓰기
    while True:
        line = f.readline()
        if not line : break
        stocklist.append(line)
    # 파일 닫기
    f.close()


    count = 0
    for code in stocklist:
        myurl = "https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A"
        myurl += code.replace("\n","")

        trlist = getTitle(myurl)
        if trlist == None:
            betalist.append("empty")
        else:
            trlist3 = trlist.findAll("tr")
            tdlist = trlist3[3].findAll("td")
            # betalist.append(tdlist[1].text) #아래쪽에서 자장해준다

        count = count + 1
        numstr = str(count)
        numstr += ' '
        numstr += code.replace("\n","")
        numstr += ' '
        numstr += tdlist[1].text
        betalist.append(numstr)
        print(numstr)

    f = open('D:/MyML/GomuTool/betalist.txt', 'w', encoding='utf8')
    # 파일에 텍스트 쓰기
    for i in betalist:
        f.write(i+'\n')
    # 파일 닫기
    f.close()

    #print(soup)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
