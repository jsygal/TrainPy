#!/usr/bin/env python3

import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html
from html.parser import HTMLParser

h = html.parser

html_data = 

msg = MIMEMultipart('alternative')
msg['Subject'] = ...
msg['From'] = ...
msg['To'] = ...
msg['Cc'] = ...
msg['Bcc'] = ...
headers = ... dict of header key / value pairs ...
for key in headers:
    value = headers[key]
    if value and not isinstance(value, basestring):
        value = str(value)
    msg[key] = value

part = MIMEText(html_data, 'html')
msg.attach(part)

outfile_name = os.path.join("/", "temp", "email_sample.eml")
with open(outfile_name, 'w') as outfile:
    gen = generator.Generator(outfile)
    gen.flatten(msg)

print "=========== DONE ============"