# Gramex Layout

Layout algorithms for visualizations.

- Calendar (pending)
- Sankey (pending)
- Sunburst (complete, to be documented)
- Treemap (pending)

[NOTE]: This is a pre-release to test the build process.


# Setup

Documentation was set up via

```shell
pip install sphinx myst-parser sphinx-book-theme
mkdir docs
cd docs
sphinx-quickstart
sphinx-apidoc -o source/ ../gramexlayout
```

Then:

- In `docs/conf.py`
  - Set `html_theme = 'sphinx_book_theme'

To release, set up build and twine

```shell
pip install build twine
```

# Release

Release source on PyPI:

```shell
python -m build --wheel
twine upload dist/*
```

Create documentation:

```shell
cd docs
make html
```
