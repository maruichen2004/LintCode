class Solution:
    def findFirstBadVersion(self, n):
        start, end = 1, n
        while start+1 < end:
            mid = (start + end) / 2
            if VersionControl.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if VersionControl.isBadVersion(start): return start
        if VersionControl.isBadVersion(end): return end
