#practice problems from chapter 1


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
