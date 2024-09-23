---
icon: material/emoticon-happy
title: "mboard"

subtitle: ""
author: "telink-semi.com"
author-url: 'xiaodong.zong@telink-semi.com'
date: "2022-08-04"
---

## 模块介绍：

!!! note "mboard系列"
    泰凌模块板 mboard 为推广泰凌芯片产品而生。当前版本v1.1 核心芯片为TLSR9218，支持zigbee,ble协议。只需下载现成的bin文件，即可通过uart来控制模块板。用户可以方便的进行芯片评估，也可把模块板集成到自己的电路系统中，为自己的系统扩展无线功能。同时为了方便用户二次开发，模块板的原理图、PCB图以及相关的BLE和zigbee sdk应用代码均为开源，用户二次开发时可自行修改。为了用户可更容易获得软件，电路图绘制软件使用的是流行且开源免费的kicad，软件开发环境可去泰凌wiki上获取。另外模块板配套的各种上位机工具也尽量用开源免费的工具开发，工具本身也开源，方便用户学习和扩展。（相应资源在文章结尾，请耐心看完)

  模块板照片：




<div class="div_center" style="text-align:center"> 
<img src="../../images/m_top.png" class="image" style="width:25%"><img src="../../images/m_bottom.png" class="image" style="width:25%">
</div>


!!! note "从上图可以看出模块板只留出了必要的接口，让接口尽可能的简单,接口定义如下："




|左侧接口     |功能|右侧接口|功能|
|:---        |:---: |:---|:---:|
|RESET     | 硬件复位 | DM   | USB DM|  
|PD3       | GPIO     | DP   | USB DP|  
|PD2       | GPIO     | SWS  | SWS下载调试 | 
|PD1       | GPIO     | TX   | uart tx  |
|PE0       | GPIO     | RX   | uart rx  |
|PC2       | GPIO     | RTS  | uart 预留 | 
|3.3V      | 电源3.3V | PB5  | GPIO |
|GND       | 电源GND  | GND  | 电源GND | 



下图为素颜照，从照片看，模块板尺寸和一枚1块钱硬币差不多.
<div class="div_center" style="text-align:center"> 
<img src="../../images/mboard_vs_coin.png" class="image" style="width:50%">
</div>

一个模块板的典型应用见下图官方底板，其中PC2连接按键，PD2,PD1连接拨码开关，UART TX，RX通过usb转串口芯片转为usb接口，可以直接连接PC：

<div class="div_center" style="text-align:center"> 
<img src="../../images/evb.gif" class="image" style="width:40%">
</div>

## 如何使用
- 使用Telink Buring Evk，通过BDT或者web BDT下载对应的bin文件到模块中(文章后面部分有详细说明)
- 通过串口使用模块板

## 下载工具

