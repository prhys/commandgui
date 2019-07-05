#!/usr/bin/env python

import os
import json
import tkinter as tk
from tkinter.ttk import Combobox

os.chdir('./scripts/')

def retrieve_index():
	try:
		#Tries to retrieve the index file, if it exists
		file = open('../index.json', 'r')
		global lista
		lista = json.load(file)
	
	except FileNotFoundError:
		#Generate index of files and categories
		categories = [directory for directory in os.listdir() if os.path.isdir(directory)]
		lista = {}
		for category in categories:
			os.chdir('./'+category)
			scripts = os.listdir()
			lista[category] = scripts
			# with open('../../index.info', 'a') as file:
			#	file.write(category+'\n')
			#	for script in scripts:
			#		file.write('\t'+script+'\n')		
			os.chdir('..')
		
		file = open('../index.json', 'w')
		json.dump(lista, file)
	
	finally:
		file.close()

retrieve_index()	

window = tk.Tk()
window.geometry('600x400')
window.title('commandgui')

#Left side combobox
cb_category = Combobox(window, values=list(lista.keys()), state='readonly')
cb_category.place(x=40, y=100)
try:
	cb_category.current(0)
except:
	cb_category.set('')

#If you change the value on the left side combobox, the right one changes automatically
def change_avaliable_scripts(*args):
	try:
		cb_script.config(values=lista[cb_category.get()])
		cb_script.current(0)
	except:
		cb_script.config(values=[])
		cb_script.set('')

cb_category.bind("<<ComboboxSelected>>",change_avaliable_scripts)

#Right side combobox
cb_script = Combobox(window, state='readonly')
cb_script.place(x=300, y=100)
change_avaliable_scripts()


#This chunk creates a button that refreshes the index, in case the files have been changed
def refresh_index():
	os.remove('../index.json')
	retrieve_index()
	cb_category.config(values=list(lista.keys()))
	try:
		cb_category.current(0)
	except:
		cb_category.set('')
	try:
		cb_script.config(values=lista[cb_category.get()])
		cb_script.current(0)
	except:
		cb_script.config(values=[])
		cb_script.set('')

bt = tk.Button(window, text='refresh index', command=refresh_index)
bt.place(x=170, y=200)

window.mainloop()