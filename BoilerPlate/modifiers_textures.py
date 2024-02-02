import bpy
from math import radians


bpy.ops.mesh.primitive_cube_add()

so = bpy.context.active_object

so.location[0] = 5

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
new_text.noise_scale = 2.0

mod_displace.texture = new_text




