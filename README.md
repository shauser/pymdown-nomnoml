# PyMdown pymdown_nomnoml plugin [![Build Status][travis-status]][travis-link]

*A PyMdown extension to render pymdown_nomnoml diagrams*

The pymdown_nomnoml extension will render any [superfence](superfences) using [pymdown_nomnoml](pymdown_nomnoml) into an SVG image. This provides a simple way to add diagrams in your documentation files in a readable syntax.

## Installation

Install the package with pip:

```bash
pip install pymdown-pymdown_nomnoml
```

Enable the extension in your `mkdocs.yml`:

```yaml
markdown_extensions:
    - pymdownx.superfences:
        custom_fences:
            - name: pymdown_nomnoml
              class: pymdown_nomnoml-diagram
              format: !!python/name:pymdown_nomnoml.fence_nomnoml_svg_b64
```

## Example

You can now use the nomnoml extension like this:

    # Document

    This is a short diagram

    ``` nomnoml
    [a] - [b]
    [b] -> [c]
    ```
    
When building, the code block will be replaced by an SVG version of the diagram. Note that there are some limitations of the SVG renderer.

## Contributing

From reporting a bug to submitting a pull request: every contribution is appreciated and welcome. Report bugs, ask questions and request features using [Github issues][github-issues].
If you want to contribute to the code of this project, please read the [Contribution Guidelines][contributing].

[travis-status]: https://travis-ci.org/shauser/pymdown-pymdown_nomnoml.svg?branch=master
[travis-link]: https://travis-ci.org/shauser/pymdown-pymdown_nomnoml
[github-issues]: https://github.com/shauser/pymdown-pymdown_nomnoml/issues
[contributing]: CONTRIBUTING.md
