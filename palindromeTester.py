#testPalindrome = input("Input word or phrase that may be a palindrome: ")
#testInverse = testPalindrome [::-1]
#print(testInverse)
#if testPalindrome == testInverse:
    #print(testPalindrome + " is a palindrome.")
#else:
    #print(testPalindrome + " is not a palindrome.")
#This code works for single words. For phrases we'll need something different.
palindromePhrase = input("Input phrase that may be a palindrome: ")
palindromePhrase = palindromePhrase.lower()
def remove(palindromePhrase):
    return palindromePhrase.replace(" ","")
palindromePhrase = remove(palindromePhrase)
palindromeTest = palindromePhrase [::-1]
if palindromeTest != palindromePhrase:
    print(palindromeTest + " is not a palindrome.")
else:
    print(palindromeTest + " is a palindrome.")