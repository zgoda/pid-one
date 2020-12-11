import os


def get_pname(pid: int) -> str:
    with open(f'/proc/{pid}/cmdline') as fp:
        data = fp.read()
    sep = '\x00' if data.endswith('\x00') else ' '
    if data.endswith(sep):
        data = data[:-1]
    cmdline = data.split(sep)
    if sep == '\x00' and len(cmdline) == 1 and ' ' in data:
        cmdline = data.split(' ')
    return ' '.join(cmdline)


def main():
    pid = os.getpid()
    proc_one = get_pname(1)
    print(f'I am PID {pid}, PID 1 is {proc_one}')


if __name__ == '__main__':
    main()
