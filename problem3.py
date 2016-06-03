from runner import Runner, runifmain, problemnumber

@runifmain(__name__)
@problemnumber(3)
class Problem3(Runner):

    def problem(self):
        max_value = -1
        for a in xrange(999, 99, -1):
            for b in xrange(999, 99, -1):
                v = a * b
                s = str(v)
                mid = len(s) / 2
                pal_a = s[:mid]
                pal_b = s[mid:]
                if pal_a == pal_b[::-1]:
                    max_value = max(v, max_value)
        return max_value
