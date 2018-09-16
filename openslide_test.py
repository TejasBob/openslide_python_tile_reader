import openslide as op
import subprocess as sp
import cv2
import numpy as np 


def main():
	slide = op.open_slide("/home/bob/Downloads/CMU-1.ndpi")
	for i in range(0, 150):
		cmd = "cp -r /home/bob/Documents/openSlide/CMU-1_files/16/1_" + str(i) + ".jpeg" + " /home/bob/Documents/data/1/"
		sp.call(cmd, shell=True)


def main2():
	tileSize = 254
	overlap = 1
	slide = op.open_slide("/home/bob/Downloads/CMU-1.ndpi")
	index = 0;
	count = 0
	while(index<38144):
		if index == 0:
			i = slide.read_region((255, 0), 0, (256,255))
		else:
			i = slide.read_region((255, index), 0 , (256,256))

		i = np.asarray(i)
		cv2.imwrite("/home/bob/Documents/data2/1/1_" + str(count) + ".jpeg", i[:,:,[2,1,0]],  [cv2.IMWRITE_JPEG_QUALITY, 90])
		index+=256
		index -= 2
		count+=1

if __name__ == '__main__':
	main()
	main2()