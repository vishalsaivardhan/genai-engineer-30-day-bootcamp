class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for character in s:
            if character.isalnum():
                cleaned += character
        return cleaned == cleaned[::-1]