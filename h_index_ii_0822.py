# 题目描述：
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
#
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
# 总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数 不超过 h 次。）
#
# 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

# 示例：
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
#      由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。


# 左闭右开区间，中位数取下整, 结果取left
class Solution02:
    def hIndex(self, citations):
        left = 0
        right = len(citations)

        while left < right:
            mid = left + (right - left) // 2
            lager_than_mid_cnt, cnt_of_mid = self.cnt_of_larger_than_n(citations, mid)
            if lager_than_mid_cnt > mid:
                left = mid + 1
            elif lager_than_mid_cnt == mid or lager_than_mid_cnt + cnt_of_mid >= mid:
                return mid
            else:
                right = mid - 1
        return left

    @staticmethod
    def cnt_of_larger_than_n(citations, n):
        cnt = 0
        cnt_of_n = 0
        for e in citations:
            if e > n:
                cnt += 1
            if e == n:
                cnt_of_n += 1
        return cnt, cnt_of_n


# 左开右闭区间， 中位数取上整。 结果取right
class Solution01:
    def hIndex(self, citations):
        left = 0
        right = len(citations)

        while left < right:
            # 取上整, 避免 left = mid 死循环
            mid = left + (right - left + 1) // 2
            cnt = self.cnt_of_larger_than_n(citations, mid)
            if cnt >= mid:
                left = mid
            else:
                right = mid - 1
        return right

    @staticmethod
    def cnt_of_larger_than_n(citations, n):
        cnt = 0
        for e in citations:
            if e >= n:
                cnt += 1
        return cnt


# 利用数组升序排序特点，快速找到大于等于n的的元数个数
class Solution:
    def hIndex(self, citations):
        left = 0
        right = len(citations)
        N = len(citations)

        while left < right:
            # 取上整, 避免 left = mid 死循环
            mid = left + (right - left + 1) // 2
            # 考察 N-mid, N-mid + 1 ..... N - 1 共mid个数这个区间
            # 情况1.
            # 若位于 N - mid 的数 < mid. 表明 引用数 >= mid的论文数必然小于mid个。因此mid不满足。
            # 此时缩小右区间。 right = mid - 1
            # 情况2：
            # citations[N - mid] >= mid: 表明论文引用数大于>=mid的论文数 大于mid篇。此时可能取到mid
            # 则有 left = mid

            if citations[N - mid] < mid:
                right = mid - 1
            else:
                left = mid
        return right
