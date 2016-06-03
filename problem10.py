from runner import Runner, runifmain, problemnumber
from utils import prime_generator

@runifmain(__name__)
@problemnumber(10)
class Problem10(Runner):

    def problem(self):
        prime_gen = prime_generator()
        prime = prime_gen.next()
        answer = 0
        while prime < 2e6:
            answer += prime
            prime = prime_gen.next()
        return answer
