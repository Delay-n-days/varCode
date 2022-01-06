# 这是一个pyside2的一个用于变量翻译命名的小程序

## 修改

需要 修改 baidu_fanyi_api.py 内的  [access_token](https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu)
内置了一个免费的百度翻译api,速度可能会有点慢
```
access_token = "输入你的token"  # 输入你的token
```


## 运行

`pip install pyside2`
`python main.py`

## 可自定义替换规则

```
voltage      =>    Vol    
current      =>    Cur    
low byte     =>   _ L    
high byte    =>   _ H    
temperature  =>   Temp    
Radiator     =>   Radia    
frequency    =>   Freq    
and          =>            
of           =>            
controller   =>   Ctrl                
torque       =>   torq    
```

程序会对翻译结果进行替换

## 输入

```
    输入电压低字节
    输入电压高字节
    输出电压低字节
    输出电压高字节
    输出电流低字节
    输出电流高字节
```

## 输出

```
    InputVol_L
    InputVol_H
    OutputVol_L
    OutputVol_H
    OutputCur_L
    OutputCur_H

```
