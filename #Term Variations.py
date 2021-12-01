#Term Variations

#Hopefully this can be used to create a pattern by complexity level

def Complexity_1(Text_Lines):
    """ EN = RU
        Examples:
        abbreviate['bri:vıeıt] v. сокращать
        abbreviated text ['bri:vıeıtıdtekst]сокращенный текст
        

        Output:
        abbreviate @ сокращать
        abbreviated text @ сокращенный текст
    
    """

def Complexity_2(Text_Lines):
    """ EN = RU + RU

        Examples:
        abatement['beıtmnt] n.1. уменьшение; ослабление
        abandonment ['bændnmnt] n.отмена, отказ
        accepted [k'septıd] adj.1.принятый; 2. допущенный

        Output:
        abatement @ уменьшение
        abatement @ ослабление
        abandonment @ отмена
        abandonment @ отказ
        accepted @ принятый
        accepted @ допущенный
    """

def Complexity_3(Text_Lines):
    """ EN = RU + POS + num + RU
        Examples:
        acceptor[k'sept] n.1. акцептор; получатель сообщения; 2. резонансный контур
        
        Output:
        acceptor @ акцептор
        acceptor @ получатель сообщения
        acceptor @ резонансный контур
    """

def Complexity_4(Text_Lines):
    """ EN = RU + ()
        Examples:
        access holes['ækseshoulz] монтажные окна (многослойной печатной пла-ты)


        Output:
        access holes @ монтажные окна
    """

def Complexity_5(Text_Lines):
    """EN - RU + См.(see)|См. тж. (See also) EN
        Examples:
        access matrix ['ækses'meıtrıks] матрица права доступа. См. authorization matrix
        access number ['ækses'nmb] номер доступа.۞Номер телефона, исполь-зуемый абонентом подписчиком для получения к онлайновой службе. См. тж. ISP, online service

        Output:
        access matrix @ матрица права доступа
        access number @ номер доступа
    """
    
def Complexity_6(Text_Lines):
    """
        Examples:
        

        Output:
    
    """