"""
SVG image generator for support matrix tables.
Generates SVG tables with color-coded status information.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Callable, Any, Dict, List, Union
from urllib.parse import urljoin

try:
    from src.svg_gen import SvgConf, SvgNode, SvgXml, gen_html, putconf, SvgRectContainer
    from src.svg_gen import SvgText, SvgTextCenter, SvgMoveTo, SvgCR, SvgLF, SvgGroup
    from src.svg_gen import SvgAdvancer, SvgSvg, SvgLine, SvgLink
    from src.matrix_parser import Systems
except ImportError as e:
    # Try alternative import path
    try:
        sys.path.append(str(Path(__file__).parent / 'src'))
        from svg_gen.svg_gen import SvgConf, SvgNode, SvgXml, gen_html, putconf, SvgRectContainer
        from svg_gen.svg_gen import SvgText, SvgTextCenter, SvgMoveTo, SvgCR, SvgLF, SvgGroup
        from svg_gen.svg_gen import SvgAdvancer, SvgSvg, SvgLine, SvgLink
        from matrix_parser import Systems
    except ImportError:
        logging.error(f"Failed to import required modules: {e}")
        logging.error("Make sure the required modules are available in the Python path")
        sys.exit(1)

# Configuration constants
DEFAULT_BG_COLOR = 'rgb(255, 128, 255)'
DEFAULT_HEAD_BG_COLOR = 'rgb(200, 200, 200)'
SUPPORTED_LANGUAGES = ['en', 'zh']


def gen_svg_table(conf: SvgConf, systems: Systems, need_systems: Dict[str, str],
                  link_func: Callable[[Any, Any, object], Union[str, None]],
                  color_func: Callable[[Any, Any, object], str]) -> SvgNode:
    """
    Generate an SVG table with the given systems.
    
    Args:
        conf: SVG configuration object
        systems: System data container
        need_systems: Dictionary mapping system keys to display names
        link_func: Function to generate links for cells
        color_func: Function to determine cell colors
    
    Returns:
        SvgNode: Complete SVG document node
    """
    putconf(conf)

    table = []

    head_row = [
        "CPU",
        "IP Core",
        "Product/Model",
    ]
    for i in need_systems.values():
        head_row.append(i)
    head_group = []
    for idx, i in enumerate(head_row):
        t = SvgText(i, True)
        head_group.append(t)
    table.append(head_group)

    for board in systems.boards:
        syscnt = 0
        for system in board.systems:
            if system.sys in need_systems.keys():
                syscnt += 1
        if syscnt == 0:
            continue

        board_group = []

        board_cpu_t = SvgText(board.cpu, False)
        board_group.append(board_cpu_t)

        board_ip_t = SvgText(board.cpu_core, False)
        board_group.append(board_ip_t)

        board_prod_t = SvgText(board.product, False)
        board_group.append(board_prod_t)

        for sys in need_systems.keys():
            flag = False
            for system in board.systems:
                if system.sys != sys:
                    continue
                flag = True
                if len(system.variant) == 1:
                    sys_t = SvgText(
                        str(system.variant[0].status), False)
                    # Use python's dynamic feature to add link without modifying the class
                    sys_t.link = system.variant[0].link
                    board_group.append(sys_t)
                    break
                var_g = []
                for var in system.variant:
                    sys_var = var.sys_var if var.sys_var is not None else "main"
                    sys_t = SvgText(sys_var + ': ' +
                                    str(var.status), False)
                    # Same as above
                    sys_t.link = var.link
                    var_g.append(sys_t)
                board_group.append(var_g)
                break
            if not flag:
                sys_t = SvgText("-", False)
                board_group.append(sys_t)
        table.append(board_group)

    col_width = [0] * len(head_row)
    for row in table:
        for idx, i in enumerate(row):
            if isinstance(i, list):
                for j in i:
                    col_width[idx] = max(col_width[idx], j.width())
            else:
                col_width[idx] = max(col_width[idx], i.width())

    row_height = [0] * len(table)
    for idx, row in enumerate(table):
        for i in row:
            if isinstance(i, list):
                row_height[idx] = max(row_height[idx],
                                      (conf.line_height() + conf.padding_y * 2) *
                                      len(i) + conf.stroke_width * (len(i) - 1))
            else:
                row_height[idx] = max(
                    row_height[idx], conf.line_height() + conf.padding_y * 2)

    doc = SvgXml()
    svg = SvgSvg()

    bg = SvgRectContainer(DEFAULT_BG_COLOR)

    top_border = SvgLine(
        sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
        stroke_width=conf.stroke_width * 2)
    bg.add_child(top_border)
    bg.add_child(SvgCR())
    bg.add_child(SvgLF())

    # Head:
    head_bg = SvgRectContainer(DEFAULT_HEAD_BG_COLOR)
    for idx, i in enumerate(table[0]):
        a = SvgAdvancer(conf.stroke_width * 2 if idx ==
                        0 else conf.stroke_width, 0)
        t = SvgTextCenter(i.text, col_width[idx], 0, True)
        g = SvgGroup()
        g.add_child(a)
        g.add_child(t)
        head_bg.add_child(g)
    head_bg.add_child(SvgCR())
    head_bg.add_child(SvgLF())

    bg.add_child(head_bg)
    bg.add_child(SvgCR())
    bg.add_child(SvgLF())

    # Now the data
    for rdx, row in enumerate(table[1:]):
        border = SvgLine(
            sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
            stroke_width=conf.stroke_width)
        bg.add_child(border)
        bg.add_child(SvgCR())
        bg.add_child(SvgLF())

        row_g = SvgGroup()
        for idx, i in enumerate(row):

            a = SvgAdvancer(conf.stroke_width * 2 if idx ==
                            0 else conf.stroke_width, 0)
            g = SvgGroup()
            g.add_child(a)

            if isinstance(i, list):
                var_g = SvgGroup()

                for jdx, j in enumerate(i):

                    link = link_func(None, None, j)
                    if link is not None:
                        t_lk = SvgLink(link)
                    else:
                        t_lk = SvgGroup()

                    t_bg = SvgRectContainer(color_func(None, idx, j.text))
                    t = SvgTextCenter(j.text, col_width[idx], 0, False)

                    t_bg.add_child(t)
                    t_lk.add_child(t_bg)
                    var_g.add_child(t_lk)

                    if jdx < len(i) - 1:

                        a = SvgAdvancer(-t.width(), 0)
                        var_g.add_child(a)
                        var_g.add_child(SvgLF())

                        b = SvgLine(
                            t.width(), 0,
                            stroke_color='rgb(128,128,128)', stroke_width=conf.stroke_width)
                        var_g.add_child(b)

                        a = SvgAdvancer(-b.width(), 0)
                        var_g.add_child(a)
                        var_g.add_child(SvgLF())

                g.add_child(var_g)
            else:
                link = link_func(None, None, i)

                if link is not None:
                    t_lk = SvgLink(link)
                else:
                    t_lk = SvgGroup()

                color = color_func(None, idx, i.text)
                t_bg = SvgRectContainer(color)
                t = SvgTextCenter(
                    i.text, col_width[idx], row_height[rdx + 1], False)

                t_bg.add_child(t)
                t_lk.add_child(t_bg)
                g.add_child(t_lk)

            row_g.add_child(g)
        bg.add_child(row_g)
        bg.add_child(SvgCR())
        bg.add_child(SvgLF())

    # Bottom border
    bottom_border = SvgLine(
        sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
        stroke_width=conf.stroke_width * 2)
    bg.add_child(bottom_border)

    # # Set the vertical lines
    svg_height = bg.height()
    bg.add_child(SvgMoveTo(0, 0))
    for idx, i in enumerate(col_width):
        bg.add_child(SvgLine(0, svg_height, stroke_width=conf.stroke_width *
                     2 if idx == 0 else conf.stroke_width))
        bg.add_child(SvgAdvancer(i, 0))
    bg.add_child(SvgLine(0, svg_height, stroke_width=conf.stroke_width * 2))

    svg.add_child(bg)
    doc.add_child(svg)

    return doc

def proc_onesys(system_arr: Dict[str, str], system: Systems,
                link_func: Callable[[Any, Any, object], Union[str, None]],
                color_func: Callable[[Any, Any, object], str]) -> SvgNode:
    """
    Process one type of system and generate SVG table.
    
    Args:
        system_arr: Dictionary of systems to process
        system: Systems data container
        link_func: Function to generate links
        color_func: Function to determine colors
    
    Returns:
        SvgNode: Generated SVG table
    """
    conf = SvgConf()
    return gen_svg_table(conf, system, system_arr, link_func, color_func)

def gen_color(_, col: int, content: str) -> str:
    """
    Generate color based on content status.
    
    Args:
        _: Unused parameter (kept for compatibility)
        col: Column index
        content: Cell content string
    
    Returns:
        str: RGB color string
    """
    # Reason: First 3 columns are metadata (CPU, IP Core, Product/Model)
    if col < 3:
        return 'rgb(226, 232, 240)'  # slate
    
    # Extract status from content (format: "variant: status")
    status = content.split(':')[-1].strip()

    color_map = {
        "Good": 'rgb(184, 230, 254)',   # blue
        "Basic": 'rgb(185, 248, 207)',  # green
        "CFH": 'rgb(255, 201, 201)',    # red
        "CFT": 'rgb(229, 231, 235)',    # gray
        "WIP": 'rgb(246, 207, 255)',    # fuchsia
        "CFI": 'rgb(255, 240, 133)',    # yellow
    }
    return color_map.get(status, 'rgb(249, 250, 251)')  # white as default

def gen_gen_link(lang: str) -> Callable[[Any, Any, object], Union[str, None]]:
    """
    Generate a link generator function for the specified language.
    
    Args:
        lang: Language code ('en', 'zh', etc.)
    
    Returns:
        Function that generates links for table cells
    
    Raises:
        ValueError: If language is not supported
    """
    if lang not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {lang}. Supported: {SUPPORTED_LANGUAGES}")
    
    lang_end = ".md" if lang == "en" else f"_{lang}.md"

    def gen_link(_, __, content) -> Union[str, None]:
        """Generate link URL for content object."""
        if not hasattr(content, 'link') or content.link is None:
            return None
        
        try:
            url = "https://github.com/ruyisdk/support-matrix/tree/main/"
            for i in content.link:
                if i.endswith('.md'):
                    i = i[:-3] + lang_end
                url = urljoin(url + '/', i)
            return url
        except (AttributeError, TypeError) as e:
            logging.warning(f"Failed to generate link for content: {e}")
            return None
    
    return gen_link


def _write_svg_files(systems_dict: Dict[str, Any], systems: Systems, 
                    link_func: Callable, color_func: Callable,
                    output_dir: Path, file_suffix: str, html_path: Union[str, None]) -> None:
    """
    Write SVG and HTML files for all system types.
    
    Args:
        systems_dict: Dictionary of system types to process
        systems: Systems data container  
        link_func: Function to generate links
        color_func: Function to determine colors
        output_dir: Output directory path
        file_suffix: File suffix for localization
        html_path: HTML output path (optional)
    """
    for system_type, system_data in systems_dict.items():
        try:
            svg = proc_onesys(system_data, systems, link_func, color_func)
            
            # Write SVG file
            svg_file = output_dir / f'{system_type}{file_suffix}.svg'
            with open(svg_file, 'w', encoding="utf-8") as f:
                f.write(str(svg))
            logging.info(f"Generated SVG: {svg_file}")
            
            # Write HTML file if requested
            if html_path:
                html_file = output_dir / f'{system_type}{file_suffix}.html'
                svg_path = os.path.join(html_path, f'{system_type}{file_suffix}.svg')
                with open(html_file, 'w', encoding="utf-8") as f:
                    f.write(gen_html(svg, svg_path))
                logging.info(f"Generated HTML: {html_file}")
                    
        except Exception as e:
            logging.error(f"Failed to generate {system_type} files: {e}")
            raise


def main() -> None:
    """
    Main function to generate SVG images for support matrix.
    """
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    parser = argparse.ArgumentParser(
        description="Generate SVG tables for support matrix",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-p', '--path', dest="path",
                        help="Support matrix path", type=str, default='..')
    parser.add_argument('-o', '--output', dest="output",
                        help="Output directory path", type=str, default='output')
    parser.add_argument('-l', '--lang', dest="lang",
                        help=f"Language ({'/'.join(SUPPORTED_LANGUAGES)})", 
                        type=str, default='en', choices=SUPPORTED_LANGUAGES)
    parser.add_argument('--html', dest="html",
                        help="Output HTML files with SVG assets at specified path", 
                        type=str, default=None)

    try:
        args = parser.parse_args()
        
        # Validate and setup paths
        input_path = Path(args.path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input path does not exist: {input_path}")
        
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Load systems data
        logging.info(f"Loading systems data from: {input_path}")
        systems = Systems(str(input_path))
        
        # Setup functions
        color_func = gen_color
        link_func = gen_gen_link(args.lang)
        
        # Generate file suffix for localization
        file_suffix = "" if args.lang == "en" else f"_{args.lang}"
        
        # Define system types to process
        systems_to_process = {
            'linux': systems.linux,
            'bsd': systems.bsd, 
            'rtos': systems.rtos,
            'others': systems.others,
            'customized': systems.customized
        }
        
        # Generate all SVG and HTML files
        logging.info("Starting SVG generation...")
        _write_svg_files(systems_to_process, systems, link_func, color_func,
                        output_dir, file_suffix, args.html)
        
        logging.info(f"Successfully generated all files in: {output_dir}")
        
    except Exception as e:
        logging.error(f"Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
