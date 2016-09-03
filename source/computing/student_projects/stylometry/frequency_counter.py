#- Nathaniel Latta (2015-12-9): initial version


import unicodedata
import sys
class FrequencyCounter(object):
    r"""

    cointains functions to do analysis on: 
    letter frequency, word frequecny, quotation frequency

    INPUT:

    a text file with english text to analyse

    OUTPUT:

    None

    EXAMPLES:

    object_name=FrequencyCounter("example.txt")

   
    """
    def __init__(self, input):
        self.input=input

        # initialize/store char frequency
        self.input_file = open(self.input, "r")
        self.expected_char_frequency_file = open("expected_frequency.txt", "r")
        self.char_frequency=self.store_all_char(self.input_file)
        self.expected_char_frequency=self.store_expected_frequency(self.expected_char_frequency_file)
        self.close_file()

        # initialize/store word frequency
        self.input_file=open(self.input,"r")
        self.word_frequency=self.store_word_frequency(self.input_file)
        self.close_file()

        # initialize/store quote frequency
        self.input_file=open(self.input,"r")
        self.quote_frequency=self.store_quote_frequency(self.input_file)
        self.close_file()

        # initialize/store phrase frequency
        self.input_file=open(self.input,"r")
        self.phrase_frequency=self.store_phrase_frequency(self.input_file,"look for a phrase")
        self.close_file()


    def close_file(self):
        r"""
    closes all the files used by the program

    INPUT:

    none


    OUTPUT:

    none


    EXAMPLES:

    class_object_name.close_file()
   
    """
        self.input_file.close()
        self.expected_char_frequency_file.close()

    def store_all_char(self,source_file):
        r"""
    harvests frequency of chars. Looks through a file char by char and increments the value corresponding to that char when it is encountered

    INPUT:

    a file of text - refer to class description to see what types of characters can be processed


    OUTPUT:

    a list of lists  where the first list holds each letter and the inner list holds the name of the letter in [0] and the frequency it occurs at in [1]


    EXAMPLES:

    frequency=class_object_name.store_all_char("source.txt")


    print(frequency)  ---->  [['!', 0], ['"', 0], ['#', 0], ['$', 0], ['%', 0], ['&', 0], ["'", 2], ['(', 6], [')', 6], ['*', 0], ['+', 0], [',', 24], ['-', 4], ['.', 14], ['/', 0], ['0', 5], ['1', 6], ['2', 1], ['3', 3], ['4', 3], ['5', 1], ['6', 2], ['7', 1], ['8', 3], ['9', 0], [':', 1], [';', 1], ['<', 0], ['=', 0], ['>', 0], ['?', 0], ['@', 0], ['A', 3], ['B', 1], ['C', 8], ['D', 0], ['E', 12], ['F', 1], ['G', 0], ['H', 4], ['I', 2], ['J', 3], ['K', 1], ['L', 5], ['M', 4], ['N', 1], ['O', 0], ['P', 0], ['Q', 0], ['R', 0], ['S', 1], ['T', 1], ['U', 0], ['V', 1], ['W', 0], ['X', 0], ['Y', 0], ['Z', 0], ['[', 2], ['\\', 0], [']', 2], ['^', 0], ['_', 0], ['`', 0], ['a', 294], ['b', 33], ['c', 73], ['d', 68], ['e', 276], ['f', 47], ['g', 54], ['h', 87], ['i', 151], ['j', 3], ['k', 9], ['l', 101], ['m', 61], ['n', 144], ['o', 121], ['p', 42], ['q', 21], ['r', 137], ['s', 145], ['t', 176], ['u', 61], ['v', 21], ['w', 25], ['x', 13], ['y', 44], ['z', 5], ['{', 0], ['|', 0], ['}', 0]]

   
    """


        destination=self.make_storage()

        next_char=source_file.read(1)

        while next_char:
            found=0
            for i in range(len(destination)):#look through the array to see if this letter has already been added
                if next_char==destination[i][0]:#if the char is already here increment it's count
                    destination[i][1]=destination[i][1]+1
                    found=1
            if found==0:
                destination.append([next_char,1])

            next_char=source_file.read(1)
        return destination

    def store_expected_frequency(self,source_file):
        r"""
    takes the file stored in source_file and looks in it for letter frequency's and then stores them in a list

    INPUT:

    a text file with frequency values for chars
    the format of "frequency.txt" should be "char #" on each line. It should contain the values a-z but also supports frequency counts on other standard ascii symbols



    OUTPUT:

    [['!', 0], ['"', 0], ['#', 0], ['$', 0], ['%', 0], ['&', 0], ["'", 0], ['(', 0], [')', 0], ['*', 0], ['+', 0], [',', 0], ['-', 0], ['.', 0], ['/', 0], ['0', 0], ['1', 0], ['2', 0], ['3', 0], ['4', 0], ['5', 0], ['6', 0], ['7', 0], ['8', 0], ['9', 0], [':', 0], [';', 0], ['<', 0], ['=', 0], ['>', 0], ['?', 0], ['@', 0], ['A', 0], ['B', 0], ['C', 0], ['D', 0], ['E', 0], ['F', 0], ['G', 0], ['H', 0], ['I', 0], ['J', 0], ['K', 0], ['L', 0], ['M', 0], ['N', 0], ['O', 0], ['P', 0], ['Q', 0], ['R', 0], ['S', 0], ['T', 0], ['U', 0], ['V', 0], ['W', 0], ['X', 0], ['Y', 0], ['Z', 0], ['[', 0], ['\\', 0], [']', 0], ['^', 0], ['_', 0], ['`', 0], ['a', 0.08167], ['b', 0.01492], ['c', 0.02782], ['d', 0.04253], ['e', 0.12702], ['f', 0.02228], ['g', 0.02015], ['h', 0.06094], ['i', 0.06966], ['j', 0.00153], ['k', 0.00772], ['l', 0.04025], ['m', 0.02406], ['n', 0.06749], ['o', 0.07507], ['p', 0.01929], ['q', 0.00095], ['r', 0.05987], ['s', 0.06327], ['t', 0.09056], ['u', 0.02758], ['v', 0.00978], ['w', 0.02361], ['x', 0.0015], ['y', 0.01974], ['z', 0.00074], ['{', 0], ['|', 0], ['}', 0]]


    EXAMPLES:

    the function is called like:

    expected_frequency=self.store_expected_frequency("frequency.txt")

    
    """
        destination=self.make_storage()

        next_line=source_file.readline()
        while next_line:
            for i in range(len(destination)):#iterates through the storage array alphabet so following code can match with frequency
                line_spit=next_line.split()#each line has two parts
                if line_spit[0]==destination[i][0]:#destination has the right structure to store % values instead of counts
                    destination[i][1]=float(line_spit[1])#set the percent when above line of code matches letters
            next_line=source_file.readline()
                
        return destination


    def make_storage(self):
        r"""
    this builds the houseing array for the program to use for char based frequency counts

    INPUT:

    none


    OUTPUT:

    none


    EXAMPLES:

    container=class_object_name.make_storage()
   

    the array will look like this
    [['!', 0], ['"', 0], ['#', 0], ['$', 0], ['%', 0], ['&', 0], ["'", 0], ['(', 0], [')', 0], ['*', 0], ['+', 0], [',', 0], ['-', 0], ['.', 0], ['/', 0], ['0', 0], ['1', 0], ['2', 0], ['3', 0], ['4', 0], ['5', 0], ['6', 0], ['7', 0], ['8', 0], ['9', 0], [':', 0], [';', 0], ['<', 0], ['=', 0], ['>', 0], ['?', 0], ['@', 0], ['A', 0], ['B', 0], ['C', 0], ['D', 0], ['E', 0], ['F', 0], ['G', 0], ['H', 0], ['I', 0], ['J', 0], ['K', 0], ['L', 0], ['M', 0], ['N', 0], ['O', 0], ['P', 0], ['Q', 0], ['R', 0], ['S', 0], ['T', 0], ['U', 0], ['V', 0], ['W', 0], ['X', 0], ['Y', 0], ['Z', 0], ['[', 0], ['\\', 0], [']', 0], ['^', 0], ['_', 0], ['`', 0], ['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0], ['{', 0], ['|', 0], ['}', 0]]



    """


