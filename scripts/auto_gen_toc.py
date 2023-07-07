import argparse


parser = argparse.ArgumentParser()

parser.add_argument('md_fname', type=str, required=True,
                    help='file name to add table of contents to')


def generate_toc(fname):
    with open(fname) as f:
        print(f.read())



if __name__ == "__main__":
    args = parser.parse_args()
    generate_toc(args.fname)