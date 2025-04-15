def is_palindrome(texto):
    limpio = ""
    for char in texto:
        if char.isalpha():
            limpio += char.lower()

    if len(limpio) <= 1:
        return True
    
   
    if limpio[0] == limpio[-1]:  
        return True
    return False
