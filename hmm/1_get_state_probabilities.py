"""Infer state probabilities by applying the normative model to a dataset.

"""

# Authors: Chetan Gohil <chetan.gohil@psych.ox.ac.uk>

import os
import numpy as np

from osl_dynamics.data import Data
from osl_dynamics.models import load

subject = "LN_VTA2"

# Load data
data = Data(f"../preproc/data/npy/{subject}.npy")

# Prepare data
pca_components = np.load("../camcan_norm_model/pca_components.npy")
data.prepare({
    "tde_pca": {"n_embeddings": 15, "pca_components": pca_components},
    "standardize": {},
})

# Load model
model = load("../camcan_norm_model")

# Get state probabilities
alpha = model.get_alpha(data)

# Save
os.makedirs(f"hmm/{subject}", exist_ok=True)
np.save(f"hmm/{subject}/alpha.npy", alpha)

# Delete temporary directory
data.delete_dir()
