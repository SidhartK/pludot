import polars as pl
from .dtypes.text import Text

def cast(col: str | pl.Expr, dtype: type[Text]) -> pl.Expr:
    expr = pl.col(col) if isinstance(col, str) else col
    return expr.cast(pl.String).map_elements(dtype, return_dtype=pl.Object)