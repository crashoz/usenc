# Contributing to usenc

Thank you for considering contributing to usenc! This document provides guidelines for contributing.

## Development Setup

1. Fork and clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/usenc.git
cd usenc
```

2. Install in development mode:

```bash
pip install -e ".[dev,docs]"
```

3. Verify the installation:

```bash
pytest
```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions focused and small

## Testing

### Running Tests

Run the full test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=usenc
```

## Documentation

Add docstrings to code to document your new encoder:

```python
class HexEncoder(Encoder):
    """
    Short encoder description

    Long encoder description, multiple lines, ...

    Examples:
    hello world -> 68656C6C6F20776F726C64
    other -> 6F74686572
    """

    params = {
        'param_name': {
            'type': str,
            'default': '',
            'help': 'Description of the param'
        },
    }
    ...
```

Build and preview documentation locally:

```bash
mkdocs serve
```

## Pull Request Process

1. Create a feature branch:

```bash
git checkout -b feature/my-new-feature
```

2. Make your changes and commit:

```bash
git add .
git commit -m "Add my new feature"
```

3. Push to your fork:

```bash
git push origin feature/my-new-feature
```

4. Open a Pull Request on GitHub

### PR Checklist

- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Code follows project style
- [ ] Commit messages are clear

## Adding New Encoders

See the [Adding Encoders](adding-encoders.md) guide for detailed instructions.

## Reporting Issues

When reporting issues, please include:

- Python version
- usenc version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions

## Questions?

Open an issue on GitHub or start a discussion!
