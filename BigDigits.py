# Michael Dvořák
# Python_3.7.0

Zero = """\
         ***     
        *   *    
       *     *   
       *     *   
       *     *   
        *   *    
         ***     
        """

One = """\
          *      
         **      
        * *      
          *      
          *      
          *      
         ***      
        """

Two = """\
         *** 
        *   *
        *  * 
          *
         *
        *
        *****
        """

Three = """\
         *** 
        *   *
            *
          ** 
            *
        *   *
         ***
          """

Four = """\
           *
          **
         * *
        *  *
       ******
           *
           *
           """

Five = """\
        *****
        *
        *
         ***
            *
        *   *
         ***
         """

Six = """\
         ***
        *
        *
        ****
        *   *
        *   *
         ***
        """

Seven = """\
         *****
             *
            * 
           *
          *
          *
          *
        """

Eight = """\
         ***
        *   *
        *   *
         ***
        *   *
        *   *
         ***
        """

Nine = """\
         ****
        *   *
        *   *
         ****
            *
            *
            *
            """

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

print("Enter a number: ")
x = input()
for i in x:
    print(Digits[int(i)])
                                
