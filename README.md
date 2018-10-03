First check out if you have gpg installed. If not install gpg or gpg2.

If you use gpg change the code on lines 45 and 49 where is "gpg2" to "gpg"

Then generate a key:

	$ gpg2 --gen-key

You can to see the options typing:

	$ gpg2 --help

This script encrypt a folder and hide it and then remove the original folder.
