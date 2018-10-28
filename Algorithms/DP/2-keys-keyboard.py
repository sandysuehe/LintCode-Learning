#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 19:16:09
# File Name: 2-keys-keyboard.py
# Description: 2 Keys Keyboard 两键的键盘
# LintCode: https://www.lintcode.com/problem/2-keys-keyboard/
#########################################################################
# 思路:
# 对于任意一个n(除了1以外)，我们最差的情况就是用n步，不会再多于n步，但是有可能是会小于n步。
# 要找出n的所有因子，然后这个因子可以当作模块的个数，我们再算出模块的长度n/i，调用递归，加上模块的个数i来更新结果res
# 当n = 1时，已经有一个A了，我们不需要其他操作，返回0
# 当n = 2时，我们需要复制一次，粘贴一次，返回2
# 当n = 3时，我们需要复制一次，粘贴两次，返回3
# 当n = 4时，这就有两种做法，一种是我们需要复制一次，粘贴三次，共4步，另一种是先复制一次，粘贴一次，得到AA，然后再复制一次，粘贴一次，得到AAAA，两种方法都是返回4
# 当n = 5时，我们需要复制一次，粘贴四次，返回5
# 当n = 6时，我们需要复制一次，粘贴两次，得到AAA，再复制一次，粘贴一次，得到AAAAAA，共5步，返回5 
#########################################################################
def minSteps(n):
    if n == 1:
        return 0
    res = n
    for i in range(n-1, 1, -1):
        if n % i == 0:
            print "n: {0}, i: {1}, n/i: {2}".format(n, i, n/i)
            res = min(res, minSteps(n/i)+i)
    return res

print minSteps(6)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
