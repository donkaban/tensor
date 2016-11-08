import sys
import os
import subprocess
import datetime

_COL_TBL = {
    '@W': '\033[97m',  # white
    '@R': '\033[91m',  # lt red
    '@Y': '\033[93m',  # lt yellow
    '@G': '\033[92m',  # lt green
    '@C': '\033[96m',  # lt cyan
    '@B': '\033[94m',  # lt blue
    '@P': '\033[95m',  # lt purple
    '@D': '\033[37m',  # lt gray
    '@d': '\033[90m',  # gray'
    '@r': '\033[31m',  # red
    '@y': '\033[33m',  # yellow
    '@g': '\033[32m',  # green
    '@c': '\033[36m',  # cyan
    '@b': '\033[34m',  # blue
    '@p': '\033[35m',  # purple

}


class logger(object):
    def __init__(self, tag):
        self.tag = str(tag)

    @staticmethod
    def fmt(msg):
        for c in _COL_TBL:
            if c in msg:
                msg = msg.replace(c, _COL_TBL[c])
                end_l = '\033[0m'
        return msg + end_l

    def raw(self, msg, endl='\n'):
        sys.stdout.write(self.fmt(msg) + endl)
        sys.stdout.flush()

    def prn(self, msg, prefix='> ', endl='\n'):
        msg = '%s [%s][%s] %s%s' % (prefix, datetime.datetime.now().strftime('%H:%M:%S'), self.tag, msg, endl)
        sys.stdout.write(self.fmt(msg))
        sys.stdout.flush()

    def nfo(self, msg, endl='\n'):
        self.prn(msg, prefix='@cI ', endl=endl)

    def wrn(self, msg, endl='\n'):
        self.prn(msg, prefix='@yW ', endl=endl)

    def err(self, msg, endl='\n'):
        self.prn(msg, prefix='@rE ', endl=endl)

    def dbg(self, msg, endl='\n'):
        self.prn(msg, prefix='@dD ', endl=endl)

    def fatal(self, msg, endl='\n'):
        self.prn(msg, prefix='@rF ', endl=endl)
        raise RuntimeError(self.fmt(msg))

    @staticmethod
    def get(tag):
        return logger(tag)


def zcall(cmd, col='@d', log_prefix='', return_ret_code=False):
    def out_adapt(msg, col):
        if msg == '':
            return

    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            env=os.environ.copy())

    std_iterator = iter(proc.stdout.readline, b"")
    err_iterator = iter(proc.stderr.readline, b"")
    while proc.poll() is None:
        for line in std_iterator:
            log.dbg(log_prefix + col + line, endl='')
        for line in err_iterator:
            log.err(log_prefix + col + line, endl='')

    if return_ret_code:
        return proc.returncode
    return proc.returncode == 0




if __name__ == '__main__':
    import time

    log = logger.get('LOG')
    log.prn('@rRED @p PURPLE @y YELLOW @gGREEN @c CYAN @b BLUE @d DARK ')
    log.prn('@RRED @P PURPLE @Y YELLOW @GGREEN @C CYAN @B BLUE @D DARK ')

    log.dbg('It is debug message')
    log.nfo('It is info  message')
    log.wrn('It is warn  message')
    log.err('It is error message')

    zcall('ls -la')
    zcall('git status')
