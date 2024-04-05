import bpy
import math

# Create as camera if one doesn't exist

if not bpy.data.objects.get('Camera'):
    bpy.ops.object.camera_add(location=(0,0,10))
    camera = bpy.context.object
else:
    # Use the existing camera
    camera = bpy.data.objects['Camera']
    
# Set the camera properties for a 2d-style setup
