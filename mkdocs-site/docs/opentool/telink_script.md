---
icon: :octicons-heart-fill-24: 
---
# telink script tool

## 工具介绍
!!! note "telink script tool"

    为了快速进行产品原型验证，我们开发了一套脚本系统。系统中，telink script tool作为一款windows端工具，通过UART接口并配合支持相同交互协议的目标板（协议开源且易移植），可实现脚本编辑、文件交互、UART收发、断点控制等功能。其系统框图如下：

    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_frame.jpg" class="image" style="width:100%">
    </div>

## 快速体验
!!! note "Rocket板快速体验"
    快速体验固件适用于泰凌B91系列的芯片，若采用的是非Rocket底板，只需将UART0_TX_PB2、UART0_RX_PB3通过USB转UART模块连接到电脑端，示例脚本处将ROCKET_BOARD的值改为false即可。

    1、下载[快速体验固件](../res/telink_script_tool/test.bin)到[Rocket板]。固件烧录可采用工具<a href="http://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-all-Series/"  target="_blank"> BDT </a>或者<a href="https://debug.telink-semi.cn/webtool/web_bdt/" target="_blank"> Web BDT </a>。
    [Rocket板]: ../../openboard/Mars/#_2

    2、下载工具[telink_script_tool](../res/telink_script_tool/telink_script_tool_v1.1.7z)，工具中自带了个示例脚本，其主要功能：每隔1秒打印采集到数据并翻转LED，每隔5秒定时器产生一次中断，按下拨轮按键可控制板子上的彩灯显示。

    3、Rocket板上采用的USB转UART信号的芯片为CH340E，请事先安装[CH340E驱动](../res/telink_script_tool/CH341SER.EXE)。用Type-C线连接Rocket板的USB_UART口和电脑，在工具主界面处点击端口按钮，选择对应的端口号后点击设置。
        <div class="div_center" style="text-align:center"> 
            <img src="../res/telink_script_tool/telink_script_tool_home_3.jpg" class="image" style="width:60%">
            <img src="../res/telink_script_tool/telink_script_tool_home_4.jpg" class="image" style="width:30%">
        </div>

    4、点击全下按钮，等待全部下载完毕提示（下载过程约五秒左右），若中途卡住了，可再次点击全下按钮
        <div class="div_center" style="text-align:center"> 
            <img src="../res/telink_script_tool/telink_script_tool_download_all.jpg" class="image" style="width:40%">
        </div>

    5、观察Rocket板现象是否跟预期一样。


## 工具使用
!!! note "Windows APP"
    工具主界面如下图所示，1号区域按钮用于系统设置，2号区域按钮用于与开发板进行交互，3号区域为文件列表区，4号区域为文件编辑区，5号区域为日志显示窗口。
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_home_2.jpg" class="image" style="width:100%">
    </div>

!!! note "系统操作"
    单击发送区的文件，文件编辑区会加载该文件内容，我们可以在编辑区内进行脚本的编辑，也可以右键进行新增或者重命名文件。
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_edit_new_file.jpg" class="image" style="width:30%">
    </div>

    1号区域内的按键功能简介如下</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 端口：弹框配置端口和波特率，需点击弹框内设置按钮完成设定</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 连接：与设定的UART端口进行连接/断开</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 刷新：刷新文件列表</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 保存：将编辑区内的文件进行保存（切换选择文件时也会自动保存）</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 清空：清空下方的log窗口内容</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 文档：打开浏览器访问在线文档</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 关于：工具由Qt构建，显示Qt相关的license</br>
    :fontawesome-brands-font-awesome:{ .icon_blue } 设置：默认模式下的部分功能设置是禁止的。设置选项的状态是重启保存的，正常用默认模式即可
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_setting.jpg" class="image" style="width:70%">
    </div>

    工具的project文件夹下，send为发送区的文件夹，receive为接收区文件夹，stytle.qss为用户自定义皮肤样式表，config.ini为系统配置文件，配置文件中将mode值改为root，然后重启应用就可解锁更多的设置权限。
