import cv2
import numpy as np
import uuid
import random
import glob
import pathlib
import os

save_path = ''
aug_data_path = ''

def image_list_from_txt(images_file):
	f = open(images_file+".txt", "r")

	image_names_list = []
	frames=0
	for x in f:
			frames=frames+1
			x= x.split('\n')[0]
			image_names_list.append(x)
			#frame = cv2.imread(x)
			#print(x)
			#print(frame.shape)
			
	return image_names_list


def get_rects(image_names_list):
	rects_list = []
	for x in image_names_list:  ###  loop over files

		x = x.replace('.png', '.txt')
		x = x.replace('.jpg', '.txt')

		try:
			text = open(x, "r")

			boxes = []
			for line in text:  ## loop over txt file lines
				box=[]
				box.append( float( line.split(' ')[1] ) )
				box.append( float( line.split(' ')[2] ) )
				box.append( float( line.split(' ')[3] ) )
				box.append( float( line.split(' ')[4] ) )
				box.append( float( line.split(' ')[0] ) )
				boxes.append(box)
				
			rects_list.append(boxes)	
		except:
			rects_list.append([])
			print('no box')
		
	#print(rects_list)
	return rects_list 

def visualize(frame, rects):
		img_h, img_w, _ = frame.shape
		for box in rects:
			x1, y1 = int((box[0] + box[2]/2)*img_w), int((box[1] + box[3]/2)*img_h)
			x2, y2 = int((box[0] - box[2]/2)*img_w), int((box[1] - box[3]/2)*img_h)
			cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
			
			cv2.putText(frame, str(int(box[4])), (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),1)

		#cv2.imshow("frame",frame)
		#key = cv2.waitKey(0) & 0xFF



def save(frame, rects):
	name = str( uuid.uuid4().hex )
	#print(name)
		
	s = open(save_path+name+".txt", "w+")
	for box in rects:
		x1   = box[0]
		y1   = box[1]
		w1   = box[2]
		h1   = box[3]
		cls  = box[4]
		
		cls, x1, y1, w1, h1 =str(int(cls))+" ", str(x1)+" ", str(y1)+" ", str(w1)+" ", str(h1)+"\n"

		#height,width,c = frame.shape
		#x1 =str( float(x+w/2)/width  )+" "
		#y1 =str( float(y+h/2)/height )+" "
		#w1 =str( float(w)/width  )+" "
		#h1 =str( float(h)/height )+"\n"

		s.write(cls+x1+y1+w1+h1) 
	s.close() 

	cv2.imwrite(save_path+name+".jpg",frame)


def fliplr(frame, rects):

	#x1, y1 = int((1-box[0] + box[2]/2)*img_w), int((box[1] + box[3]/2)*img_h)
	#x2, y2 = int((1-box[0] - box[2]/2)*img_w), int((box[1] - box[3]/2)*img_h)
	
	for box in rects:
		box[0] =  1-box[0]
	
	cv2.flip(frame, 1, frame)
	return  frame, rects
	
def flipud(frame, rects):

	#x1, y1 = int((1-box[0] + box[2]/2)*img_w), int((box[1] + box[3]/2)*img_h)
	#x2, y2 = int((1-box[0] - box[2]/2)*img_w), int((box[1] - box[3]/2)*img_h)
	
	for box in rects:
		box[1] =  1-box[1]
	
	cv2.flip(frame, 0, frame)
	return  frame, rects


def random_resize_hw(frame, rects):
	h,w,c = frame.shape
	blank = np.zeros((h,w,c), np.uint8)

	rand = np.random.randint(80, 100)
	randX = rand/100
	rand = np.random.randint(80, 100)
	randY = rand/100
	
	for box in rects:
		box[0] =  box[0]*randX
		box[1] =  box[1]*randY
	
	frame = cv2.resize(frame, (0,0), fx=randX , fy=randY ) 
	h,w,c = frame.shape
	
	blank[:h,:w]=frame
	
	return blank, rects

def add_gaussian_noise(X_img): # imgs
    gaussian_noise_imgs = []
    row, col, _ = X_img.shape
    # Gaussian distribution parameters
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    
    # for imgs
    gaussian = (np.random.random((row, col, 3))*50).astype(np.uint8)
    #gaussian = np.concatenate((gaussian, gaussian, gaussian), axis = 2)
    gaussian_img = cv2.addWeighted(X_img, 0.75, gaussian, 0.25, 0)
    #gaussian_noise_imgs.append(gaussian_img)


    #gaussian_noise_imgs = np.array(gaussian_noise_imgs, dtype = np.float32)
    return gaussian_img #gaussian_noise_imgs

def augment_gaussian(rgbImg):
    #augmented_images = []
    
    # original image
    #augmented_images.append(rgbImg)

    # fliped x-axis
    #rimg = rgbImg.copy()
    #cv2.flip(rimg, 1, rimg)
    #augmented_images.append(rimg)

    # add gaussian noise
    #for _ in range(10):
    gaussian_noise = rgbImg.copy()
    cv2.randn(gaussian_noise, (0,0,0),(20,20,20))
    rgbImg[rgbImg>230]=230
    
    gaussian = rgbImg + gaussian_noise
    #augmented_images.append(rimg + gaussian_noise)

    #for _ in range(10):
    #    uniform_noise = rgbImg.copy()
    #    cv2.randu(uniform_noise, 0, 1)
    #    augmented_images.append(rgbImg + uniform_noise)
    #    #augmented_images.append(rimg + uniform_noise)

    return gaussian


