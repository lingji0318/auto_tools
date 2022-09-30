import os
import sys
url_jpeg="../data/jpeg/ILSVRC2012_val_00000056_result"
url_265="../data/imagenet-20-15-h265"
url_s265="../data/sampleVideoEncoder"
url_MP="../data/MOT16-09_Plugin"
url_M="../data/MOT16-09"
url_264="../data/imagenet-20-15-h264"
n="../data/Number"
c="channel"
d="device"
filepath = sys.argv[1]


def sampleIpe(dev):
    print("\033[0;33;40msampleIpe",dev,"\033[0m")
    sh = os.popen("./sampleIpe -i ../data/jpeg/ILSVRC2012_val_00000056.JPEG -d %s -s 1" %(dev))
    output = sh.read()
    print(output)
    os.popen("mv %s.JPEG %s_%s.JPEG" %(url_jpeg,url_jpeg,dev))

def sampleMulVideoDecoder(dev,cha):
    print("\033[0;33;40msampleMulVideoDecoder", "芯片数量",dev,"通道数",cha,"\033[0m")
    sh=os.popen("./sampleMulVideoDecoder -i ../data/imagenet-20-15-h265.mp4 -d %s -c %s -s 1" %(dev,cha))
    output=sh.read()
    print(output)

def sampleVideoEncoder(dev):
    print("\033[0;33;40msampleVideoEncoder", dev, "\033[0m")
    sh=os.popen("./sampleVideoEncoder -i ../data/jpeg/ -o ../data/sampleVideoEncoder.265 -d %s" %(dev))
    output = sh.read()
    print(output)
    os.popen("mv %s.265 %s_%s.265" % (url_s265, url_s265, dev))

def sampleYolov5MulChnVideo_Plugin(dev,cha):
    print("\033[0;33;40msampleYolov5MulChnVideo_Plugin", "芯片数量", dev, "通道数", cha, "\033[0m")
    sh=os.popen("./sampleYolov5MulChnVideo-Plugin -m ../models/yolov5s/Net_0 -i ../data/MOT16-09.mp4 "
                "-p ../plugin/libYolov5Plugin.so -d %s -c %s -s 1" %(dev,cha))
    output = sh.read()
    print(output)

def sampleLenetMulChnVideo(dev,cha):
    print("\033[0;33;40msampleLenetMulChnVideo", "芯片数量", dev, "通道数", cha, "\033[0m")
    sh=os.popen("./sampleLenetMulChnVideo -m ../models/lenet/Net_0 -i ../data/Number.mp4"
                " -d %s -c %s -s 1" %(dev,cha))
    output = sh.read()
    print(output)

def sampleTranscoder(dev):
    print("\033[0;33;40msampleTranscode", dev, "\033[0m")
    sh=os.popen("./sampleTranscoder -i ../data/imagenet-20-15-h264.mp4 -d %s" %(dev))
    output = sh.read()
    print(output)
    os.popen("mv %s.265 %s_%s.265" % (url_264, url_264, dev))

def sampleYolov5MulChnVideo(dev,cha):
    print("\033[0;33;40msampleYolov5MulChnVideo", "芯片数量", dev, "通道数", cha, "\033[0m")
    sh=os.popen("./sampleYolov5MulChnVideo -m ../models/yolov5s/Net_0 -i ../data/MOT16-09.mp4 "
                "-d %s -c %s -s 1" %(dev,cha))
    output = sh.read()
    print(output)

if filepath=="-h"or filepath=="--help":
    print("\033[0;33;40m放入sdksample bin目录下，不加参数直接执行即可\033[0m")
else:
    sampleIpe(0)
    sampleIpe(1)
    sampleIpe("0,1")
    sh = os.popen("md5sum %s_0.JPEG %s_1.JPEG %s_0,1.JPEG" %(url_jpeg,url_jpeg,url_jpeg))
    output=sh.read()
    print(output)

    sampleMulVideoDecoder("0,1",3)
    sh=os.popen("md5sum %s_%s0_%s0.yuv %s_%s0_%s1.yuv %s_%s0_%s2.yuv %s_%s1_%s0.yuv %s_%s1_%s1.yuv "
                "%s_%s1_%s2.yuv" %(url_265,d,c,url_265,d,c,url_265,d,c,url_265,d,c,url_265,d,c,url_265,d,c))
    output=sh.read()
    print(output)

    sampleVideoEncoder(0)
    sampleVideoEncoder(1)
    sampleVideoEncoder("0,1")
    sh = os.popen("md5sum %s_0.265 %s_1.265 %s_0,1.265" %(url_s265,url_s265,url_s265))
    output=sh.read()
    print(output)

    sampleYolov5MulChnVideo_Plugin("0,1",3)
    sh=os.popen("md5sum %s_%s0_%s0.264 %s_%s0_%s1.264 %s_%s0_%s2.264 %s_%s1_%s0.264 %s_%s1_%s1.264 "
                "%s_%s1_%s2.264" %(url_MP,d,c,url_MP,d,c,url_MP,d,c,url_MP,d,c,url_MP,d,c,url_MP,d,c))
    output=sh.read()
    print(output)

    sampleLenetMulChnVideo("0,1",3)
    sh=os.popen("md5sum %s_%s0_%s0.264 %s_%s0_%s1.264 %s_%s0_%s2.264 %s_%s1_%s0.264 %s_%s1_%s1.264 "
                "%s_%s1_%s2.264" %(n,d,c,n,d,c,n,d,c,n,d,c,n,d,c,n,d,c))
    output=sh.read()
    print(output)


    sampleTranscoder(0)
    sampleTranscoder(1)
    sampleTranscoder("0,1")
    sh = os.popen("md5sum %s_0.265 %s_1.265 %s_0,1.265" %(url_264,url_264,url_264))
    output=sh.read()
    print(output)

    sampleYolov5MulChnVideo("0,1",3)
    sh=os.popen("md5sum %s_%s0_%s0.264 %s_%s0_%s1.264 %s_%s0_%s2.264 %s_%s1_%s0.264 %s_%s1_%s1.264 "
                "%s_%s1_%s2.264" %(url_M,d,c,url_M,d,c,url_M,d,c,url_M,d,c,url_M,d,c,url_M,d,c))
    output=sh.read()
    print(output)



