#Faisal 


import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)
print "Human Test!!..kot2 ni bot ler...manatahu"
print '\n'
test_text = input ("masukkan any number haa: ")
test_number = int(test_text)
print ("ni kan no yg you masukkan tadi: ", test_number)
print "tahniah ler, anda manusia ye bukan bot hihi"

print ' \n '
print "=" * 60
print "slmt dtg, ni asgmt hacking faisal guna scapy in python!!"
print "=" * 60


# Ask for input
print ' \n '
victimIP    = raw_input("masukkan IP target lerr: ")
victimServerIP  = socket.gethostbyname(victimIP)

# Print a nice banner with information
print ' \n '
print "-" * 60
print "tunggu jap, tgh scan open port ni", victimServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((victimServerIP, port))
        if result == 0:
            print "Port {}: 	 Open ni haaa".format(port)
        sock.close()

except KeyboardInterrupt:
    print "kau tekan Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "takleh connect ke target IP pun!!!"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ' \n'
print 'Scanning siap dalam masa: ', total
