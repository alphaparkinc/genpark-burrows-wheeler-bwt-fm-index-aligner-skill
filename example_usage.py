from client import FMIndex

def main():
    print("=== Testing Burrows-Wheeler FM-Index Aligner ===")
    fm = FMIndex()
    bwt = fm.bwt_transform("banana")
    print("BWT transform of 'banana':", bwt)
    assert "$" in bwt

    matches = fm.count_matches(bwt, "an")
    print("Matches for 'an':", matches)
    assert matches == 2
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
