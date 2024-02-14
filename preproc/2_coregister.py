"""Coregistration.

"""

# Authors: Chetan Gohil <chetan.gohil@psych.ox.ac.uk>

import numpy as np

from osl import source_recon, utils


def save_fiducials(src_dir, subject, preproc_file, smri_file, epoch_file):
    """Saves fiducials/headshape for OSL."""

    with open(f"data/fiducials/{subject}_smri_fid.txt", "r") as file:
        data = file.readlines()

    nas = [float(x) for x in data[0].split()[1:]]
    lpa = [float(x) for x in data[1].split()[1:]]
    rpa = [float(x) for x in data[2].split()[1:]]

    nas[0], nas[1], nas[2] = nas[1], -nas[0], nas[2]
    lpa[0], lpa[1], lpa[2] = lpa[1], -lpa[0], lpa[2]
    rpa[0], rpa[1], rpa[2] = rpa[1], -rpa[0], rpa[2]

    polhemus_nasion = nas
    polhemus_rpa = rpa
    polhemus_lpa = lpa
    polhemus_headshape = [0, 0, 0]

    filenames = source_recon.rhino.get_coreg_filenames(src_dir, subject)
    np.savetxt(filenames["polhemus_nasion_file"], polhemus_nasion)
    np.savetxt(filenames["polhemus_rpa_file"], polhemus_rpa)
    np.savetxt(filenames["polhemus_lpa_file"], polhemus_lpa)
    np.savetxt(filenames["polhemus_headshape_file"], polhemus_headshape)


config = """
    source_recon:   
    - compute_surfaces:
        include_nose: False    
    - save_fiducials: {}
    - coregister:
        use_nose: False
        use_headshape: False
"""

# List of subject IDs
subjects = ["LN_VTA2"]

# Lists for input files
preproc_files = ["data/preproc/mg04938_BrainampDBS_20170504_01_preproc_raw.fif"]
smri_files = ["data/smri/LN_VTA2.nii"]

# Output directory
coreg_dir = "data/coreg"

# Do coregistration
source_recon.run_src_batch(
    config,
    src_dir=coreg_dir,
    subjects=subjects,
    preproc_files=preproc_files,
    smri_files=smri_files,
    extra_funcs=[save_fiducials],
)
