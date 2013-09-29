# ======================================================================

import string
import random
import enchant
from enchant.tokenize import get_tokenizer

# ======================================================================

class Sentence(object):
    """
    NAME
        Sentence

    PURPOSE
        Define a mutatable sentence.

    COMMENTS
        The Sentence is mutated in a random way. 

    INITIALISATION
    
    METHODS

       setsentence(initialsentence)
       
       setmutationrates(donothingrate,pointmutationrate,insertionrate,deletionrate)
       
       mutate(mutationsteps)
       
       display()
       

    BUGS

    AUTHORS
      This file is part of the TextEvolution project, by David Harris
    """

# ----------------------------------------------------------------------------

    def __init__(self):
        
        self.name = 'a sentence, that can be mutated'
        self.sentence = ''
        self.donothingrate = 0
        self.pointmutationrate = 0
        self.insertionrate = 0
        self.deletionrate = 0
        
        self.d = enchant.Dict("en_US")
        self.tknzr = get_tokenizer("en_US")
        
        return None

# ----------------------------------------------------------------------------

    def __str__(self):
        return 'I am %s' % (self.name)

# ----------------------------------------------------------------------------

    def setsentence(self,sentence):
        
        self.sentence = sentence
        

        return None

# ----------------------------------------------------------------------------

    def setmutationrates(self,donothing,point,insertion,deletion):

        self.donothingrate = donothing
        self.pointmutationrate = point
        self.insertionrate = insertion
        self.deletionrate = deletion
        
        return None
        
# ----------------------------------------------------------------------------

    def display(self):

        #print "Sentence:",self.sentence
        print self.sentence
        
        return None

# ----------------------------------------------------------------------------

    def mutate(self,steps):
        #print "Steps:", steps
        for mutationstep in range(0,steps):
            #print "Mutation step:", mutationstep
            # Select mutation type and do the mutation
            mutationtype = random.randint(0, 99)

            if mutationtype < self.donothingrate: # make no mutation at all
                continue
                #print "Do nothing"
            elif mutationtype < self.donothingrate+self.pointmutationrate: # mutate one letter
                randomposition = random.randint(0,len(self.sentence)-1)
                #print randomposition
                randomletter = string.letters[random.randint(0,51)]
                #print randomletter
                self.sentence = self.sentence[:randomposition] + randomletter + self.sentence[randomposition+1:]
                
            elif mutationtype <  self.donothingrate+self.pointmutationrate+self.insertionrate: # insert one letter
                randomposition = random.randint(0,len(self.sentence)-1)
                #print randomposition
                randomletter = string.letters[random.randint(0,51)]
                #print randomletter
                self.sentence = self.sentence[:randomposition] + randomletter + self.sentence[randomposition:]
                
            else: # delete one letter
                randomposition = random.randint(0,len(self.sentence)-1)
                #print randomposition
                self.sentence = self.sentence[:randomposition] + self.sentence[randomposition+1:]
                
            # Correct after the mutation
            # print self.d.check(self.sentence)
            
            newsentence = ''
            
            for word in self.tknzr(self.sentence):
            	#print word, self.d.suggest(word[0])[0]
            	if len(word[0])>1:
            	    if self.d.check(word[0]):
            	    	newword = word[0]
            	    else:
            	        if self.d.suggest(word[0]):
            	            newword = self.d.suggest(word[0])[0]
            	        else:
            	            newword = ''  
            	else:
            	    newword = ''
            	
            	#print word, newword    
        
                newsentence = newsentence + ' ' + newword
                
            self.sentence = newsentence
            
        return None
        
# ============================================================================
