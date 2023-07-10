import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('--fname', type=str, help='file name to add table of contents to')

def get_structure(content):
    heading_locs = [m.start() for m in re.finditer('#+', content)]
    list_struct = []
    for i in heading_locs:
        text = content[i:].split('\n')[0]
        list_struct.append(text)
        
    return heading_locs, list_struct


def gen_toc(structure):
    prev = 1
    toc = '''
<div class="DivTableOfContentsLink toc">
    <ul class="toc__list">
        <ul class="toc__sublist">'''
    for k in structure:
        cur = sum([1 for c in k if c=='#'])
        if cur==prev:
            toc += f'''
    <li><a href="#{k.replace(" ","-")}">{k.replace("#","").strip()}</a></li>'''
        elif cur+1==prev:
            toc += f'''
    </ul>
    <li><a href="#{k.replace(" ","-")}">{k.replace("#","").strip()}</a></li>'''

        elif cur==prev+1:
            toc += f'''
    <ul class="toc__sublist">
        <li><a href="#{k.replace(" ","-")}">{k.replace("#","").strip()}</a></li>'''
        prev=cur

    toc += '''
        </ul>
    </ul>
</div>'''
    return toc

def update_content(content, indices, toc, links):
    content_new = content[0:indices[0]] + '\n' + toc + '\n' + links[0] +'\n\n'
    for i in range(1,len(indices)):
        content_new +=  '\n' + content[indices[i-1]:indices[i]] + '\n' + links[i] + '\n' 

    return content_new

def generate_toc(fname):

    with open(fname) as f:    
        content = f.read()
        indices, structure = get_structure(content)
        toc = gen_toc(structure)
        links = [f'<p id = "{i.replace("#","").strip().replace(" ","-")}"></p>' for i in structure]
        content_updated = update_content(content, indices, toc, links)
        
        with  open(fname.replace('.md','_new.md'),'w+') as fnew: 
            fnew.write(content_updated)
        
    

if __name__ == "__main__":
    args = parser.parse_args()
    generate_toc(args.fname)