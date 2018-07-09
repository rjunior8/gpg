import os
import sys
from datetime import datetime

l1 = os.listdir()

if ".backup" in l1:
	pass
else:
	os.mkdir(".backup")

if len(sys.argv) != 4:
	print("\nUSAGE:\n\t=== To Encrypt ===\n\n\t\tpython3 code1.py -e [username] {folder}")
	print("\n\t=== To Decrypt ===\n\n\t\tpython3 code1.py -d [output] {file_encrypted}\n")
	sys.exit(2)
elif sys.argv[1] == "-e" and not sys.argv[2] is None and os.path.isdir(sys.argv[3]) == True and not sys.argv[3] is None:
	folder = sys.argv[3].replace('/', '')
	gpg_file = ".{}.tar.gz.gpg".format(folder)
	if gpg_file in l1:
		old_file = ".{}{}".format(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), gpg_file)
		os.rename(gpg_file, old_file)
		os.system('mv {} .backup'.format(old_file))
	os.system('tar -czf .{}.tar.gz {}'.format(folder, sys.argv[3]))
	os.system('gpg -e -r {} .{}.tar.gz'.format(sys.argv[2], folder))
	os.system('sudo rm -r {} .{}.tar.gz'.format(sys.argv[3], folder))
	sys.exit(0)
elif sys.argv[1] == "-d" and not sys.argv[2] is None and os.path.isfile(sys.argv[3]) and os.path.splitext(sys.argv[3])[1] == ".gpg":
	os.system('gpg -d -o {}.tar.gz {}'.format(sys.argv[2], sys.argv[3]))
	os.system('tar -xzf {}.tar.gz'.format(sys.argv[2]))
	os.system('sudo rm -r {}.tar.gz'.format(sys.argv[2]))
	sys.exit(0)
else:
	print("\nUSAGE:\n\t=== To Encrypt ===\n\n\t\tpython3 code1.py -e [username] {folder}")
	print("\n\t=== To Decrypt ===\n\n\t\tpython3 code1.py -d [output] {file_encrypted}\n")
	sys.exit(2)

