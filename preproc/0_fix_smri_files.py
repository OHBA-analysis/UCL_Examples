"""Fix sform code of structurals.

This script uses FSL to set the sform code of any structural
whose sform code is not 1 or 4 to make sure it is compatible
with OSL.

Warning: this script will permanently change the SMRI file.
"""

import numpy as np
import nibabel as nib

from osl import source_recon

files = ["data/smri/LN_VTA2.nii"]

for file in files:
    smri = nib.load(file)

    # Fix sform code
    sformcode = smri.header.get_sform(coded=True)[-1]
    if sformcode not in [1, 4]:
        cmd = f"fslorient -setsformcode 1 {file}"
        source_recon.rhino.utils.system_call(cmd)

print("Done")
