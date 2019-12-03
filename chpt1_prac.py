#practice problems from chapter 1
import unittest
import numpy as np
#1.1 determine if string has all unique characters
def is_unique(input_string):
    myhash = {}

    for i in range(len(input_string)):
        if input_string[i] not in myhash:
            myhash[input_string[i]]=i #just save index of where we found this character
        else:
            print("not unique!")
            return False
    print("unique!")
    return True

#1.2 check permutation, given two strings, write a method to decide if one is a permutation of the other

def addto_dict(mydict, input_string):
    for i in range(len(input_string)):
        if input_string[i] not in mydict:
            mydict[input_string[i]] = 1 #set val to one
        else:
            mydict[input_string[i]]+=1

def check_permutation(string1,string2):
    #ok here I think we want to create a dictionary of characters and their values
    #where the value is the number of times that key has appeared
    string1_dict = {}
    string2_dict = {}

    addto_dict(string1_dict,string1)
    addto_dict(string2_dict, string2)

    if string1_dict == string2_dict:
        print("they're permutations!")
        return True
    else:
        print ("they're not permutations!")
        return False

#1.3

#1.4 palindrome permutation
def pal_perm(input_string):
    myhash = {}

    for i in range(len(input_string)):
        if input_string[i] in myhash:
            myhash[input_string[i]] += 1
        else:
            myhash[input_string[i]] = 1

    #now go through hash table and make sure there is <= 1 odd value
    numodds = 0
    for key in myhash:
        if myhash[key]%2 != 0:
            numodds+=1
    if numodds > 1:
        return False
    return True

#1.5 One Away

def one_away(string1, string2):
    #first check if we are off by one in len, which requires replace or remove
    len1 = len(string1)
    len2 = len(string2)
    lendiff = len1-len2
    
    if abs(lendiff) > 1:
        return False

    #replace case
    if lendiff ==0:
        editcount = 0
        #then we're just looking to see if all elements are the same
        for i in range(len1):
            if string1[i] != string2[i]:
                editcount +=1
        if editcount > 1:
            return False

    #insert into string1 case
    if lendiff == -1:
        editcount = 0
        i=0
        j=0
        while (i < len1 and j < len2):
            if string1[i] != string2[j]:
                editcount +=1
                if editcount > 1:
                    return False
                j+=1 #advance j to represent inserting something into i and pairing it across to j
            i+=1
            j+=1
    if lendiff == 1:
        editcount = 0
        i=0
        j=0
        while (i < len1 and j < len2):
            if string1[i] != string2[j]:
                editcount +=1
                if editcount > 1:
                    return False
                i+=1 #advance i to represent removing from string1
            i+=1
            j+=1
    return True

#1.6 string compression
def compress_string(input_string):
    myhash = {}

    for i in range(len(input_string)):
        if input_string[i] in myhash:
            myhash[input_string[i]] += 1
        else:
            myhash[input_string[i]] = 1
    
    comp_string = ""
    for character in myhash:
        comp_string+=character + str(myhash[character])
    
    if len(comp_string <= input_string):
        return comp_string
    else:
        return input_string


#1.7 rotate matrix, first take, use np.rot90.  Didn't do it in place here though
def rotate_matrix(input_array):
    myshape = np.shape(input_array)
    if myshape[0] != myshape[1]:
        return "Not the correct shape"
    N = myshape[0]

    #i value goes to j value, j value goes to -i, at least for clockwise rotation
    new_array = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            new_array[i][j] = input_array[N-j-1][i]
    return new_array

#to do this in place, consider basically "shells" of the array, 1 element thick, save one side, rotate through the rest, then the remaining side is equal to the side you first saved
#try implementing this tomorrow!

def zero_matrix(input_array):
    myshape = np.shape(input_array)
    for i in range(myshape[0]):
        for j in range(myshape[1]):
            if input_array[i][j] == 0:
                input_array[i,:] *= 0 #zero out, in a numpy type way, need to do loop if we can't use numpy
                input_array[:,j] *= 0
                break #break out of j loop once we do this, since they're already 0
    return input_array

#do rotate string problem later, a while after looking at soln