class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordList=set(wordList)
        visited = set([beginWord])
        q = deque([[beginWord,1]])
        while q:
            w,l=q.popleft()
            if w == endWord:
                return l
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqgrstuvwxyz':
                    nextWord = w[:i] + c + w[i+1:]
                    if nextWord in wordList and nextWord not in visited:
                        visited.add(nextWord)
                        q.append([nextWord,l+1])
            
        return 0
            



        