!!! Abstract "BDT"

    === "WebBDT"
        为了跨平台，方便用户改造工具，Telink新推出了基于web的下载调试工具：:octicons-heart-fill-24:{ .heart }[Web BDT](https://debug.telink-semi.cn/web_bdt/)
        
        通过网页来进行bin文件下载，以及对程序进行调试.
        
        支持windows,linux,MAC,android平台，只需要一个兼容的网页浏览器即可。
        
        :octicons-heart-fill-24:{ .heart }[详细文档](https://debug.telink-semi.cn/doc/webtools/page1/)

    === "老工具"
        Telink原来的下载工具为: [BDT](http://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-all-Series)在windows平台使用.

        建议尽量使用新的下载工具。




    

    



## 模块构建为Zigbee网络
<p>一个典型的zigbee mesh网络如下所示，新设备入网时，网络中必须有一个coordinator设备：</p>
<div class="div_center" style="text-align:center"> 
<img src="../../images/zigbee.png" class="image" style="width:70%">
</div>

!!! info "mboard模块板构建zigbee网络步骤如下："

     1. 下载 zigbee_coordinator.bin 到其中一个模块板
     2. 下载 zigbee_router.bin 到其他多个模块板
     3. coordinator 设备先上电，此时模块板上led灯亮，表示允许其他设备入网（3分钟内）
     4. router 设备上电，router设备led闪烁，表示入网成功
     5. 组网成功后，通过UART发送数据即可实现广播或者定点传输数据（UART发送一笔数据最长64字节）
  
相关配置说明:

模块板接口   |功能说明
:-         |:----
 TX/RX      | UART TX/RX，8数据位，1停止位，无奇偶检验，波特率默认为115200
 PC2        | 可接主控MCU，或者按键，上电初始化时需保持未按下状态<br>对于coordinator, 单击：限定时间内允许入网；双击：关闭入网许可<br>对于rounter, 单击：广播发送自身网络地址； 双击：广播用户自定义设备ID号；长按：恢复出厂设置
 PD1,PD2 | 模式配置控制IO（使用过程中可动态切换模式，切换间隔与按键长按的时间一致，默认为两秒）: <br> 00: 广播透传模式，uart收到任何数据都通过zigbee广播出去，zigbee收到的数据通过uart发送<br>01: command模式，功能码使用示例见后面的描述<br>10: 定位模式，router收集移动模块定位数据，定期发送给coordinator<br>11: 移动模式，router定期广播自定义ID号

!!! note "说明"
    + 设备广播自身的ID号时，会带有头部 5A A5；
    + 设备广播自身短地址时，会带有头部 A5 5A；
    + 设备广播自身长地址时，会带有头部 A5 A5；
    + 设置命令应答（默认关闭）会带有尾部 5A 5A；

!!! note "gpio_group和pwm_group数组定义如下："

    ``` c
    const gpio_pin_e gpio_group[] = {
    GPIO_PD3,GPIO_PE0,GPIO_PA5,GPIO_PA6,
        GPIO_PA7,GPIO_PB2,GPIO_PB3,GPIO_PB4,
        GPIO_PB5
    };
    const pwm_pin_e pwm_group[][2] = {
    {PWM_PWM0_PB4,0},
        {PWM_PWM1_PB5,1},
        {PWM_PWM3_N_PD3,3},
        {PWM_PWM3_PE0,3}
    };
    ```

!!! note "配置为command模式时，UART 命令格式如下（reurn为关闭回显和命令应答，执行完指令后UART的返回的数据；除了功能码0x00，其他控制命令长度固定；设定的值断电可保存）："

code |example |example describe |return|support
:-         |:----  |:---- |:---- |:----
0x00|00 5C 29 11 22 33|往网络地址为0x5c29的设备发送数据 11 22 33|NULL|ALL
0x01|01|打开回显功能|NULL|ALL
0x02|02|关闭回显功能|NULL|ALL
0x03|03 00 25 80|设置UART波特率为0x2580(9600，复位后生效)|NULL|ALL
0x04|04 B4|设置限定入网时间为0xB4秒|NULL|Coordinator
0x05|05 10|设置设备ID号为0x10|NULL|Router
0x06|06 05|设定广播ID的周期为0x05秒|NULL|Router
0x07|07 28|设置短按检测时间为0x28毫秒（复位后生效）|NULL|ALL
0x08|08 01 F4|设置短按检测时间为0x01F4毫秒（复位后生效）|NULL|ALL
0x09|09|广播发送自身短地址|NULL|ALL
0x0A|0A|广播发送自身长地址|NULL|ALL
0x0B|0B|广播发送自定义ID号|NULL|Router
0x0C|0C 00 01|设置引脚gpio_group[0x00]为0x01(高)电平|NULL|ALL
0x0D|0D 01|读取引脚gpio_group[0x01]电平|01（高电平）|ALL
0x0E|0E 02 00|设置设备（允许）入网时引脚gpio_group[0x02]为0x00(低)电平|NULL|ALL
0x0F|0F 03 00|设置设备死机时引脚gpio_group[0x03]为0x00(低)电平|NULL|ALL
0x10|10 00 00 00 27 10 32|设置引脚pwm_group[0x00]为PWM功能，频率为0x00002710HZ，占空比为0x32%|NULL|ALL
0x11|11|关闭所有设定的PWM功能|NULL|ALL
0x12|12|重启最后一次配置的PWM功能|NULL|ALL
0x13|13|返回0x01代表在正确模式下|01|ALL
0x14|14|显示自定义ID号|10|Router
0x15|15|显示广播自定义ID的周期|05|Router
0x16|16|显示限定入网时间（单位为秒）|B4|Coordinator
0x17|17|返回0x01代表开启了回显功能|00|ALL
0x18|18|显示PAN_ID|06 10|ALL
0x19|19|显示coordinator的长地址|A4 C1 38 D1 97 0B 25 3C|Router
0x1A|1A|显示本设备长地址|A4 C1 38 8E D6 90 F7 E0|ALL
0x1B|1B|显示本设备短地址|44 20|ALL
0x1C|1C|显示本设备类型 00:D_COORDINATOR  01:ROUTER  02:END_DEV|01|ALL
0x1D|1D|显示按键的短按时间(2B)和长按时间(1B)，单位:秒|C8 07 D0|ALL
0x1E|1E|显示入网和死机时的触发IO编号(gpio_group)及触发电平|02 00 03 00|ALL
0x1F|1F|显示PWM引脚编号(pwm_group,1B,ff表示未选)周期(4B)和占空比(1B)|00 00 00 27 10 32|ALL
0x20|20|显示所有数据|详情见下方描述|ALL
0x21|21|打开设置指令的命令应答(后缀5A A5)|5A 5A|ALL
0x22|22|关闭设置指令的命令应答(后缀5A A5)|NULL|ALL
0x30|30|设置参数为默认值|5A 5A|ALL
0x31|31|复位芯片|NULL|ALL
0x32|32|恢复出场设置|NULL|ALL

在command模式下，关闭回显和命令应答后，发送指令0x20，UART返回所有设定相关的数据

+ example: 01 01 C2 00 06 10 A4 C1 38 D1 97 0B 25 3C A4 C1 38 8E D6 90 F7 E0 44 20 14 00 00 02 C8 07 D0 02 00 03 00 00 00 00 27 10 32 00 01
+ 字段描述：

describe |length|example|example describe
:-        |:----  |:---- |:----
当前模式|1|01|当前为command模式
复位后的波特率|3|01 C2 00|复位后波特率为0x01c200
PAN ID|2|06 10|PAN ID为0x0610
coordinator长地址|8|A4 C1 38 D1 97 0B 25 3C|0xA4C138D1970B253C
自身长地址|8|A4 C1 38 8E D6 90 F7 E0|0XA4C1388ED690F7E0
自身短地址|2|44 20|0X4420
限定入网时间|1|14|限定入网时间为0x14秒
回显功能|1|00|00：未开启回显 01：开启回显
设备ID|1|00|设备ID为0x00
ID广播周期|1|02|广播设备ID的周期为0x02秒
短按检测时间|1|C8|短按检测时间为0xC8毫秒
长按检测时间|2|07 D0|长按检测时间为0x07D0毫秒
入网时的触发IO编号(gpio_group)及触发电平|1+1|02 00|入网触发IO为gpio_group[2],触发电平为0x00
死机时的触发IO编号(gpio_group)及触发电平|1+1|03 00|死机触发IO为gpio_group[3],触发电平为0x00
PWM引脚pwm_group编号(ff表示未选)周期和占空比|1+4+1|00 00 00 27 10 32|设置pwm_group[0x00]引脚为PWM功能 频率为0x00002710HZ,占空比为0x32%
设置指令的命令应答(后缀5A A5)|1|00|00：不添加；01：添加
设备类型|1|01|00:D_COORDINATOR  01:ROUTER  02:END_DEV

设备出厂时的默认设定：

功能 |默认设置
:-         |:----
UART回显|关闭
设置指令的命令应答(后缀5A A5)|不添加
UART波特率|115200
设备ID|0x00
设备广播自身ID的周期|2秒
PWM设定|不开启
短按检测时间|200毫秒
长按检测时间|2秒
单击按键后协调器限定的入网时间|180秒
入网时的触发IO|gpio_group[2]
入网时的触发IO的触发电平|低电平
死机时的触发IO|gpio_group[3]
死机时的触发IO的触发电平|低电平

## 模块构建为BLE网络


