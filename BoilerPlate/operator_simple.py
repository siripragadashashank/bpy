import bpy
from math import radians
from bpy.props import *

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # create properties
    
    noise_scale : FloatProperty(
        name = "Noise Scale",
        description = "The scale of the noise",
        default = 1.0,
        min = 0.0,
        max = 2.0
    
    )


    def execute(self, context):
        
        
        bpy.ops.mesh.primitive_cube_add()

        so = bpy.context.active_object

        so.rotation_euler[0] += radians(45)

        mod_subsurf = so.modifiers.new("My Modifier", 'SUBSURF')

        mod_subsurf.levels = 3


        # smoothing the smooth way
        bpy.ops.object.shade_smooth()


        '''
        Smoothing the hard way
        '''
        # mesh = so.data
        # for face in mesh.polygons:
        #    face.use_smooth = True


        # create a displacement modifier
        mod_displace = so.modifiers.new("My Displacement", 'DISPLACE')

        # create the texture
        new_text = bpy.data.textures.new("My Texture", 'DISTORTED_NOISE')
        new_text.noise_scale = self.noise_scale

        mod_displace.texture = new_text


        # create a material
        new_material = bpy.data.materials.new(name="My Material")

        so.data.materials.append(new_material)

        new_material.use_nodes = True
        nodes = new_material.node_tree.nodes

        material_output = nodes.get("Material Output")
        node_emission = nodes.new(type='ShaderNodeEmission')

        node_emission.inputs[0].default_value = (0.0, 0.3, 1.0, 1)
        node_emission.inputs[1].default_value = 500.0


        links = new_material.node_tree.links
        new_link = links.new(node_emission.outputs[0],material_output.inputs[0])

        return {'FINISHED'}



def register():
    bpy.utils.register_class(SimpleOperator)



def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
