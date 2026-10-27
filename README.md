# Correlated block-mask imputation workspace

Edit imputer.py only. Implement class Imputer with fit(rows) -> self and
transform(rows) -> a list of complete rows. Each row has six real-valued
features; a missing cell is Python None. Observed cells must be returned
unchanged (within 1e-12), and every imputed value must be finite. The fit
matrix contains 900 rows and no complete row. Each row reveals exactly
three of six features, from one of the 20 possible visible triples. These
overlapping triples provide pairwise evidence about channel dependence,
but no single training row reveals the full covariance. The evaluation
matrix contains 240 independently generated partial rows with the same
mask family. The method sees only masked training and evaluation
rows, never the original missing values, latent factors, evaluator files, or
reference implementation.

The data come from an episode-specific two-factor sensor model with small
independent noise. Feature loadings differ between episodes. Missing masks
are drawn from a small family of multi-feature sensor outages, rather than
independent cell deletion. Score is the root-mean-square reconstruction error
on **originally missing** evaluation cells; lower is better. Python 3.12
standard library suffices, with no network or GPU. A complete-row covariance
model is one possible approach, but any method meeting the contract may pass.
