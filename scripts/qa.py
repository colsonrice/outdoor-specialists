from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
from PIL import Image
root=Path(__file__).resolve().parent.parent/'site'
class Check(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0;self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.errors.append('Duplicate ID '+a['id'])
   self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='img' and 'alt' not in a:self.errors.append('Image missing alt')
  for key in ['src','href']:
   if a.get(key):self.refs.append(a[key])
c=Check();c.feed((root/'index.html').read_text())
for ref in c.refs:
 u=urlsplit(ref)
 if u.scheme or u.netloc:continue
 if u.fragment and u.fragment not in c.ids:c.errors.append('Missing anchor '+ref)
 if u.path and not (root/unquote(u.path)).exists():c.errors.append('Missing file '+ref)
for p in (root/'assets').glob('*.webp'):
 with Image.open(p) as im:im.verify()
assert c.h1==1
assert 'noindex' in (root/'index.html').read_text()
assert not c.errors,c.errors
print(f'PASS: {len(c.refs)} local/link references checked; images valid; anchors valid; demo noindex enabled.')
