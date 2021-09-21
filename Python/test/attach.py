#!/usr/bin/env python3

import email
import os
from emaildata.attachment import Attachment

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

message = email.message_from_file(open(__location__,'mail.eml'))
for content, filename, mimetype, message in Attachment.extract(message):
    print (filename)
    with open(filename, 'w') as stream:
        stream.write(content)
    # If message is not None then it is an instance of email.message.Message
    if message:
        print ("The file {0} is a message with attachments.".format(filename))