def apply_brightness_contrast(input_img, brightness = 1, contrast =1):
    rand = np.random.randint(80, 120)
    brightness = rand/100
    contrast = np.random.randint(1, 20)

    #0.9*img
    buf = cv2.addWeighted(input_img, brightness, input_img, 0, 0)


    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf


def motion_blur(img):
	# Specify the kernel size. 
	# The greater the size, the more the motion. 
	kernel_size = 5
  
	# Create the vertical kernel. 
	kernel_v = np.zeros((kernel_size, kernel_size)) 
  
	# Create a copy of the same for creating the horizontal kernel. 
	kernel_h = np.copy(kernel_v) 
  
	# Fill the middle row with ones. 
	kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size) 
	#kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size) 
  
	# Normalize. 
	kernel_v /= kernel_size 
	#kernel_h /= kernel_size 
  
	# Apply the vertical kernel. 
	vertical_mb = cv2.filter2D(img, -1, kernel_v) 
	#horizonal_mb = cv2.filter2D(img, -1, kernel_h)
	return vertical_mb

def sharpen(frame):
	sharpen_kernel  = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	frame = cv2.filter2D(frame, -1, sharpen_kernel)
	
	return frame

def add_image(frame):

	
	aug_files = glob.glob(aug_data_path+'*.png')
	how_many  = len(aug_files)
	#print(aug_files, how_many )
	
	randint = random.randint(1, how_many-1)
	this_file = aug_files[randint]
	#print('this file',this_file)

	img = cv2.imread(this_file)
	
	h,w,c = frame.shape
	img = cv2.resize(img, (w,h)) 
	
	#cv2.imshow('frame', frame)
	#cv2.imshow('img', img)
	#key = cv2.waitKey(0) & 0xFF
	
	frame = cv2.addWeighted(frame, 0.9, img, 0.1, 0)

	return frame
	




def augment(frame, rects, augmentation=1):


	
	if random.randint(0, 1):
			frame, rects = fliplr (frame, rects)
	if random.randint(0, 1):
			frame, rects = flipud (frame, rects)
	if random.randint(0, 1):
			frame, rects = random_resize_hw(frame, rects)
			
	if augment:	

		koef = 0.2
			
		if random.random() <= koef:	
			frame = cv2.blur(frame,(2,2))
		if random.random() <= koef:
			frame = sharpen(frame)
		#if random.randint(0, 1):
		#	frame = motion_blur(frame)
		if random.random() <= koef:
			frame = apply_brightness_contrast(frame)
		#if random.random() <= koef:
		#	frame = augment_gaussian(frame)
		if random.random() <= koef:	
			frame = add_gaussian_noise(frame)
		if random.random() <= koef:  
			frame = add_image(frame)
	
	return frame, rects


def main_loop(image_names_list, rects_list, augmentation=1):

	for i in range(len(image_names_list)):

		image_name = image_names_list[i]
		rects = rects_list[i]
		
		frame = cv2.imread(image_name)
		
		frame, rects = augment(frame, rects, augmentation)
		
		save(frame, rects)
		visualize(frame, rects)
		

def file_list(folder = './'): 


	files1 = glob.glob(folder+'*.jpg')
	files2 = glob.glob(folder+'*.png')
	files = files1+files2

	
	#path = str( pathlib.Path().resolve() )
	#path = '../drive/MyDrive/yolo/agenerated/true/'
	
	
	#print(files)
	return files


def run_folder(folder = 'fura/', n=10, augmentation=1):
	for i in range(n):
		#image_names_list = image_list_from_txt(folder)
		image_names_list = file_list(folder)
		rects_list  = get_rects(image_names_list)
		main_loop(image_names_list, rects_list, augmentation)
	print(folder,'len', len(image_names_list))
		
		
if __name__ == '__main__':
	#path = str( pathlib.Path().resolve() )
	#print(path)
	
	#save_path = '../drive/MyDrive/yolo/agenerated/true/save/'
	save_path = './save_heavy/'
	#os.mkdir(save_path)
	
	# gdisk1
	#aug_data_path = '../drive/MyDrive/yolo/agenerated/true/aug_data/'
	#run_folder('../drive/MyDrive/yolo/agenerated/true/heavy/', n=20)
	#run_folder('../drive/MyDrive/yolo/agenerated/true/fura/', n=20)
	#run_folder('../drive/MyDrive/yolo/agenerated/true/aug_data/', n=1, augmentation=0 )
	
	# gdisk2
	save_path = './save_heavy/'
	aug_data_path = './yolo/agenerated/true/aug_data/'
	run_folder('./yolo/agenerated/true/heavy/', 10)
	run_folder('./yolo/agenerated/true/fura/', 10)
	run_folder('./yolo/agenerated/true/aug_data/', augmentation=0 )
	
	# pc
	#save_path = './save/'
	#aug_data_path = './aug_data/'
	#run_folder('./heavy/', 10)
	#run_folder('./fura/', 10)
	#run_folder('./aug_data/', augmentation=0 )





