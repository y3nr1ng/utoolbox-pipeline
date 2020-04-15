import logging
from prefect import Task
from typing import Tuple

"""
NOTE 
how to assign dask resource requirements?
    prefect.engine.executors.dask, L86, _prep_dask_kwargs

add tag "dask-resource:process=1" -> "{'process': 1}"
"""

__all__ = ["DiscreteStepBinning"]

logger = logging.getLogger("utoolbox.pipeline.tasks")


class Binning(Task):
    def __init__(self, bin_shape, **kwargs):
        self.bin_shape = bin_shape
        super().__init__(**kwargs)

    def run(self, array):
        raise NotImplementedError


class DiscreteStepBinning(Binning):
    """
    Select every Nth pixel along each axis.
    """

    def run(self, array):
        slices = self._build_slices(array.ndim)
        return array[slices]

    ##

    def _build_slices(self, ndim: int) -> Tuple[slice]:
        """
        Build proper slice objects according to current array dimension.
        
        Args:
            ndim (int): number of dimensions
        """
        if isinstance(self.bin_shape, tuple):
            n = len(self.bin_shape)
            if n > ndim:
                logger.warning("ignore excessive binning specifications")
                bin_shape = self.bin_shape[-ndim:]
            elif n < ndim:
                logger.warning("additional axes are not binned")
                bin_shape = (None,) * (ndim - n) + self.bin_shape
            else:
                bin_shape = self.bin_shape
        else:
            # assuming all axes share the same binning factor
            bin_shape = (self.bin_shape,) * ndim
        return tuple(slice(None, None, step) for step in bin_shape)
