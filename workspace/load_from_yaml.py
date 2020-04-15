import importlib
import inspect
import logging
from pprint import pprint

from yaml import SafeLoader, load, load_all

logger = logging.getLogger("utoolbox.cli")


def main():
    src_file = "downsample.yml"
    with open(src_file, "r") as fd:
        config = list(load_all(fd, Loader=SafeLoader))

    print("dump config")
    pprint(config)
    print()

    print("looking for tasks")
    module = importlib.import_module("utoolbox.pipeline.tasks")
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(name)
    print()


if __name__ == "__main__":
    main()
