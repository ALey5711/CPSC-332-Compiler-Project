import importlib.util
import sys
from conversion import lineConversion

def import_from_path(module_to_use, file):
    spec = importlib.util.spec_from_file_location(module_to_use, file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_to_use] = module
    spec.loader.exec_module(module)
    return module
