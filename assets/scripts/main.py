#!/usr/bin/env python3
"""
Parse metadata of systems and boards
"""
import os
import argparse
import yaml
import frontmatter

from csv2svg import gen_html, SvgConf, gen_svg_table


class System:
    """
    eg:
    ---
    sys: deepin
    sys_ver: 23
    sys_var: null

    status: basic
    last_update: 2024-06-21
    ---
    """
    sys: str
    sys_ver: str | None
    sys_var: str | None
    status: str
    last_update: str
    link: str | None

    def strip(self):
        """
        dummy for strip the system
        """
        return self

    def __str__(self):
        return status_map(self.status)

    def __len__(self):
        return len(status_map(self.status))

    def __init_by_file(self, path, base_link=""):
        base_name = os.path.basename(path)
        self.link = os.path.join(base_link, base_name)
        meta_path = os.path.join(path, 'README.md')
        with open(meta_path, 'r', encoding="utf-8") as file:
            post = frontmatter.load(file)
            if 'sys' not in post.keys():
                print(f"Error: {path} has no frontmatter")
                return
            if post['sys'] == 'revyos':
                self.sys = 'debian'
            else:
                self.sys = post['sys']
            self.sys_ver = post['sys_ver']
            self.sys_var = post['sys_var']
            self.status = post['status']
            self.last_update = post['last_update']

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.sys = kwargs['sys']
            self.sys_ver = kwargs['sys_ver']
            self.sys_var = kwargs['sys_var']
            self.status = kwargs['status']
            self.last_update = kwargs['last_update']
            self.link = kwargs['link']
        else:
            self.__init_by_file(*args, **kwargs)


def status_map(status: str):
    """
    map status to pretty string
    """
    if status == 'wip':
        return 'WIP'
    if status == 'cft':
        return 'CFT'
    if status == 'cfh':
        return 'CFH'
    if status == 'basic':
        return 'Basic'
    if status == 'good':
        return 'Good'
    return status


class Board:
    """
    a collection of systems and eg:
    ---
    product: VisionFive 2
    cpu: JH7110
    cpu_core: SiFive U74 + SiFive S7 + SiFive E24
    ---
    """
    product: str
    cpu: str
    link: str
    cpu_core: str
    systems: list[System]

    def append_system(self, system: System):
        """
        append a system to the board
        """
        self.systems.append(system)

    def gen_row(self, system_arr: dict[str]):
        """
        generate a row of the table
        """
        row = [
            self.cpu,
            self.cpu_core,
            self.link,
            self
        ]

        na_count = 0

        for k, _ in system_arr.items():
            for system in self.systems:
                if system.sys == k:
                    row.append(system)
                    break
            else:
                row.append('N/A')
                na_count += 1

        if na_count == len(system_arr):
            return None

        return row

    def strip(self):
        """
        dummy for strip the board
        """
        self.product = self.product.strip()
        return self

    def __str__(self):
        return self.product

    def __len__(self):
        return len(self.product)

    def __init__(self, path: str):
        base_name = os.path.basename(path)
        self.link = base_name
        readme_path = os.path.join(path, 'README.md')
        with open(readme_path, 'r', encoding="utf-8") as file:
            post = frontmatter.load(file)
            self.product = post['product']
            self.cpu = post['cpu']
            self.cpu_core = post['cpu_core']
        self.systems = []

        for folder in os.listdir(path):
            if os.path.isdir(os.path.join(path, folder)):
                system = System(os.path.join(path, folder), self.link)
                self.append_system(system)

        if os.path.exists(os.path.join(path, 'others.yml')):
            with open(os.path.join(path, 'others.yml'), 'r', encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
                for i in data:
                    system = System(
                        sys=i['sys'],
                        sys_ver=i['sys_ver'],
                        sys_var=i['sys_var'],
                        status=i['status'],
                        last_update='2000-00-00',
                        link=None
                    )
                    self.append_system(system)


class Systems:
    """
    support matrix of systems
    """
    linux: dict[str]
    bsd: dict[str]
    rtos: dict[str]
    others: dict[str]

    exclude_dir = [
        'assets',
        '.git',
        '.vscode',
        '__pycache__',
    ]
    boards: list[Board]

    def __init__(self, path):
        meta_path = os.path.join(path, 'assets', 'metadata.yml')
        with open(meta_path, 'r', encoding="utf-8") as file:
            def mp(x):
                res = {}
                for l in x:
                    for i in l.items():
                        res[i[0]] = i[1]
                return res
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.linux = mp(data['linux'])
            self.bsd = mp(data['bsd'])
            self.rtos = mp(data['rtos'])
            self.others = mp(data['others'])
        self.boards = []
        for folder in os.listdir(path):
            if folder in self.exclude_dir:
                continue
            p = os.path.join(path, folder)
            if os.path.isdir(p):
                board = Board(p)
                self.boards.append(board)


def gen_color(_, col, content):
    """
    gen svg color
    """
    white = (255, 255, 255)
    gray = (220, 220, 220)
    green = (203, 255, 203)
    yellow = (255, 255, 203)
    red = (255, 203, 203)
    if col < 3:
        return white
    if "Good" == str(content) or "Basic" == str(content):
        return green
    if "CFT" == str(content):
        return yellow
    if "WIP" == str(content) or "CFH" == str(content):
        return red
    return gray


def gen_link(_, __, content):
    """
    gen link
    """
    if hasattr(content, 'link') and content.link is not None:
        return f"https://github.com/ruyisdk/support-matrix/tree/main/{content.link}"
    return None


def proc_onesys(system_arr: dict[str], system: System):
    """
    process one type of system
    """
    head = ['CPU', 'IP Core', 'link', 'Product/Model']
    for _, v in system_arr.items():
        head.append(v)
    data = []
    for board in system.boards:
        row = board.gen_row(system_arr)
        if row is not None:
            data.append(row)
    data = sorted(data, key=lambda x: str(x[2]).strip())

    svg_head = head[:2] + head[3:]
    svg_data = [row[:2] + row[3:] for row in data]
    conf = SvgConf(
        color_gen_func=gen_color,
        link_gen_func=gen_link,
    )
    res = gen_svg_table(conf, svg_head, svg_data)

    return res

def main():
    """
    main
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest="path",
                        help="support matrix path", type=str, default='.')
    parser.add_argument('-o', '--output', dest="output",
                        help="output path", type=str, default='.')
    parser.add_argument('--html', dest="html",
                        help="output html, with svg assets at arg", type=str, default=None)

    args = parser.parse_args()

    p = args.path
    systems = Systems(p)

    html_path = args.html
    svg = proc_onesys(systems.linux, systems)
    with open(os.path.join(args.output, 'linux.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'linux.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'linux.svg')))
    svg = proc_onesys(systems.bsd, systems)
    with open(os.path.join(args.output, 'bsd.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'bsd.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'bsd.svg')))
    svg = proc_onesys(systems.rtos, systems)
    with open(os.path.join(args.output, 'rtos.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'rtos.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'rtos.svg')))
    svg = proc_onesys(systems.others, systems)
    with open(os.path.join(args.output, 'others.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'others.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'others.svg')))


if __name__ == "__main__":
    main()
