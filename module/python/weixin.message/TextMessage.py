#!/usr/bin/python
#Filename: 
#author: Chester LU <usoluyun@gmail.com>

import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError


class TextMessage(object):
    def __init__(self, test_msg):
        """

        @rtype : xml object
        """
        try:
            self.to_username = test_msg.find('ToUserName').text
            self.from_username = test_msg.find('FromUserName').text
            self.create_time = test_msg.find('CreateTime').text
            self.msg_type = test_msg.find('MsgType').text
            self.msg_id = test_msg.find('MsgId').text
            self.content = test_msg.find('Content').text
        except ParseError:
            print "Unexpected error: ", sys.exc_info()[0]


if __name__ == "__main__":
    with open('../../../xml/msg_text_example.xml', 'r') as d:
        test_msg = TextMessage(ElementTree.parse(d))
        print test_msg.to_username
        print test_msg.from_username
        print test_msg.create_time
        print test_msg.msg_type
        print test_msg.msg_id
        print test_msg.content

