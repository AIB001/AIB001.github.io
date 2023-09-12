# Shell脚本基本命令
## shell变量
### shell变量定义
```shell
variable='value'
#shell中，变量和等号之间不能有空格
for var in `ls /etc`
for var in $(ls /etc)
#类似于python在语句中对变量赋值
#上面的雨具用于将/etc下目录的文件名循环出来
```
###shell变量的使用
```shell
var='value'
echo $var
#引用变量时需要在变量前用$,变量外的花括号在一些时候不能缺少
var1='value1'
echo $var1
var1='value2'
#对变量重新赋值
readonly var1 #设置var1成为只读变量
unset var1    #删除变量
```
### 字符转变量 
#### 定义和引用字符串
```shell
var1='value'
var2="value \"$var1\" \n"
echo $var1
echo -e $var2
#单引号字符中不能有变量，双引号变量中可以有变量，也可以有转义字符
```
#### 字符串函数
```shell
var_string="value"
echo ${#var_string}            #输出字符串函数，引用字符串首字母的指针
echo ${var_string:1:4}         #提取字符串，字符串变量从string[0]开始
echo `expr index "$string" la` #查找l和a首次出现在何处
```

### shell数组变量
#### 定义数组变量
```shell
#圆括号表示数组,下面是两种定义方式
array=(val1 val2 val3)
array1=(
val4
val5
val
)
#也可以分别定义变量
array3[0]=1
array3[1]=2
```
### 读取数组
```shell
array=(val1 val2 val3)
echo ${array[@]} #@表示阅读这个数组所有元素
```

##shell脚本传递参数
shell使用“$”来传递参数，
```shell
$# #传递参数的个数
$* #以一个字符串的形式显示传递的参数
$@ #显示所有传递参数
``` 

## 数组
### 关联数组的申明
```shell
declear -A array=(["name1"]=value1 ["name2"]=value2)
echo ${array["name1"]}
#name称为数组的建，value称为数组的值
```

### 数组相关的操作
```shell
array=(val1 val2 val3)
echo ${array[*]}
echo ${array[@]}
#获取数组所有的值
echo ${#array[@]} #获取数组的长度
```

## shell运算符
### 数学运算符
原生bash不支持数学运算，一般通过‘expr’等命令实现
```shell
var=`expr 2 + 2`
echo $var
#使用``将表达式包含
#数字和运算符之间需要用空格间隔，不然会输出字符串
a=10
b=20
var=`expr $a \* $b`
echo $var
#乘法运算需要用'\*'进行转义
```

### 布尔和逻辑运算符
+ !:  非运算
+ -o: 或运算
+ -a: 与运算
+ &&: AND
+ ||: OR
条件表达式要放在'[   ]'之间，并且要有括号
```shell
a=10
b=20
if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
```

## echo命令
echo 命令用于字符串的输出
```shell
echo "\"value\""
#echo中可以输出转移字符
read var
echo "$var"
#read从标准输入中读取一行，然后赋值给var，echo用于输出变量
echo "The Result equals to" > "file path"
#echo 用于将命令输出到指定路径的文件
```

## printf命令
printf是一个仿照C语言中printf的命:%s %c %d %f 都是格式替代符，％s 输出一个字符串，％d 整型输出，％c 输出一个字符，％f 输出实数，以小数形式输出.
```shell
printf "%-10s %-5d %-4.2f"
#-10是左对齐占据10个字符
#-4.2表示左对齐占据4个字符，保留两个小数点
```

### shell流程控制
#### 一般条件判断
```shell
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi
```
#### case条件语句
```shell
case judge_value in
mode1)
    command1
    command2
    ...
    commandN
    ;;
mode2)
    command1
    command2
    ...
    commandN
    ;;
esac

```
#### for循环
```shell
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```
#### while循环
```shell
while condition
do
    command
done
```
## shell函数
```shell
[ function ] funname [()]

{

    action;

    [return int;]

}
```

## shell文件包含
```shell
source filemname #包含外部脚本
```
