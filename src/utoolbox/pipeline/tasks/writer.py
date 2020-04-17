import logging
from prefect import Task
from typing import Optional

__all__ = ["ZarrWriter"]

logger = logging.getLogger("utoolbox.pipeline.tasks")


class Writer(Task):
    def __init__(self):
        pass

    def run(self, store: str, data):
        raise NotImplementedError


class ZarrWriter(Writer):
    def __init__(self):
        pass

    def run(self, store: str, data, path: Optional[str] = None):
        """
        Args:
            store (str): path to the store directory in file system
            data : the data to save
            path (str, optional): group path within the store
        """
        pass

    ##

    def _write_dask_array(self):
        pass

    def _write_numpy_array(self):
        pass
