import os
import sys
from datetime import datetime
import argparse

try:
  eg = """Examples:

            === To Encrypt ===
                    python3 code3.py -e -n [username] -i {folder}
            === To Decrypt ===
                    python3 code3.py -d -w [output] -o {file_encrypted}"""

  ap = argparse.ArgumentParser(prog="Cheshire", description="Cheshire's cat", epilog=eg, formatter_class=argparse.RawDescriptionHelpFormatter)
  ap.add_argument("-e", "--encrypt", help="Encrypt a folder", action="store_false")
  ap.add_argument("-d", "--decrypt", help="Decrypt a folder", action="store_false")
  ap.add_argument("-n", "--name", help="Name of the user")
  ap.add_argument("-i", "--encf", help="Directory's name to encrypt")
  ap.add_argument("-o", "--decf", help="Directory's name to decrypt")
  ap.add_argument("-w", "--write", help="Directory's name to save the files")
  args = vars(ap.parse_args())

  if len(sys.argv) != 6:
    ap.print_help()
    sys.exit(2)
  elif not args["encrypt"] is None and not args["name"] is None and not args["encf"] is None and os.path.isdir(args["encf"]) is True:
    abspath = os.path.abspath(sys.argv[5])
    dirpath = os.path.dirname(os.path.realpath(sys.argv[5]))
    folder = os.path.basename(os.path.normpath(sys.argv[5]))
    l1 = os.listdir(dirpath)
    abspath.replace("~/", "")

    if not ".backup" in l1:
      os.mkdir("{}/.backup".format(dirpath))

    gpg_file1 = "{}/.{}.tar.gz.gpg".format(dirpath, folder)
    gpg_file2 = ".{}.tar.gz.gpg".format(folder)

    if gpg_file2 in l1:
      old_file = "{}/.{}-{}.tar.gz.gpg".format(dirpath, datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), folder)
      os.rename(gpg_file1, old_file)
      os.system('mv {} {}/.backup'.format(old_file, dirpath))

    os.system('tar -czf {}/.{}.tar.gz -C {}/ {}/'.format(dirpath, folder, dirpath, folder))
    os.system('gpg2 -e -r {} {}/.{}.tar.gz'.format(args["name"], dirpath, folder))
    os.system('sudo rm -r {} {}/.{}.tar.gz'.format(abspath, dirpath, folder))
    sys.exit(0)
  elif not args["decrypt"] is None and not args["write"] is None and os.path.isfile(args["decf"]) is True and args["decf"].endswith(".gpg") is True:
    os.system('gpg2 -d -o {}.tar.gz {}'.format(args["write"], args["decf"]))
    os.mkdir(args["write"])
    os.system('tar -xzf {}.tar.gz -C {}'.format(args["write"], args["write"]))
    os.system('sudo rm -r {}.tar.gz'.format(args["write"]))
    sys.exit(0)
  else:
    ap.print_help()
    sys.exit(2)
except argparse.ArgumentError as exc:
  print(exc.message, "\n", exc.argument)
except Exception as e:
  print("\n{}\nError on line: {}\n".format(e, sys.exc_info()[-1].tb_lineno))
  sys.exit(2)



