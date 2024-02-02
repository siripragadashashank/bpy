import bpy

vertices = [
    (1, 1, 0),
    (1, -1, 0),
    (-1, -1, 0),
    (-1, 1, 0),
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

edges = []
faces = [(0, 1, 2, 3), (4,5,6,7), (0,4,7,3), (0,1,5,4), (1,2,6,5), (7,6,2,3)]


new_mesh = bpy.data.meshes.new("new_mesh")
new_mesh.from_pydata(vertices, edges, faces)

new_mesh.update()

new_object = bpy.data.objects.new("new_object", new_mesh)

view_layer = bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)