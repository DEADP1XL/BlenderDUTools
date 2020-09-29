# BlenderDUTools
Blender Add-On to Prepare Models for .obj Export to Dual Universe for Projectors

# Compatibility:
Designed for Blender 2.90.1 but may be compatible with other versions. Untested outside 2.90.1.

# Process:
Automatically sets normals to faces (for optimal in-game shading) and optionally applies a Wireframe Modifier with a default 0.125m thickness. Makes it easy to apply these same changes to a large number of objects at once.

# Install:
Add to Blender via Edit -> Preferences -> Add-Ons -> Install

# Usage:
1. In Object Mode, select all items to be prepared for export
2. Click 'Prep as Wireframe' or 'Prep as Solid Model' button from the DU Tools panel in the sidebar (hide/show with 'N' key by default)
3. Export to .obj as usual (I recommend setting it to only export selection, and to not use materials).
