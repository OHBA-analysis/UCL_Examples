# Example scripts for preprocessing/source reconstructing CTF data

## Pipeline

In this example we:

- `1_preprocess.py`: Preprocess the sensor-level data.
- `2_coregister.py`: Coregister the MEG and sMRI data.
- `3_source_reconstruct.py`: Beamform the sensor-level data and parcellate to give us the source-level data.
- `4_sign_flip.py`: Fix the dipole sign ambiguity (we align the sign of the parcel time courses across subjects). This is only needed if we're training a group-level model on time-delay emebdded data.
- `5_save_npy.py`: Save the source data as vanilla numpy files in (time, parcels) format.

## Parallelisation

See [here](https://github.com/OHBA-analysis/osl/tree/main/examples/parallelisation) for how to parallelise these scripts.
