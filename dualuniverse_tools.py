bl_info = {
    "name": "Dual Universe Export Prep",
    "author": "DEAD_P1XL",
    "version":(1,0),
    "blender": (2, 90, 1),
    "category": "Object",
    "location": "Operator Search",
    "description": "Prep Models for Export to Dual Universe",
    "warning":"",
    "doc_url":"",
    "tracker_url":""
}

import bpy
import os

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class MESH_OT_dualUniverseTools(bpy.types.Operator):
    """Prepare mesh for .obj export to Dual Universe"""
    bl_idname = "mesh.du_export_prep"
    bl_label = "DU Export Prep"
    bl_options = {'REGISTER', 'UNDO'}
    wireframe: bpy.props.BoolProperty(
        name="Convert to Wireframe",
        description="Applies a wireframe modifier for better appearance in game.",
        default=True
    )

    def execute(self, context):
        if len(context.selected_objects) < 1:
            return {'CANCELLED'}

        sel = context.selected_objects
        act = context.active_object
        context.active_object.select_set(False)

        for obj in sel:
            context.view_layer.objects.active = obj
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.set_normals_from_faces()
            bpy.ops.object.editmode_toggle()
            if self.wireframe == True:
                hasMod = 0
                for mod in obj.modifiers:
                    if mod.type == "WIREFRAME":
                        hasMod = 1
                if not hasMod:            
                    bpy.ops.object.modifier_add(type='WIREFRAME')
                    obj.modifiers["Wireframe"].thickness = 0.125
                else:
                    obj.modifiers["Wireframe"].show_viewport = True
            else:
                for mod in obj.modifiers:
                    if mod.type == "WIREFRAME":
                        obj.modifiers.remove(obj.modifiers.get("Wireframe"))

        for obj in sel:
            obj.select_set(state=True)
        
        return {'FINISHED'}


class VIEW3D_PT_dualUniverseTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "DU Tools"
    bl_label = "DU Tools"
    
    def draw(self, context):
        props = self.layout.operator('mesh.du_export_prep', text='Prep As Wireframe')
        props.wireframe=True
        props2 = self.layout.operator('mesh.du_export_prep', text='Prep As Solid Model')
        props2.wireframe = False

    
def register():
    bpy.utils.register_class(MESH_OT_dualUniverseTools)
    bpy.utils.register_class(VIEW3D_PT_dualUniverseTools)
    
def unregister():
    bpy.utils.unregister_class(MESH_OT_dualUniverseTools)
    bpy.utils.unregister_class(VIEW3D_PT_dualUniverseTools)