import pandas as pd
from bs4 import BeautifulSoup
import re

def convertHtmlToCSV(filePath):
    with open(filePath) as f:
        soup = BeautifulSoup(f, 'html.parser')
    common=">[^><]+<"
    txt1=soup.find_all("th")
    txt2=soup.find_all("td")
    for i in range(len(txt1)):
        txt1[i]=str(txt1[i]).replace(" ",'')
        txt1[i]=str(txt1[i]).replace("\n",'')
    for i in range(len(txt2)):
        txt2[i]=str(txt2[i]).replace(" ",'')
        txt2[i]=str(txt2[i]).replace("\n",'')
    th=[]
    td=[]
    for i in txt1:
        if re.findall(common, str(i)):
            th.append(re.findall(common, str(i))[0][1:-1])
    for i in txt2:
        if re.findall(common, str(i)):
            td.append(re.findall(common, str(i))[0][1:-1])
    dict={}
    ind=0
    enum={}
    for i in th:
        dict[i]=[]
        enum[ind]=i
        ind+=1
    ind=0
    for i in td:
        dict[enum[ind]].append(i)
        ind+=1
        ind%=len(dict)
    df = pd.DataFrame(dict)
    df.to_csv('./sample.csv')


def main():
    path=r"C:\Users\Kunal\Downloads\sample-example.html"
    convertHtmlToCSV(path)
    
if __name__ == '__main__':
    main()
