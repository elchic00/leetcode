def merge(intervals):
    if len(intervals[0]) == 0:
        return None
    mergedArr = []
    intervals.sort()
    for interval in intervals:
        if not mergedArr or mergedArr[-1][1] < interval[0]:
            mergedArr.append(interval)
        else:
            mergedArr[-1][1] = max(mergedArr[-1][1], interval[1])
    return mergedArr
        
if __name__ == '__main__':
    print(merge([[1,4], [2,5], [7,9]]))
    print(merge([[1,4], [2,6], [3,5]]))
    print(merge([[6,7], [2,4], [5,9]]))
    print(merge([[7,9]]))
    print(merge([[]]))
