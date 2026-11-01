class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D = s.lower()
        T = t.lower()

        if len(T) != len(D):
            return False

        T = list(T)

        for i in range(len(D)):
            found = False
            for j in range(len(T)):
                if D[i] == T[j]:
                    T.pop(j)
                    found = True
                    break
            if not found:
                return False

        return True
