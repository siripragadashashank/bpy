import bpy


bpy.ops.mesh.primitive_cube_add(size=3, location=(0, 0, 1.5))
cube = bpy.context.active_object 
bpy.ops.mesh.primitive_plane_add(size=50)
plane = bpy.context.active_object


light_source = bpy.data.lights.new('light', type='SUN')
light = bpy.data.objects.new('light', light_source)
bpy.context.collection.objects.link(light)
light.location = (3, -4, 5)
light.data.energy = 200.0



cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)

cam.location=(25, -3, 20)
bpy.context.collection.objects.link(cam)

mat = bpy.data.materials.new(name='Material')
mat.use_nodes = True

mat_nodes = mat.node_tree.nodes
mat_links = mat.node_tree.links

cube.data.materials.append(mat)


mat_nodes['Principled BSDF'].inputs['Metallic'].default_value = 1.0
mat_nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.005634, 0.018529, 0.800000, 1.0)
mat_nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.167

mat = bpy.data.materials.new(name='Material')
mat.use_nodes = True

mat_nodes = mat.node_tree.nodes
mat_links = mat.node_tree.links

plane.data.materials.append(mat)


mat_nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.005634, 0.018529, 0.800000, 1.0)
mat_nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.0


scene = bpy.context.scene
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath='/blender.png'


