#!/usr/bin/env python3

#Author: Hoang Tan Phan
#Author ID: htphan1
#Date Created: 2020/09/24

import sys

if len(sys.argv) == 2:
	timer = int(sys.argv[1])
	while timer != 0:
		print(timer)
		timer = timer - 1
else:
	timer = 3
	while timer != 0:
		print(timer)
		timer = timer - 1	
print('blast off!')
