from pathlib import Path
import re,html,subprocess,concurrent.futures,urllib.parse,json,hashlib
from PIL import Image,ImageOps,ImageDraw
base='https://outdoorspecialists.net/'
def fetch(url):return subprocess.check_output(['curl','-fLsS','--max-time','30',url.replace(' ','%20')])
for i in range(38,45):
 p=Path(f'source/pages/attachment-{i}.html');p.write_bytes(fetch(base+f'?attachment_id={i}'))
urls=set()
for p in Path('source/pages').glob('*'):
 s=html.unescape(p.read_text())
 for u in re.findall(r'''(?:src|href)=["']([^"']+)["']''',s):
  if re.search(r'\.(jpg|jpeg|png|gif|webp)(\?|$)',u,re.I) or 'callback=image' in u:urls.add(u.replace('http://','https://'))
 if p.suffix=='.css':
  for u in re.findall(r'url\([\'\"]?([^\)\'\"]+)',s):urls.add(urllib.parse.urljoin(base+'wp-content/themes/highlight/style.css',u))
def save(u):
 name=urllib.parse.unquote(urllib.parse.urlparse(u).path.rsplit('/',1)[-1])
 if 'callback=' in u:name='sidebar-'+urllib.parse.parse_qs(urllib.parse.urlparse(u).query)['pid'][0]+'.jpg'
 name=re.sub(r'[^\w.\-]','-',name)
 p=Path('assets/originals')/name
 try:
  b=fetch(u);p.write_bytes(b)
  im=Image.open(p);return dict(url=u,file=str(p),width=im.width,height=im.height,sha256=hashlib.sha256(b).hexdigest())
 except Exception as e:return dict(url=u,error=str(e))
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=8).map(save,sorted(urls)))
Path('source/asset-manifest.json').write_text(json.dumps(rows,indent=2))
photos=[r for r in rows if r.get('width',0)>400 and r.get('height',0)>200]
canvas=Image.new('RGB',(1000,((len(photos)+3)//4)*190),'white');d=ImageDraw.Draw(canvas)
for n,r in enumerate(photos):
 im=Image.open(r['file']).convert('RGB');im.thumbnail((240,155));x=(n%4)*250;y=(n//4)*190;canvas.paste(im,(x,y));d.text((x,y+157),Path(r['file']).name,fill='black')
canvas.save('source/contact-sheet.jpg')
print(json.dumps(rows,indent=2));print('Photo count:',len(photos))
