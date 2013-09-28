#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>

import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError


class TextMessageReply(object):
    def __init__(self, msg):
        """

        @rtype : xml object
        """
        try:
            self.to_username = msg.find('ToUserName').text
            self.from_username = msg.find('FromUserName').text
            self.create_time = msg.find('CreateTime').text
            self.msg_type = msg.find('MsgType').text
            self.msg_id = msg.find('MsgId').text
            self.content = msg.find('Content').text
        except ParseError:
            print "Unexpected error: ", sys.exc_info()[0]


if __name__ == "__main__":
    with open('../../../xml/msg_text_example.xml', 'r') as d:
        test_msg = TextMessageReply(ElementTree.parse(d))
        print test_msg.to_username
        print test_msg.from_username
        print test_msg.create_time
        print test_msg.msg_type
        print test_msg.msg_id
        print test_msg.content

