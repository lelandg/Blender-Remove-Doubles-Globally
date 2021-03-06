import bpy
from bpy.props import *
import bmesh

bl_info = {
    "version": (0, 1),
    "blender": (2, 79, 0),
    "author": "Leland Green",
    "name": "Remove Doubles Globally",
    "description": """Removes doubles from all meshes in a scene""" ,
    "category": "TOOLS",
}

def initSceneProperties(scn):
    """Register data types and initialize values stored in each scene, if not already present."""
    bpy.types.Scene.min_distance = FloatProperty(
        name = "min_distance", 
        description = "Minimum Distance",
        default = 0.005,
        min = 0,
        max = 1,
        precision = 3)
    if 'min_distance' not in scn.keys():
        scn['min_distance'] = 0.005
    return

initSceneProperties(bpy.context.scene)
 
class VIEW3D_PT_tools_GlobalRemoveDoublesPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Remove Doubles Globally"
    bl_idname = "OBJECT_PT_grd_panel"
    bl_space_type = 'VIEW_3D'
    bl_category = "Tools"
    bl_region_type = 'TOOLS'
    bl_icon = 'WORLD_DATA'
    #bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Remove doubles from all objects, selected or not.", icon='WORLD_DATA')

        row = layout.row()
        
        scene = context.scene
        global min_distance
        layout.prop(scene, "min_distance", 'Minimum distance between two points')
        
        row = layout.row()
        layout.operator("grd_panel.remove_doubles_global")
        row = layout.row()


class OBJECT_OT_GlobalRemoveDoublesButton(bpy.types.Operator):
    bl_idname = "grd_panel.remove_doubles_global"
    bl_label = "Remove Doubles Globally"
 
    def execute(self, context):
        try:
            scene = context.scene
            
            bm = bmesh.new()
            min_distance = scene['min_distance']
            mesh_count = len(bpy.data.meshes)
            total_verts = 0
            total_verts_removed = 0

            for m in bpy.data.meshes:
                self.report({'INFO'}, "Processing %s" % (str(m), ) )
                bm.from_mesh(m)
                len1 = len(bm.verts)
                total_verts += len1
                self.report({'INFO'}, "Processing %s: %d verts" % (str(m), len1 ))
                bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=min_distance)
                len2 = len(bm.verts)
                num_removed = len1-len2
                total_verts_removed += num_removed
                self.report({'INFO'}, "Processed %s: removed %d of %d verts" % (str(m), (num_removed), len1))
                bm.to_mesh(m)
                m.update()
                bm.clear()

            bm.free()            
            self.report({'INFO'}, "Finished %d meshes: Removed %d of %d verts)" % (mesh_count, total_verts_removed, total_verts))
        except:
            self.report({'ERROR'}, "%s" % (traceback.print_exc(), ))
            self.report({'ERROR'}, "Abort after %d meshes -- see Info window for details. (Are you in Edit mode?): Removed %d of %d verts)" % (mesh_count, total_verts_removed, total_verts))

        return{'FINISHED'}
    

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 

if __name__ == "__main__":
    register()
