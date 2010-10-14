/**
 * $Id: wm_event_system.h 27639 2010-03-21 01:14:04Z gsrb3d $
 *
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version. 
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2007 Blender Foundation.
 * All rights reserved.
 *
 * 
 * Contributor(s): Blender Foundation
 *
 * ***** END GPL LICENSE BLOCK *****
 */
#ifndef WM_EVENT_SYSTEM_H
#define WM_EVENT_SYSTEM_H

/* return value of handler-operator call */
#define WM_HANDLER_CONTINUE	0
#define WM_HANDLER_BREAK	1
#define WM_HANDLER_HANDLED	2
#define WM_HANDLER_MODAL	4 /* MODAL|BREAK means unhandled */

struct ScrArea;
struct ARegion;

/* wmKeyMap is in DNA_windowmanager.h, it's savable */

typedef struct wmEventHandler {
	struct wmEventHandler *next, *prev;
	
	int type, flag;				/* type default=0, rest is custom */
	
	/* keymap handler */
	wmKeyMap *keymap;			/* pointer to builtin/custom keymaps */
	rcti *bblocal, *bbwin;		/* optional local and windowspace bb */
	
	/* modal operator handler */
	wmOperator *op;						/* for derived/modal handlers */
	struct ScrArea *op_area;			/* for derived/modal handlers */
	struct ARegion *op_region;			/* for derived/modal handlers */

	/* ui handler */
	wmUIHandlerFunc ui_handle;  		/* callback receiving events */
	wmUIHandlerRemoveFunc ui_remove;	/* callback when handler is removed */
	void *ui_userdata;					/* user data pointer */
	struct ScrArea *ui_area;			/* for derived/modal handlers */
	struct ARegion *ui_region;			/* for derived/modal handlers */
	struct ARegion *ui_menu;			/* for derived/modal handlers */
	
	/* fileselect handler re-uses modal operator data */
	struct bScreen *filescreen;			/* screen it started in, to validate exec */
	
	/* drop box handler */
	ListBase *dropboxes;
	
} wmEventHandler;


/* handler flag */
		/* after this handler all others are ignored */
#define WM_HANDLER_BLOCKING		1



/* custom types for handlers, for signalling, freeing */
enum {
	WM_HANDLER_DEFAULT,
	WM_HANDLER_FILESELECT
};


/* wm_event_system.c */
void		wm_event_add			(wmWindow *win, wmEvent *event_to_add);
void		wm_event_free_all		(wmWindow *win);
void		wm_event_free			(wmEvent *event);
void		wm_event_free_handler	(wmEventHandler *handler);

			/* goes over entire hierarchy:  events -> window -> screen -> area -> region */
void		wm_event_do_handlers	(bContext *C);

void		wm_event_add_ghostevent	(wmWindowManager *wm, wmWindow *win, int type, int time, void *customdata);

void		wm_event_do_notifiers	(bContext *C);

/* wm_keymap.c */

/* wm_dropbox.c */
void		wm_dropbox_free(void);
void		wm_drags_check_ops(bContext *C, wmEvent *event);
void		wm_drags_draw(bContext *C, wmWindow *win, rcti *rect);

#endif /* WM_EVENT_SYSTEM_H */
