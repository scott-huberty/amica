import argparse
from simulate_data import write_data


def generate_sklearn_tutorial_data():
    """
    https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html
    """
    import numpy as np
    from scipy import signal


    rng = np.random.default_rng(0)
    n_samples = 2000
    time = np.linspace(0, 8, n_samples)

    s1 = np.sin(2 * time)                     # Sinusoidal
    s2 = np.sign(np.sin(3 * time))            # Square wave
    s3 = signal.sawtooth(2 * np.pi * time)    # Sawtooth

    S = np.c_[s1, s2, s3]
    S += 0.2 * rng.standard_normal(S.shape)   # Add noise
    S /= S.std(axis=0)                        # Standardize

    A = np.array([[1, 1, 1],
                [0.5, 2, 1.0],
                [1.5, 1.0, 2.0]])           # Mixing matrix

    X = S @ A.T                               # Observed mixtures
    return X


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate data from https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html"
    )
    parser.add_argument(
        "--output", type=str, required=True,
    )
    args = parser.parse_args()

    sklearn_data = generate_sklearn_tutorial_data()
    write_data(sklearn_data, args.output)
