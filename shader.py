bl_info = {
    "name": "Shader",
    "author": "SS",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy

class ShaderMainPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Library"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add a shader")
        row.operator('')
        

class SHADER_OT_DAIMOND(bpy.types.Operator):
    bl_label = 'Daimond'
    bl_idname = 'shader.daimond_operator'
    
    def execute(self, context):
        


def register():
    bpy.utils.register_class(ShaderMainPanel)


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)


if __name__ == "__main__":
    register()