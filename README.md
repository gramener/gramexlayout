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
sphinx-quickstart --project gramexlayout --author "Anand S" --release 0.1.0 --language en --suffix .md --suffix .rst --no-batchfile --no-sep --ext-autodoc --extensions myst_parser
sphinx-apidoc --no-toc --module-first --output-dir . ../gramexlayout
```

Then:

- In `docs/conf.py`
  - Set `html_theme = 'sphinx_book_theme'

To release, set up build and twine

```shell
pip install build twine
```

# Release

Update the version number in `setup.py`. Then:

```shell
git commit . -m"BLD: Release version x.x.x"
git push
```

Release source on PyPI:

```shell
rm -rf dist/
python -m build --wheel
twine upload dist/*
```

Create documentation:

```shell
cd docs
make html
```
