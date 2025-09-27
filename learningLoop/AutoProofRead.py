'''
Created on 25-Mar-2024

@author: jeete
'''
import lmproof as lm

## Function for proofreading 
def Proofread(text):
    proof = lm.load("en")
    error_free_text = proof.proofread(text)
    return error_free_text

## Sample Text
TEXT = 'The varialbe was initilized with an invald value, causing the progam to throw a runtime erro.'

## Function Call 
print(Proofread(TEXT))

# --------------------------
# The variable was initialized with an invalid value, causing the program to throw a runtime error.