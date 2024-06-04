import importlib
import logging
import os
import re
import subprocess
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')

# Just need matplotlib and numpy :)
subprocess.check_output([sys.executable, "-m", "pip", "install", 'numpy', 'matplotlib'])
subprocess.check_output([sys.executable, "-m", "pip", "install", 'proplot', '--no-dependencies'])

proplot_path = importlib.machinery.PathFinder().find_spec('proplot').submodule_search_locations[0]

def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, open(f"{file}.bak", "w", encoding="utf-8") as f2:
        txt = f1.read()
        changed_txt = re.sub(old_str, new_str, txt, re.S | re.M)
        f2.write(changed_txt)

    os.remove(file)
    os.rename(f"{file}.bak", file)

ori_path_1 = os.path.join(proplot_path, 'colors.py')
ori_str_1 = \
"""    attr = '_cmap_registry' if hasattr\(mcm, '_cmap_registry'\) else 'cmap_d'"""
new_str_1 = \
"""    # attr = '_cmap_registry' if hasattr(mcm, '_cmap_registry') else 'cmap_d'
    attr = '_colormaps' if hasattr(mcm, '_colormaps') else 'cmap_d'"""

ori_path_2 = os.path.join(proplot_path, 'figure.py')
ori_str_2 = \
"""        if self\._cachedRenderer:
            renderer = self\._cachedRenderer"""
new_str_2 = \
"""        # if self._cachedRenderer:
        # renderer = self._cachedRenderer
        # if self.canvas._get_renderer():
        # renderer = self.canvas._get_renderer()
        # else:
        canvas = self.canvas
        if canvas and hasattr(canvas, 'get_renderer'):
            renderer = canvas.get_renderer()"""

ori_path_3 = os.path.join(proplot_path, 'figure.py')
ori_str_3 = \
"""            canvas = self\.canvas
            if canvas and hasattr\(canvas, 'get_renderer'\):
                renderer = canvas\.get_renderer\(\)
            else:
                from matplotlib\.backends.backend_agg import FigureCanvasAgg
                canvas = FigureCanvasAgg\(self\)
                renderer = canvas\.get_renderer\(\)"""
new_str_3 = \
"""            # from matplotlib.backends.backend_agg import FigureCanvasAgg
            # canvas = FigureCanvasAgg(self)
            # renderer = canvas.get_renderer()
            from matplotlib import backend_bases
            renderer = backend_bases._get_renderer(self)"""

ori_path_4 = os.path.join(proplot_path, 'internals/rcsetup.py')
ori_str_4 = "CMAPSEQ = 'Fire'"
new_str_4 = "CMAPSEQ = 'magma'"
ori_path_5 = os.path.join(proplot_path, '__init__.py')
ori_str_5 = "import pkg_resources as pkg"
new_str_5 = "import importlib_metadata"

ori_path_6 = os.path.join(proplot_path, '__init__.py')
ori_str_6 = \
"""try:
    version = __version__ = pkg\.get_distribution\(__name__\)\.version
except pkg\.DistributionNotFound:
    version = __version__ = 'unknown'"""
new_str_6 = "version = __version__ = importlib_metadata.metadata('proplot').get('version')"

alter(ori_path_1, ori_str_1, new_str_1)
alter(ori_path_2, ori_str_2, new_str_2)
alter(ori_path_3, ori_str_3, new_str_3)
alter(ori_path_4, ori_str_4, new_str_4)
alter(ori_path_5, ori_str_5, new_str_5)
alter(ori_path_6, ori_str_6, new_str_6)

try:
    proplot = importlib.import_module('proplot')
    print(f"proplot安装成功 version: {proplot.__version__}")
except Exception as e:
    print(f"proplot安装失败: {e}")