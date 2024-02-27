if "bpy" in locals():
  
    import importlib
    importlib.reload(spaceship_generator)
else:
    from . import spaceship_generator
#nothing else
import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty
from bpy.types import Operator

def menu_func(self, context):
    self.layout.operator(GenerateSpaceship.bl_idname, text="Spaceship")

def register():
    bpy.utils.register_class(GenerateSpaceship)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(GenerateSpaceship)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

def reset_scene():
    for item in bpy.data.objects:
        item.select = item.name.startswith('Spaceship')
    bpy.ops.object.delete()
    for material in bpy.data.materials:
        if not material.users:
            bpy.data.materials.remove(material)
