import os
import sys
import urllib.request
import xml.etree.ElementTree as etree
import webbrowser

def Set_map():
    client_id = "SmUpG9NpShByzd1X1LbU"
    client_secret = "AcoyKCqpsb"
    encText = urllib.parse.quote("화정4동")
    # url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
    url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        f = open("test.xml","wb")
        f.write(response_body)
        f.close()

        tree = etree.parse("test.xml")
        root = tree.getroot()

        for x_point in root.iter("x"):
            print(x_point.text)
        for y_point in root.iter("y"):
            print(y_point.text)

        #url_png = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=" + client_id + "&url=file://c&crs=EPSG:4326&center="+ x_point.text+","+y_point.text+"&level=10&w=600&h=600&baselayer=satellite&overlayers=anno_satellite&format=jpeg"
        #request = urllib.request.Request(url_png)
        #request.add_header("X-Naver-Client-Id", client_id)
        #request.add_header("X-Naver-Client-Secret", client_secret)
        #response = urllib.request.urlopen(request)
        #rescode = response.getcode()
        #if (rescode == 200):
        #    webbrowser.open_new(url_png)
        #else:
        #    print("Error Code:" + rescode)
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)




Set_map()