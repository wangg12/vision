from __future__ import annotations

from typing import Any, Optional, Union

import torch

from ._datapoint import Datapoint


class Video(Datapoint):
    """[BETA] :class:`torch.Tensor` subclass for videos.

    Args:
        data (tensor-like): Any data that can be turned into a tensor with :func:`torch.as_tensor`.
        dtype (torch.dtype, optional): Desired data type of the bounding box. If omitted, will be inferred from
            ``data``.
        device (torch.device, optional): Desired device of the bounding box. If omitted and ``data`` is a
            :class:`torch.Tensor`, the device is taken from it. Otherwise, the bounding box is constructed on the CPU.
        requires_grad (bool, optional): Whether autograd should record operations on the bounding box. If omitted and
            ``data`` is a :class:`torch.Tensor`, the value is taken from it. Otherwise, defaults to ``False``.
    """

    def __new__(
        cls,
        data: Any,
        *,
        dtype: Optional[torch.dtype] = None,
        device: Optional[Union[torch.device, str, int]] = None,
        requires_grad: Optional[bool] = None,
    ) -> Video:
        tensor = cls._to_tensor(data, dtype=dtype, device=device, requires_grad=requires_grad)
        if data.ndim < 4:
            raise ValueError
        return cls._wrap(tensor)

    def __repr__(self, *, tensor_contents: Any = None) -> str:  # type: ignore[override]
        return self._make_repr()


_VideoType = Union[torch.Tensor, Video]
_VideoTypeJIT = torch.Tensor
_TensorVideoType = Union[torch.Tensor, Video]
_TensorVideoTypeJIT = torch.Tensor
