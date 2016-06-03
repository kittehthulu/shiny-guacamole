from runner import Runner, runifmain, problemnumber

@runifmain(__name__)
@problemnumber(6)
class Problem6(Runner):

    def problem(self):
        s = range(1, 101)
        b = sum(s) ** 2
        a = sum(map(lambda x: x ** 2, s))
        return b - a