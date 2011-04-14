#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

import bpy
from math import acos
from rigify.utils import MetarigError
from rigify.utils import copy_bone
from rigify.utils import org_name, make_mechanism_name


class Rig:
    """ A delta rig.
        Creates a setup that will place its child at its position in pose mode,
        but will not modifying its child's position in edit mode.
        This is a mechanism-only rig (no control or deformation bones).

    """
    def __init__(self, obj, bone, params):
        """ Gather and validate data about the rig.
            Store any data or references to data that will be needed later on.
            In particular, store references to bones that will be needed.
            Do NOT change any data in the scene.  This is a gathering phase only.

        """
        bb = obj.data.bones

        if bb[bone].children is None:
            raise MetarigError("RIGIFY ERROR: bone '%s': rig type requires one child." % org_name(bone.name))
        if bb[bone].use_connect == True:
            raise MetarigError("RIGIFY ERROR: bone '%s': rig type cannot be connected to parent." % org_name(bone.name))

        self.obj = obj
        self.org_bones = {"delta": bone, "child": bb[bone].children[0].name}
        self.org_names = [org_name(bone), org_name(bb[bone].children[0].name)]

    def generate(self):
        """ Generate the rig.
            Do NOT modify any of the original bones, except for adding constraints.
            The main armature should be selected and active before this is called.

        """
        bpy.ops.object.mode_set(mode='EDIT')
        eb = self.obj.data.edit_bones

        org_delta = self.org_bones["delta"]
        org_delta_e = eb[self.org_bones["delta"]]
        org_child = self.org_bones["child"]
        org_child_e = eb[self.org_bones["child"]]

        # Calculate the matrix for achieving the delta
        child_mat = org_delta_e.matrix.invert() * org_child_e.matrix
        mat = org_delta_e.matrix * child_mat.invert()

        # Create the delta bones.
        delta_e = eb[copy_bone(self.obj, self.org_bones["delta"])]
        delta_e.name = make_mechanism_name(self.org_names[0])
        delta = delta_e.name

        # Set the delta to the matrix's transforms
        set_mat(self.obj, delta, mat)

        bpy.ops.object.mode_set(mode='OBJECT')

        # Constrain org_delta to delta
        con = self.obj.pose.bones[org_delta].constraints.new('COPY_TRANSFORMS')
        con.name = "delta"
        con.target = self.obj
        con.subtarget = delta

    @classmethod
    def create_sample(self, obj):
        # generated by rigify.utils.write_metarig
        bpy.ops.object.mode_set(mode='EDIT')
        arm = obj.data

        bones = {}

        bone = arm.edit_bones.new('delta')
        bone.head[:] = 0.0000, -0.1198, 0.1253
        bone.tail[:] = -0.0000, -0.2483, 0.2785
        bone.roll = -0.0000
        bone.use_connect = False
        bones['delta'] = bone.name
        bone = arm.edit_bones.new('Bone')
        bone.head[:] = -0.0000, 0.0000, 0.0000
        bone.tail[:] = -0.0000, 0.0000, 0.2000
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['delta']]
        bones['Bone'] = bone.name

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['delta']]
        pbone.rigify_type = 'misc.delta'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.rigify_parameters.add()
        pbone = obj.pose.bones[bones['Bone']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'

        bpy.ops.object.mode_set(mode='EDIT')
        for bone in arm.edit_bones:
            bone.select = False
            bone.select_head = False
            bone.select_tail = False
        for b in bones:
            bone = arm.edit_bones[bones[b]]
            bone.select = True
            bone.select_head = True
            bone.select_tail = True
            arm.edit_bones.active = bone


def set_mat(obj, bone_name, matrix):
    """ Sets the bone to have the given transform matrix.
    """
    a = obj.data.edit_bones[bone_name]

    a.head = (0, 0, 0)
    a.tail = (0, 1, 0)

    a.transform(matrix)

    d = acos(a.matrix.to_quaternion().dot(matrix.to_quaternion())) * 2.0

    roll_1 = a.roll + d
    roll_2 = a.roll - d

    a.roll = roll_1
    d1 = a.matrix.to_quaternion().dot(matrix.to_quaternion())
    a.roll = roll_2
    d2 = a.matrix.to_quaternion().dot(matrix.to_quaternion())

    if d1 > d2:
        a.roll = roll_1
    else:
        a.roll = roll_2
