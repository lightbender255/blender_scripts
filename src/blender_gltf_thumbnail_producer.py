from asyncio.windows_events import NULL
import bpy

# Create as camera if one doesn't exist
camera = NULL

if not bpy.data.objects.get('Camera'):
    bpy.ops.object.camera_add(location=(0,0,10))
    camera = bpy.context.object
else:
    # Use the existing camera
    camera = bpy.data.objects['Camera']


# Set the camera properties for a 2d-style setup
camera.data.type = "ORTHO"
camera.data.orthoscale = 5
camera.rotation_euler = (0,0,0)
camera.location = (0,0,10)

# set the active camera for the scene
bpy.context.scene.camera = camera

bpy.ops.mesh.primitive_cube_add(size=2)
cube = bpy.context.object
cube.location = (3,0,1)
scene = bpy.context.scene
scene.render.filepath = "output"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080

