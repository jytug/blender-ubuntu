/**
 * $Id: py_capi_utils.h 31705 2010-09-01 19:39:37Z gsrb3d $
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
 * Contributor(s): Campbell Barton
 *
 * ***** END GPL LICENSE BLOCK *****
 */
 
#ifndef PY_CAPI_UTILS_H
#define PY_CAPI_UTILS_H

struct PyObject;

void			PyC_ObSpit(char *name, PyObject *var);
void			PyC_LineSpit(void);
PyObject *		PyC_ExceptionBuffer(void);
PyObject *		PyC_Object_GetAttrStringArgs(PyObject *o, Py_ssize_t n, ...);
void			PyC_FileAndNum(const char **filename, int *lineno);
int				PyC_AsArray(void *array, PyObject *value, int length, PyTypeObject *type, char *error_prefix);

/* follow http://www.python.org/dev/peps/pep-0383/ */
PyObject *		PyC_UnicodeFromByte(const char *str);
const char *	PuC_UnicodeAsByte(PyObject *py_str, PyObject **coerce); /* coerce must be NULL */

#endif // PY_CAPI_UTILS_H