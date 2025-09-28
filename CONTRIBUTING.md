# 🤝 Contributing to EdgeConnect Face Reconstruction

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

- **🐛 Bug Reports**: Report issues and bugs
- **💡 Feature Requests**: Suggest new features
- **📝 Documentation**: Improve docs and tutorials
- **🔧 Code**: Submit bug fixes and new features
- **🧪 Testing**: Help test the software
- **🎨 Examples**: Create example use cases

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/your-username/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction

# Add upstream remote
git remote add upstream https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. Create a Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/your-bug-fix
```

## 📝 Development Guidelines

### Code Style

We use the following tools for code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **isort**: Import sorting
- **mypy**: Type checking

Run before committing:

```bash
# Format code
black src/ scripts/ tests/

# Sort imports
isort src/ scripts/ tests/

# Check linting
flake8 src/ scripts/ tests/

# Type checking
mypy src/
```

### Code Structure

```
src/
├── __init__.py          # Package initialization
├── face_reconstructor.py  # Main reconstruction class
├── utils.py             # Utility functions
└── models/              # Model implementations (if any)

scripts/                 # Command-line scripts
tests/                   # Unit tests
docs/                    # Documentation
```

### Coding Standards

- **Python 3.7+ compatibility**
- **Type hints** for all public functions
- **Docstrings** for all classes and functions
- **Clear variable names**
- **Comments for complex logic**

Example function:

```python
def process_image(image_path: str, threshold: int = 240) -> np.ndarray:
    """
    Process an image for face reconstruction.

    Args:
        image_path: Path to the input image
        threshold: White mask detection threshold (0-255)

    Returns:
        Reconstructed image as numpy array

    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If threshold is invalid
    """
    # Implementation here
    pass
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_utils.py

# Run specific test
pytest tests/test_utils.py::test_load_image
```

### Writing Tests

Create tests for new functionality:

```python
import pytest
import numpy as np
from src.utils import load_image

def test_load_image():
    """Test image loading functionality."""
    # Test with valid image
    image = load_image('path/to/test/image.jpg')
    assert isinstance(image, np.ndarray)
    assert len(image.shape) == 3

    # Test with invalid path
    with pytest.raises(FileNotFoundError):
        load_image('nonexistent.jpg')
```

## 📄 Documentation

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """
    Brief description of the function.

    Longer description if needed. This can span multiple
    lines and provide detailed information.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param1 is negative
        TypeError: When param2 is not a string

    Example:
        >>> result = function_name(5, "hello")
        >>> print(result)
        True
    """
    pass
```

### Documentation Updates

When adding features:

1. Update relevant docstrings
2. Add examples to README
3. Update API documentation
4. Add to changelog

## 🐛 Bug Reports

### Before Reporting

1. **Search existing issues** to avoid duplicates
2. **Try the latest version**
3. **Check the documentation**

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment**
- OS: [e.g. Windows 10, macOS 11, Ubuntu 20.04]
- Python Version: [e.g. 3.8.5]
- Package Version: [e.g. 1.0.0]

**Additional Context**
Any other context about the problem
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature

**Problem It Solves**
What problem does this feature address?

**Proposed Solution**
How would you like it to work?

**Alternatives Considered**
Other solutions you've considered

**Additional Context**
Any other context or screenshots
```

## 🔄 Pull Request Process

### 1. Prepare Your Changes

```bash
# Make sure you're on your feature branch
git checkout feature/your-feature-name

# Make your changes
# Add tests for new functionality
# Update documentation

# Run tests and linting
pytest
black src/ scripts/ tests/
flake8 src/ scripts/ tests/
```

### 2. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "feat: add batch processing functionality

- Add batch_process method to FaceReconstructor
- Add command-line script for batch processing
- Include tests and documentation
- Closes #123"
```

### Commit Message Format

Use conventional commits:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

### 3. Push and Create PR

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
# Use the PR template below
```

### Pull Request Template

```markdown
**Description**
Brief description of changes

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Other (please describe)

**Testing**
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

**Checklist**
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)

**Related Issues**
Closes #123
```

## 🏷️ Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

Example: `1.2.3`

### Release Checklist

For maintainers:

1. Update version in `setup.py` and `src/__init__.py`
2. Update `CHANGELOG.md`
3. Run full test suite
4. Create release branch
5. Tag release
6. Create GitHub release
7. Deploy to PyPI

## 🎖️ Recognition

Contributors will be:

- **Listed in README.md**
- **Mentioned in release notes**
- **Added to contributors list**

## ❓ Questions?

- **GitHub Discussions**: [Ask questions](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/discussions)
- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **Discord**: [Join our community](https://discord.gg/your-invite)

## 📜 Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

Thank you for contributing! 🙏

**ABDULLAH AHMAD**
Project Maintainer