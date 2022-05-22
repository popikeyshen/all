import glob
import pathlib
import os

def file_list(folder = './'): 


	files1 = glob.glob(folder+'*.jpg')
	files2 = glob.glob(folder+'*.png')
	files = files1+files2
	
	files = map(os.path.basename, files)

	return files
	

folder_to_files = '../darknet/save/'
path_to_list = '../drive/MyDrive/yolo/agenerated/true/'

files = file_list(folder_to_files )

# ../drive/MyDrive/yolo/saveV3/0cfcf3a294ed4c0fb3320c5ce57b41e4.jpg

#path = pathlib.Path().resolve()
#path = '..'+str(path)+'/'
#print(path)


s = open(path_to_list + "trueData.txt", "w+")
for f in files:
	s.write( folder_to_files + str(f)+'\n' ) 
s.close() 
