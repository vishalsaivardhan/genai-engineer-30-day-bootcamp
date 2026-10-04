class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for x in range(1,n+1):
            temp = ""
            if x % 3 ==0 and x % 5 == 0:
                temp = "FizzBuzz"
            elif x % 3==0:
                temp = "Fizz"
            elif x % 5 == 0:
                temp = "Buzz"
            else:
                temp = str(x)
            answer.append(temp)
        return answer