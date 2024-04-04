# demoExp.py
# 2021-007-15 by JarutEx (https://www.jarutex.com)
import esp
print("> Class ..................: {}".format(esp.__name__))
print("> Firmware checking ......:");
print("validate :{}".format(esp.check_fw()))
print("> Flash ID ...............: {}".format(esp.flash_id()))
print("> Flash size .............: {}".format(esp.flash_size()))
print("> Flash User Start .......: {}".format(esp.flash_user_start()))
print("> memory infoamtion ......: {}".format(esp.meminfo()))
print("> Memory allocation ......:")
print("     before malloc 4KB ...: {} Bytes".format(esp.freemem()))
x = esp.malloc(4096)
print("     location of x .......: {}".format(x))
print("     after malloc 4KB ....: {} Bytes".format(esp.freemem()))
esp.free(x)
print("     after free ..........: {} Bytes".format(esp.freemem()))
x = esp.malloc( esp.freemem() + 1 )
if (x == 0):
    print("Not enough memory!!!")
