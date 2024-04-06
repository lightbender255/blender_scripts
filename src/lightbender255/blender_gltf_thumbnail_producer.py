""" This script sets up a camera and a cube in Blender to produce a thumbnail image.

The script performs the following steps:
1. Checks if a camera object exists in the scene. If not, it creates a new camera.
2. Sets the camera properties for a 2D-style setup.
3. Sets the active camera for the scene.
4. Adds a cube object to the scene and positions it.
5. Sets the output file path and resolution for rendering.

Note: This script assumes that it is being run in Blender's scripting environment.
"""

import bpy
import sys
import os
import pprint


# Add the local directory to the Python path
sys.path.append(os.path.dirname(__file__))

cur_dir = bpy.path.abspath("../output")
pprint.pp("Dir:" + cur_dir)
# Create as camera if one doesn't exist

def renderImage(outputPath, camera):
    bpy.data.scenes['Scene'].render.filepath = outputPath
    bpy.data.scenes['Scene'].camera = camera
    pprint.pp(camera)
    bpy.ops.render.render(write_still = True)

def add_cube(location,size=2):
    bpy.ops.mesh.primitive_cube_add(size=2)
    cube = bpy.context.object
    cube.location = (3,0,1)

if not bpy.data.objects.get('Camera'):
    bpy.ops.object.camera_add(location=(0,0,10))
    camera = bpy.context.object
else:
    # Use the existing camera
    camera = bpy.data.objects.get('Camera')

# Set the camera properties for a 2D-style setup
if camera:
    camera.data.type = "ORTHO"
camera.data.ortho_scale = 5
camera.rotation_euler = (0,0,0)
camera.location = (0,0,10)

# Set the active camera for the scene
bpy.context.scene.camera = camera

add_cube((0,0,0))
scene = bpy.context.scene
scene.render.filepath = "output"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080

# renderImage("./test", camera)
# camera.data.orthoscale = 5
camera.rotation_euler = (0,0,0)
camera.location = (0,0,10)

# set the active camera for the scene
bpy.context.scene.camera = camera
scene = bpy.context.scene
scene.render.filepath = "output"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080

pprint.pp(cur_dir + "/test")

renderImage("M:/src/blender_scripts/output/test", camera)
