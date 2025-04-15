def is_palindrome(texto):
    limpio = ""
    for char in texto:
        if char.isalpha():
            limpio += char.lower()