import sys
import re
import os

def fio_test(model):
    sh= os.popen("fio --rw=%s --ioengine=libaio --direct=1 --directory=/fio_test --size=32g --bs=16m --name=iotest" %(model))
    output= sh.read()
    print(output)
    return output

print("\033[0;33;40mfio_test\033[0m")
print("\033[0;33;40m硬盘顺序读测试\033[0m")

file = open('fio_shunxu.txt', 'a')
file.write("硬盘顺序读测试\n")
output1=fio_test("read")
file.write(output1)

print("\033[0;33;40m硬盘顺序写测试\033[0m")
file.write("硬盘顺序写测试\n")
output2=fio_test("write")
file.write(output2)
file.close()

print("\033[0;33;40m硬盘随机读测试\033[0m")
file = open('fio_suiji.txt', 'a')
file.write("硬盘随机读测试\n")
output3=fio_test("randread")
file.write(output3)

print("\033[0;33;40m硬盘随机写测试\033[0m")
file.write("硬盘随机写测试\n")
output4=fio_test("randwrite")
file.write(output4)

file.close()

os.popen("cd /fio_test")
os.popen("rm -f iotest.0.0")