#33-126
#93 iterations
        destination=[1]*93
        for i in range(93):
            temp=[chr(i+33),0]    #see above note  # 32 is ' '
            destination[i]=temp
        return destination



    def combine_alphabet_cases(self):


        r"""
    this function takes the frequency's stored for a char and copies the value to exist for both the lower case and upper case instantiation of the char for easy referency in cases that are not case sensitive

    INPUT:

    none


    OUTPUT:

     the text "aAAbb" will store the values for a and b as A=2 a=3 B=0 b=2 once this function is run it will be counted as A=3 a=3 B=2 b=2



    """

        for i in range(26):
            self.char_frequency[32+i][1]=self.char_frequency[32+i][1]+self.char_frequency[64+i][1]
            self.char_frequency[64+i][1]=self.char_frequency[32+i][1]

    def print_frequency(self,to_print):
        r"""
    this function takes the frequency's stored for a char and copies the value to exist for both the lower case and upper case instantiation of the char for easy referency in cases that are not case sensitive

    INPUT:

    none


    OUTPUT:
    the output will be formated in the form:
    ! 0
    " 6
    # 0
    ...
    ..
    .


    """

        for i in range (len(to_print)):
            print(str(to_print[i][0])+" "+str(to_print[i][1]))


    def compare_alphabet(self):
        r"""
    this function looks at the frequency (expressed as a percent) of a char in the document and compares it to the expected values and prints a comparison.

    INPUT:

    none


    OUTPUT:

     LETTER    Expected Frequency     Actual Frequency
   A-------------0.08167----------------0.131415929204
   B-------------0.01492----------------0.0150442477876
   C-------------0.02782----------------0.0358407079646
   D-------------0.04253----------------0.0300884955752
   E-------------0.12702----------------0.127433628319
   F-------------0.02228----------------0.0212389380531
   G-------------0.02015----------------0.0238938053097
   H-------------0.06094----------------0.0402654867257
   I-------------0.06966----------------0.0676991150442
   J-------------0.00153----------------0.00265486725664
   K-------------0.00772----------------0.00442477876106
   L-------------0.04025----------------0.0469026548673
   M-------------0.02406----------------0.0287610619469
   N-------------0.06749----------------0.0641592920354
   O-------------0.07507----------------0.0535398230088
   P-------------0.01929----------------0.0185840707965
   Q-------------0.00095----------------0.00929203539823
   R-------------0.05987----------------0.0606194690265
   S-------------0.06327----------------0.0646017699115
   T-------------0.09056----------------0.0783185840708
   U-------------0.02758----------------0.0269911504425
   V-------------0.00978----------------0.00973451327434
   W-------------0.02361----------------0.0110619469027
   X-------------0.0015----------------0.00575221238938
   Y-------------0.01974----------------0.0194690265487
   Z-------------0.00074----------------0.00221238938053


    EXAMPLES:

    lettercounter=FrequencyCounter("test.txt")
    lettercounter.compare_alphabet()
   


    """


        self.actual_frequency=self.make_storage()
        self.combine_alphabet_cases()
        total_letters=0.0
        for i in range (26):
            total_letters=total_letters+self.char_frequency[32+i][1]
        print(" LETTER    Expected Frequency     Actual Frequency")
        for i in range(26):
            temp=self.char_frequency[32+i][1]/total_letters
            if (i==0):
                print("first letter is : "+self.actual_frequency[64+i][0]+" ")
                print(temp)
            
            self.actual_frequency[64+i][1]=temp
            print("   "+chr(i+65)+"-------------"+str(self.expected_char_frequency[64+i][1])+"----------------"+str(temp))

    def guess(self,letter):
        r"""
   description

    compares the expected frequency to the actual frequency and tries to match each letter actual frequcny with a letter that has a similar expected frequency
    the first number returned is the most likely guess based off of frequency

    INPUT:

    a char between a and z


    OUTPUT:

    an array of chars that represent possibles identities of the passed in letter. the number of items in the array is based on how many potential matches are found where a potential match is a letter with a frequency difference that is smaller than the difference of the last potential match.
    thus the output will always contain at least the value that was guessed if there was not another letter found with a closer difference from expected frequncy    

    EXAMPLES:


    for example if the letter a has an actual frequncy of 0.131 it will guss that that letter might actually be e since the expected frequency value of e is 0.127 thus the difference will be the smallest when compared to the other letters



    lettercounter=FrequencyCounter("textfile.txt")
    classname.guess(chr(i+97))

    
    """
        if((ord(letter)<97)or(ord(letter)>122)):
            print("Error guess(letter) letter is out of range\n")
            exit()
        
        lookup=ord(letter)-32
     

        self.sorted_expected
        self.sorted_actual


        for i in range(26):
            if (self.sorted_actual[i][0]==letter):
                return self.sorted_expected[i][0]

        guess_val=[]
        guess_val.append(chr(64+32))
        return guess_val


    def guess_all(self):
        r"""
    makes a guess for each letter of the alphabet as to which letter the input letter might correspond to

    INPUT:

    - ``self`` 


    OUTPUT:

    output will look like:

    a might be ['e', 'a']
    b might be ['b']
    c might be ['l', 'c']
    d might be ['c', 'b', 'a', 'd']
    e might be ['e', 'a']
    f might be ['f']
    g might be ['m', 'f', 'c', 'b', 'g']
    h might be ['l', 'd', 'c', 'b', 'h']
    i might be ['n', 'i', 'h', 'a']
    j might be ['j']
    k might be ['j', 'b', 'k']
    l might be ['d', 'c', 'l']
    m might be ['c', 'b', 'm']
    n might be ['s', 'h', 'n']
    o might be ['r', 'h', 'd', 'c', 'a', 'o']
    p might be ['p', 'g', 'b']
    q might be ['v', 'k', 'b', 'q']
    r might be ['h', 'r']
    s might be ['s', 'n', 'h', 'a']
    t might be ['o', 'a', 't']
    u might be ['u', 'c', 'b']
    v might be ['v', 'k', 'b']
    w might be ['v', 'k', 'b', 'w']
    x might be ['k', 'j', 'b', 'x']
    y might be ['p', 'g', 'f', 'b', 'y']
    z might be ['j', 'z']



    EXAMPLES:

    This example illustrates how to call the guess_all function

    lettercounter=FrequencyCounter("textfile.txt")
    lettercounter.guess_all()

    which gives the output above where the suggestion corresponds to the relationship between the expected and actuall letter frequency's


    NOTE::

    This will guess for letters between a and z
    the first letter in the returned array of .guess() is the most likely letter

    """

        self.sorted_expected=self.merge_sort_by_frequency_decending(self.expected_char_frequency)
        self.sorted_actual=self.merge_sort_by_frequency_decending(self.actual_frequency)




        for i in range(26):
            print(chr(i+97)+" might be "+str(self.guess(chr(i+97))))

    def store_word_frequency(self,source_file):    #   WILL NEED TO SANITIZE DATA
        r"""
   description

    INPUT:


    OUTPUT:

    

    EXAMPLES:

    
    """
        destination=[]
        next_line=source_file.readline()
        
        while next_line:
            line_split=next_line.split()
            for i in range(len(line_split)):

                #this is where the non a-z characters get removed from the storage.
                temp=""
                for l in range(len(line_split[i])):
                    if (   (line_split[i][l]>=" ") and (line_split[i][l]<="@")     ):
                        pass
                    elif (    (line_split[i][l]>="[") and (line_split[i][l]<="_")      ):
                        pass
                    elif (    (line_split[i][l]>="{") and (ord(line_split[i][l])<=127)      ):
                        pass
                    else:
                        temp=temp+(line_split[i][l].lower())


                line_split[i]=temp


                if(temp!=""):
                    if(len(destination))==0:
                        destination.append([line_split[0],1])
                    else:
                        foundword=False
                        for x in range(len(destination)):
                            if line_split[i]==destination[x][0]:
                                destination[x][1]=destination[x][1]+1
                                foundword=True
                        if(foundword==False):
                            destination.append([line_split[i],1])
            next_line=source_file.readline()

        return destination



    def merge_sort_by_frequency_decending(self,source):
        r"""
   description

    takes a list of frequency's in the form [ [item,count], [item2,count],...   ]

    INPUT:
    a list of items in the form above. they will be sorted according to count highest to lowest

    OUTPUT:

    returns the sorted list

    EXAMPLES:

    sorted_frequency=classname.merge_sort_by_frequency_decending(classname.word_frequency)

    
    """
        A=[]
        B=[]
        combine=[]
        odd=False

        if (len(source)>1):
            mid=len(source)/2
            
            if ( ( len(source)%2)==0  ):
                odd=False
            else:
                odd=True
            # creates A and B if source is only len two then the function does not need to be called again as this will split it
            for i in range(int(mid)):
                A.append(source[i])

            if(odd):
                for i in range(int(len(source)-mid)+1):#dropping last letter
                    B.append(source[i+int(mid)])
            else:
                for i in range(int(len(source)-mid)):#dropping last letter
                    B.append(source[i+int(mid)])
            if(len(A)>1):
                A=self.merge_sort_by_frequency_decending(A)
            if(len(B)>1):
                B=self.merge_sort_by_frequency_decending(B)

            while ((len(A)>0)or(len(B)>0)):
                if((len(A)>0)and(len(B)>0)):
                    if(A[0][1]>B[0][1]):
                        combine.append(A[0])#where do i add on the other half of the data?
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                elif ( (len(A)>0) and (len(B)<=0) ):
                    #take from A
                    combine.append(A[0])
                    A.pop(0)
                elif ( (len(A)<=0) and (len(B)>0)   ):
                    #take from B
                    combine.append(B[0])
                    B.pop(0)
                else:#this should never run?
                    
                    #combine singles
                    if(A[0][1]>B[0][1]):
                        combine.append(A[0])
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                



        else:
            combine=source[0]
        return combine


    def merge_sort_by_frequency_ascending(self,source):
        r"""
   description

    takes a list of frequency's in the form [ [item,count], [item2,count],...   ]

    INPUT:
    a list of items in the form above. they will be sorted according to count lowest to highest

    OUTPUT:

    returns the sorted list

    EXAMPLES:

    sorted_frequency=classname.merge_sort_by_frequency_ascending(classname.word_frequency)

    
    """
        A=[]
        B=[]
        combine=[]
        odd=False

        if (len(source)>1):
            mid=len(source)/2
            
            if ( ( len(source)%2)==0  ):
                odd=False
            else:
                odd=True
            # creates A and B if source is only len two then the function does not need to be called again as this will split it
            for i in range(int(mid)):
                A.append(source[i])

            if(odd):
                for i in range(int(len(source)-mid)+1):#dropping last letter
                    B.append(source[i+int(mid)])
            else:
                for i in range(int(len(source)-mid)):#dropping last letter
                    B.append(source[i+int(mid)])
            if(len(A)>1):
                A=self.merge_sort_by_frequency_ascending(A)
            if(len(B)>1):
                B=self.merge_sort_by_frequency_ascending(B)

            while ((len(A)>0)or(len(B)>0)):
                if((len(A)>0)and(len(B)>0)):
                    if(A[0][1]<B[0][1]):
                        combine.append(A[0])#where do i add on the other half of the data?
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                elif ( (len(A)>0) and (len(B)<=0) ):
                    #take from A
                    combine.append(A[0])
                    A.pop(0)
                elif ( (len(A)<=0) and (len(B)>0)   ):
                    #take from B
                    combine.append(B[0])
                    B.pop(0)
                else:#this should never run?
                    
                    #combine singles
                    if(A[0][1]>B[0][1]):
                        combine.append(A[0])
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                



        else:
            combine=source[0]
        return combine


    def merge_sort_by_alphabetical(self,source):
        r"""
    description

    takes a list of frequency's in the form [ [item,count], [item2,count],...   ] where item is a string

    INPUT:
    a list of items in the form above. they will be sorted according to alphatetical order

    OUTPUT:

    returns the sorted list

    EXAMPLES:

    sorted_frequency=classname.merge_sort_by_alphatetical(classname.word_frequency)


    """
        A=[]
        B=[]
        combine=[]

        if (len(source)>1):
            mid=len(source)/2
            for i in range(int(mid)):
                A.append(source[i])
            for i in range(len(source)-int(mid)):
                B.append(source[i+int(mid)])
            if(len(A)>1):
                A=self.merge_sort_by_alphabetical(A)
            if(len(B)>1):
                B=self.merge_sort_by_alphabetical(B)

            while ((len(A)>0)or(len(B)>0)):
                if((len(A)>0)and(len(B)>0)):
                    #take from both
                    if(A[0][0].lower()[0]<B[0][0].lower()[0]):
                        combine.append(A[0])
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                elif ( (len(A)>0) and (len(B)<=0) ):
                    #take from A
                    combine.append(A[0])
                    A.pop(0)
                elif ( (len(A)<=0) and (len(B)>0)   ):
                    #take from B
                    combine.append(B[0])
                    B.pop(0)
                else:#this should never run?
                    
                    #combine singles
                    if(A[0][0]>B[0][0]):
                        combine.append(A[0])
                        A.pop(0)
                    else:
                        combine.append(B[0])
                        B.pop(0)
                



        else:
            combine=source[0]

        
        return combine







    def sort_words(self,input_val):
        r"""
   description

   sorts the word_frequency var according to a specification (currently set in function)

    INPUT:

    an int that corresponds to the amount of sort options avalible. In this case 1, 2 or 3. 1 will toggle frequency descending 2 will toggle frequency ascending while 3 will toggle alphabetical

    OUTPUT:

    none (use print_frequency)

    EXAMPLES:

    just call this function on a word_frequency var and it will reorganize the list to be alphabetical or greatest to least
    
    """

        if(input_val==1):
            self.word_frequency=self.merge_sort_by_frequency_decending(self.word_frequency)
        if(input_val==2):
            self.word_frequency=self.merge_sort_by_frequency_ascending(self.word_frequency)
        if(input_val==3):
            self.word_frequency=self.merge_sort_by_alphabetical(self.word_frequency)
            

    def store_quote_frequency(self,source_file):
        r"""
   description

    INPUT: text file to read in from


    OUTPUT: returns array with all qutoes

    

    EXAMPLES:
        class_object_name=object_name("example.txt")
        object_name.print_frequency(class_object_name.quote_frequency)
    
    """
       
        next_line=source_file.readline()

        quote=[]
        quote_string=""
        quote_found=0

        while next_line: 
            line_split=next_line.split()
            for i in range(len(line_split)):#check each word that was read in on the line
                # this pulls out appropriate letters from a string and reconstructs it
                temp=""
                for l in range(len(line_split[i])):         
                    if ( line_split[i][l]=="\""   ):
                        # check for " " here
                        quote_found=quote_found+1#ever time we find a quote we increment so we know when the quote closes
                        temp=temp+line_split[i][l]
                    if (quote_found>0):#this makes us only pull words when we are within a quote
                        if ( ((line_split[i].lower()[l])>="a")and((line_split[i].lower()[l])<='z')   ):
                            temp=temp+(line_split[i][l])#add words #I removed making them lower case I don't think we need that
                        elif (line_split[i][l]=="\""):#evey time we get here if a quote is found we've already delt with it so we skip here so we don't have repititious occurances
                            pass
                        else:
                            temp=temp+(line_split[i][l])#add symbols
                quote_string=quote_string+temp
                if(quote_found>0):
                    quote_string=quote_string+" "
                # here the word is added to the array if it is the first of it's type or incrmented if it already has a value
                if(quote_found==2):
                    quote_found=0;#tell program that we are on a new quote
                    if(len(quote))==0:#if the quote array is empty just add the quote on
                        quote.append([quote_string,1])
                        quote_string=""#reset the contents of the harvested quote for the next iteration
                    else:#if the quote array is not empty we need to check to see if the quote already exists
                        foundquote=False
                        for x in range(len(quote)):
                            if quote_string==quote[x][0]:
                                quote[x][1]=quote[x][1]+1
                                foundquote=True
                        if(foundquote==False):
                            quote.append([quote_string,1])
                        quote_string=""#reset the contents of the harvested quote for the next iteration
            next_line=source_file.readline()

        return quote


    def store_phrase_frequency(self,source_file,phrase):    #   WILL NEED TO SANITIZE DATA
        r"""
   description

    INPUT: text file to read in from and a string which is the prase to look for in that textfile


    OUTPUT: returns number of phrases found  ....... maybe should show near matches???

    
    EXAMPLES:
        class_object_name=object_name("example.txt")
        object_name.print_frequency(class_object_name.quote_frequency)
    
    """
        
        next_line=source_file.readline()

        phrase_found=""
        phrase_count=0
        split_phrase=phrase.split()
        phrase_index=0
        phrase_array=[]

        while next_line: 
            line_split=next_line.split()
            
            for i in range(len(line_split)):#check each word that was read in on the line
                if ( split_phrase[phrase_index].lower() == line_split[i].lower()  ):#leave this lower() only if switching to case sensitive storing
                    phrase_found=phrase_found.lower()+line_split[i].lower()            # this would not stay
                    phrase_index=phrase_index+1
                    if ( not((len(split_phrase)-0)==phrase_index)  ):
                        phrase_found=phrase_found.lower()+" "
                else:
                    if(split_phrase[0].lower()==line_split[i].lower()):
                        phrase_index=1
                        phrase_found=line_split[i].lower()
                    else:
                        phrase_index=0
                        phrase_found=""

                #check for completion of entire phrase
                if ((len(split_phrase)-0)==phrase_index):
                    #lookto see if.... phrase_array already contains it if so increment
                    if (len(phrase_array)==0):
                        phrase_array=[[phrase_found,1]]
                    else:
                        located_phrase=0
                        for x in range(len(phrase_array)) :
                            if (phrase_array[x][0]==phrase_found    ):
                                phrase_array[x][1]=phrase_array[x][1]+1
                                located_phrase=1
                        if(located_phrase==0):
                            phrase_array.append([phrase_found,1])
                    phrase_index=0
                    phrase_found=""

            next_line=source_file.readline()

        return phrase_array








