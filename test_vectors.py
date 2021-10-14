from implementation import hamming_backup


if __name__ == '__main__':

    # here, X represents the 'original secret' seed phrase.
    X = 'useless theme rescue solve stable idea render cotton run round fiscal push correct fish frown miss endless floor nasty wild squirrel long process vacant'

    # A, B, and C are the three parts of a Hamming backup of X.
    # A was generated randomly; (B, C) were computed from (X, A).
    A = 'eight camera discover pink leg picture color afford cheap flip panel coffee damage open seminar hood park roof indoor merge female honey rack blossom'
    B = 'door umbrella path easily note educate snow inject payment retire loyal stand major novel stairs tower topple minute ancient soul elite grit glory harvest'
    C = 'wasp clutch circle common demand naive file doll deliver family erode finish limit fortune engage allow art hurdle trim save soon marriage joy loyal'

    print('Running tests...')

    assert(hamming_backup(X, A) == (B, C))
    assert(hamming_backup(X, B) == (C, A))
    assert(hamming_backup(X, C) == (A, B))
    assert(hamming_backup(A, X) == (C, B))
    assert(hamming_backup(B, X) == (A, C))
    assert(hamming_backup(C, X) == (B, A))

    assert(hamming_backup(A, B) == (X, C))
    assert(hamming_backup(B, C) == (X, A))
    assert(hamming_backup(C, A) == (X, B))
    assert(hamming_backup(B, A) == (C, X))
    assert(hamming_backup(C, B) == (A, X))
    assert(hamming_backup(A, C) == (B, X))

    print('...tests completed.')
