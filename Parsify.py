# Notes:
    #Non ascii characters
        # [^\x00-\x7F]+

    #Cyrillic alphabets with normal(english)
        # ^[A-Za-z.!@?#"$%&:;() *\+,\/;\-=[\\\]\^_{|}<>\u0400-\u04FF]*$
    
    #Cyrillic
        # [a-z\u0400-\u04FF]
        # [ЁёА-я]
    
    #Blank lines
        # \n\s

    #Lines start with anything other than an english letter
        #\n\W

    #Can we export pdf and maintain Bold font? This would save a TON of editing so each term entry can be formatted to have it's own line, and any line not starting with bold
        #will fall onto the same line as the term until final editing      
    
    #This character '۞' appears >10k times but is not consistent throughout document (at the end of Russian definition to easily be cut out)

def Page_markers(Text_Lines):
    """" Remove identified page markers

        Current symbol =
    
    """

def Fix_Hyphens(Text_Lines):
    """Remove end of line hyphenated words
        Example:

        
        Some lines have a space after '-'
        Example2:

        Desired:
    
    """

def Term_delimiter(Text_Lines):
    """Replace pronounciation string with delimiter '@' after manual review to remove/modify entries with '@'
        ^another unique delimiter if preferred.  Chosen for easily identifiable delimiter

        Example:


        Replace '(\[.*?\])' with '@'
            Need to add expression to identify where [] is multi-line
        
        Desired:
    
    """

def Remove_parts_of_speech(Text_Lines):
    """Remove parts of speech indicators in text
        Example:

        Remove (adj\.|cj\.|n\.|num\.|pl\.|pref\.|pron\.|prop\.|prp\.|v\.)
            Need to add expression to exclude any of these which are preceeded by a character and not a space
    
    """

