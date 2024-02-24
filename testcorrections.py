#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:28:16 2024

@author: nitika
"""


# Part 2, Question 1
def count_unique_proteins(p_list):
    '''The following counts unique protein numbers.'''
    return len(set(p_list[i][:7] for i in range(len(p_list))))


# Part 2, Question 2
def count_proteins(p_list):
    '''The following returns a dictionary of counts.'''
    newlist = list(p_list[i][:7] for i in range(len(p_list)))
    counts = dict()
    for i in newlist:
        counts[i] = counts.get(i, 0) + 1
    return counts


# Part 2, Question 3

# x = count_proteins(list1)
# y = count_proteins(list2)
def merge_protein_counts(dict1, dict2):
    '''The following merges two protein counts dictionaries.'''
    items = list(dict1.keys()) + list(dict2.keys())
    list_of_tup = []
    for item in items:
        if (item in dict1.keys()) and (item in dict2.keys()):
            list_of_tup.append(tuple((dict1.get(item), dict2.get(item))))
        elif item in dict1.keys():
            list_of_tup.append(tuple((dict1.get(item), 0)))
        elif item in dict2.keys():
            list_of_tup.append(tuple((0, dict2.get(item))))
    d_pc = dict(zip(items, list_of_tup))
    return d_pc


# Part 3, Question 1
def dates_to_iso8601(dlist):
    mon = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07',"Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
    iso = []
    for element in dlist:
        year = element[-4:]
        if element[0:3] in mon.keys():
            month = mon.get(element[0:3])
        day = str(element[-8:-6])
        if day[0:1] == " ":
            day = day.replace(" ", "0")
        iso.append("{}-{}-{}".format(year, month, day))
    return iso


# Part 3, Question 2
def sort_dates(date_list):
    format_list = dates_to_iso8601(date_list)
    official = sorted(format_list)
    rev_mon = {"01": 'January', "02": 'February', "03": 'March', "04":          'April', "05": 'May', "06": 'June', "07": 'July', "08": 'August', "09": 'September', "10": 'October', "11": 'November', "12": 'December'}
    rev_iso = []
    for element in official:
        year = element[:4]
        month = rev_mon.get(element[5:7])
        day = str(element[-2:])
        if day[0:1] == "0":
            day = day.replace("0", "")
        rev_iso.append("{} {}, {}".format(month, day, year))
    return rev_iso

# hello = ["February 6, 1992", "February 18, 1992", "February 18, 1942", "February 27, 1992", "September 6, 1994", "December 1, 1993"]
