import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('--fname', type=str, help='file name to add table of contents to')


def generate_toc(fname):

    with open(fname) as f:    
        content = f.read()
        heading_locs = [m.start() for m in re.finditer('#+', content)]
        structure = {}
        level_prev = 1
        parent = []
        for i in heading_locs:
            text = content[i:].split('\n')[0]
            level_cur = len([m.start() for m in re.finditer('#', text)])
            text = text.replace('#','').strip()
            
            if level_cur==1:
                parent = parent[0:-2]
            if level_cur>level_prev:
                parent.append(old_text)
            
            if level_cur-level_prev>=1 or parent is not None:
                temp_structure = structure
                for p in parent:
                    temp_structure = temp_structure[p]
                temp_structure.update({text:{}})
            elif parent is None:
                structure.update({text:{}})

            old_text = text
            print(structure)
            level_prev = level_cur

if __name__ == "__main__":
    args = parser.parse_args()
    generate_toc(args.fname)