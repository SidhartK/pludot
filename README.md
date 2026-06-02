# pludot: Polars Unstructured Data Objects and Transforms

Current approaches to using LLMs and other techniques for unstructured data analysis over dataframes treat text columns as plain strings with a bolted on model call. The missing piece is that the column of political speeches and a column of customer support tickets are both `pl.String` types in Polars, despite them being semantically quite different – and that difference should inform every operation run on them. 

## Why does this need to be reflected in the datatype?

The two core claims are:

1. This semantic information about the type is useful. It is important to understand the specific flavor of text data that you are handling. 


The core idea `pludot` introduces is a type hierarchy for text columns. Instead of `String`, a column can be `Prose`, `Code`, `Markup`, etc. 

These types carry semantic context that gets passed automatically to any model-backed operation. The intent is declared once upon type definition and the whole pipeline benefits.

