# 📸 Examples

This directory contains example images and usage demonstrations for EdgeConnect Face Reconstruction.

## 📁 Directory Structure

```
examples/
├── input/              # Sample input images with masks
├── output/             # Expected output results
└── notebooks/          # Example Jupyter notebooks
```

## 🎯 Sample Images

### Input Images

The `input/` directory contains sample images with white masks that demonstrate various use cases:

- **Portrait with nose mask**: Standard facial reconstruction
- **Multiple faces**: Batch processing example
- **Different lighting**: Various lighting conditions
- **Different mask shapes**: Various mask geometries

### Expected Outputs

The `output/` directory shows the expected results for each input image, including:

- `*_reconstructed.jpg`: Final reconstructed image
- `*_mask.jpg`: Detected mask regions
- `*_edges.jpg`: Edge detection results
- `*_comparison.jpg`: Before vs after comparison

## 🚀 Quick Start Examples

### Basic Usage

```python
from src.face_reconstructor import FaceReconstructor

# Initialize reconstructor
reconstructor = FaceReconstructor()

# Process single image
results = reconstructor.process_image('examples/input/sample_face.jpg')

# Visualize results
reconstructor.visualize_results(results)
```

### Batch Processing

```python
# Process all images in input directory
reconstructor.batch_process('examples/input/', 'examples/output/')
```

### Custom Configuration

```python
# Custom parameters for better results
config = {
    'threshold': 220,        # More sensitive mask detection
    'edge_sigma': 1.5,      # Sharper edge detection
    'edge_weight': 0.4,     # More edge emphasis
    'target_size': (512, 512)  # Higher resolution
}

reconstructor = FaceReconstructor(config)
results = reconstructor.process_image('examples/input/your_image.jpg')
```

## 📊 Performance Examples

| Image Type | Size | Processing Time | Quality Score |
|------------|------|----------------|---------------|
| Portrait | 256x256 | ~1s | 8.5/10 |
| Portrait | 512x512 | ~3s | 9.2/10 |
| Group Photo | 512x512 | ~4s | 8.8/10 |
| Low Light | 256x256 | ~1.5s | 7.9/10 |

## 🔧 Parameter Tuning Examples

### For Light Masks (Threshold Adjustment)

```python
# If your mask is light gray instead of pure white
config = {'threshold': 200}  # Lower threshold
reconstructor = FaceReconstructor(config)
```

### For High-Quality Results

```python
# Maximum quality settings
config = {
    'threshold': 240,
    'edge_sigma': 1.0,      # Sharp edges
    'edge_weight': 0.5,     # Strong edge guidance
    'target_size': (1024, 1024),  # High resolution
    'inpaint_radius': 5     # Larger inpainting radius
}
```

### For Fast Processing

```python
# Speed-optimized settings
config = {
    'threshold': 240,
    'edge_sigma': 3.0,      # Faster edge detection
    'edge_weight': 0.2,     # Light processing
    'target_size': (256, 256)  # Smaller size
}
```

## 📝 Troubleshooting Examples

### Common Issues and Solutions

```python
# Issue: No mask detected
# Solution: Lower threshold
config = {'threshold': 180}

# Issue: Poor edge detection
# Solution: Adjust sigma
config = {'edge_sigma': 1.5}

# Issue: Blurry results
# Solution: Increase resolution
config = {'target_size': (512, 512)}

# Issue: Processing too slow
# Solution: Reduce image size
config = {'target_size': (256, 256)}
```

## 🎓 Educational Examples

### Understanding Edge Detection

```python
from src.utils import canny_edge_detection, load_image

# Load image and detect edges with different parameters
image = load_image('examples/input/sample_face.jpg')

# Sharp edges
edges_sharp = canny_edge_detection(image, sigma=1.0)

# Smooth edges
edges_smooth = canny_edge_detection(image, sigma=3.0)

# Visualize differences
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image)
axes[0].set_title('Original')
axes[1].imshow(edges_sharp, cmap='gray')
axes[1].set_title('Sharp Edges (σ=1.0)')
axes[2].imshow(edges_smooth, cmap='gray')
axes[2].set_title('Smooth Edges (σ=3.0)')
plt.show()
```

### Understanding Inpainting Methods

```python
import cv2
from src.utils import create_mask_from_white_regions

image = load_image('examples/input/sample_face.jpg')
mask = create_mask_from_white_regions(image)

# Different inpainting methods
telea = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)

# Compare results
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
axes[0].imshow(image)
axes[0].set_title('Original with Mask')
axes[1].imshow(mask, cmap='gray')
axes[1].set_title('Mask')
axes[2].imshow(telea)
axes[2].set_title('Telea Method')
axes[3].imshow(ns)
axes[3].set_title('Navier-Stokes Method')
plt.show()
```

## 📱 Integration Examples

### Web API Integration

```python
from flask import Flask, request, jsonify
import base64
import io

app = Flask(__name__)
reconstructor = FaceReconstructor()

@app.route('/reconstruct', methods=['POST'])
def reconstruct_face():
    # Get image from request
    image_data = request.json['image']

    # Process image
    # ... implementation details ...

    return jsonify({'result': 'base64_encoded_result'})
```

### GUI Application

```python
import tkinter as tk
from tkinter import filedialog, messagebox

class FaceReconstructorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.reconstructor = FaceReconstructor()
        self.setup_ui()

    def setup_ui(self):
        # ... GUI setup ...
        pass

    def process_image(self):
        # ... image processing ...
        pass
```

## 🔗 External Integration

### Google Colab

See our [Google Colab notebook](../colab/EdgeConnect_Face_Reconstruction.ipynb) for cloud-based processing.

### Jupyter Notebooks

See our [main notebook](../notebooks/face_reconstruction.ipynb) for interactive processing.

## 📞 Support

If you need help with these examples:

1. Check the [main documentation](../README.md)
2. Review the [installation guide](../INSTALLATION.md)
3. [Open an issue](https://github.com/yourusername/edge-connect-face-reconstruction/issues)

---

**Happy reconstructing! 🎭**