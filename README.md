Hamming backups reference implementation
========================================

This is a _reference implementation_ of Hamming backups as introduced
in [this cp4space post][1].

The purpose of this code is to aid you in writing and debugging your
own implementation of Hamming backups -- for example, if you're the
developer of a hardware wallet and wish to add this feature.

This requires Python 3 and the [mnemonic package][2] as dependencies.

There are two Python files here:

- `implementation.py` contains the reference implementation.
- `test_vectors.py` checks the correctness of the implementation.

### install
python3 -m pip install .

sudo cp ./seedxor_completion /etc/bash_completion.d/

### uninstall
pip3 uninstall seedxor

[1]: https://cp4space.hatsya.com/2021/09/10/hamming-backups-a-2-of-3-variant-of-seedxor/
[2]: https://pypi.org/project/mnemonic/
