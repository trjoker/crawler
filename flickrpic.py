import flickrapi
import urllib
import os
import sys
import requests
import re
import urllib
import json
import socket
import urllib.request
import urllib.parse
import urllib.error
# 设置超时
import time

socket.setdefaulttimeout(30)
API_KEY = '90202ae94bac166ea37546b7f3aaa964'
API_SECRET = 'd6ecaca50580ba5f'
TAG = 'chair'
NAME = 'chair'
PIC_SIZE = 'url_z'
# PIC_SIZE = 'url_n'
PATH = "E:/picdata/untreated/"

# 输入API的key和secret
flickr = flickrapi.FlickrAPI(API_KEY, API_SECRET, cache=True)


def download(photo):
    pass


def save_image(photos, word):
    counter = 1
    if not os.path.exists(PATH + word):
        os.mkdir(PATH + word)
    # 判断名字是否重复，获取图片长度
    for photo in photos:

        try:
            url = str(photo.get(PIC_SIZE))
            path = PATH + word + '/' + word + str(counter) + '.jpg'
            print(url)
            time.sleep(0.1)
            urllib.request.urlretrieve(url,
                                       path)
        except socket.timeout:
            # count = 1
            # while count <= 5:
            #     try:
            #         url = str(photo.get(PIC_SIZE))
            #         path = PATH + word + '/' + word + str(counter) + '.jpg'
            #         urllib.request.urlretrieve(url, path)
            #         break
            #     except socket.timeout:
            #         err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
            #         print(err_info)
            #         count += 1
            #         continue
            # if count > 5:
            #     print("downloading picture fialed!")
            continue
        except urllib.error.HTTPError as urllib_err:
            print(urllib_err)
            continue
        except Exception as err:
            time.sleep(1)
            print(err)
            print("产生未知错误，放弃保存")
            continue
        else:
            print("小黄图+1,已有" + str(counter) + "张小黄图")
            counter += 1
    return


# downloading images
def crawler():
    try:
        photos = flickr.walk(text=TAG, sort="relevance", per_page=5, pages=1, extras=PIC_SIZE)
        save_image(photos, NAME)
    except Exception as e:
        print(e.args)


crawler()
