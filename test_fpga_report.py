import os
import sys
import openpyxl
import re

filepath = sys.argv[1]


# filepath='../../test'


if filepath=="-h"or filepath=="--help":
    print("\033[0;33;40mpython3 main.py model_url loop\033[0m")
    print("\033[0;33;40meg:python3 main.py ../model/ 1000\033[0m")
    print("\033[0;33;40m报告生成在test_fpga_result文件夹中\033[0m")
else:
    loop = sys.argv[2]
    dirname = os.listdir(filepath)
    os.popen("mkdir test_fpga_result")
    # 模型名称文件
    file = open('test_fpga_result/mode_name.txt', 'w')
    for i in range(0, len(dirname)):
        s = str(dirname[i]).replace('[', '').replace(']', '')
        s = s.replace("'", '').replace(',', '') + '\n'
        file.write(s)
    file.close()

    #fps,duration数值文件
    file = open('test_fpga_result/fps_duration_result.txt', 'w')
    for n in range(0, len(dirname)):
        model_url = filepath + str(dirname[n])
        # print(model_url)
        sh = os.popen("./test_fpga -m %s -l %s -r 3" % (model_url, loop))
        output = sh.read()
        fps = re.search(r'(?<=FPS = )\d*\.\d*',output).group()+"  "
        duration=re.search(r'(?<=duration )\d*\.\d*',output).group()+"\n"
        # print(output)
        file.write(fps)

        file.write(duration)
        #print(fps)
    file.close()





