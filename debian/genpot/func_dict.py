#dict's key: the function name
#dict's value: a list containts the position info, 
#              which tells to strip out which argument( count it from 0!)
#you may find most of the function declarations in source\blender\include\BIF_interface.h

func_dict={
#uiSetButLock(int val, char *lockstr);
'uiSetButLock': [1],

#uiNewBlock(struct ListBase *lb, char *name, short dt, short font, short win);
#used for program internal?

#uiGetBlock(char *name, struct ScrArea *sa);
#used for program internal?

#uiBlockPickerButtons(struct uiBlock *block, float *col, float *hsv, float *old, char mode, short retval);
#have nothing to do with po?

#uiDefBut(uiBlock *block, 
#					   int type, int retval, char *str, 
#					   short x1, short y1, 
#					   short x2, short y2, 
#					   void *poin, 
#					   float min, float max, 
#					   float a1, float a2,  char *tip);
'uiDefBut':[3,13],

#uiDefButF(uiBlock *block, int type, int retval, char *str, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButF':[3,13],

#uiDefButBitF(uiBlock *block, int type, int bit, int retval, char *str, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButBitF':[4,14],

#uiDefButI(uiBlock *block, int type, int retval, char *str, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButI':[3,13],

#uiDefButBitI(uiBlock *block, int type, int bit, int retval, char *str, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButBitI':[4,14],

#uiDefButS(uiBlock *block, int type, int retval, char *str, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButS':[3,13],

#uiDefButBitS(uiBlock *block, int type, int bit, int retval, char *str, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButBitS':[4,14],

#uiDefButC(uiBlock *block, int type, int retval, char *str, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButC':[3,13],

#uiDefButBitC(uiBlock *block, int type, int bit, int retval, char *str, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefButBitC':[4,14],


#uiDefIconBut(uiBlock *block,
#					   int type, int retval, int icon,
#					   short x1, short y1,
#					   short x2, short y2,
#					   void *poin,
#					   float min, float max,
#					   float a1, float a2,  char *tip);
'uiDefIconBut': [13],

#uiDefIconButF(uiBlock *block, int type, int retval, int icon, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButF':  [13],

#uiDefIconButBitF(uiBlock *block, int type, int bit, int retval, int icon, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButBitF':  [14],

#uiDefIconButI(uiBlock *block, int type, int retval, int icon, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButI':  [13],

#uiDefIconButBitI(uiBlock *block, int type, int bit, int retval, int icon, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButBitI':  [14],

#uiDefIconButS(uiBlock *block, int type, int retval, int icon, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButS':  [13],


#uiDefIconButBitS(uiBlock *block, int type, int bit, int retval, int icon, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButBitS':  [14],

#uiDefIconButC(uiBlock *block, int type, int retval, int icon, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButC':  [13],

#uiDefIconButBitC(uiBlock *block, int type, int bit, int retval, int icon, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconButBitC':  [14],


#uiDefIconTextBut(uiBlock *block, int type, int retval, int icon, char *str, short x1, short y1, short x2, short y2, void *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextBut':  [4,14],

#uiDefIconTextButF(uiBlock *block, int type, int retval, int icon, char *str, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButF':  [4,14],

#uiDefIconTextButBitF(uiBlock *block, int type, int bit, int retval, int icon, char *str, short x1, short y1, short x2, short y2, float *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButBitF':  [5,15],

#uiDefIconTextButI(uiBlock *block, int type, int retval, int icon, char *str, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButI':  [4,14],

#uiDefIconTextButBitI(uiBlock *block, int type, int bit, int retval, int icon, char *str, short x1, short y1, short x2, short y2, int *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButBitI':  [5,15],

#uiDefIconTextButS(uiBlock *block, int type, int retval, int icon, char *str, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButS':  [4,14],

#uiDefIconTextButBitS(uiBlock *block, int type, int bit, int retval, int icon, char *str, short x1, short y1, short x2, short y2, short *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButBitS':  [5,15],

#uiDefIconTextButC(uiBlock *block, int type, int retval, int icon, char *str, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButC':  [4,14],

#uiDefIconTextButBitC(uiBlock *block, int type, int bit, int retval, int icon, char *str, short x1, short y1, short x2, short y2, char *poin, float min, float max, float a1, float a2,  char *tip);
'uiDefIconTextButBitC':  [5,15],

#typedef void		(*uiIDPoinFuncFP)	(char *str, struct ID **idpp);
#shoud not to be.

#uiDefIDPoinBut(struct uiBlock *block,
#						uiIDPoinFuncFP func, int retval, char *str,
#						short x1, short y1,
#						short x2, short y2,
#						void *idpp, char *tip);
'uiDefIDPoinBut':  [3,9],

#uiDefBlockBut(uiBlock *block, uiBlockFuncFP func, void *func_arg1, char *str, short x1, short y1, short x2, short y2, char *tip);
'uiDefBlockBut':  [3,8],

#uiDefPulldownBut(uiBlock *block, uiBlockFuncFP func, void *func_arg1, char *str, short x1, short y1, short x2, short y2, char *tip);
'uiDefPulldownBut':  [3,8],

#uiDefIconTextBlockBut(uiBlock *block, uiBlockFuncFP func, void *arg, int icon, char *str, short x1, short y1, short x2, short y2, char *tip);
'uiDefIconTextBlockBut':  [4,9],

#uiDefKeyevtButS(uiBlock *block, int retval, char *str, short x1, short y1, short x2, short y2, short *spoin, char *tip);
'uiDefKeyevtButS':  [2,8],

#pupmenu(char *instr);
'pupmenu':  [0],

#pupmenu_col(char *instr, int maxrow);
'pupmenu_col':  [0],


#uiNewPanelTabbed(char *, char *);
'uiNewPanelTabbed':  [0,1],

#uiNewPanel(struct ScrArea *sa, struct uiBlock *block, char *panelname, char *tabname, int ofsx, int ofsy, int sizex, int sizey);
'uiNewPanel':[2,3],

#uiFindOpenPanelBlockName(ListBase *lb, char *name);
#not this one

########################################
##void BIF_undo_push(char *str)  from source\blender\src\space.c
'BIF_undo_push':[0],
##source\blender\src\space.c ends
########################################


########################################
##from source\blender\src\toolbox.c
##in fact, only the string to be showed on screen can be translated
##all of these function can take the varible parameters
##so this is only a quick and dirty solution
##static int vconfirm(char *title, char *itemfmt, va_list ap)
'vconfirm':[0],

##static int confirm(char *title, char *itemfmt, ...)
'confirm':[0],

##int okee(char *str, ...)
'okee':[0],

##void notice(char *str, ...)
'notice':[0],

##void error(char *fmt, ...) 
##read error_po.py for details

##short button(short *var, short min, short max, char *str)
'button':[3],

##short sbutton(char *var, float min, float max, char *str)
'sbutton':[3],

##short fbutton(float *var, float min, float max, float a1, float a2, char *str)
'fbutton':[5],

##void draw_numbuts_tip(char *str, int x1, int y1, int x2, int y2)
'draw_numbuts_tip':[0],

##int do_clever_numbuts(char *name, int tot, int winevent)
'do_clever_numbuts':[0],

##void add_numbut(int nr, int type, char *str, float min, float max, void *poin, char *tip)
'add_numbut':[2,6],


##source\blender\src\toolbox.c ends
########################################

########################################
##from source\blender\include\BSE_filesel.h

##void activate_fileselect(int type, char *title, char *file, void (*func)(char *));
'activate_fileselect':[1,2],

##void activate_imageselect(int type, char *title, char *file, void (*func)(char *));
'activate_imageselect':[1,2],

##source\blender\include\BSE_filesel.h ends
########################################

#sprintf(naam, "header %d", curarea->headwin);
#sprintf(tmpstr,formatstring,"Object",ID_OB, ICON_OBJECT);
'sprintf':[0,1,2],

##we can not translate the info on console?
##2 methods in Blender, any more? it is not uniform!
##
##fprintf(stderr, "Unknown fileformat\n");
#'fprintf':[1],
##printf("Can't duplicate Nurb\n");
#'printf':[0],

########################################
##source\blender\python\api2_2x\gen_utils.c

##PyObject *EXPP_ReturnPyObjError( PyObject * type, char *error_msg );
#'EXPP_ReturnPyObjError':[1],

##int EXPP_ReturnIntError( PyObject * type, char *error_msg );
#'EXPP_ReturnIntError':[1],

##source\blender\python\api2_2x\gen_utils.c ends
########################################

########################################
##source\blender\blenlib\BLI_dynstr.h
##void	BLI_dynstr_append(DynStr *ds, char *cstr);
'BLI_dynstr_append':[1],
##source\blender\blenlib\BLI_dynstr.h ends
########################################

}