print("----------------------------------------")
print("|                                      |")
print("|  Press 1 to enter a file to be read  |")
print("|  Press 2 to use defaults             |")
print("|                                      |")
print("----------------------------------------")

source_file_choice=input("")


if (source_file_choice=="1"):
    source_file_main=input("Please enter your input file \n")
    lettercounter=FrequencyCounter(source_file_main)
else:
    lettercounter=FrequencyCounter("test.txt")

print("------------------------------------")
print("|                                  |")
print("|  Press 1 for letter comparisons  |")
print("|  Press 2 for letter guesses      |")
print("|  Press 3 for word frequency's    |")
print("|  Press 4 for quote finder        |")
print("|  Press 5 to search a phrase      |")
print("|                                  |")
print("------------------------------------")

operation=input("")


if (operation=="1"):
    lettercounter.print_frequency(lettercounter.char_frequency      )

if (operation=="2"):

    lettercounter.print_frequency(lettercounter.char_frequency)
    lettercounter.compare_alphabet()
    lettercounter.guess_all()



if(operation=="3"):
    sort_type=input("Press 1 to use a frequency based descending sort\nPress 2 to use a frequency based ascending sort\nPress 3 to use a alphabetical sort\n")
    if(sort_type=="2"):
        lettercounter.sort_words(2)
    if(sort_type=="1"):        
        lettercounter.sort_words(1)
    if(sort_type=="3"):
        lettercounter.sort_words(3)
    lettercounter.print_frequency(lettercounter.word_frequency)

#quote frequency
if(operation=="4"):
    lettercounter.print_frequency(lettercounter.quote_frequency)

# phrase frequency
if(operation=="5"):
    lettercounter.print_frequency(lettercounter.phrase_frequency)


# print(chr(40960))
# print(chr(3972))
# print("\u20ac")


# greek="ἀλλ᾽ ἡμῖν εἷς θεὸς ὁ πατήρ ἐξ οὗ τὰ πάντα καὶ ἡμεῖς εἰς αὐτόν καὶ εἷς κύριος Ἰησοῦς Χριστός δι᾽ οὗ τὰ πάντα καὶ ἡμεῖς δι᾽ αὐτοῦ"


# print(greek)


# source for greek :
# http://www.greekbible.com/index.php
