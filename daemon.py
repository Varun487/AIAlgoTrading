import sys, os

def main(  ):
    """ An example daemon main routine; writes a datestamp to file
        /tmp/daemon-log every 10 seconds.
    """
    import time

    f = open("/tmp/daemon-log", "w")
    #f1 = open("/home/samrudhi/CapstoneProject_AITradingPlatform/hi.py", "r")
    with open("/home/samrudhi/CapstoneProject_AITradingPlatform/hi.py", 'r') as f1:
        text = f1.read()
    while 1:
        
        f.write('%s\n' % text)
        f.flush(  )
        time.sleep(10)

if __name__ == "__main__":
    # Do the Unix double-fork magic; see Stevens's book "Advanced
    # Programming in the UNIX Environment" (Addison-Wesley) for details
    try:
        pid = os.fork(  )
        if pid > 0:
            # Exit first parent
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (
            e.errno, e.strerror)
        sys.exit(1)

    # Decouple from parent environment
    os.chdir("/")
    os.setsid(  )
    os.umask(0)

    # Do second fork
    try:
        pid = os.fork(  )
        if pid > 0:
            # Exit from second parent; print eventual PID before exiting
            print "Daemon PID %d" % pid
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (
            e.errno, e.strerror)
        sys.exit(1)

    # Start the daemon main loop
    main(  )