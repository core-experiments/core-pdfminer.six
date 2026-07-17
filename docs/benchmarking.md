# Benchmarking

The benchmark suite uses [Airspeed Velocity](https://asv.readthedocs.io/) to measure internal hot paths and
representative PDF extraction workloads across commits.

Install the benchmark dependencies and validate discovery:

```shell
uv sync --group benchmark
uv run --group benchmark asv check
```

Run a quick smoke benchmark against the current checkout:

```shell
uv run --group benchmark asv run --quick --show-stderr HEAD^
```

Run the complete suite for the current commit:

```shell
uv run --group benchmark asv run HEAD^
```

Compare the optimized fork against the upstream baseline:

```shell
uv run --group benchmark asv continuous upstream-baseline HEAD
```

The immutable `upstream-baseline` tag points to upstream commit
`a18de2a9c479b4c847538500017b449ddaec177e`. ASV also uses this revision as the starting point for regression
detection. Moving the `upstream/master` remote does not change existing comparisons.

The suite is split into these layers:

- parser tokenization and deep cross-reference chains;
- stream filters, predictors, text decoding, and low-level codecs;
- CMap and encoding lookup;
- character geometry, spatial indexing, and layout analysis;
- text, HTML, XML, hOCR, and tagged converter output;
- representative end-to-end extraction across simple text, CMaps, vector-heavy documents, cyclic XObjects,
  encrypted documents, academic PDFs, and malformed edge cases.

ASV writes environments, raw results, and reports below `.asv/`; those generated files are not committed.
