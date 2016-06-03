from runner import Runner, runifmain, problemnumber
from utils import factors

@runifmain(__name__)
@problemnumber(12)
class Problem12(Runner):

    def problem(self):
        l = []
        n = 0
        while len(l) <= 500:
            n += 1
            s = n * (n + 1) / 2
            l = factors(s)
        return s