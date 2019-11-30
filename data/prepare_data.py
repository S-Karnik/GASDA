#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:32:00 2019

@author: sathwik
"""

import os

def main():
    # training data
    kitti_set_path = "../datasets/kitti/train.txt"
    with open(kitti_set_path) as tf:
        paths = tf.readlines()
    
    delimited_paths = []
    
    for path_line in paths:
        for path in path_line.split(' '):
            if (path[-4:] == '.png'):
                delimited_paths.append(path)
            elif (path[-5:] == '.bin\n'):
                delimited_paths.append(path[:-1])
    
    

main()