!!! note "操作板子"
    2号区域按钮用于与开发板进行交互，在UART连接成功后才可以进行操作。其功能简介如下</br>
    ⬆️ 读取：将开发板内的脚本文件和断点描述文件都读至project/receive目录下，点击接收区文件列表可以在工具的编辑区内查看文件内容
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool__rec.jpg" class="image" style="width:65%">
    </div>

    ⤵️ 下载：单击发送列表内的文件后点击下载，会将该文件下载到开发板内</br>
    ⤵️ 全下：将project/send目录下的所有脚本文件和断点描述文件都下载至开发板内</br>
    ❌ 删除：单击文件列表，删除对应电脑端的文件。若勾选了系统设置中的选项："连同板内文件一起删除"，则在删除接收列表内的文件时也会尝试删除板内同名文件</br>
    🐞 断点：将project/send目录下的断点描述文件都下载至开发板内。断点的介绍看下文中的"断点使用"章节</br>
    🚫 清除：将电脑端断点描述文件清空，并删除开发板内的断点描述文件</br>
    🔁 复位：将UART的RST信号拉低100毫秒后再拉高，Rocket将CH340E_RST连接到了芯片复位引脚上，该信号会触发芯片硬件复位</br>
    :octicons-heart-fill-24:{ .heart } 终端：点击后会出现弹窗。在脚本运行时，跟开发板通过UART进行交互。弹窗界面如下：1号区域为UART数据接收区，2号区域为功能按钮，3号区域内有三个子区域</br>
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_terminal.jpg" class="image" style="width:80%">
    </div>

    单条发送：在输入框内输入数据，点击2号区域内的发送数据按钮，可以将数据发送给开发板
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_terminal_1.jpg" class="image" style="width:80%">
    </div>

    断点控制：除了rts复位，其余功能只有在断点停留时才可生效
        <tr>
            <th>按钮名称</th>
            <th>按钮功能</th>
        </tr>
        <tr>
            <td>继续运行</td>
            <td>跳过停留处的断点继续往下运行</td>
        </tr>
        <tr>
            <td>全速运行</td>
            <td>取消所有断点，全速运行</td>
        </tr>
        <tr>
            <td>打印断点</td>
            <td>打印所有断点信息</td>
        </tr>
        <tr>
            <td>取消断点</td>
            <td>取消停留处的断点</td>
        </tr>
        <tr>
            <td>内核状态</td>
            <td>程序读取CSR寄存器和PC值，并打印出来</td>
        </tr>
        <tr>
            <td>执行脚本</td>
            <td>执行按钮下发的输入框内的脚本</td>
        </tr>
        <tr>
            <td>rts复位</td>
            <td>将UART的RST信号拉低100毫秒后再拉高</td>
        </tr>
    </table>

    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_terminal_2.jpg" class="image" style="width:80%">
    </div>

    读写数据：在断点停留时，才可以进行此项操作。先选择要读取的对象：Core/Flash/Analog，再输入地址和长度，最后点击读取/写入按钮
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_terminal_3.jpg" class="image" style="width:80%">
    </div>

!!! note "脚本编写"
    以lua脚本为例，用户需编写main.lua脚本，参考示例脚本实现setup、loop函数。如果要实现中断功能，需编写irq.lua脚本并实现irq_entry函数，这三个函数在程序中的调用逻辑如下所示</br>
    ``` c
    // 中断处理函数
    void xxx_irq_handler(void){ 
        // 清除中断标志位
        clear_irq_state;
        // 调用lua脚本中的函数irq_entry，并将该中断号传递给该函数
        call_lua_one_par("irq_entry",IRQ_NUMBER); 
    }

    void main() {
        // 系统初始化
        sys_init(); 
        // 调用lua脚本中的初始化函数
        call_lua_function("setup"); 
        while (1) {
            // 调用lua脚本中的loop函数
            call_lua_function("loop");
        }
    }
    ```

    用户可以下载其他名称的lua脚本到芯片中，并在main.lua中引入这些文件并使用其中的功能（示例代码中有体现）。</br>

!!! note "断点使用"
    为了方便开发者进行调试，系统实现了简易的断点功能。需要注意的是在中断函数里打断点是不会生效的。具体使用步骤如下：</br>
    1、勾选/取消断点：点击代码行号右侧可以勾选此处断点，再次点击可以取消此处断点。日志窗口处会有断点提示，并且系统会将断点信息同步写入电脑端的断点配置文件中。
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_bk_1.jpg" class="image" style="width:50%">
        <img src="../res/telink_script_tool/telink_script_tool_bk_2.jpg" class="image" style="width:30%">
    </div>

    2、点击主界面中的"断点"/"全下"按钮可以将电脑端的断点配置文件下载进开发板内。点击"清除"按钮可清空电脑端断点配置文件，并删除开发板内的断点配置文件。:octicons-heart-fill-24:{ .heart }开发板每次上电都会先读取并解析断点配置文件，并按配置运行。
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_bk_3.jpg" class="image" style="width:10%">
        <img src="../res/telink_script_tool/telink_script_tool_bk_4.jpg" class="image" style="width:70%">
    </div>

    3、点击主界面中的"终端"按钮，在断点停留时可进行一系列操作。这里的操作不会影响开发板内的断点配置文件。
    <div class="div_center" style="text-align:center"> 
        <img src="../res/telink_script_tool/telink_script_tool_terminal_2.jpg" class="image" style="width:70%">
        <img src="../res/telink_script_tool/telink_script_tool_terminal_3.jpg" class="image" style="width:70%">
    </div>

