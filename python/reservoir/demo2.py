#!/usr/bin/python

import random

sample_rate = 0.2

def sample(data_total_num):
    global sample_rate
    sample_list = []; 
    sample_num = int(data_total_num * sample_rate)
    for i in range(sample_num):
        sample_list.append(i)
    for i in range(sample_num, data_total_num):
        m = random.randint(0, i)
        if m < sample_num:
            sample_list[m] = i 
    return sample_list

def main():
    print sample(25)

if __name__ == '__main__':
    main()
