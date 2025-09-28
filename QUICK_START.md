# 🚀 Quick Start Guide

Get up and running with EdgeConnect Face Reconstruction in under 5 minutes!

## ⚡ Super Quick Start (1 minute)

### Option 1: Google Colab (Zero Setup)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/edge-connect-face-reconstruction/blob/main/colab/EdgeConnect_Face_Reconstruction.ipynb)

Click the badge above → Run all cells → Upload your image → Get results!

### Option 2: One-Line Install
```bash
pip install git+https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
```

## 🎯 Quick Demo (3 minutes)

### 1. Install
```bash
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction
pip install -r requirements.txt
```

### 2. Test
```bash
python scripts/test_reconstruction.py
```

### 3. Process Your Image
```bash
python scripts/process_user_image.py path/to/your/image.jpg
```

## 📱 Platform-Specific Quick Start

### 🖥️ Windows
```cmd
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction
python -m pip install -r requirements.txt
python scripts\test_reconstruction.py
```

### 🍎 macOS
```bash
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction
python3 -m pip install -r requirements.txt
python3 scripts/test_reconstruction.py
```

### 🐧 Linux
```bash
sudo apt install python3-pip git
git clone https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction.git
cd edge-connect-face-reconstruction
pip3 install -r requirements.txt
python3 scripts/test_reconstruction.py
```

## 🔧 Quick Configuration

```python
from src.face_reconstructor import FaceReconstructor

# Basic usage
reconstructor = FaceReconstructor()
results = reconstructor.process_image('your_image.jpg')

# Custom parameters
config = {
    'threshold': 220,        # Lower for light masks
    'target_size': (512, 512)  # Higher resolution
}
reconstructor = FaceReconstructor(config)
results = reconstructor.process_image('your_image.jpg')
```

## 🎨 Quick Jupyter Start

```bash
pip install jupyter
jupyter notebook notebooks/face_reconstruction.ipynb
```

## 🐳 Quick Docker Start

```bash
docker build -t edge-connect .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output edge-connect
```

## 🔄 Quick Batch Processing

```bash
# Process all images in a folder
python scripts/batch_process.py input_folder/ output_folder/
```

## 📊 Quick Results

After processing, you'll get:
- `*_reconstructed.jpg` - Your result! 🎉
- `*_comparison.jpg` - Before vs after
- `*_mask.jpg` - Detected mask
- `*_edges.jpg` - Edge detection

## 🆘 Quick Help

**Issues?**
- Lower threshold if no mask detected: `--threshold 200`
- Use smaller images if slow: `--size 256 256`
- Check [troubleshooting guide](INSTALLATION.md#troubleshooting)

**Questions?**
- [GitHub Issues](https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/issues)
- [Documentation](README.md)

---

**That's it! You're ready to reconstruct faces! 🎭**

Need more details? Check the [full documentation](README.md).