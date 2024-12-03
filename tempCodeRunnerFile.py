for pos in len(intervals):
        if intervals[pos] == "don't()":
        # pop elements until do() is found
            while intervals[pos] != "do()":
                intervals.pop(pos)
                pos += 1