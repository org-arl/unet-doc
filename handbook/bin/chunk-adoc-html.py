import copy, re, sys
from bs4 import BeautifulSoup

### settings

build = sys.argv[1]+'/'
base = sys.argv[2]

### load asciidoctor generated html

with open(build+base+'.html', 'rt') as fp:
    soup = BeautifulSoup(fp, 'lxml')

### helper functions

part_intro = {}
part_toc = {}
next_ch = {}
prev_ch = {}
ch_title = {}

def part_filename(id):
    return base+id+'.html'

def chapter_filename(id):
    return base+id+'.html'

def make_nav_bar(prev_title, next_title):
    nav_left_td = soup.new_tag('td', width='50%', align='left')
    if prev_title is not None:
        nav_left = soup.new_tag('a', href=chapter_filename(prev_title), style='text-decoration: none;')
        nav_left.string = '<<< ['+ch_title[prev_title]+']'
        nav_left_td.contents = [nav_left]
    nav_right_td = soup.new_tag('td', width='50%', align='right')
    if next_title is not None:
        nav_right = soup.new_tag('a', href=chapter_filename(next_title), style='text-decoration: none;')
        nav_right.string = '['+ch_title[next_title]+'] >>>'
        nav_right_td.contents = [nav_right]
    nav_bar = soup.new_tag('table', width='100%')
    nav_bar_tr = soup.new_tag('tr')
    nav_bar_tr.contents = [nav_left_td, nav_right_td]
    nav_bar.contents = [nav_bar_tr]
    return nav_bar

### rewrite links

content = soup.body.find_all(id='content')[0]
parts = soup.find_all('h1', 'sect0')
chapters = soup.find_all('div', 'sect1')

for part in parts:
    id = part['id']
    div = part.find_next_sibling('div')
    if 'partintro' in div['class']:
        part_intro[id] = div
    for a in soup.find_all(href='#'+id):
        a['href'] = part_filename(id)
        part_toc[id] = list(a.parent.children)

last_ch = None
for chapter in chapters:
    id = chapter.h2['id']
    ch_title[id] = re.sub(r'^\d+\. *', '', chapter.h2.string)
    next_ch[last_ch] = id
    prev_ch[id] = last_ch
    last_ch = id
    for a in soup.find_all(href='#'+str(id)):
        a['href'] = chapter_filename(id)
    for s in chapter.find_all(['h3','h4','h5','h6']):
        for a in soup.find_all(href='#'+str(s['id'])):
            a['href'] = chapter_filename(id)+a['href']

### write out chunked html files

for part in parts:
    id = part['id']
    content.clear()
    content.append(part)
    if id in part_intro:
        content.append(copy.copy(part_intro[id]))
    for toc in part_toc[id][1:-1]:
        content.append(copy.copy(toc))
    with open(build+part_filename(id), 'wt') as fp:
        print(soup.prettify(), file=fp)

last_chapter = None
for chapter in chapters:
    id = chapter.h2['id']
    content.clear()
    content.append(chapter)
    content.append(make_nav_bar(prev_ch[id] if id in prev_ch else None, next_ch[id] if id in next_ch else None))
    last_chapter = chapter.h2.string
    with open(build+chapter_filename(id), 'wt') as fp:
        print(soup.prettify(), file=fp)
