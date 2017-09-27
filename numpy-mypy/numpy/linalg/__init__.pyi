from typing import Tuple, Any, Union
from .. import _ArrayLike, ndarray, Scalar


def eigh(a: _ArrayLike[Scalar],
         UPTO: str = 'L') -> Tuple[ndarray[Scalar], ndarray[Scalar]]:
    ...


def pinv(a: _ArrayLike[Scalar], rcond: float = 1e-15) -> ndarray[Scalar]:
    ...


def svd(a: _ArrayLike[Scalar], full_matrices: bool = True, compute_uv: bool = True
        ) -> Tuple[ndarray[Scalar], ndarray[Scalar], ndarray[Scalar]]:
    ...


def norm(x: _ArrayLike[Scalar],
         ord: Any = None,
         axis: Any = None,
         keepdims: bool = False) -> Union[float, ndarray[float]]:
    ...
