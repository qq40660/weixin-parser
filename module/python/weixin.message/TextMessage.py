#!/usr/bin/python
#Filename: 
#author: Chester LU <usoluyun@gmail.com>

import os,sys
from xml.etree import ElementTree

class TextMessage(object):
    '''
    The weixin text message adaptor
    '''
    def __init__(self, testmsg):
        try:
            self.ToUserName   = testmsg.find('ToUserName').text
            self.FromUserName = testmsg.find('FromUserName').text
            self.CreateTime   = testmsg.find('CreateTime').text
            self.MsgType      = testmsg.find('MsgType').text
            self.MsgId        = testmsg.find('MsgId').text
            self.Content      = testmsg.find('Content').text
        except:
            print "Unexptected error: " ,  sys.exc_info()[0]

if __name__=="__main__":
    with open('/Users/usoluyun/Nutstore/weixin/xml/msg_text_example.xml','r') as d:
        testmsg = TextMessage(ElementTree.parse(d))
        print testmsg.ToUserName
        print testmsg.FromUserName
        print testmsg.CreateTime
        print testmsg.MsgType
        print testmsg.MsgId
        print testmsg.Content

