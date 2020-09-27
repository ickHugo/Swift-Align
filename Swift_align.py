#
# Hugo Swift-Align or SA
#
import bpy

bl_info = {
    "name": "Swift Align",
    "author": "Hugo Bo Jonsson <ickhugo1@gmail.com>",
    "version": (1,0),
    "Blender": (2, 83, 6),
    "category": "Transform",
    "description": "Align vertices along an axis.",
    "location": "View3D > Sidebar > Edit"
}


class TRANSFORM_OT_Swift_align_X(bpy.types.Operator):

    bl_idname = "transform.swift_align_x"
    bl_label = "Align X-Axis"

    def execute(self, context):
        bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return {"FINISHED"}

class TRANSFORM_OT_Swift_align_Y(bpy.types.Operator):

    bl_idname = "transform.swift_align_y"
    bl_label = "Align Y-Axis"

    def execute(self, context):
        bpy.ops.transform.resize(value=(1, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return {"FINISHED"}

class TRANSFORM_OT_Swift_align_Z(bpy.types.Operator):

    bl_idname = "transform.swift_align_z"
    bl_label = "Align Z-Axis"

    def execute(self, context):
        bpy.ops.transform.resize(value=(1, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return {"FINISHED"}

# ########################################
# ##### GUI and registration #############
# ########################################

class VIEW3D_PT_transform_swift_align(bpy.types.Panel):
    bl_label  = "Swift Align"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Edit"

    def draw(self, context):
        self.layout.operator('transform.swift_align_x')
        self.layout.operator('transform.swift_align_y')
        self.layout.operator('transform.swift_align_z')



classes = (
    TRANSFORM_OT_Swift_align_X,
    TRANSFORM_OT_Swift_align_Y,
    TRANSFORM_OT_Swift_align_Z,
    VIEW3D_PT_transform_swift_align,
    )
        

def register():
    print("Swift Align registered")
    for className in classes:
        bpy.utils.register_class(className)


def unregister():
    print("Swift Align unregistered")
    for className in classes:
        bpy.utils.unregister_class(className)