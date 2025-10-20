"""This function was taken from AMICA-Python. Once that package is public, lets use it"""
import argparse
from pathlib import Path

import numpy as np


def generate_toy_data(n_samples=1000, mix_signals=True, noise_factor=None):
    """
    Generate toy data consisting of a sine and square wave.

    Parameters
    ----------
    n_samples : int, optional
        The number of samples to generate. Default is 1000.
    mix_signals : bool, optional
        If True, the two signals will be linearly mixed. Default is True.
    noise_factor : float, optional
        If not None, Gaussian noise with this standard deviation will be added to
        the signals (e.g. nois_factor could be set to 0.05).

    Returns
    -------
    mixed_signals : ndarray, shape (n_samples, 2)
        The mixed signals as a 2D numpy array.
    """
    seed = 123456
    rng = np.random.default_rng(seed)
    t = np.arange(1, n_samples + 1)
    a = np.sin(t * 2*np.pi*0.004)
    b = np.sign(np.sin(t * 2*np.pi*0.006))
    if noise_factor is not None:
        a += noise_factor * rng.standard_normal(len(t))
        b += noise_factor * rng.standard_normal(len(t))
    x = np.vstack([a, b]).T

    # optionally mix the signals
    if mix_signals:
        x = np.dot(x, [[0.9, 0.1], [0.1, 0.9]])
    return x


def write_data(data, filename):
    """Save data to a binary file in Fortran-compatible format.
    
    Parameters
    ----------
    data : array-like
        The data of shape (n_samples, n_features) to save. Will be converted to a
        Fortran-contiguous array of type float32.
    filename : str or Path
        The path to the output binary file.
    
    Returns
    -------
    data : np.ndarray
        The Fortran-contiguous array that was saved.
    path : Path
        The path to the saved file.
    """
    # tofile ravels matrices in C order, so force Fortran order.
    fpath = Path(filename).expanduser().resolve()
    # We actually have to write in C order to be Fortran compatible.
    # Or transpose the data First and write in Fortran order.
    # Because Fortran program expects (n_features, n_samples)
    vector = data.T.astype("<f4").ravel(order="F")
    vector.tofile(fpath)
    return fpath, data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate toy data consisting of a sine and square wave."
    )
    parser.add_argument(
        "--n-samples", type=int, default=1000,
        help="The number of samples to generate. Default is 1000."
    )
    parser.add_argument(
        "--mix-signals", action="store_true",
        help="If set, the two signals will be linearly mixed. Default is False."
    )
    parser.add_argument(
        "--noise-factor", type=float, default=None,
        help="If set, Gaussian noise with this standard deviation will be added to "
             "the signals (e.g. nois_factor could be set to 0.05). Default is None."
    )
    parser.add_argument(
        "--output", type=str, default="toy_data.bin",
        help="Output file name for the generated toy data. Default is 'toy_data.bin'."
    )
    args = parser.parse_args()

    toy_data = generate_toy_data(
        n_samples=args.n_samples,
        mix_signals=args.mix_signals,
        noise_factor=args.noise_factor
    )

    # Save the generated data to a binary file in Fortran order
    write_data(toy_data, args.output)
    print(f"Toy data of shape {toy_data.shape} saved to {args.output}")