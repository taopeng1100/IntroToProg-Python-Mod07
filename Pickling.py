# Use this script to test and show how python pickling works
# Use this site to learn the python pickling: https://www.tutorialspoint.com/python-pickling
# Created by Tao Peng on 05.20.2021

# import pickle module #
import pickle
# wb for write in bytes, and pickle.dump to write a list to a file in binary #
mylist = ['FDN','Manuscipt','grant']
with open("Test_demo_pickling.txt", "wb") as fh:
    pickle.dump(mylist, fh)

# rb for read in bytes, and pickle.load to convert a pickled list to an unpickled list #
File_pickled = open ("Test_demo_pickling.txt", "rb")
mylist_unpickled = pickle.load(File_pickled)
print(mylist_unpickled)