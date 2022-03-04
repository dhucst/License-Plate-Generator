"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
from collections import namedtuple
from itertools import chain

import tokens
from license_plate import TokenSet

Pattern = namedtuple(
    'Pattern', ['size', 'background_file', 'token_sets', 'locations', 'colors'])

# 蓝牌140

# 一个车牌包含几个字符？
size = 7

# 每一位字符可以使用的的字符组
mixed = list(chain(tokens.ALPHABETS, tokens.DIGITS))
targets = [tokens.PROVINCES, tokens.ALPHABETS,
           mixed, mixed, mixed, mixed, mixed]

# 每一位字符的位置：左上角的像素坐标
locations = [(15, 25), (72, 25), (151, 25), (208, 25),
             (265, 25), (322, 25), (379, 25)]

# 每一位字符的颜色(BGR)
colors = [(255, 255, 255), (255, 255, 255), (255, 255, 255),
          (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255)]

# 字符图像的存储位置
token_dir = 'assets/tokens/condensed-0'

# 背景图像的路径
background_file = 'assets/background/blue/140.png'

assert len(targets) == size, f"Token长度{len(targets)}不等于{size}。"
assert len(locations) == size, f"位置长度{len(locations)}不等于{size}。"
assert len(colors) == size, f"色彩长度{len(colors)}不等于{size}。"

BLUE = Pattern(
    size=7,
    background_file=background_file,
    token_sets=[TokenSet(chars, token_dir) for chars in targets],
    locations=locations,
    colors=colors)
