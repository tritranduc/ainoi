import gtts
from playsound import playsound
import os
"""import shutil
from unittest import TestCase
#from pathology.path import Path
import pathlib
import inspect"""
def noinhe (noi,ngonnguinput,so) :
	a = os.getcwd()
	tao = a + "\\new"
	b = os.listdir(a)
	bc = "  ,  ".join(b)
	bcst = str (bc)
	acdft = a + "\\new\\"
	path = a
	new_name = "bạn có thể xoá"
	if "new" not in bcst:
		#tạo một thưu mục mới có tên là testdir
		os.mkdir(tao)
		print(os.listdir(path))

	mytext = noi
	duondan = acdft
	ten =  "abc"
	stso = str(so)
	duoi = ".mp3"
	tenfile =  duondan + ten + stso + duoi

	so = so
	import gtts
	from playsound import playsound
	ngonngu = ngonnguinput
	ghf = str(ngonngu)
	tts = gtts.gTTS(mytext, lang=ghf,slow =False,lang_check=True)
	tts.save(tenfile)
	playsound(tenfile,True)
	os.remove(tenfile)
	a1 = os.listdir()
	a2 = os.listdir()
	a3 ="  ,  ".join(a2)
	print(a3)
