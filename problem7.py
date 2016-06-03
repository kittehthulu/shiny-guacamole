from runner import Runner, runifmain, problemnumber
from utils import prime_generator

@runifmain(__name__)
@problemnumber(7)
class Problem7(Runner):

    def problem(self):
        prime_gen = prime_generator()
        for i in xrange(1, 10001):
            prime_gen.next()
        return prime_gen.next()