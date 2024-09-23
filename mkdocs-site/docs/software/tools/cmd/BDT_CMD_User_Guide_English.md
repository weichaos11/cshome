
The tool was developed and tested on Ubuntu 20.04.3 LTS, 64-bit operating system.  Compile and test in macos M, intel series. 

Version v1.4。Please update the burning EVK firmware version to **V3.6** before using.

## Introduce

​	It mainly supports EVK mode, and some chips support USB mode. They are listed in the following table. They are explained in subsequent detailed use cases.

|                                | evk mode                        | usb mode          |
| :----------------------------- | ------------------------------- | ----------------- |
| read/write flash (rf, wf)      | support                         | only 826x support |
| read/write sram (rc, wc)       | support                         | only 82xx support |
| read/wirte analog (ra, wa)     | support                         | only 82xx support |
| download in flash              | support                         | not support       |
| download in core               | support                         | only 82xx support |
| erase in flash/core            | support                         | only 82xx support |
| check pc (pc)                  | support                         | only 82xx support |
| check  global parameters (var) | support                         | only 82xx support |
| reset in flash or sram         | support                         | only 82xx support |
| sws                            | support                         | not support       |
| run step stop                  | support, B91and B92 not support | only 82xx support |
| ac                             | support                         | not support       |
| lsusb | support | support     |
| up   | not support | support |

## Chip parameters

```
B92 9518 B80 B85 B87 B89_A1 8232 8266 8267 8269 8366 8368 8367_i 8367_e 8369_i 8369_e
```

## Command Example

Command Options

```c
-u : Indicates usb mode,The default mode is EVK.
-s : The number of bytes read and written, which follows -s. eg: -s 16; -s 1k.
-e : Erasing, used in Flash and core erasing.
-c : Represents core, commonly used reset command. 
-i : Specifies the input file followed by the file path, often used to specify the download file. eg: -i /home/8258_gpio.bin.
-o : Specifies the output file, followed by the file path, often used to save read binary data to a file. eg: -o /home/readflash.bin
-p : Represents the printing process, often used for flash operations.
-b,-d : Bus and devid of usb devices. This parameter is required when multiple USB devices exist.
```

**Supports the function of USB mode. You can add the -u option after the command.**

If there are multiple EVK devices, the VID and PID of EVK devices are the same. You can control a specified EVK device by specifying its **bus, devid**.

If you use usb debugging mode, you also need to specify **bus, devid** to control the device.

```c
Example, added after the command. -b:bus -d:devid
./bdt 8258 sws -b 1 -d 1
./bdt 8258 sws -b 1 -d 2

./bdt 8258 sws -b 1 -d 1 -u
./bdt 8258 sws -b 1 -d 2 -u
```

## sws

Set the rate, and detect whether the EVK and the target board connection is normal.

```c
# Sets the specified SWS value.
# b0:address 10:Rate parameter value.The first two (b0 10) are set evK SWire CLK values; The last two (B0 10) are the target development board swire CLK values.
./bdt 8258 sws b0 10 b0 10 

# If no value is specified, the default SWS value is B0 10 b0 10.
./bdt 8258 sws
```

Writing SWS values must be followed by SWS command arguments.

## activate

Run this command when the program is in low power mode.

```c
./bdt 8258 ac
```

## reset 

Restart, the program starts from Flash or SRAM.

```c
# Restart the device from the Flash
./bdt 8258 reset

# Restart the device from the Sram
./bdt 8258 reset -c
```

## read/write flash

**read flash(rf)**

If the read quantity is less than 1KB, the read data will be printed. Larger than 1KB will be saved to the default file.

Default file name example: `save1020-11294102.bin`

```c
# Read 16 bytes of flash address 0x00
./bdt 8258 rf 0x00 -s 16
./bdt 8258 rf 0x00 -s 1k

# Reads the data output to the specified file
./bdt 8258 rf 0x00 -s 16 -o readflash.bin
```

**write flash(wf)**

flash Erasure is required before writing, and the default unit of erasure is 4K.

```c
# Write 4 bytes of data to flash 0x00.
./bdt 8258 wf 0x00 01 02 03 04 -s 4

# Erase first, then write data.
./bdt 8258 wf 0x00 01 02 03 04 -s 4 -e

# Write a file to Flash, download function.
# Write files without the -e and -s option.
./bdt 8258 wf 0x00 -i bin/USB_Demo.bin
```

## read/write core

**read core(rc)**

If the read quantity is less than 1KB, the read data will be printed. Larger than 1KB will be saved to the default file.

Default file name example: `save1020-11294102.bin`

```c
# Read 16 bytes of sram address 0x40000
./bdt 8258 rc 0x40000 -s 16
./bdt 8258 rc 0x40000 -s 1k

# Reads the data output to the specified file.
./bdt 8258 rc 0x40000 -s 16 -o readsram.bin
```

**write core(wc)**

```c
# Write 4 bytes of data to sram 0x40000
./bdt 8258 wc 0x40000 01 02 03 44 -s 4

# Write a file to sram, download function.
# Write files without the -e and -s option.
./bdt 8258 wc 0x40000 -i bin/USB_Demo.bin
```

## read/wirte analog 

 **read analog(ra)**

```c
# Read 16 bytes of analog address 0x40000
./bdt 8258 ra 0x00 -s 16
```

 **write analog(wa)**

```c
#  Write 4 bytes of data to analog 0x00.
./bdt 8258 wa 0x00 01 02 03 44 -s 4
```

## check pc/parameter

View the PC pointer value, global parameter list (VAR).

You need to configure the. LST file to view the PC pointer value.

```c
# Prints program run pointer.
./bdt 8258 pc

# Print the current PC pointer in detail.
./bdt 8258 pc -i USB_PRINT_LOG.lst

# Prints a list of current program parameters (address, length, value).
/bdt 8258 var -i USB_PRINT_LOG.lst
```

## run stop start stall

Run, stop the program.

```c
./bdt 8258 run
./bdt 8258 stop
```

start, stall the program

```c
./bdt 8258 start
./bdt 8258 stall
```

## step

Step through the program.

```c
./bdt 8258 step
```

## up

Update EVK firmware

-i : Specifies the firmware file path to update.

-v : Query evk version number

```c
# The chip used by burning evk is 8266 
./bdt 8266 up -i fw/Firmware_v3.4.bin
./bdt 8266 up -i fw/Firmware_v3.4.bin -ev
./bdt 8266 up -ev
```

## lsusb

List connected USB devices. 

```c
./bdt lsusb

# -v : View usb descriptors
./bdt lsusb -v
```

# FAQ



