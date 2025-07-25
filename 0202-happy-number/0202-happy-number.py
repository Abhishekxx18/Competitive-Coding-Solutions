class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            total = 0
            while n:
                rem = n % 10
                total += rem * rem
                n //= 10
            if total == 1:
                return True
            if total in visited:
                return False
            visited.add(total)
            n = total
            
