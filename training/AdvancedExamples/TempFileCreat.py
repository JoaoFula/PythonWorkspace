# working with temp files
import tempfile
# create a temporary file and write some data into it
fp = tempfile.TemporaryFile()
fp.write(b"Hello world!")
# read data from file
fp.seek(0)
fp.read()
b'Hello world'
# close the file and it will be removed
fp.close()

# create a temporary file through context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b"Hello world!")
    fp.seek(0)
    fp.read()
b'Hello world'
#file is now closed and removed

#create a temporary directory through context manager
with tempfile.TemporaryFile() as tmpdirname:
    print('Created temporary directory', tmpdirname)