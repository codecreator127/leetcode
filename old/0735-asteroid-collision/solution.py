from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)

            else:
                while True:
                    peek = stack[-1]
                    if peek < 0:
                        stack.append(ast)
                        break
                    elif peek == -ast:
                        stack.pop()
                        break
                    elif peek > -ast:
                        break
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(ast)
                            break
        return stack
