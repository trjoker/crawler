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

API_KEY = 'key'
API_SECRET = 'password'
TAG = 'automobile'
NAME='automobile'
PIC_SIZE = 'url_z'
PATH = "E:/图片数据集/未筛/下载/"

# 输入API的key和secret
flickr = flickrapi.FlickrAPI(API_KEY, API_SECRET, cache=True)


def save_image(photos, word):
    counter = 1
    if not os.path.exists(PATH + word):
        os.mkdir(PATH + word)
    # 判断名字是否重复，获取图片长度
    for photo in photos:
        try:
            # url = photo.get(PIC_SIZE)
            # print(str(url))
            time.sleep(0.1)
            urllib.request.urlretrieve(photo.get(PIC_SIZE),
                                       PATH + word + '/' + word + str(counter) + '.jpg')
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
        photos = flickr.walk(tags=TAG, per_page=5, pages=1, extras=PIC_SIZE)
        save_image(photos, NAME)
    except Exception as e:
        print(e.args)


crawler()