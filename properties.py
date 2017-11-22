a00=( '''
######################################################################
#  ______  _____                                   _   _             #
#  | ___ \/  __ \                                 | | (_)            #
#  | |_/ /| /  \/  _ __  _ __ ___  _ __   ___ _ __| |_ _  ___  ___   #
#  |  __/ | |     | '_ \| '__/ _ \| '_ \ / _ \ '__| __| |/ _ \/ __|  #
#  | |    | \__/\ | |_) | | | (_) | |_) |  __/ |  | |_| |  __/\__ \  #
#  \_|     \____/ | .__/|_|  \___/| .__/ \___|_|   \__|_|\___||___/  #
#                 | |             | |                                #
#                 |_|             |_|                                #
#                                                                    #
######################################################################



################{{{{coded by ismael al-safadi}}}}##################

''')
import getpass
c=getpass.getuser()
#before using this script you should install this librarys , by cmd.. just write the commands 1:cd/ then press enter 
#2:cd python27 then press enter  3:cd Scripts then press enter  4:pip install platform then press enter
# now platform installed
#Repeat the steps for (psutil ,socket  and subprocess )
def write_data(data):
        file_data="C:/Users/%s/Desktop/pr.txt" % c 
        m=open(file_data,'a')
        m.write(data)
        
     
import platform
import win32com.client
import os
import sys
import psutil
import time
import socket 
import subprocess
a0=('########################## system #########################')

a1=('system   :', platform.system())
a2=('node     :', platform.node())
a3=('release  :', platform.release())
a4=('version  :', platform.version())
a5=('machine  :', platform.machine())
a6=('processor:', platform.processor())

a7=('\n')
a8=('########################## cpu #########################')
percentc=psutil.cpu_percent()
a9=('the percent cpu used :',percentc)

a10=('Number of cpu in the processor :',(psutil.cpu_count()))
freq=psutil.cpu_freq()
current=freq.current
minn=freq.min
maxx=freq.max
a11=('*cpu frequency* ')
a12=('1:current :',current)
a13=('2:min :',minn)
a14=('3:max :',maxx)
state=(psutil.cpu_stats())
ctx_switches=state.ctx_switches
interrupts=state.interrupts
soft_interrupts=state.soft_interrupts
syscalls=state.syscalls
a15=('*cpu state*')
a16=('Context Switch:',ctx_switches)
a17=('interrupts:',interrupts)
a18=('software interrupts :' ,soft_interrupts)
a19=('syscalls:',syscalls)




a20=('########################## memory #########################')
memory=(psutil.virtual_memory())
total=memory.total
available=memory.available
used=memory.used
free=memory.free
percentm=memory.percent
a21=('the total memory :', (total))
a22=('the used memory :', (used))
a23=('the available memory :', (available))
a24=('the percent of using  memory :', (percentm),'%')


a26=('\n' )   
a27=('########################disk##########################')

disk=psutil.disk_usage('/')
totald=disk.total
usedd=disk.used
freed=disk.free
percentd=disk.percent
a28=('total disk size:',total)
a29=('used disk:',usedd)
a30=('free disk:',freed)
a31=('the percent disk used:',percentd,'%')

counters=psutil.disk_io_counters()
read_count=counters.read_count
write_count=counters.write_count
read_bytes=counters.read_bytes
write_bytes=counters.write_bytes
read_time=counters.read_time
write_time=counters.write_time

a32=('read counter:',read_count)
a33=('write counter:',write_count)
a34=('read bytes:',read_bytes)
a35=('write bytes:',write_bytes)
a36=('read time:',read_time)
a37=('write time:',write_time)
a38=('\n')
a39=('########################network##########################')

net=psutil.net_io_counters()
bytes_sent=net.bytes_sent
bytes_recv=net.bytes_recv
packets_sent=net.packets_sent
packets_recv=net.packets_recv
errin=net.errin
errout=net.errout
dropin=net.dropin
dropout=net.dropout
a40=('bytes sent',bytes_sent)
a41=('bytes recv',bytes_recv)
a42=('packets sent',packets_sent)
a43=('packets recv',packets_recv)
a44=('errin',errin)
a45=('errout',errout)
a46=('dropin',dropin)
a47=('dropout',dropout)
a48=('the local ip addr:',(socket.gethostbyname(socket.gethostname())))
a49=('\n')
a50=('########################battery##########################')

battery=psutil.sensors_battery()
percantb=battery.percent
secselfb=battery.secsleft
power_plugged=battery.power_plugged
a51=('percant of charging :',percantb,'%')

a52=('time left:',secselfb)
a53=('power plugged:',power_plugged)
a54=('\n')
a55=('########################services#########################')
a56=("*The service running now*")
processes= subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
a57=(processes)
data=[a00,a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13,a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a26, a27, a28, a29,a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46,a47, a48, a49, a50, a51, a52, a53, a54, a55, a56,a57]
for i in data:
        write_data(str(i)+'\n')
        
        
