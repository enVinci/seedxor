from seedxor.implementation import hamming_backup

def test12():
    # here, X represents the 'original secret' seed phrase.
    X = 'mule gift aware increase venue symbol crew answer alter jewel apart wave'

    # A, B, and C are the three parts of a Hamming backup of X.
    # A was generated randomly; (B, C) were computed from (X, A).
    A = 'pave solar buzz merry tomato grab point crazy model sell physical open'
    B = 'various casual debate fly dress stool satoshi pelican duty situate average bonus'
    C = 'scout metal daring path feel hungry clock odor sniff large please inner'

    print('Running 12 word mnemonic tests...')

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

    print('...tests for 12 word mnemonic completed.')

def test15():
    # here, X represents the 'original secret' seed phrase.
    X = 'drop success course ethics truth extra bag square guard anxiety mixture bless fantasy case bundle'

    # A, B, and C are the three parts of a Hamming backup of X.
    # A was generated randomly; (B, C) were computed from (X, A).
    A = 'game purse peanut glow begin artwork tide diesel actual kit injury visual battle puzzle oxygen'
    B = 'city kangaroo tattoo fuel raccoon chalk antenna tail photo grunt lottery utility merry this brief'
    C = 'cry aunt exclude inform evidence keep wet crisp ship blind lazy basic slogan home oppose'

    print('Running 15 word mnemonic tests...')

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

    print('...tests for 15 word mnemonic completed.')

def test18():
    # here, X represents the 'original secret' seed phrase.
    X = 'lend venture green harsh enough cement champion build same armed body reject census artwork pumpkin stay source draw'

    # A, B, and C are the three parts of a Hamming backup of X.
    # A was generated randomly; (B, C) were computed from (X, A).
    A = 'prepare coil frost frost argue toy poem maid local very monkey duty soft drink toilet ridge pause town'
    B = 'fortune actual rural merge oak kingdom lava gossip sight this jazz practice satisfy pulse equal nerve over fruit'
    C = 'mirror target mammal satisfy stove rigid wolf you void boring thing flip february together act weekend uncle where'

    print('Running 18 word mnemonic tests...')

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

    print('...tests for 18 word mnemonic completed.')

def test24():
    # here, X represents the 'original secret' seed phrase.
    X = 'useless theme rescue solve stable idea render cotton run round fiscal push correct fish frown miss endless floor nasty wild squirrel long process vacant'

    # A, B, and C are the three parts of a Hamming backup of X.
    # A was generated randomly; (B, C) were computed from (X, A).
    A = 'eight camera discover pink leg picture color afford cheap flip panel coffee damage open seminar hood park roof indoor merge female honey rack blossom'
    B = 'door umbrella path easily note educate snow inject payment retire loyal stand major novel stairs tower topple minute ancient soul elite grit glory harvest'
    C = 'wasp clutch circle common demand naive file doll deliver family erode finish limit fortune engage allow art hurdle trim save soon marriage joy loyal'

    print('Running 24 word mnemonic tests...')

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

    print('...tests for 24 word mnemonic completed.')

if __name__ == '__main__':
    test12()
    test15()
    test18()
    test24()
