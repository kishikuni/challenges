# http://tinyurl.com/jmlkvxm

import re


#-- Challenge 01
with open('zen.txt') as f:
    mls = f.read()

m = re.findall("Dutch.", mls, re.MULTILINE)
print(m)


#-- Challenge 02
ad = "Arizona: 479, 501, 870. California: 209, 213, 650."
m = re.findall("\d",ad, re.IGNORECASE)
print(m)

#-- Challenge 03
msg = "The ghost that says boo haunts the loo."
m = re.findall(".oo", msg, re.IGNORECASE)
print(m)
