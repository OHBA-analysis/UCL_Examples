"""Preprocessing.

"""

# Authors: Chetan Gohil <chetan.gohil@psych.ox.ac.uk>

from osl import preprocessing

# Settings
config = """
    preproc:
    - filter: {l_freq: 1, h_freq: 125, method: iir, iir_params: {order: 5, ftype: butter}}
    - notch_filter: {freqs: 50 100}
    - resample: {sfreq: 250}
"""

# Create a list of paths to files to preprocess
inputs = [
    "data/raw/sub-001/meg/sub-001_task-resteyesopen_meg.ds",
    "data/raw/sub-002/meg/sub-002_task-resteyesopen_meg.ds",
]

# Directory to save output to
outdir = "data/preproc"

# Do preprocessing
preprocessing.run_proc_batch(
    config,
    inputs,
    outdir=outdir,
    overwrite=True,
)
