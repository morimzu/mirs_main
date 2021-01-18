# 自己位置の保存，更新モジュール
Num = 1 #消毒したい机の数

def my_position(pos):
    if pos == Num:
        return True, pos
    else:
        pos += 1
        return  False, pos