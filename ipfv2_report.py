import os
import sys
import openpyxl
import re

filepath = sys.argv[1]


# filepath='../../test'


if filepath=="-h"or filepath=="--help":
    print("\033[0;33;40mpython3 ipfv2.py model_url loop\033[0m")
    print("\033[0;33;40meg:python3 ipfv2.py ../model/ 1000\033[0m")
    print("\033[0;33;40m报告生成在 inferPerfv2_result文件夹中\033[0m")
else:
    loop = sys.argv[2]
    dirname = os.listdir(filepath)
    os.popen("mkdir inferPerfv2_result")
    # # 模型名称文件
    # file = open('inferPerfv2_result/mode_name.txt', 'w')
    # for i in range(0, len(dirname)):
    #     s = str(dirname[i]).replace('[', '').replace(']', '')
    #     s = s.replace("'", '').replace(',', '') +'\n'
    #     file.write(s)
    # file.close()

    #fps,duration数值文件
    file = open('inferPerfv2_result/fps_microseconds_result.txt', 'w')
    for n in range(0, len(dirname)):
        model_url = filepath + str(dirname[n])+'/Net_0/'
        print("\033[0;33;40m",model_url,"\033[0m")
        sh = os.popen("./inferPerfv2 %s %s" % (model_url, loop))
        output = sh.read()
        print(output)
        flag=re.search("ERROR",output)
        model_name = str(dirname[n])+"  "
        file.write(model_name)
        if(flag):
            microseconds='ERROR'+"  "
            frame_rate='ERROR'+"\n"
        else:
            microseconds = re.search(r'(?<=microseconds: )\d*\.\d*',output).group()+"  "
            frame_rate=re.search(r'(?<=frame rate )\d*\.\d*',output).group()+"\n"
        file.write(microseconds)

        file.write(frame_rate)
        #print(fps)
    file.close()





