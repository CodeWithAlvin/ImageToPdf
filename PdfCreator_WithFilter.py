##neccessary imports##
from PIL import Image,ImageEnhance
import os,datetime

#class to get paths
class Paths:
	def __init__(self,value):
		self.path=value
	
class chcwd():
	@staticmethod		
	def MainDirectly():
		if os.path.exists(path_image.path):
			os.chdir(path_image.path)
		else:
			os.mkdir(path_image.path)
			os.chdir(path_image.path)
		
	@staticmethod
	def ExportedPath():
		if not os.path.exists(path_exported.path):	
			os.mkdir(path_exported.path)

class PhotoFilter:
	@staticmethod
	def Filter1(image,no):
		img=Image.open(image)			
		#converting to black and white
		color=ImageEnhance.Color(img)
		step1=color.enhance(0.1)
		# adjusting Shapness
		sharp=ImageEnhance.Sharpness(step1)
		step2=sharp.enhance(5)		
		# adjusting Contrast
		contrast=ImageEnhance.Color(step2)
		step3=contrast.enhance(2)
		#Adjusting brightness
		brightness=ImageEnhance.Brightness(step3)
		step4=brightness.enhance(2)
		print(f"===================================\n{no} photo filtered \n")
		return step4

class operation:
	@staticmethod
	def Pdf(pics_list):
		#first image obj
		img1=pics_list[0]
		#removing first image obj
		pics_list.remove(img1)
		img1.save(f"{path_exported.path}/AlvinSaini-{date}.pdf",save_all=True,append_images=pics_list)
		print(f"===================================\n[ AlvinSaini-{date}.pdf ] Created")

	@staticmethod
	def Image (pic_list):
		i=1
		for obj in pic_list:
	 		obj.save(f"{path_exported.path}/{i}.jpg")
	 		i+=1
		print("===================================\nImages Saved")
																					
																						
if __name__=="__main__":	
	pics_obj=[]
	date=datetime.datetime.now()																								
	#object of class PATHS 		
	path_image=Paths("/storage/emulated/0/PythonPdfMaker")
	path_exported=Paths("/storage/emulated/0/PythonPdfMaker/exported")
	
	chcwd.MainDirectly()
	chcwd.ExportedPath()
	image_list=[fil for fil in os.listdir() if fil.endswith(".jpg")]

	for v in range(0,len(image_list)):
		pic=PhotoFilter.Filter1(image_list[v],v+1)
		pics_obj.append(pic)
		v+=1
	
	inp=input("Press \n•P for pdf\n•I for Images\n•B for both\n")
	
	if inp=="P" or inp=="p":
		operation.Pdf(pics_obj)
	elif inp=="I" or inp=="i":
	 	operation.Image(pics_obj)
	elif inp=="b" or inp=="B":
		operation.Image(pics_obj)
		operation.Pdf(pics_obj)

