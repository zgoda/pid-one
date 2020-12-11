import atexit
import signal
import sys
import time


def bye():
    print('End of the world')


def signal_handler(signum, stack):
    print(f'Got signal {signum}, I have to go')
    time.sleep(2)
    print('All cleaned up, bye')
    sys.exit(0)


def main():
    print('I am at your service')
    time.sleep(1)
    while True:
        print('Working hard for 2 seconds')
        time.sleep(2)


if __name__ == '__main__':
    atexit.register(bye)
    signal.signal(signal.SIGTERM, signal_handler)
    main()
