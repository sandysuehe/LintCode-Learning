#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-16 17:11:04
# File Name: scheduleCourse.py
# Description: 
#########################################################################
def scheduleCourse(courses):
    cur_time = 0

    import Queue
    queue = Queue.PriorityQueue()

    # 对courses按课程close_time进行升序排序
    courses = sorted(courses, key=lambda s: s[1])

    for course in courses:
        duration = course[0]
        close_time = course[1]
        cur_time += duration

        # 遍历每个course的duration，升序存入queue
        queue.put(-duration)

        # 如果cur_time > close_time,将queue中的最大duration弹出来
        # cur_time = cur_time - max_duration
        if cur_time > close_time:
            max_duration = -(queue.get())
            cur_time -= max_duration
    return queue.qsize()


courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print scheduleCourse(courses)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
