from mnemonic import Mnemonic

english = Mnemonic("english")

def _left_rotate_4(half2):

    n = len(half2)
    return [(((half2[i] << 4) | (half2[(i+1) % n] >> 4)) & 255) for i in range(n)]


def _right_rotate_4(half2):

    n = len(half2)
    return [(((half2[i] >> 4) | (half2[(i+n-1) % n] << 4)) & 255) for i in range(n)]


def split_mnemonic(words):
    '''
    Splits a 256-bit seed (represented as a BIP39 mnemonic) into two
    128-bit halves (each represented as a list of 16 uint8s).
    '''

    # extract the entropy and check it:
    ent = list(english.to_entropy(words))

    n = len(ent) >> 1

    # split into two halves:
    half1 = ent[:n]
    half2 = ent[n:]

    # left-rotate second half by 4 bits (to match pen-and-paper approach):
    half2 = _left_rotate_4(half2)

    return half1, half2


def combine_halves(half1, half2):
    '''
    Combines two 128-bit halves (each represented as a list of 16 uint8s)
    into a 256-bit seed (represented as a BIP39 mnemonic).
    '''

    # right-rotate second half by 4 bits:
    half2 = _right_rotate_4(half2)

    # concatenate:
    ent = bytes(half1 + half2)

    # convert back to mnemonic (computing checksum):
    words = english.to_mnemonic(ent)

    return words


def xor_lists(first, *others):
    '''
    Applies the XOR function, elementwise, to lists of integers
    of equal length.

    For example:

    xor_lists([1, 4, 1, 5, 9, 2, 6, 5], [3, 5, 8, 9, 7, 9, 3, 2])
    returns [2, 1, 9, 12, 14, 11, 5, 7]
    '''

    result = first
    for other in others:
        result = [x ^ y for (x, y) in zip(result, other)]
    return result


def hamming_backup(X, A):
    '''
    This can be used to create and recover Hamming backups.

    Creation: if you have a secret seed mnemonic X and another randomly
    generated seed mnemonic A, then calling hamming_backup(X, A) will
    return a pair (B, C) of new seed mnemonics. Then {A, B, C} is a
    Hamming backup for the original seed X.

    Recovery: if you have two parts of the backup and call this function
    on those parts, then this will return -- in some order -- the third
    part of the backup and the original seed X. More specifically:

    hamming_backup(A, B) returns (X, C)
    hamming_backup(B, C) returns (X, A)
    hamming_backup(C, A) returns (X, B)
    hamming_backup(B, A) returns (C, X)
    hamming_backup(C, B) returns (A, X)
    hamming_backup(A, C) returns (B, X)
    '''

    x1, x2 = split_mnemonic(X)
    a1, a2 = split_mnemonic(A)

    b1 = xor_lists(a1, a2, x2)
    b2 = xor_lists(a2, b1, x1)
    c1 = xor_lists(b1, b2, x2)
    c2 = xor_lists(b2, c1, x1)

    B = combine_halves(b1, b2)
    C = combine_halves(c1, c2)

    return B, C
