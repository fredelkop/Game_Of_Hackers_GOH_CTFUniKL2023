import os
import tarfile #Module used to work with tar files

for i in range(2023, 0, -1): #For loop from 2023 to 0 going down by 1
	fn = "UniKL" + str(i) + ".tar"
	print(fn)
	tar = tarfile.open(fn)
	tar.extractall()
	tar.close()