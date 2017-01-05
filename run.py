import sys
import time
from urwid import *
from subprocess import *

PIDS = []

def start_display(callback1, callback2):
    txt_ember = ListBox(SimpleListWalker([Text(u"Ember")]))
    txt_java = ListBox(SimpleListWalker([Text(u"Java")]))
    cols = Columns([txt_ember,txt_java], 1)
    loop = MainLoop(cols)
    loop.set_alarm_in(0.5, lambda l,y: callback1(l,txt_ember))
    loop.set_alarm_in(0.5, lambda l,y: callback2(l,txt_java))
    loop.run()
    for p in PIDS:
        if p.poll() == None:
            print 'killing '+p.pid
            p.kill()

def run(command, dir, log):
    return Popen(command, bufsize=1, stdout=log, stderr=log, cwd=dir)

def write_stream(loop, pane, s):
    for line in iter(s.readline, ''):
        pane.body.append(Text(line))
        pane.set_focus(pane.focus_position+1)
        # size = len(pane.contents)
        # pane.move_cursor_to_coords(size, 1, size-1)
    loop.set_alarm_in(0.5, lambda loop,y: write_stream(loop, pane, s))

def start():
    EFILE = 'kit_ember.log'
    JFILE = 'kit_java.log'
    elog = open(EFILE,'w')
    jlog = open(JFILE,'w')
    ember = run(['ember', 's'], 'frontend', elog)
    java = run(['bash','gradlew','--console=plain','bootRun'], 'base-server', jlog)
    PIDS = [ember,java]
    eout = open(EFILE)
    jout = open(JFILE)
    start_display(lambda loop,pane: write_stream(loop, pane, eout), lambda loop,pane: write_stream(loop, pane, jout))

def usage():
    print 'Usage: python run.py start/stop'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        command = sys.argv[1]
        if command == 'start':
            start()
        else:
            print 'Uknown command '+command
            usage()
