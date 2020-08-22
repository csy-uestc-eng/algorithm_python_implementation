class Solution:
    def findBestValue(self, arr, target):
        n = len(arr)

        def sum_of_replce_larger_than_value(value):
            ret = 0
            for e_ in arr:
                ret += min(e_, value)
            return ret
        min_value = float("inf")
        sum_arr = 0
        max_value = 0
        for e in arr:
            min_value = min(e, min_value)
            max_value = max(e, max_value)
            sum_arr += e

        if sum_arr <= target:
            return max_value
        if min_value > target:
            return min_value

        left = target // n
        right = max_value
        while left < right:
            mid = left + (right - left) // 2
            sum_value = sum_of_replce_larger_than_value(mid)
            if sum_value == target:
                right = mid
            elif sum_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return min([abs(sum_of_replce_larger_than_value(left - 1) - target), left - 1],
                   [abs(sum_of_replce_larger_than_value(left) - target), left],
                   [abs(sum_of_replce_larger_than_value(left + 1) - target), left + 1]
                   )[1]
