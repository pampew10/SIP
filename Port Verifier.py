import os

#Scans most common
nmap = "nmap 192.168.1.1"
nmapoutput = os.popen(nmap).read()
nmap2 = "nmap 192.168.2.1"
nmapoutput2 = os.popen(nmap).read()

nmapoutputarray = []
nmapoutputarray2 = []
unmatcheditems = []

lines = 0
lines2 = 0
for line in nmapoutput.splitlines():
    lines = lines + 1
    #if lines >= 6:
    if "port" in line:
        if "state" in line:
            if "service" in line:
                correctline = lines
    try:
        correctline
    except:
        print("not defined")
    else:
        if lines >= correctline:
            print(line)
            nmapoutputarray.append(line)

for line in nmapoutput2.splitlines():
    lines2 = lines2 + 1
    if "port" in line:
        if "state" in line:
            if "service" in line:
                correctline2 = lines2  
    try:
        correctline2
    except:
        print("not defined")
    else:
        if lines >= correctline2:
            print(line)
            nmapoutputarray2.append(line)

for i in nmapoutputarray:
    if i in nmapoutputarray2:
        print("No")
    else:
        unmatcheditems.append(i)
print(unmatcheditems)
