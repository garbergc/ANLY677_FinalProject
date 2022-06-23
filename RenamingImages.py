#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:54:03 2022

@author: claregarberg
"""

import os

root = "/Users/claregarberg/Documents/Graduate School/Summer 2022/Image Analytics/Project/Images"

os.chdir(root)

for dir, subdirs, files in os.walk("."):
    for i, f in enumerate(files):
        if f == ".DS_Store":
            continue
        else:
            folder_name = dir[2:]
            name_new = folder_name + str(i)
            path_new = root + "/" + folder_name
            #print(name_new)
            os.rename(os.path.join(path_new, f), os.path.join(path_new, name_new))