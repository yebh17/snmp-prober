		                                              NETWORK PERFORMANCE MONITORING

Description:

A script to probe an SNMP agent and find the rate of change for several counters between successive probes/ samples. The rate calculated for each counter/OID will be displayed on the console, one line for each calculated rate, the output format will be described in detail in 'output format'.

Futhermore, as the only requirement on the OIDs is that they are of the type COUNTER, this means that there are both 32 and 64 bit versions of counters. The solution handles both counter types, and in the case that a counter wraps (ie goes from a high number to a low number), the solution will address/rectify (if its possible).

The solution also handles  an SNMP agent restartings (i.e. the sysUpTime OID becomes less than it was before, ie. it starts counting from zero), and timeouts, i.e. the device does not respond to your request in time.

So, in an overall the solution maintains the requested sampling frequency (i.e. the requests from your solution will be sent so that the sampling frequency is maintained, irrespectively if the device has responded or not).

Note:
1.      The script runs with an SNMP library ‘easysnmp’ and so the script only runs on python2.7 version.

2.      If running on a Ubuntu 20.04 machine, you might get into errors with ‘python2.7’, ‘pip’ and ‘easysnmp’ installations. So you can follow the following pages in order to overcome them.

        a. https://linuxhint.com/install_python_pip_tool_ubuntu/ (For ‘python2.7’ and ‘pip’ installations)

        b. https://easysnmp.readthedocs.io/en/latest/ (For ‘easysnmp’ installation)

Requirements:
1.      easysnmp library (https://easysnmp.readthedocs.io/en/latest/)

2.      python2.7 version

3.      Agent IP and port number to probe

4.      Linux OS

5.      64-bit machine would be preferable

6.      Minimum 2GB RAM

Steps to run prober:
1.      cd /tmp/ (change directory to temporary directory in order to run the script temporarily and get deleted later)

2.      git clone https://github.com/yebh17/snmp-prober.git

3.      pip install easysnmp (Install easysnmp library, if already had it, skip it)

4.      /tmp/snmp-prober/prober Agent IP:port:community sample frequency samples OID1 OID2 …….. OIDn

•       (Agent IP: IP address of the agent you wanted to probe.)

•       (port: port number of the agent you wanted to probe.)

•       (Community: Usually ‘public’)

•       (sample frequency: Sampling frequency expressed in Hz, you can have it between 10 and 0.1 Hz.)

•       (samples: Number of successful samples the solution does before terminating, hence the value should be greater or equal to 2. If the value is -1 that means it runs forever (until CTRL-C is pressed, or the app is terminated in someway))

•       (OID: OIDs to be probed (they are absolute, cf. IF-MIB::ifInOctets.2 for interface 2, or 1.3.6.1.2.1.2.2.1.10.2 [1]))


Sample output:

$ /tmp/snmp-prober/prober Agent-IP:port:public 1 18 OID

1602942345 | 53526001

1602942346 | 53526001

1602942347 | 53526001

1602942348 | 53526001

1602942349 | 53526001

1602942350 | 53526001

1602942351 | 53526001

1602942352 | 53526001

1602942353 | 53526001

1602942354 | 53526001

1602942355 | 53526001

1602942356 | 53526001

1602942357 | 53526001

1602942358 | 53526001

1602942359 | 53526001

1602942360 | 53526001

1602942361 | 53526001

1602942362 | 53526001



