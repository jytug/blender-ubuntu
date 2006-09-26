'''
strip out arguments from function strcat and strcpy in specified src files

Because clouds of strcat and strcpy are used, I do not put it in near_all_po.py

To custom your script, roll down till "if __name__=='__main__'"

Note, if a string is stored in a variant, no program knows and then write it's value to PO file. So we always have to search the unfound msgid manually.

If anybody find a bug, or knows how to use re module to search and strip out  the strings, please let me know. Thanx.

Copyright: iced oyster< http://blender.blogchina.com > 2005
You can use this program freely, but CANNOT claim that you is the author.
'''

import os
import glob
import re
import sys

debug_po=0

func_dict={
'strcpy':[1],
'strcat':[1],
}


def split_blender_str(s):
	idx_id=s
	temp=[]

	if '|' not in idx_id:
		if (idx_id.endswith(':')==0 and len(idx_id.strip())>1) \
			or (idx_id.endswith(':') and len(idx_id[:-1].strip())>1):
			temp.append(s)
	else:
		idx_id=idx_id.split('|')
		idx_id=filter(lambda e:e not in ('','""'),idx_id)
		idx_id=filter(lambda e:(e.endswith(':')==0 and len(e.strip())>1) or \
								(e.endswith(':') and len(e[:-1].strip())>1),idx_id)
		for i in idx_id:
			'''
			from source\blender\src\buttons_editing.c
			but=uiDefButS(block, MENU, REDRAWVIEW3D,
				"Skinnable %x0|" "Unskinnable %x1|" "Head %x2|"
				"Neck %x3|" "Back %x4|" "Shoulder %x5|" "Arm %x6|"
				"Hand %x7|" "Finger %x8|" "Thumb %x9|" "Pelvis %x10|"
				"Leg %x11|" "Foot %x12|" "Toe %x13|" "Tentacle %x14",
				bx-10,by-19,117,18, &curBone->boneclass, 0.0, 0.0, 0.0, 0.0,
				"Classification of armature element");
			'''

			temp.append(i)

	for kbd in [ 'ctrl ', 'alt ', 		#'shift '
				'shift+', 'ctrl+', 'alt+', \
				'numpad',			#'emualte numpad'\
				'leftarrow','rightarrow','uparrow','downarrow',\
				'left arrow','right arrow','up arrow','down arrow',\
				'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',\
				'pageup', 'page up', 'pgup', 'pg up',
				'pagedown','page down', 'pgdn','pg dn',
				]:
		temp=filter(lambda e:e.lower().startswith(kbd)==0,temp)

	shift_except=map(lambda e:'f%0i'%e, range(1,13))
	shift_except+=['ctrl ', 'alt ',
					'numpad',
					'leftarrow','rightarrow','uparrow','downarrow',\
					'left arrow','right arrow','up arrow','down arrow',\
					'pageup', 'page up', 'pgup', 'pg up',
					'pagedown','page down', 'pgdn','pg dn',
				]
	shift_except=map(lambda e:'shift '+e,shift_except)
	for kbd in shift_except:
		temp=filter(lambda e:e.lower().startswith(kbd)==0,temp)
	temp=filter(lambda e:e.lower() not in ['tab','shift tab'],temp)
	temp=filter(lambda e:e.lower().startswith('shift')==0 or\
				(e.lower().startswith('shift') and len(e)>7) ,temp)

	if temp:
		temp=map(lambda e:e.split('%t')[0],temp)

	#msgid "Add Sequence Strip%t|Images%x1|Movie%x102|Audio%x103|Scene%x101|Plugin%x10|Cross%x2|Gamma Cross%x3|Add%x4|Sub%x5|Mul%x6|Alpha Over%x7|Alpha Under%x8|Alpha Over Drop%x9|Wipe%x13|Glow%x14"
	##"GiQuality %t|None %x0|Low %x1|Medium %x2 |High %x3|Higher %x4|Best %x5|Use Blender AO settings %x6"
	if temp:
		temp=map(lambda e:e.split('%x')[0],temp)

	temp=filter(lambda e:e!='',temp)
	return temp

func_dict_key=func_dict.keys()

