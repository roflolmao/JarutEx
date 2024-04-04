# code11-1
import socket
import network
import esp
import time
import gc
import time
import machine as mc
servoL = mc.PWM(mc.Pin(5),freq=50)
servoR = mc.PWM(mc.Pin(4),freq=50)

def robotForward():
    global servoL,servoR
    servoL.duty(120)
    servoR.duty(40)

def robotStop():
    global servoL,servoR
    servoL.duty(0)
    servoR.duty(0)
    
def robotBackward():
    global servoL,servoR
    servoL.duty(40)
    servoR.duty(120)
    
def robotTurnRight():
    global servoL,servoR
    servoL.duty(120)
    servoR.duty(120)
    
def robotTurnLeft():
    global servoL,servoR
    servoL.duty(40)
    servoR.duty(40)

motionState = 0 # 0-Stop,1-Forward,2-Backward,3-TurnLeft,4-TurnRight

def webPage():
    global motionState
    html = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.button {  border: none;  color: white;  padding: 20px;  text-align: center;  text-decoration: none;
  display: inline-block;  font-size: 14
  px;  margin: 4px 2px;  cursor: pointer;  border-radius: 4%;
  width: 100%; height: 100%;
}
.button1 {  background-color: #3ABC40; }
.button2 {  background-color: #BC4040; }
</style></head><body><table>
"""
    if motionState == 0:
        html += """
<tr>
<td></td>
<td><a href='/?robot=forward'><button class='button button2'>Forward</button></a></td>
<td></td>
</tr>
<tr>
<td><a href='/?robot=left'><button class='button button2'>Turn Left</button></a></td>
<td><a href='/?robot=stop'><button  class='button button1'>Stop</button></a></td>
<td><a href='/?robot=right'><button class='button button2'>Turn Right</button></a></td>
</tr>
<tr>
<td></td>
<td><a href='/?robot=backward'><button class='button button2'>Backward</button></a></td>
<td></td>
</tr>
"""
    elif motionState == 1:
        html += """
<tr>
<td></td>
<td><a href='/?robot=forward'><button class='button button1'>Forward</button></a></td>
<td></td>
</tr>
<tr>
<td><a href='/?robot=left'><button class='button button2'>Turn Left</button></a></td>
<td><a href='/?robot=stop'><button  class='button button2'>Stop</button></a></td>
<td><a href='/?robot=right'><button class='button button2'>Turn Right</button></a></td>
</tr>
<tr>
<td></td>
<td><a href='/?robot=backward'><button class='button button2'>Backward</button></a></td>
<td></td>
</tr>
"""
    elif motionState == 2:
        html += """
<tr>
<td></td>
<td><a href='/?robot=forward'><button class='button button2'>Forward</button></a></td>
<td></td>
</tr>
<tr>
<td><a href='/?robot=left'><button class='button button2'>Turn Left</button></a></td>
<td><a href='/?robot=stop'><button  class='button button2'>Stop</button></a></td>
<td><a href='/?robot=right'><button class='button button2'>Turn Right</button></a></td>
</tr>
<tr>
<td></td>
<td><a href='/?robot=backward'><button class='button button1'>Backward</button></a></td>
<td></td>
</tr>
"""
    elif motionState == 3:
        html += """
<tr>
<td></td>
<td><a href='/?robot=forward'><button class='button button2'>Forward</button></a></td>
<td></td>
</tr>
<tr>
<td><a href='/?robot=left'><button class='button button1'>Turn Left</button></a></td>
<td><a href='/?robot=stop'><button  class='button button2'>Stop</button></a></td>
<td><a href='/?robot=right'><button class='button button2'>Turn Right</button></a></td>
</tr>
<tr>
<td></td>
<td><a href='/?robot=backward'><button class='button button2'>Backward</button></a></td>
<td></td>
</tr>
"""
    else:
        html += """
<tr>
<td></td>
<td><a href='/?robot=forward'><button class='button button2'>Forward</button></a></td>
<td></td>
</tr>
<tr>
<td><a href='/?robot=left'><button class='button button2'>Turn Left</button></a></td>
<td><a href='/?robot=stop'><button  class='button button2'>Stop</button></a></td>
<td><a href='/?robot=right'><button class='button button1'>Turn Right</button></a></td>
</tr>
<tr>
<td></td>
<td><a href='/?robot=backward'><button class='button button2'>Backward</button></a></td>
<td></td>
</tr>
"""
    html += "</table></body></html>"
    return html

# main program
if __name__ == '__main__':
    robotStop()
    ap = network.WLAN(network.AP_IF)
    ssid = 'JarutEx-AP'
    password = '123456789'
    ap.active(True)
    ap.config(essid=ssid, password=password)
    while ap.active() == False:
          pass
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        #print('conn {} from {}'.format(conn, addr))
        request = str(conn.recv(1024))
        #print('request = {}'.format(request))
        robotCmdStop = request.find('/?robot=stop')
        robotCmdForward = request.find('/?robot=forward')
        robotCmdBackward = request.find('/?robot=backward')
        robotCmdTurnLeft = request.find('/?robot=left')
        robotCmdTurnRight = request.find('/?robot=right')
        if robotCmdStop == 6:
            motionState = 0
            robotStop()
        if robotCmdForward == 6:
            motionState = 1
            robotForward()
        if robotCmdBackward == 6:
            motionState = 2
            robotBackward()
        if robotCmdTurnLeft == 6:
            motionState = 3
            robotTurnLeft()
        if robotCmdTurnRight == 6:
            motionState = 4
            robotTurnRight()
        response = webPage()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.send(response)
        conn.close() 
