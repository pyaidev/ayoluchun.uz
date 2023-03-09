import re


facebook_regex = re.compile(r'^(https?://)?(www\.)?facebook.com/(?P<username>[a-zA-Z0-9(\.\?)?])+$')
telegram_regex = re.compile(r'^(https?://)?(www\.)?telegram.com/(?P<username>[a-zA-Z0-9(\.\?)?])+$')
linkden_regex = re.compile(r'^(https?://)?(www\.)?linkden.com/(?P<username>[a-zA-Z0-9(\.\?)?])+$')
imkon_regex = re.compile(r'^(https?://)?(www\.)?imkon.uz/(?P<username>[a-zA-Z0-9(\.\?)?])+$')