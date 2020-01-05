# -*- coding: utf-8 -*-

import sys
from collections import deque
import copy

# Linux中，在新的一行的开头，按下Ctrl-D，就代表EOF（
# 如果在一行的中间按下Ctrl-D，则表示输出"标准输入"的缓存区，所以这时必须按两次Ctrl-D）；
# Windows中，Ctrl-z也可以结束表示EOF。（
# 顺便提一句，Linux中按下Ctrl-Z，表示将该进程中断，在后台挂起，
# 用fg命令可以重新切回到前台；按下Ctrl-C表示终止该进程。）
# 文件结束符仅表示输入流到达了结束状态，并没有在文件中真实存在。在文件读取时，可能通过文件长度来
# 判断文件结束。在系统输入时，需要通过手动按ctrl-D或ctrl-z来结束
# python中按下ctrl+D即表示文件结束


def input_handle():
    """数组列表n * m
    n :横
    m: 纵
    :return:m, n， 数组
    """

    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    s = None
    arr = []
    i = 0
    # ctrl + D退出条件
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.find('S') != -1:
            s = (i, line.find('S'))
        arr.append(list(line))
        i += 1
    return n, m, arr, s


class Maze(object):
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr

    def shortest_path(self, s):
        def get_next(x, y, his):
            next_node = []
            if x - 1 >= 0 and self.arr[x - 1][y] != '1' and his[x - 1][y] == 0:
                next_node.append((x - 1, y))
            if x + 1 <= self.n - 1 and self.arr[x + 1][y] != '1' and his[x + 1][
                y] == 0:
                next_node.append((x + 1, y))
            if y - 1 >= 0 and self.arr[x][y - 1] != '1' and his[x][y - 1] == 0:
                next_node.append((x, y - 1))
            if y + 1 <= self.m - 1 and self.arr[x][y + 1] != '1' and his[x][
                y + 1] == 0:
                next_node.append((x, y + 1))
            return next_node

        history = copy.deepcopy(self.arr)
        for i in range(self.n):
            for j in range(self.m):
                history[i][j] = 0
        sx, sy = s
        history[sx][sy] = 2

        cnt = 0
        q = deque()
        q.append(s)
        while len(q) != 0:
            cur_x, cur_y = q.popleft()
            if self.arr[cur_x][cur_y] == 'E':
                return cnt
            nexts = get_next(cur_x, cur_y, history)
            for next_x, next_y in nexts:
                if self.arr[next_x][next_y] == 'E':
                    return cnt + 1
                q.append((next_x, next_y))
                history[next_x][next_y] = 1
            if history[cur_x][cur_y] == 2:
                if len(q) != 0:
                    last_x, last_y = q.pop()
                    history[last_x][last_y] = 2
                    q.append((last_x, last_y))
                cnt = cnt + 1
        return 'no way'


def func():
    row, column, array, s = input_handle()
    print(Maze(row, column, array).shortest_path(s))


if __name__ == "__main__":
    func()
