from runner import Runner, runifmain, problemnumber

@runifmain(__name__)
@problemnumber(14)
class Problem14(Runner):

    def problem(self):
        collatz = {}
        max_chain = -1
        max_index = 1
        for x in xrange(1, int(1e1)):
            chain = self.getChain(collatz, x)
            if len(chain) > max_chain:
                max_chain = len(chain)
                max_index = x
        return max_index

    def getChain(self, collatz, n):
        if n == 1:
            collatz[1] = [1]
        else:
            if n not in collatz:
                chainL = self.getChain(collatz, self.f(n))
                collatz[n] = chainL[::]
                collatz[n].append(n)
        return collatz[n]

    def f(self, n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1