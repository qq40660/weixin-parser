#!/usr/bin/python
#Filename: 
#author: Chester LU <usoluyun@gmail.com>

import os,sys
from xml.etree import ElementTree

class TextMessage(object):

    ToUserName   = ''
    FromUserName = ''
    CreateTime   = ''
    MsgType      = ''
    MsgId        = ''
    Content      = ''


    def __init__(self, xmldoc):
        try:
            if (xmldoc != None):
                self.__class__.ToUserName   = xmldoc.find('ToUserName').Text
                self.__class__.FromUserName = xmldoc.find('FromUserName').Text
                self.__class__.CreateTime   = xmldoc.find('CreateTime').Text
                self.__class__.MsgType      = xmldoc.find('MsgType').Text
                self.__class__.MsgId        = xmldoc.find('MsgId').Text
                self.__class__.Content      = xmldoc.find('Content').Text
        except:
            print "Unexptected error: " ,  sys.exc_info()[0]

if __name__=="__main__":
    with open('/Users/usoluyun/Nutstore/weixin/xml/msg_text_example.xml','r') as d:
        xmldoc = TextMessage(ElementTree.parse(d))
        print xmldoc.ToUserName
        print xmldoc.FromUserName
        print xmldoc.CreateTime
        print xmldoc.MsgType
        print xmldoc.MsgId
        print xmldoc.Content

