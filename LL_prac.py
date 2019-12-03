import numpy as np

class node:
    def __init__(self,myval):
        self.val = myval
        self.next = None


#if we want to include default values of None for the data and the next node we do
class node_default:
    def __init__(self,val=None,nextnode=None):
        self.val = val
        self.nextnode = nextnode

rootnode = node_default(5)
rootnode.nextnode = node(10)
print(rootnode.nextnode.val)
