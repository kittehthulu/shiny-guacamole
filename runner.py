import time
import traceback

class Runner(object):

    def problem(self):
        pass

    def run(self):
        try:
            answer = self.problem()
            print 'Answer for problem %s: %s' % (self.number, answer)
        except:
            print 'Error in Problem %s.' % self.number
            print traceback.format_exc()

def runifmain(mainname):
    def deco(clas):
        a = time.time()
        if mainname == '__main__':
            clas().run()
        b = time.time()
        print 'Ran in %s seconds.' % (b - a)
        return clas
    return deco

def problemnumber(num):
    def decorator(clas):
        setattr(clas, 'number', num)
        return clas
    return decorator
