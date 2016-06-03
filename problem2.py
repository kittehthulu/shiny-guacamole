from runner import Runner, runifmain, problemnumber
from utils import fibo_generator

@runifmain(__name__)
@problemnumber(2)
class Problem2(Runner):

    def problem(self):
        answer = []
        fibogen = fibo_generator()
        fibo = fibogen.next()
        while fibo < 4e6:
            if fibo % 2 == 0:
                answer.append(fibo)
            fibo = fibogen.next()
        return sum(answer)