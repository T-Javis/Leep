# -*- coding: utf-8 -*-
#!/usr/bin/python


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
    	print('000',s,l,r,s[l],s[r])
        l -= 1; r += 1
        #print('111',l,r,s[l],s[r])
        print('2222',s[l+1:r])
        print('-'*10)
    return s[l+1:r]


s='abeffebc'  #abcdefgfedcb
res=''
for i in range(len(s)):
	print('333',s,i,i)
	print('*'*10)

	tmp=helper(s,i,i)
	if len(tmp)>len(res):
		res=tmp
		print('444',res)
	
	print('777',s,i,i+1)
	tmp=helper(s,i,i+1)
	if len(tmp)>len(res):
		res=tmp
		print('555',res)
	print('-'*30)


class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in xrange(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

print Solution().longestPalindrome("abcdefgfedcb")
print Solution().longestPalindrome("abeffebc")


