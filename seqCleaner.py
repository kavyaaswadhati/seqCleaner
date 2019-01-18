#!/usr/bin/env python3 
# Name: Kavya Aswadhati (kaswadha) 
# Group Members: None

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example: 
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring (str):
    def length (self):
        return (length(self))
    
    def purify(self):
        ''' Return an upcased version of the string, collapsing a single run of Ns.'''
        upped = self.upper()
        # find the number of 'N's in the block and first index of the block
        numN = upped.count('N')
        indexN = upped.find('N')
        purified =  str (upped[:indexN] +'{' + str (numN) + '}' +upped[(indexN+numN):])
        return purified
    
def main():
    ''' Get user DNA data and clean it up.'''
    data = input('DNA data?')
    thisDNA = DNAstring (data)
    pureData = thisDNA.purify()
    print (pureData)
    
main()