def genpo(files):
	all_msgid=[]
	for file in files:
		current_msgid=[]

		if os.path.isfile(file):
			if os.path.splitext(file)[-1].upper() in ['.C', 'CPP']:	#.H, .HPP?

				f_in=open(file)
				line=f_in.readline()

				while line:
					if line!=None:
						line=line.strip()

						line_temp=' '

						while line.endswith(';')!=1 and line_temp:
							line_temp=f_in.readline()
							if line_temp:
								line_temp=line_temp.strip()
								if line_temp.endswith('\\'):
									line_temp=line_temp[:-1]
								line+=line_temp

						line=line.replace(',""',',NIL_NULL')
						line=line.replace(', ""',',NIL_NULL')
						line=line.replace(',\t""',',NIL_NULL')
						line=line.replace('"",','NIL_NULL,')
						line=line.replace('"" ,',',NIL_NULL ,')
						line=line.replace('""\t,',',NIL_NULL\t,')
						line=line.replace('," "',',NIL_NULL')
						line=line.replace(', " "',',NIL_NULL')
						line=line.replace(',\t" "',',NIL_NULL')
						line=line.replace('" ",','NIL_NULL,')
						line=line.replace('" " ,',',NIL_NULL ,')
						line=line.replace('" "\t,',',NIL_NULL\t,')
						line=line.replace(',"\t"',',NIL_NULL')
						line=line.replace(', "\t"',',NIL_NULL')
						line=line.replace(',\t"\t"',',NIL_NULL')
						line=line.replace('"\t",','NIL_NULL,')
						line=line.replace('"\t" ,',',NIL_NULL ,')
						line=line.replace('"\t"\t,',',NIL_NULL\t,')

						line=line.replace('""','')
						line=line.replace('" "','')
						line=line.replace('"\t"','')

						for funcname in func_dict_key:
							line_temp=line
							found=re.search('%s[ \t]*\('%funcname,line_temp)
							if found!=None:

								line_temp=line_temp[found.start()+len(found.group()):-1]
								line_temp=line_temp.strip()
								line_temp=line_temp.replace(r'\"',r"\'")
								line_temp=re.split('([^,"]+|"[^"]*")',line_temp)
								line_temp=map(lambda e:e.replace(r"\'",r'\"'), line_temp)

								line_temp=map(lambda e:e.strip(),line_temp)
								line_temp=filter(lambda e:e not in ['',',','"','\\n'],line_temp)


								for idx in func_dict[funcname]:
									try:
										idx_id=line_temp[idx]
										if idx_id.startswith('"') and idx_id.endswith('"')  and idx_id!='""':
											idx_id=idx_id[1:-1]
											idx_id_split=split_blender_str(idx_id)

											idx_id_split=filter(lambda e:'%' not in e,idx_id_split)

											if len(idx_id_split)==1:
												if debug_po:
													current_msgid+=['msgid "'+idx_id_split[0]+'"\n'+'msgstr "blahblah"\n']
													#all_msgid_dict[idx_id_split[0]]='blahblah'
												else:
													current_msgid+=['msgid "'+idx_id_split[0]+'"\n'+'msgstr ""\n']

											elif len(idx_id_split)>1:
												current_msgid+=['#'*59+'\n'+
															'###  must break down the following line at "|"\n'+
															'###  msgid "'+idx_id+'"\n'+
															'###  msgstr ""\n'
															]
												for i in idx_id_split:
													if debug_po:
														current_msgid+=['msgid "'+i+'"\n'+'msgstr "blahblah"\n']
														#all_msgid_dict[i]='blahblah'
													else:
														current_msgid+=['msgid "'+i+'"\n'+'msgstr ""\n']
												current_msgid+=['###  breakdown ends\n'+
															'#'*59+'\n'
															]
									except:
										pass

						line=f_in.readline()

				if  current_msgid:
					current_msgid=['#'*59+'\n'+'###  from file %s\n' % file+'#'*59+'\n']+current_msgid

				if  current_msgid:
					all_msgid+=current_msgid

	#return all_msgid

	for i in all_msgid:
		print i

if __name__=='__main__':
	#the fold of your Blender src
	blender_src_path=r'L:\blender src\source'

	
	#
	#Q: How to know which src file should be place here?
	#A: 1.run near_all_po.py, replace msgstr "" with msgstr "blahblah"
	#   2.launch Blender, and use your new mo file
	#   3.if you find anything else other than "blahblah", write it down
	#   4.search it in Blender src
	#   5.if you find it in function strcat or strcpy, 
	#     write the name of the C/CPP file here.
	#
	#   generally, if you find one untranslated msgid, 
	#   you can find more in the same C/CPP file.
	fnames=glob.glob(blender_src_path+r'\blender\src\header*.c')
	fnames+=glob.glob(blender_src_path+r'\blender\src\button*.c')
	fnames+=[
			blender_src_path+r'\blender\src\space.c',
			blender_src_path+r'blender\src\toolbox.c',
		]
	
	#the output file
	fout=open('spec.po','w')
	sys.stdout=fout

	genpo(fnames)
	
	fout.close()
	sys.stdout=sys.__stdout__
