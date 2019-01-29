"""
Copyright 2018-2019
Dan Aukes, Cole Brauer
"""
"""
Material data array

Properties:
  r, g, b - color used to represent material
  process - method used to create parts made of this material
  blur - defines whether material and process support blurring
  cleanup - defines what subtractive cleanup process should be used

Processes:
  3dp: 3D Printing
  laser: Laser Cutting
  ins: Inserted component
"""

materials = [{'r': 1,   'g': 0,   'b': 0,   'process': '3dp', 'blur': True,  'cleanup': 'none'},  # 0 - multi-material 3D printing
             {'r': 0,   'g': 1,   'b': 0,   'process': '3dp', 'blur': True,  'cleanup': 'laser'}, # 1 - multi-material 3D printing with laser cleanup
             {'r': 0,   'g': 0,   'b': 1,   'process': '3dp', 'blur': True,  'cleanup': 'none'},  # 2 - multi-material 3D printing
             {'r': 0.5, 'g': 0.5, 'b': 0.5, 'process': 'ins', 'blur': False, 'cleanup': 'none'},  # 3 - inserted component
             {'r': 1,   'g': 1,   'b': 0,   'process': '3dp', 'blur': False, 'cleanup': 'none'}]  # 4 - single-material 3D printing