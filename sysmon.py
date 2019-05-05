import sys
import psutil

def cpuinfo ():
    cpu=psutil.cpu_times(percpu=False)
    return cpu

def memory ():
    mem = psutil.virtual_memory()
    return mem

def swap ():
    swap=psutil.swap_memory()
    return swap

def proc ():
    procarr = list()
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
	procarr.append(proc.info)
    return(procarr)

cpudata = cpuinfo()
memdata = memory()
swapdata = swap()
procdata = proc()

if __name__ == "__main__" :
    if len(sys.argv) == 1 :
	print("Use help to see availaable parameters of script")
    elif sys.argv[1] == "cpuinfo" :
	print "CPU times\n"+\
	      "cpu.idle:   %f\n" % (cpudata.idle)+\
    	      "cpu.user:   %f\n" % (cpudata.user)+\
    	      "cpu.guest:  %f\n" % (cpudata.guest)+\
    	      "cpu.iowait: %f\n" % (cpudata.iowait)+\
    	      "cpu.nice:   %f\n" % (cpudata.nice)+\
    	      "cpu.system: %f\n" % (cpudata.system)
    elif sys.argv[1] == "meminfo" :
	print "System memory usage\n"+\
    	      "memory.total:  %f\n" % (memdata.total/1024/1024) +\
    	      "memory.used:   %f\n" % (memdata.used/1024/1024) +\
    	      "memory.free:   %f\n" % (memdata.free/1024/1024) +\
    	      "memory.shared: %f\n" % (memdata.shared/1024/1024)
    elif sys.argv[1] == "swapinfo" :
	print "Swap info\n"+\
    	      "swap.total: %f\n" % (swapdata.total/1024/1024)+\
    	      "swap.used: %f\n" % (swapdata.used/1024/1024)+\
    	      "swap.free %f\n" % (swapdata.free/1024/1024)
    elif sys.argv[1] == "procinfo" :
	for row in procdata:
	    print(row)
    elif sys.argv[1] == "help" :
	print ("\
 cpuinfo - this parameter show cpu times info\n \
memifo - this parameter show memory info\n \
swapinfo - this parameter show swap info\n \
procinfo - this parameter show running procesess in host system\n \
help - use this for show this menu \
	      ")
