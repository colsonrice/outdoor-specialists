from pathlib import Path
import re,subprocess
root=Path(__file__).resolve().parent.parent
css=(root/'source/fonts.css').read_text();out=''
for n,block in enumerate(re.findall(r'@font-face \{.*?\}',css,re.S)):
 if "'Manrope'" in block: continue
 url=re.search(r'url\((.*?)\)',block)[1];name=f'font-{n}.ttf';p=root/'site/assets'/name
 if not p.exists():subprocess.run(['curl','-fsSL',url,'-o',str(p)],check=True)
 out+=block.replace(url,name)+'\n'
(root/'site/assets/fonts.css').write_text(out)
