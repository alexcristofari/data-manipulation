def PalindromeCreator(strParam):
    # __define-ocg__ - Check if string is already a palindrome or can become one
    varFiltersCg = strParam
    
    def is_palindrome(s):
        return s == s[::-1]
    
    if is_palindrome(strParam):
        return "palindrome"
    
    n = len(strParam)
    
    for i in range(n):
        new_str = strParam[:i] + strParam[i+1:]
        if len(new_str) >= 3 and is_palindrome(new_str):
            varOcg = strParam[i]
            return varOcg
    
    for i in range(n):
        for j in range(i+1, n):
            new_str = strParam[:i] + strParam[i+1:j] + strParam[j+1:]
            if len(new_str) >= 3 and is_palindrome(new_str):
                varOcg = strParam[i] + strParam[j]
                return varOcg
    
    varOcg = "not possible"
    return varOcg

if __name__ == "__main__":
    print(PalindromeCreator("abjchba"))  # Output: jc