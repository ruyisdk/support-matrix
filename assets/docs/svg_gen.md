## svg gen

整个 SVG 可以被看成根据一个左上角绝对坐标绘制各个 object 的序列。这个序列可以被看成一个树，树的根是整个 SVG，树的叶子是各个 object。

而在绘制时，采用一个绝对游标，记录当前绘制的位置，每个 object 都是相对于游标的位置绘制的。绘制顺序采用后序遍历，绘制完一个 object 后，游标会被移动到 object 的**右上角**。

一些特殊的 object 会改变游标的绘制方式：
- `SvgLF`：换行，行高定义为当前行最高的 object 的高度
- `SvgCR`：重置游标到 0
- `SvgAdvanced`：自定义一个不绘制但是会改变游标的 object，用于设置行高或将游标移动到某个相对位置（如 dx=-3 -> xpos-=3）
- `SvgMoveTo`：忽略以上所有规则，直接移动游标到指定位置，新起一行

如下是一个 Hello World 的例子：
```python
from svg_gen import *

xml = SvgXml()
svg = SvgSvg()

text = SvgText("Hello World!")
text_bg = SvgRectContainer(fill='rgb(128, 128, 128)')
text_bg.add(text)

text_height = text_bg.height
text_width = text_bg.width + 2 # 2 为两个边框的宽度

border_top = SvgLine(text_width, 0)
svg.add(border_top)
svg.add(SvgCR())
svg.add(SvgLF())

border_left = SvgLine(0, text_height)
svg.add(border_left)

svg.add(text_bg)
border_right = SvgLine(0, text_height)
svg.add(border_right)

svg.add(SvgCR())
svg.add(SvgLF())

border_bottom = SvgLine(text_width, 0)
svg.add(border_bottom)

xml.add(svg)

xml.generate()
```