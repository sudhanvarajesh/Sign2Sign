from moviepy.editor import *
import os 
import time
start_time = time.time()
#res = ['DOG','ABC','YOU']
res = ['123456789abcdef']
cliplist=[]	
for i in res:
	filename = i+".mp4"
	filename1 = i.lower() + ".mp4"
	if filename1 not in os.listdir("ISLimages\\words"):
		for j in i:
			print('inside letters')
			filename = j+".mp4"
			clip = VideoFileClip(os.path.join("ISLimages\\letters",filename))
			cliplist.append(clip)
	else:
		clip = VideoFileClip(os.path.join("ISLimages\\words",filename1))
		cliplist.append(clip)
final = concatenate_videoclips(cliplist,method="compose")
print("--- %s seconds ---" % (time.time() - start_time))
#final.write_videofile("ISLimages\\merged.mp4")	
#print("--- %s seconds ---" % (time.time() - start_time))