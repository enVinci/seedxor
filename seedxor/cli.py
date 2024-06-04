from seedxor.implementation import hamming_backup
from seedxor.test_vectors import test12, test15, test18, test24
import argparse

def end(A, B, C, X):
    if X:
        print("X: " + X)
    if A:
        print("A: " + A)
    if B:
        print("B: " + B)
    if C:
        print("C: " + C)
    exit(0)

def main():
    parser = argparse.ArgumentParser('Create the shards(AB,BC,AC) or restore an original secret mnemonic seedphrase(X) using 2-of-3 variant of SeedXOR (Hamming Backup).')
    parser.add_argument("-A", "--first", default=None, action="store", help="First shard (-A '...')")
    parser.add_argument("-B", "--second", default=None, action="store", help="Second shard (-B '...')")
    parser.add_argument("-C", "--third", default=None, action="store", help="Third shard (-C '...')")
    parser.add_argument("-X", "--secret", default=None, action="store", help="Secret mnemonic (-X '...')")
    parser.add_argument("--test", default=False, action="store_true", help="Run tests")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.1.0')
    args = parser.parse_args()

    if args.test:
        test12()
        test15()
        test18()
        test24()
        exit(0)

    A = args.first
    B = args.second
    C = args.third
    X = args.secret

    # Create
    if X and A:
        B, C = hamming_backup(X, A)
        end(None, B, C, None)
    if X and B:
        C, A = hamming_backup(X, B)
        end(A, None, C, None)
    if X and C:
        A, B = hamming_backup(X, C)
        end(A, B, None, None)
    if A and X:
        C, B = hamming_backup(A, X)
        end(None, B, C, None)
    if B and X:
        A, C = hamming_backup(B, X)
        end(A, None, C, None)
    if C and X:
        B, A = hamming_backup(C, X)
        end(A, B, None, None)
    # Restore
    if A and B:
        X, C = hamming_backup(A, B)
        end(None, None, C, X)
    if B and C:
        X, A = hamming_backup(B, C)
        end(A, None, None, X)
    if C and A:
        X, B = hamming_backup(C, A)
        end(None, B, None, X)
    if B and A:
        C, X = hamming_backup(B, A)
        end(None, None, C, X)
    if C and B:
        A, X = hamming_backup(C, B)
        end(A, None, None, X)
    if A and C:
        B, X = hamming_backup(A, C)
        end(None, B, None, X)

    print('Provide at least two arguments.')
    exit(1)

if __name__ == "__main__":
    main()
