#!/usr/bin/python
import sys
from easysnmp import Session,exceptions

def main(argv):
    if len(argv) == 4:
        print("arguments length passes")
        sys_var = argv[0].split(':')
        if len(sys_var) == 3:
            agent_ip = sys_var[0]
            port= sys_var[1]
            community = sys_var[2]
            sample_freq = argv[1]
            samples = argv[2]
            oid = argv[3]
            snmp_prober(agent_ip,port,community,sample_freq,samples,oid)
        else:
            print("Invalid System details <Agent_Ip:Port:Community>",len(sys_var))
            sys.exit()
    else:
        print("Invalid Input Format",len(argv))
        sys.exit()
    

def snmp_prober(agent_ip,port,community,sample_freq,samples,oid):
    previous = []
    current = []
    temp = 0
    previous_time = 0
    timeouts = 0
    rebbots = 0
        
    print(agent_ip,port,community,sample_freq,samples,oid) 

if __name__ == "__main__":
   main(sys.argv[1:])
