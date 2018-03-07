from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear")
head = '''
	||        ||        |||    |||  |||||||||  |||||||||
	||       ||||       || |  | ||  ||         || 
       	||      ||  ||      ||  ||  ||  ||         || 
	||     ||    ||     ||      ||  |||||      |||||||||
||	||    ||||||||||    ||      ||  ||                ||
||	||   ||        ||   ||      ||  ||                ||
  ||||||    ||          ||  ||      ||  |||||||||  |||||||||   

--------------- A YouTube video downloader ------------------
-----------------------------------------------------------AN 
'''

menulist = '''
1. Download
2. Exit
'''
print head

def quit():
    con = raw_input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
	print "Thank you for using james!"
        exit()
    else:
        os.system("clear")
        print head
        menu()

def download():
	try:
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('YouTube URL: ')])
            print("")
            quit()
	except(KeyboardInterrupt):
		print ""

def menu():
	print menulist
	try:
		choice = input("james:~$")
		if choice == 1:
			download()
		elif choice == 2:
			quit()
		else:
			print "Wrong option number!"
			menu()
	except(KeyboardInterrupt):
		print ""

menu()
