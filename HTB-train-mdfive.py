import requests
import hashlib
import re

lien="http://178.128.40.63:30379/"
r=requests.session()
g=r.get(lien)
gl=re.search(r"<h3 align='center'>(\w*)</h3>",g.text)


tools=hashlib.md5(gl.group(1).encode('utf-8')).hexdigest()
print("donne md5 :-{}".format(tools))

data={'hash':tools}
g = r.post(url = url, data = data)

print(g.text)
