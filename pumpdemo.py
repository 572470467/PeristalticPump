from pump import PeristalticPump
import sys
num=int(sys.argv[1])
if __name__ == '__main__':
    t=PeristalticPump(4,17,27)
    t.burst(num)

