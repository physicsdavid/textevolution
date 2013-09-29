import textevolution

DONOTHING = 50
POINTMUTATE = 40
INSERTION = 5
DELETION = 5

MUTATESTEPS = 1

#Initialize a text object

darwin = textevolution.Sentence();

darwin.setsentence("This is a test sentence.")

# set the mutation parameters

darwin.setmutationrates(DONOTHING,POINTMUTATE,INSERTION,DELETION)

for mutationstep in range(0,100):
    #print mutationstep
    # evolve the text as required
    darwin.mutate(MUTATESTEPS)

    # display the evolved text
    darwin.display()



