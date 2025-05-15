# type: ignore
import sys, pathlib
sys.path.append("/home/sebastian.cavada/Documents/scsv/tiny_experiment/tinygrad")
sys.path.append(pathlib.Path(__file__).parent.as_posix())
sys.path.append(pathlib.Path(__file__).parent.parent.as_posix())
try: import extra.torch_backend.backend  # noqa: F401 # pylint: disable=unused-import
except ImportError as e: raise ImportError("torch frontend not in release\nTo fix, install tinygrad from a git checkout with pip install -e .") from e