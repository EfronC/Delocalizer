import os
import argparse
from dotenv import load_dotenv

load_dotenv()

from delocalizer import Delocalizer

parser = argparse.ArgumentParser(description='Modify a subtitle track to make a delocalized version from a JSON file.')
parser.add_argument('--shift', dest='shift', type=float, action="store", default=0.0,
                   help='Shift time')
parser.add_argument('--j', dest='jfile', type=str, action="store", default=False,
                   help='JSON file')
parser.add_argument('--l', dest='language', type=str, action="store", default=False,
                   help='Language to search')
parser.add_argument('--w', dest='words', type=str, action="store", default=False,
                   help='Use an external lambda to get the keywords JSON')
parser.add_argument('--f', dest='folder', type=str, action="store", default=False,
                   help='Folder to save')
parser.add_argument('--k', dest='keep_subs', action=argparse.BooleanOptionalAction,
                   help='Keep unlocalized sub file')
parser.add_argument('--no-mux', dest='nomux', action=argparse.BooleanOptionalAction,
                   help='Not to make the last step')

path = './Finished'

def main():
	if not os.path.exists(path):
		os.mkdir(path)
	args = parser.parse_args()

	delocalizer = Delocalizer()
	s = delocalizer.prepare_data(args)
	if s:
		delocalizer.delocalize()

if __name__ == '__main__':
	main()
