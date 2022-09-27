#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_c = None
    else:
        first_c = sentence[0]
    return(len(sentence), first_c)
