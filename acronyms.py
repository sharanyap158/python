# check if a string is acronym of words
'''
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

 

Example 1:

Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 
'''
def isAcronym(words, s):
    inp1=''.join(inp2[0] for inp2 in words) 
    return inp1== s
inputs=input()
words =inputs.strip().split()
s= input()
print(isAcronym(words, s))
