const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#nav');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';nav.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu();});
document.addEventListener('click',e=>{if(!e.target.closest('.header'))closeMenu();});
document.querySelectorAll('a[href="#design"],a[href="#build"],a[href="#care"]').forEach(a=>a.addEventListener('click',()=>{document.querySelector(a.getAttribute('href')).open=true;}));
const projects=[...document.querySelectorAll('.project')];
const filters=[...document.querySelectorAll('[data-filter]')];
filters.forEach(b=>b.addEventListener('click',()=>{filters.forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b));});let count=0;projects.forEach(p=>{p.hidden=b.dataset.filter!=='all'&&p.dataset.category!==b.dataset.filter;if(!p.hidden)count++;});document.querySelector('.gallery-status').textContent=b.dataset.filter==='all'?`Showing all ${count} project photos`:`Showing ${count} ${count===1?'photo':'photos'}`;}));
const dialog=document.querySelector('#lightbox');let active=0;let visible=projects;let opener;
function showPhoto(){const p=visible[active];document.querySelector('#lightbox-img').src=`assets/${p.dataset.image}.webp`;document.querySelector('#lightbox-img').alt=p.querySelector('img').alt;document.querySelector('#lightbox-title').textContent=p.dataset.title;document.querySelector('#lightbox-caption').textContent=p.querySelector('.project-caption>span').textContent;document.querySelector('#lightbox-count').textContent=`${active+1} / ${visible.length}`;}
projects.forEach(p=>p.addEventListener('click',()=>{opener=p;visible=projects.filter(x=>!x.hidden);active=visible.indexOf(p);showPhoto();dialog.showModal();}));
function step(delta){active=(active+delta+visible.length)%visible.length;showPhoto();}
document.querySelector('#prev-photo').addEventListener('click',()=>step(-1));document.querySelector('#next-photo').addEventListener('click',()=>step(1));document.querySelector('#close-lightbox').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
dialog.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();step(1);}if(e.key==='ArrowLeft'){e.preventDefault();step(-1);}});dialog.addEventListener('close',()=>opener?.focus());
if(location.hash){const t=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(t?.tagName==='DETAILS')t.open=true;}
