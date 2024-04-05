import time
import sys
from machine import DAC, Pin, freq
import gc

gc.enable()
gc.collect()
freq(240000000)

dacPin1 = Pin(25) # ต่อกับลำโพง
dacPin2 = Pin(26) # ต่อกับ adcPin1

dac1 = DAC( dacPin1 )
dac2 = DAC( dacPin2 )

def playWavFile( fName ):
    monoFile = open(fName,"rb")
    mark = monoFile.read(4)
    if (mark != b'RIFF'):
        print("ไม่ใช้ WAV!")
        monoFile.close()
        sys.exit(1)
    fileSize = int.from_bytes(monoFile.read(4),"little")
    print("File size = {} bytes".format(fileSize))
    fileType = monoFile.read(4)
    if (fileType != b'WAVE'):
        print("ไม่ใช้ WAV!!")
        monoFile.close()
        sys.exit(2)

    chunk = monoFile.read(4)
    lengthFormat = 0
    audioFormat = 0
    numChannels = 0
    sampleRate = 0
    byteRate = 0
    blockAlign = 0

    if (chunk == b'fmt '):
        lengthFormat = int.from_bytes(monoFile.read(4),"little")
        audioFormat = int.from_bytes(monoFile.read(2),"little") 
        numChannels = int.from_bytes(monoFile.read(2),"little")
        sampleRate = int.from_bytes(monoFile.read(4),"little")
        byteRate = int.from_bytes(monoFile.read(4),"little") 
        blockAlign = int.from_bytes(monoFile.read(2),"little") 
        bitsPerSample = int.from_bytes(monoFile.read(2),"little")
    
        print("Length of format data = {}".format(lengthFormat))
        print("Audio's format = {}".format(audioFormat))
        print("Number of channel(s) = {}".format(numChannels))
        print("Sample rate = {}".format(sampleRate))
        print("Byte rate = {}".format(byteRate))
        print("Block align = {}".format(blockAlign))
        print("Bits per sample = {}".format(bitsPerSample))
        
        minValue = 255
        maxValue = 0
    
        chunk = monoFile.read(4)
        if (chunk != b'data'):
            print("ไม่ใช้ WAV!!!!")
            monoFile.close()
            sys.exit(5)
        dataSize = int.from_bytes(monoFile.read(4),"little")
        print("Data size = {}".format(dataSize))
        if (bitsPerSample > 8):
            print("ไม่รองรับข้อมูลที่มากกว่า 8 บืต")
            monoFile.close()
            sys.exit(6)
        buffer = monoFile.read(dataSize)
        # find min/max
        for i in range(len(buffer)):
            if (buffer[i] > maxValue):
                maxValue = buffer[i]
            if (buffer[i]<minValue):
                minValue = buffer[i]
        # normalize
        xScale = 255.0/(maxValue-minValue)
        # play
        tm = int(1000000/sampleRate)
        for i in range(len(buffer)):
            data = int(((buffer[i]-minValue)*xScale))
            dac1.write( data )  
            time.sleep_us(tm)
        print("---------------------------")
    
    if (audioFormat != 1):
        print("ไม่รองรับกรณีที่ไม่ใช้ PCM!!!")
        monoFile.close()
        sys.exit(3)
    monoFile.close()
    dac1.write( 0 )
    
############### main program
playWavFile("/mono.wav")
time.sleep_ms(1000)
playWavFile("/mono2.wav")
time.sleep_ms(1000)
