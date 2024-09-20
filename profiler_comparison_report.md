# Profiler Comparison Report

## Polars Profiler Output

```

  _     ._   __/__   _ _  _  _ _/_   Recorded: 15:20:23  Samples:  48
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.066     CPU time: 0.069
/   _/                      v4.7.3

Profile at /Users/kaisenyao/Desktop/Polars_descriptive/test.py:33

0.066 <module>  test.py:1
|- 0.045 read_dataset_pl  main.py:13
|  `- 0.045 wrapper  polars/_utils/deprecation.py:86
|        [114 frames hidden]  polars, fsspec, importlib, pathlib, <...
`- 0.021 generate_summary_pl  main.py:28
   |- 0.018 DataFrame.to_pandas  polars/dataframe/frame.py:2296
   |     [4 frames hidden]  polars, pyarrow, <built-in>
   |        0.017 Version  pyarrow/vendored/version.py:301
   |- 0.002 wrapper  pandas/util/_decorators.py:325
   |     [6 frames hidden]  pandas, <built-in>
   `- 0.001 DataFrame.describe  polars/dataframe/frame.py:4831
         [3 frames hidden]  polars, <built-in>


```

## Pandas Profiler Output

```

  _     ._   __/__   _ _  _  _ _/_   Recorded: 15:20:23  Samples:  9
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.010     CPU time: 0.010
/   _/                      v4.7.3

Profile at /Users/kaisenyao/Desktop/Polars_descriptive/test.py:43

0.009 <module>  test.py:1
|- 0.008 generate_summary_pd  main.py:20
|  |- 0.004 DataFrame.__repr__  pandas/core/frame.py:1204
|  |     [43 frames hidden]  pandas, re
|  |- 0.003 DataFrame.describe  pandas/core/generic.py:11734
|  |     [15 frames hidden]  pandas
|  `- 0.001 [self]  main.py
`- 0.001 read_dataset_pd  main.py:6
   `- 0.001 read_csv  pandas/io/parsers/readers.py:868
         [3 frames hidden]  pandas


```
