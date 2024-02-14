# Example scripts for preprocessing/source reconstructing CTF data

## Pipeline

In this example we:

- `1_preprocess.py`: Preprocess the sensor-level data.
- `2_coregister.py`: Coregister the MEG and sMRI data. Note, `0_fix_smri_files.py` needs to be used to fix sMRI files with incorrect sform codes.
- `3_source_reconstruct.py`: Beamform the sensor-level data and parcellate to give us the source-level data.
- `4_sign_flip.py`: Align the sign of each parcel time course to a template subject from the normative model.

## Parallelisation

See [here](https://github.com/OHBA-analysis/osl/tree/main/examples/parallelisation) for how to parallelise these scripts.
