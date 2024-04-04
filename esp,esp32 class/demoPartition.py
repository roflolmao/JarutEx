#############################################################
# demoPartition.py
# (C) 2021, JarutEx
# https://www.jarutex.com
#############################################################
import esp32

def showPartitionInfo( x ):
    part = esp32.Partition(x)
    info = part.info()
    print("Partition information")
    printPartitionInfo(info)
    print("    Number of blocks {}".format(part.ioctl(4,...)))
    print("    block size ..: {} byte(s)".format(part.ioctl(5,...)))
    
def printPartitionInfo( info ):
    print("    Name ........: {}".format(info[4]))
    print("    Type ........: {}".format(info[0]))
    print("    SubType .....: {}".format(info[1]))
    print("    Address .....: {}".format(info[2]))
    print("    Size  .......: {} Bytes".format(info[3]))
    print("    Encrypted ...: {}".format(info[5]))
    
def showPartitions():
    partApp = esp32.Partition.find(type=esp32.Partition.TYPE_APP)
    partData = esp32.Partition.find(type=esp32.Partition.TYPE_DATA)
    print("APP Partition ({})".format(len(partApp)))
    for i in range(len(partApp)):
        print("  {}.{}".format(i+1,partApp[i]))
        printPartitionInfo(partApp[i].info())
        print("    Number of blocks {}".format(partApp[i].ioctl(4,...)))
        print("    block size ..: {} byte(s)".format(partApp[i].ioctl(5,...)))
    print("DATA Partition ({})".format(len(partData)))
    for i in range(len(partData)):
        print("  {}.{}".format(i+1,partData[i]))
        printPartitionInfo(partData[i].info())
        print("    Number of blocks {}".format(partData[i].ioctl(4,...)))
        print("    block size ..: {} byte(s)".format(partData[i].ioctl(5,...)))
    
showPartitions()
showPartitionInfo( "nvs" )
running = esp32.Partition(esp32.Partition.RUNNING)
print("esp32.Partition.RUNNING")
printPartitionInfo(running.info())
try:
    nextRunning = running.get_next_update()
except:
    print("No next update!")
