import atexit
import multiprocessing
import random
import signal
import sys
import time

procs = set()


def vm_exit_handler():
    print('Cleanup on VM shutdown')
    time.sleep(1)
    print('VM cleaned, bye')


def _handler(signum: int):
    sig = signal.strsignal(signum) or signum
    print(f'Got signal {sig}, will handle it now')
    time.sleep(1)


def handle_term(signum, frame):
    _handler(signum)
    print('Terminating spawned processes')
    for p in procs:
        p.terminate()
    print("Now I'm good to go")
    sys.exit(0)


def handle_abort(signum, frame):
    _handler(signum)
    print('Aborting execution')


def do_work(num):
    while True:
        wrk_sec = random.randint(2, 4)  # noqa: DUO102
        print(f'Worker {num} doing work for {wrk_sec} seconds')
        time.sleep(wrk_sec)
        print(f'Worker {num} work done')
        time.sleep(1)


if __name__ == '__main__':
    print('Me and my workers we are at your service')
    time.sleep(1)
    for n in range(4):
        p = multiprocessing.Process(name=f'worker-{n}', target=do_work, args=(n, ))
        procs.add(p)
        p.start()
    atexit.register(vm_exit_handler)
    signal.signal(signal.SIGTERM, handle_term)
    signal.signal(signal.SIGABRT, handle_abort)
    for p in procs:
        p.join()
