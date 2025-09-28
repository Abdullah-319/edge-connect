# 🛠️ Installation Guide

Comprehensive installation guide for EdgeConnect Face Reconstruction on all platforms.

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.7 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **GPU**: Optional (CPU works fine for most use cases)

### Recommended Requirements
- **Python**: 3.8 or 3.9
- **RAM**: 8GB or more
- **GPU**: NVIDIA GPU with CUDA support (for faster processing)

## 🚀 Quick Installation

### Option 1: One-Line Install (Recommended)

```bash
pip install git+https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
```

### Option 2: Clone and Install

```bash
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction
pip install -e .
```

## 📱 Platform-Specific Instructions

### 🖥️ Windows

#### Method 1: Using Anaconda (Recommended)

1. **Download and install Anaconda:**
   - Visit [anaconda.com](https://www.anaconda.com/products/distribution)
   - Download Python 3.8+ version
   - Run installer with default settings

2. **Create environment and install:**
   ```cmd
   # Open Anaconda Prompt
   conda create -n edge-connect python=3.8
   conda activate edge-connect

   # Clone repository
   git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
   cd edge-connect-face-reconstruction

   # Install dependencies
   pip install -r requirements.txt

   # Test installation
   python scripts/test_reconstruction.py
   ```

#### Method 2: Using Python from python.org

1. **Install Python:**
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.8+ for Windows
   - ⚠️ **Important**: Check "Add Python to PATH" during installation

2. **Install the package:**
   ```cmd
   # Open Command Prompt (cmd)
   python -m pip install --upgrade pip

   # Clone repository
   git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
   cd edge-connect-face-reconstruction

   # Create virtual environment
   python -m venv venv
   venv\Scripts\activate

   # Install
   pip install -r requirements.txt

   # Test
   python scripts/test_reconstruction.py
   ```

### 🍎 macOS

#### Method 1: Using Homebrew (Recommended)

1. **Install Homebrew:**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python and dependencies:**
   ```bash
   # Install Python
   brew install python@3.9 git

   # Clone repository
   git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
   cd edge-connect-face-reconstruction

   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install
   pip install -r requirements.txt

   # Test
   python scripts/test_reconstruction.py
   ```

#### Method 2: Using Python from python.org

1. **Install Python:**
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.8+ for macOS
   - Run the installer

2. **Install the package:**
   ```bash
   # Open Terminal
   git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
   cd edge-connect-face-reconstruction

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   python scripts/test_reconstruction.py
   ```

### 🐧 Linux (Ubuntu/Debian)

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv git -y

# Install OpenCV dependencies
sudo apt install libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 -y

# Clone repository
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Test installation
python scripts/test_reconstruction.py
```

### 🐧 Linux (CentOS/RHEL)

```bash
# Install Python and dependencies
sudo yum update -y
sudo yum install python3 python3-pip git -y

# Install OpenCV dependencies
sudo yum groupinstall "Development Tools" -y
sudo yum install mesa-libGL-devel libXext-devel libSM-devel libXrender-devel -y

# Continue with standard installation
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python scripts/test_reconstruction.py
```

## 🐳 Docker Installation

### Quick Start with Docker

```bash
# Build the image
docker build -t edge-connect-face .

# Run with volume mounting
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output edge-connect-face

# Interactive mode
docker run -it edge-connect-face /bin/bash
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  edge-connect:
    build: .
    volumes:
      - ./input:/app/input
      - ./output:/app/output
    environment:
      - PYTHONPATH=/app
```

Run with:
```bash
docker-compose up
```

## ☁️ Google Colab

The easiest way to get started without any local installation:

1. **Open the Colab notebook:**
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/edge-connect-face-reconstruction/blob/main/colab/EdgeConnect_Face_Reconstruction.ipynb)

2. **Run all cells** - everything will be installed automatically!

## 🔧 Development Installation

For contributors and developers:

```bash
# Clone repository
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/

# Run linting
flake8 src/
black src/
```

## 🐛 Troubleshooting

### Common Issues

#### 1. `ModuleNotFoundError: No module named 'cv2'`
```bash
pip uninstall opencv-python opencv-contrib-python
pip install opencv-python
```

#### 2. `ImportError: libGL.so.1` (Linux)
```bash
sudo apt install libgl1-mesa-glx
```

#### 3. Permission denied (Windows)
- Run Command Prompt as Administrator
- Or add `--user` flag: `pip install --user -r requirements.txt`

#### 4. `Python not found` (Windows)
- Reinstall Python with "Add to PATH" checked
- Or use full path: `C:\Python39\python.exe`

#### 5. Memory errors
- Use smaller image sizes: `--size 256 256`
- Close other applications
- Increase virtual memory

#### 6. Slow processing
- Use GPU version: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118`
- Reduce image size
- Use batch processing for multiple images

### Platform-Specific Issues

#### macOS: `command not found: pip`
```bash
python3 -m pip install --upgrade pip
```

#### Windows: `'python' is not recognized`
```cmd
# Use py launcher instead
py -m pip install -r requirements.txt
```

#### Linux: Permission denied for directories
```bash
sudo chown -R $USER:$USER ~/.local/
```

## ✅ Verify Installation

After installation, verify everything works:

```bash
# Test basic functionality
python -c "from src.face_reconstructor import FaceReconstructor; print('✅ Installation successful!')"

# Run full test
python scripts/test_reconstruction.py

# Check dependencies
python -c "import cv2, torch, numpy as np, PIL; print('✅ All dependencies installed!')"
```

## 📦 Optional Dependencies

### GPU Support (NVIDIA)

For faster processing with CUDA:

```bash
# Check CUDA version
nvidia-smi

# Install PyTorch with CUDA support
# For CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### Jupyter Support

For interactive notebooks:

```bash
pip install jupyter notebook ipywidgets
jupyter notebook notebooks/face_reconstruction.ipynb
```

## 🆘 Getting Help

If you encounter issues:

1. **Check the [troubleshooting section](#-troubleshooting)**
2. **Search [existing issues](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/issues)**
3. **Create a [new issue](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/issues/new)** with:
   - Your operating system
   - Python version (`python --version`)
   - Full error message
   - Steps to reproduce

## 📧 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/issues)
- **Discussions**: [Ask questions and share ideas](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/discussions)
- **Email**: [your.email@example.com](mailto:your.email@example.com)

---

⭐ **Star the repository** if this guide helped you!