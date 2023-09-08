# 이미지 호스팅 사이트 : https://ifh.cc/
# svg to png : https://svgtopng.com/ko/
import http.client
import json

Lvimg = ['https://ifh.cc/g/LQJ8Cl.png',
         'https://ifh.cc/g/FT8wxt.png',
         'https://ifh.cc/g/vglZza.png',
         'https://ifh.cc/g/84ZwnK.png',
         'https://ifh.cc/g/jmvQGd.png',
         'https://ifh.cc/g/vq0OmX.png',
         'https://ifh.cc/g/prytZK.png',
         'https://ifh.cc/g/4qNJzr.png',
         'https://ifh.cc/g/Qr2qts.png',
         'https://ifh.cc/g/hrqNMn.png',
         'https://ifh.cc/g/1Do8WT.png',
         'https://ifh.cc/g/7R2zBx.png',
         'https://ifh.cc/g/VvTqo3.png',
         'https://ifh.cc/g/gsskxd.png',
         'https://ifh.cc/g/9CXcLK.png',
         'https://ifh.cc/g/prjtVB.png',
         'https://ifh.cc/g/FNlh9p.png',
         'https://ifh.cc/g/bArAfo.png',
         'https://ifh.cc/g/Rs28s4.png',
         'https://ifh.cc/g/vQmNCg.png',
         'https://ifh.cc/g/BDOcSH.png',
         'https://ifh.cc/g/oNaczn.png',
         'https://ifh.cc/g/Bf33HX.png',
         'https://ifh.cc/g/GfZlFn.png',
         'https://ifh.cc/g/g5DQnz.png',
         'https://ifh.cc/g/sOo3GL.png',
         'https://ifh.cc/g/B8pVqV.png',
         'https://ifh.cc/g/Nhx9pV.png',
         'https://ifh.cc/g/Yff080.png',
         'https://ifh.cc/g/5aWOtd.png',
         'https://ifh.cc/g/fxHXjy.png']

def get_tier_img(pid):
    conn = http.client.HTTPSConnection("solved.ac")

    headers = { 'Accept': "application/json" }

    conn.request("GET", "/api/v3/problem/show?problemId={}".format(pid), headers=headers)

    res = conn.getresponse()
    data = res.read()

    solved = json.loads(data.decode("utf-8"))
    lv = int(solved.get("level"))
    
    return Lvimg[lv]