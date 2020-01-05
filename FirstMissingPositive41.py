# -*- coding: utf-8 -*-
import sys


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sects = list()
        sects.append([0, 0])
        sects.append([sys.maxsize, sys.maxsize])
        for i in nums:
            if i <= 0:
                continue
            for seq, sect in enumerate(sects):
                if sect[0] <= i <= sect[1]:
                    # in sect
                    break
                elif sect[0] - 1 == i:
                    if sects[seq - 1][1] - 1 == i:
                        sects.remove(sect)
                        sects[seq - 1][1] = sect[1]
                        break
                    else:
                        sect[0] = sect[0] - 1
                        break
                elif sect[1] + 1 == i:
                    if sects[seq + 1][0] - 1 == i:
                        sect[1] = sects[seq + 1][1]
                        sects.remove(sects[seq + 1])
                        break
                    else:
                        sect[1] = sect[1] + 1
                        break
                elif i < sect[0] - 1:
                    sects.insert(seq, [i, i])
                    break
                else:
                    continue
        return sects[0][1] + 1




