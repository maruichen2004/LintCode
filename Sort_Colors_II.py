class Solution:
    def sortColors2(self, colors, k):
        for i in range(len(colors)):
            while colors[i] > 0:
                num = colors[i]
                if colors[num-1] > 0:
                    colors[i], colors[num-1] = colors[num-1], -1
                elif colors[num-1] < 0:
                    colors[num-1], colors[i] = colors[num-1] - 1, 0
                else:
                    colors[num-1], colors[i] = -1, 0
        idx = len(colors) - 1
        for i in reversed(range(k)):
            cnt = -colors[i]
            if cnt == 0: continue
            while cnt > 0:
                colors[idx] = i + 1
                idx -= 1
                cnt -= 1
