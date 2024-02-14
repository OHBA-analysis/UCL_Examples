"""Fix sform code of structurals.

This script uses FSL to set the sform code of any structural
whose sform code is not 1 or 4 to make sure it is compatible
with OSL.

Warning: this script will permanently change the SMRI file.
"""

import numpy as np
import nibabel as nib

from osl import source_recon

def run(cmd):
    print(cmd)
    source_recon.rhino.utils.system_call(cmd)

files = ["LN_VTA2.nii"]

for file in files:
    # Copy the original file
    run(f"cp data/smri_original/{file} data/smri")
    file = f"data/smri/{file}"

    # Set the sform code to 1
    run(f"fslorient -setsformcode 1 {file}")
