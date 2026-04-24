# Recitation Activity 1
# Omotola AJAO
# Section 002R
# oaa5544@psu.edu

def translate(translation, msg):
    """
        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """     
    msg = msg.lower()
    words = msg.split()
    translated = []
    for word in words:
        if word in translation:
            translated.append(translation[word])
        else:
            translated.append(word)
    return " ".join(translated)










if __name__ == "__main__":
    import doctest
    doctest.testmod()