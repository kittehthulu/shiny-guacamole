from runner import Runner, runifmain, problemnumber

@runifmain(__name__)
@problemnumber(9)
class Problem9(Runner):

    def problem(self):
        for a in xrange(1, 1000):
            for b in xrange(a, 1000):
                for c in xrange(b, 1000):
                    pt = a ** 2 + b ** 2
                    if pt == c ** 2:
                        if a + b + c == 1000:
                            return a * b * c
        return -1