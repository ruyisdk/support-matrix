# pylint: disable=unused-import, wildcard-import, unused-wildcard-import
"""
Prelude for upload plugins.
"""

import logging
logger = logging.getLogger(__name__)

try:
    from src.ruyi_index_updator.ruyi_index_parser import *
    from src.matrix_parser import VInfo
    from src.ruyi_index_updator.upload_plugin_base import UploadPluginBase
except ModuleNotFoundError:
    # Things above is used for type hinting
    # when the module is used as a plugin, load will fail
    pass
