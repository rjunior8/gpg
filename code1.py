import os
import sys
from datetime import datetime

if len(sys.argv) != 4:
	print("\nUSAGE:\n\t=== To Encrypt ===\n\n\t\tpython3 code1.py -e [username] {folder}")
	print("\n\t=== To Decrypt ===\n\n\t\tpython3 code1.py -d [output] {file_encrypted}\n")
	sys.exit(2)
elif sys.argv[1] == "-e" and os.path.isdir(sys.argv[3]) == True:
	abspath = os.path.abspath(sys.argv[3])
	dirpath = os.path.dirname(os.path.realpath(sys.argv[3]))
	folder = os.path.basename(os.path.normpath(sys.argv[3]))
	l1 = os.listdir(dirpath)
	abspath.replace("~/", "")

	if ".backup" in l1:
		pass
	else:
		os.mkdir("{}/.backup".format(dirpath))

	gpg_file1 = "{}/.{}.tar.gz.gpg".format(dirpath, folder)
	gpg_file2 = ".{}.tar.gz.gpg".format(folder)

	if gpg_file2 in l1:
		old_file = "{}/.{}-{}.tar.gz.gpg".format(dirpath, datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), folder)
		os.rename(gpg_file1, old_file)
		os.system('mv {} {}/.backup'.format(old_file, dirpath))

	os.system('tar -czf {}/.{}.tar.gz -C {}/ {}/'.format(dirpath, folder, dirpath, folder))
	os.system('gpg -e -r {} {}/.{}.tar.gz'.format(sys.argv[2], dirpath, folder))
	os.system('sudo rm -r {} {}/.{}.tar.gz'.format(abspath, dirpath, folder))
	sys.exit(0)
elif sys.argv[1] == "-d" and os.path.isfile(sys.argv[3]) and os.path.splitext(sys.argv[3])[1] == ".gpg":
	os.system('gpg -d -o {}.tar.gz {}'.format(sys.argv[2], sys.argv[3]))
	os.mkdir(sys.argv[2])
	os.system('tar -xzf {}.tar.gz -C {}'.format(sys.argv[2], sys.argv[2]))
	os.system('sudo rm -r {}.tar.gz'.format(sys.argv[2]))
	sys.exit(0)
else:
	print("\nUSAGE:\n\t=== To Encrypt ===\n\n\t\tpython3 code1.py -e [username] {folder}")
	print("\n\t=== To Decrypt ===\n\n\t\tpython3 code1.py -d [output] {file_encrypted}\n")
	sys.exit(2)

