import textevolution

DONOTHING = 30
POINTMUTATE = 60
INSERTION = 10
DELETION = 0

MUTATESTEPS = 5

#Initialize a text object

darwin = textevolution.Sentence();

#darwin.setsentence("From so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved.")
#darwin.setsentence("An American monkey, after getting drunk on brandy, would never touch it again, and thus is much wiser than most men.")
#darwin.setsentence("I have tried lately to read Shakespeare, and found it so intolerably dull that it nauseated me.")
darwin.setsentence("I love fools' experiments. I am always making them.")

# set the mutation parameters

darwin.setmutationrates(DONOTHING,POINTMUTATE,INSERTION,DELETION)

darwin.display()

for mutationstep in range(0,30):
    #print mutationstep
    # evolve the text as required
    darwin.mutate(MUTATESTEPS)

    # display the evolved text
    darwin.display()



