"""
#
# Part: Python PIP
#
"""

# pip list  
# python.exe -m pip install --upgrade pip
# pip install camelcase


import camelcase
camel = camelcase.camelcase()
txt = "hello wolrd"
print(camel.hump(txt))