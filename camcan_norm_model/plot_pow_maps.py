"""Plot networks.

"""

import numpy as np

from osl_dynamics.models import load
from osl_dynamics.analysis import modes, power

# Load state covariances
model = load(".")
covs = model.get_covariances()

# Calculate covariances in parcel space
pca_components = np.load("pca_components.npy")
covs = modes.raw_covariances(
    covs,
    n_embeddings=15,
    pca_components=pca_components,
)

# Plot
power.save(
    covs,
    mask_file="MNI152_T1_8mm_brain.nii.gz",
    parcellation_file="Glasser52_binary_space-MNI152NLin6_res-8x8x8.nii.gz",
    subtract_mean=True,
    plot_kwargs={"views": ["lateral"], "symmetric_cbar": True},
    filename="covs_.png",
)
