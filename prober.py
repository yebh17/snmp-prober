#!/usr/bin/python
from easysnmp import Session,exceptions
from time import time,sleep
import sys

def main(argv):
    if len(argv) == 4:
        print("arguments length passes")
        sys_var = argv[0].split(':')
        if len(sys_var) == 3:
            agent_ip = sys_var[0]
            port= int(sys_var[1])
            community = sys_var[2]
            sample_freq = float(argv[1])
            samples = int(argv[2])
            oid = ['1.3.6.1.2.1.1.3.0'] 
            oid +=  argv[3:]
            snmp_prober(agent_ip,port,community,sample_freq,samples,oid)
        else:
            print("Invalid System details <Agent_Ip:Port:Community>",len(sys_var))
            sys.exit()
    else:
        print("Invalid Input Format",len(argv))
        sys.exit()
    

def snmp_prober(agent_ip,port,community,sample_freq,samples,oid):
    interval = 1.0/sample_freq
    previous = []
    current = []
    temp = 0
    timeout = 0
    reboots = 0
    session = Session(hostname=agent_ip,remote_port=port,community=community,version=2)
    previous_time = 0
    rates = []
    while(temp<samples):
        request_time = time()
        try:
            print("oid type<<<<<<<<<<<<<<",type(oid))
            current = session.get(oid)
            print("<<<<<current",current)

        except exceptions.EasySNMPTimeoutError:
            temp += 1
            timeout += 1
            continue
        resptime = time()

            

    print(agent_ip,port,community,sample_freq,samples,oid) 

if __name__ == "__main__":
   main(sys.argv[1:])