!!! note "接口列表"
    示例工程中将接口放在了<a href="https://github.com/telink-semi/openboard/blob/main/opensdk/Mars_B91/telink_rocket_driver_sdk/demo/vendor/Rocket_EVB/lua_interface/my_lua_reg.c"target="_blank">my_lua_reg.c</a>处，这些接口可在脚本文件中调用，接口的描述如下</br>
    1、Rocket板相关：
    <table border="1" style="margin-left: auto;margin-right: auto;">
        <tr>
            <th>接口原型</th>
            <th>接口功能</th>
            <th>调用示范</th>
        </tr>
        <tr>
            <td>rocket_init()</td>
            <td>初始化板子上的器件</td>
            <td>rocket_init()</td>
        </tr>
        <tr>
            <td>rocket_oled_cls()</td>
            <td>清空OLED屏幕</td>
            <td>rocket_oled_cls()</td>
        </tr>
        <tr>
            <td>rocket_oled_cls_y(Y)</td>
            <td>OLED屏幕一共六行，清空第Y和Y+1行</td>
            <td>rocket_oled_cls_y(0)</td>
        </tr>
        <tr>
            <td>rocket_oled_show_str(x,y,string)</td>
            <td>在屏幕上显示字符串，字符串行高为2，x∈[0,127] y∈[0,6] string为字符串</td>
            <td>rocket_oled_show_str(0,0,"hello world")</td>
        </tr>
        <tr>
            <td>rocket_sht30_read()</td>
            <td>读取温湿度数据，返回值为两个float</td>
            <td>temp,humi = rocket_sht30_read()</td>
        </tr>
        <tr>
            <td>lua_rocket_adc_read()</td>
            <td>读取ADC采集到的电压值和计算到的R13阻值，返回值为两个int</td>
            <td>vol,r13 = rocket_adc_read()</td>
        </tr>
        <tr>
            <td>rocket_lis2dh_read()</td>
            <td>读取三轴加速度器数据，返回值为三个int</td>
            <td>x,y,z = rocket_lis2dh_read()</td>
        </tr>
        <tr>
            <td>rocket_button_read()</td>
            <td>读取按键数据，返回一个int，返回0代表没有按键按下，返回1、2、3分别代表左、中、右键按下</td>
            <td>button_value = rocket_button_read()</td>
        </tr>
        <tr>
            <td>rocket_ws2812b_set(color)</td>
            <td>设置彩灯颜色，color为int型，数据格式为GRB，如0xff0000代表Green色</td>
            <td>rocket_ws2812b_set(0xff0000)</td>
        </tr>
    </table>

    2、读写相关：
    <table border="1" style="margin-left: auto;margin-right: auto;">
        <tr>
            <th>接口原型</th>
            <th>接口功能</th>
            <th>调用示范</th>
        </tr>
        <tr>
            <td>analog_write_reg8(addr,data)</td>
            <td>往模拟寄存器地址addr处写入一个字节的数据data</td>
            <td>analog_write_reg8(0x12,0x34)</td>
        </tr>
        <tr>
            <td>analog_write_reg16(addr,data)</td>
            <td>往模拟寄存器地址addr处写入半个字的数据data</td>
            <td>analog_write_reg16(0x12,0x3456)</td>
        </tr>
        <tr>
            <td>analog_write_reg32(addr,data)</td>
            <td>往模拟寄存器地址addr处写入一个节的数据data</td>
            <td>analog_write_reg32(0x12,0x12345678)</td>
        </tr>
        <tr>
            <td>analog_write_reg8_buff(addr,buff,len)</td>
            <td>往模拟寄存器地址addr处写入一组字节数据buff，len为写入的长度，不能大于1024</td>
            <td> 
                buff = {} </br>
                buff[1] = 0x12  buff[2] = 0x34</br>
                buff[3] = 0x56  buff[4] = 0x78</br>
                analog_write_reg8_buff(0x12,buff,4)
            </td>
        </tr>
        <tr>
            <td>analog_read_reg8(addr)</td>
            <td>从模拟寄存器地址addr处读取一个字节的数据</td>
            <td>data_8 = analog_read_reg8(0x12)</td>
        </tr>
        <tr>
            <td>analog_read_reg16(addr)</td>
            <td>从模拟寄存器地址addr处读取半个字的数据</td>
            <td>data_16 = analog_read_reg16(0x12)</td>
        </tr>
        <tr>
            <td>analog_read_reg32(addr)</td>
            <td>从模拟寄存器地址addr处读取一个字的数据</td>
            <td>data_32 = analog_read_reg32(0x12)</td>
        </tr>
        <tr>
            <td>analog_read_reg8_buff(addr,len)</td>
            <td>从模拟寄存器地址addr处读取一组字节数据buff，len为读取的长度，其不能大于1024</td>
            <td> 
                buff={} </br>
                buff,read_len = analog_read_reg8_buff(0x12,20)
            </td>
        </tr>
    </table>

    与之类似的读写接口如下，见名之意，它们操作的对象为SRAM何寄存器。</br>
    ``` c
      write_sram8、write_sram16、write_sram32
      write_sram8_buff、write_sram16_buff、write_sram32_buff
      read_sram8、read_sram16、read_sram32
      read_sram8_buff、read_sram16_buff、read_sram32_buff
      write_reg8、write_reg16、write_reg32
      read_reg8、read_reg16、read_reg32
    ```

    3、GPIO相关：</br>
    <table border="1" style="margin-left: auto;margin-right: auto;">
        <tr>
            <th>接口原型</th>
            <th>接口功能</th>
            <th>调用示范</th>
        </tr>
        <tr>
            <td>gpio_function_en(PAD_NUM)</td>
            <td>将引脚PAD_NUM设置为GPIO功能，PAD号为字符串类型</td>
            <td>gpio_function_en('PB6')</td>
        </tr>
        <tr>
            <td>gpio_function_dis(PAD_NUM)</td>
            <td>关闭引脚PAD_NUM的GPIO功能</td>
            <td>gpio_function_dis('PB6')</td>
        </tr>
        <tr>
            <td>gpio_output_en(PAD_NUM)</td>
            <td>打开PAD_NUM输出功能</td>
            <td>gpio_output_en('PB6')</td>
        </tr>
        <tr>
            <td>gpio_output_dis(PAD_NUM)</td>
            <td>关闭PAD_NUM输出功能</td>
            <td>gpio_output_dis('PB6')</td>
        </tr>
        <tr>
            <td>gpio_input_en(PAD_NUM)</td>
            <td>打开PAD_NUM输入功能</td>
            <td>gpio_input_en('PB6')</td>
        </tr>
        <tr>
            <td>gpio_input_dis(PAD_NUM)</td>
            <td>关闭PAD_NUM输入功能</td>
            <td>gpio_input_dis('PB6')</td>
        </tr>
        <tr>
            <td>gpio_high(PAD_NUM)</td>
            <td>设置PAD_NUM输出高</td>
            <td>gpio_high('PB6')</td>
        </tr>
        <tr>
            <td>gpio_low(PAD_NUM)</td>
            <td>设置PAD_NUM输出低</td>
            <td>gpio_low('PB6')</td>
        </tr>
        <tr>
            <td>gpio_toggle(PAD_NUM)</td>
            <td>翻转PAD_NUM的输出</td>
            <td>gpio_toggle('PB6')</td>
        </tr>
        <tr>
            <td>gpio_set_up_down_res(PAD_NUM,mode)</td>
            <td>设置PAD_NUM模拟上下拉，mode取值为0-3，0:浮空，1:上拉1M，2:下拉100K 3:上拉10K</td>
            <td>gpio_set_up_down_res('PB6',1)</td>
        </tr>
        <tr>
            <td>gpio_set_irq(PAD_NUM,IQR_TYPE)</td>
            <td>设置GPIO_IRQ中断，IQR_TYPE为触发模式，取值为0-3，0:上升沿，1:下降沿，2:高电平 3:低电平</td>
            <td>gpio_set_irq('PD1',1)</td>
        </tr>
        <tr>
            <td>gpio_set_gpio2risc0_irq(PAD_NUM,IQR_TYPE)</td>
            <td>设置IRQ_RISC0中断，IQR_TYPE为触发模式，取值为0-3，0:上升沿，1:下降沿，2:高电平 3:低电平</td>
            <td>gpio_set_gpio2risc0_irq('PD2',1)</td>
        </tr>
        <tr>
            <td>gpio_set_gpio2risc1_irq(PAD_NUM,IQR_TYPE)</td>
            <td>设置IRQ_RISC1中断，IQR_TYPE为触发模式，取值为0-3，0:上升沿，1:下降沿，2:高电平 3:低电平</td>
            <td>gpio_set_gpio2risc1_irq('PD3',1)</td>
        </tr>
    </table>    

    4、其他：
    <table border="1" style="">
        <tr>
            <th>接口原型</th>
            <th>接口功能</th>
            <th>调用示范</th>
        </tr>
        <tr>
            <td>SYS_DEBUG_EN()</td>
            <td>开启断点功能</td>
            <td>SYS_DEBUG_EN()</td>
        </tr>
        <tr>
            <td>print_riscv_reg()</td>
            <td>打印程序读取到的CSR寄存器和PC值</td>
            <td>print_riscv_reg()</td>
        </tr>
        <tr>
            <td>core_interrupt_enable()</td>
            <td>打开全局总中断</td>
            <td>mstatus = core_interrupt_enable()</td>
        </tr>
        <tr>
            <td>core_interrupt_disable()</td>
            <td>关闭全局总中断</td>
            <td>core_interrupt_disable()</td>
        </tr>
        <tr>
            <td>core_restore_interrupt(mstatus)</td>
            <td>由传入值恢复全局中断</td>
            <td>core_restore_interrupt(mstatus)</td>
        </tr>
        <tr>
            <td>get_mem_perused()</td>
            <td>获取动态内存使用率</td>
            <td>value = get_mem_perused()</td>
        </tr>
        <tr>
            <td>set_timer0_cycle(ms)</td>
            <td>设置定时器0的定时周期(毫秒)</td>
            <td>set_timer0_cycle(1000)</td>
        </tr>
        <tr>
            <td>set_timer1_cycle(ms)</td>
            <td>设置定时器1的定时周期(毫秒)</td>
            <td>set_timer1_cycle(1000)</td>
        </tr>
        <tr>
            <td>delay_us(us)</td>
            <td>延时函数(us)</td>
            <td>core_restore_interrupt(10)</td>
        </tr>
        <tr>
            <td>delay_ms(ms)</td>
            <td>延时函数(ms)</td>
            <td>delay_ms(10)</td>
        </tr>
    </table>
