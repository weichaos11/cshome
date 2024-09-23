
import sys
import re


class DisSet:
    def __init__(self):
        self.fg_color='31'
        self.bk_color='40'
        self.ft_type='0'
        
    def color(self,color,bkcolor,fttype='none'):
        if color=='black':
            self.fg_color='30'
        elif color=='red':
            self.fg_color='31'
        elif color=='green':
            self.fg_color='32'
        elif color=='yellow':
            self.fg_color='33'
        elif color=='blue':
            self.fg_color='34'
        elif color=='purple':
            self.fg_color='35'
        elif color=='cyan':
            self.fg_color='36'
        elif color=='white':
            self.fg_color='37'
        else:
            self.fg_color='31'
            
        if   bkcolor=='black':
            self.bk_color='40'
        elif bkcolor=='red':
            self.bk_color='41'
        elif bkcolor=='green':
            bk_color='42'
        elif bkcolor=='yellow':
            self.bk_color='43'
        elif bkcolor=='blue':
            self.bk_color='44'
        elif bkcolor=='purple':
            self.bk_color='45'
        elif bkcolor=='cyan':
            self.bk_color='46'
        elif bkcolor=='white':
            self.bk_color='47'
        else:
            self.bk_color='40'
            
        if fttype=='underline':
            self.ft_type='4'
        elif fttype=='flicker':
            self.ft_type='5'
        else:
            self.ft_type='0'
            
        self.set()
        
    def set(self):
        dis_str="\033["+self.ft_type+";"+self.fg_color+";"+self.bk_color+"m";
        print(dis_str)
        
    def reset(self):
        print("\033[0m")


display=DisSet()


if len(sys.argv) < 3:
    display.color("red","black")
    print("错误：未提供足够的参数。")
    print("用法：python.exe table.py <input.md> <output.md> ...")
    display.reset()
    sys.exit()
 
# 打印脚本名称
print("Script name:", sys.argv[0])
input_md = sys.argv[1]
output_md = sys.argv[2]
print("input file:", input_md)
print("output file:", sys.argv[2])

with open(input_md, 'r') as file:
    # 读取文件内容，并将每一行作为数组中的一个元素存储
    content = file.readlines()

line_max = len(content)

substring="------------------------------------------"
spacestring=" "
g_busy=0
table_header=[''] * 100
table_index=list(range(1, 100))
table_item=[''] * 100
table_h_line=-1
table_i_line=0
table_cols_cnt=0

with open(output_md, 'w') as file:
    for i in range(line_max):
        
        if(g_busy==0):    
            if substring in content[i]:
                display.color("yellow","black")
                print("###### Fnd long table  in line :%d" %i)
                g_busy = 1
                words = content[i+2].split()
               # global table_cols_cnt
                table_cols_cnt = len(words)
                #print("table col cnt=%d" %table_cols_cnt)
                table_h_line = i+3
                start=0
                for j in range(table_cols_cnt):
                    table_index[j]=start
                    start=content[i+2].find(' ',start)
                    start=start+1
                    #print(start)
                table_index[table_cols_cnt] = len(content[i+2])
                for j in range(table_cols_cnt):
                    t_end=table_index[j+1]
                    if(t_end>len(content[i+1])-1):
                        t_end=len(content[i+1])-1
                        #print("t_end= %d" %t_end)
                    table_header[j]=content[i+1][table_index[j]:t_end];
                    #print(table_header[j])
                    table_item[j]=""
                    
        if(g_busy==0):
            file.write(content[i]) # 正常内容，直接写入新文件
         
                    
        if(i== table_h_line): #这里输出表格的头部
            g_busy=2
            file.write("<html>")
            file.write("\t<table border=\"1\">\n")
            file.write("\t\t<tr>\n")
            for j in range(table_cols_cnt):
                file.write("\t\t\t<th>\n")
                file.write("\t\t\t\t"+table_header[j]+'\n')
                file.write("\t\t\t</th>\n");
            file.write("\t\t</tr>\n");
            
            
        if(g_busy==2):  #这里整理表格内容
            letters=re.findall('\w',content[i]) #判断是否为空行
            if(len(letters)==0):
                
                if substring in content[i]:
                    if not (spacestring  in content[i]):
                        display.color("green","black")
                        print("****** long table end in line :[%d]" %i)
                        file.write("\t</table>\n")
                        file.write("</html>")
                        g_busy = 0
                else:
                    #print("(%d)=======>" %i)
                    file.write("\t\t<tr>\n")
                    for j in range(table_cols_cnt):
                        file.write("\t\t\t<td>\n")
                        file.write("\t\t\t\t"+table_item[j]+'\n')
                        file.write("\t\t\t</td>\n");
                        table_item[j]=""
                        
                    file.write("\t\t</tr>\n");
                
            else:
                #print("(%d)---apend" %i) 
                for j in range(table_cols_cnt):
                    t_end=table_index[j+1]
                    if(t_end>len(content[i])-1):
                        t_end=len(content[i])-1
                        #print("t_end= %d" %t_end)
                    #table_item[j]=table_item[j]+content[i][table_index[j]:t_end]+"<br>\n\t\t\t\t";
                    table_item[j]=table_item[j]+content[i][table_index[j]:t_end]+"\n\t\t\t\t";
            
                    
display.color("blue","black") 
print("<script end>")                   
display.reset()              
            
