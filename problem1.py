from runner import Runner, runifmain, problemnumber

@runifmain(__name__)
@problemnumber(1)
class Problem1(Runner):

    def problem(self):
        answer = 0
        for i in xrange(0, 1000):
            if i % 3 == 0:
                answer += i
            elif i % 5 == 0:
                answer += i
        return answer