## 固件构建
  
!!! info "固件构建"
    快速体验中使用到的固件里面的接口是固定且有限的。用户可下载<a href="https://github.com/telink-semi/openboard/tree/main/opensdk/Mars_B91/telink_rocket_driver_sdk/demo/vendor/Rocket_EVB"target="_blank">源码</a>自己进行二次开发。</br>

    用户可以在源码下的<a href="https://github.com/telink-semi/openboard/blob/main/opensdk/Mars_B91/telink_rocket_driver_sdk/demo/vendor/Rocket_EVB/lua_interface/my_lua_reg.c"target="_blank">my_lua_reg.c</a>处增加自己想要的接口，也可以直接将源码直接移植到其他平台。</br>

    针对泰凌的B91系列芯片，在工程目录下我们提供了生成lib库的参考脚本，可将生成的lib库加载到自己工程里进行编译产生固件。在Telink IoT Studio的设置中将tlua_lib.a和数学库加进去，并将文件夹lua_interface和telink_lua_lib中相关头文件加入工程，初始化和主循环中调用lib库中的两个接口<img src="../res/telink_script_tool/tlua_lib.jpg" class="image" style="width:100%"><img src="../res/telink_script_tool/math_lib.jpg" class="image" style="width:100%">
    
    ``` c
        #include "lua_interface/my_lua_reg.h"
        #include "lua_interface/my_lua_interface.h"
        #include "telink_lua_lib/lua/lua_extend.h"

        void user_init()
        {
            telink_lua_lib_init(lua_lib,&lua_interface);
        }

        void main_loop(void)
        {
            while(1){
                telink_lua_main_loop();
            }
        }
    ```

    在中断函数处调用Lua的irq_entry函数，示例如下
    ```c
    _attribute_ram_code_sec_noinline_ void gpio_irq_handler(void)
    {
        gpio_clr_irq_status(FLD_GPIO_IRQ_CLR);
        c_call_lua_one_par("irq_entry",IRQ25_GPIO);
    }
    ```