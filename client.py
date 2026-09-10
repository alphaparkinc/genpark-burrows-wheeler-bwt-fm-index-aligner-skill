class FMIndex:
    """
    FM-Index and Burrows-Wheeler Transform Engine.
    Enables compressed pattern searches via Last-to-First (LF) mapping.
    """
    def bwt_transform(self, s):
        s += "$"
        rotations = sorted([s[i:] + s[:i] for i in range(len(s))])
        return "".join(r[-1] for r in rotations)

    def count_matches(self, bwt, pattern):
        first_col = sorted(bwt)
        top = 0
        bottom = len(bwt) - 1

        for char in reversed(pattern):
            new_top = -1
            new_bottom = -1
            for idx in range(top, bottom + 1):
                if bwt[idx] == char:
                    rank = bwt[:idx].count(char)
                    fc_idx = first_col.index(char) + rank
                    if new_top == -1:
                        new_top = fc_idx
                    new_bottom = fc_idx
            if new_top == -1:
                return 0
            top = new_top
            bottom = new_bottom

        return bottom - top + 1
