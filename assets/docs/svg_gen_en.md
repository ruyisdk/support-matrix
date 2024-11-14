## SVG Generator

An entire SVG can be seen as a sequence of objects drawn based on absolute coordinates starting from the top-left corner. This sequence can be considered as a tree, where the root is the entire SVG, and the leaves are individual objects.

During drawing, an absolute cursor is used to track the current drawing position. Each object is drawn relative to the cursor's position. The drawing order follows a post-order traversal: after an object is drawn, the cursor moves to the **top-right corner** of that object.

Certain special objects can modify the cursor's behavior:
- `SvgLF`: Line feed, moving to a new line. The line height is determined by the tallest object in the current line.
- `SvgCR`: Resets the cursor to the beginning of the line, which is 0.
- `SvgAdvanced`: A custom object that does not draw but modifies the cursor, useful for setting line height or moving the cursor to a relative position (e.g., `dx=-3 -> xpos-=3`).
- `SvgMoveTo`: Ignores all the above rules and directly moves the cursor to a specified position, starting a new line.

Here is an example of a "Hello World" SVG:

```python
from svg_gen import *

xml = SvgXml()
svg = SvgSvg()

text = SvgText("Hello World!")
text_bg = SvgRectContainer(fill='rgb(128, 128, 128)')
text_bg.add(text)

text_height = text_bg.height
text_width = text_bg.width + 2 # 2 is the sum of width of borders

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

This example demonstrates the creation of an SVG with a "Hello World!" text, including borders around it.