/**
 * $Id: GPU_KeyboardDevice.h 26841 2010-02-12 13:34:04Z campbellbarton $
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
 * The Original Code is Copyright (C) 2001-2002 by NaN Holding BV.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

#ifndef __GPU_KEYBOARDDEVICE_H
#define __GPU_KEYBOARDDEVICE_H

#include <X11/keysym.h>
#include <X11/X.h> // Brilliant name, eh? Stupid !@#!$!@#@@% This is
 // actually needed so as not to get name clashes between Object from
 // blender and Object from X11... The proper include would be
 // Intrinsic.h . Yes, we are a bunch of sado-masochists. Let's hurt
 // ourselves!

#include "GPC_KeyboardDevice.h"

class GPU_KeyboardDevice : public GPC_KeyboardDevice
{
public:

	void register_X_key_down_event(KeySym k);
	void register_X_key_up_event(KeySym k);
	
	GPU_KeyboardDevice(void);
	virtual ~GPU_KeyboardDevice()
	{
		/* intentionally empty */
	}
	
 private: 
	SCA_IInputDevice::KX_EnumInputs
		convert_x_keycode_to_kx_keycode(unsigned int key);
};

#endif  // _GPU_KEYBOARDDEVICE_H

