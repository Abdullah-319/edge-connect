# Face Reconstruction with EdgeConnect

This implementation provides face reconstruction capabilities using EdgeConnect-inspired techniques for inpainting masked regions in facial images.

## Features

- Automatic detection of white mask regions (like the nose mask in your image)
- Edge-guided inpainting using Canny edge detection
- Multiple inpainting algorithms (Telea and Fast Marching)
- Jupyter notebook for interactive usage
- Command-line script for batch processing

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Dependencies are already installed**, but if you need to reinstall:
   ```bash
   pip install -r requirements_updated.txt
   ```

## Usage

### Option 1: Jupyter Notebook (Recommended)

1. **Start Jupyter:**
   ```bash
   source venv/bin/activate
   jupyter notebook face_reconstruction.ipynb
   ```

2. **Follow the notebook cells** to:
   - Load and process your image
   - Visualize the reconstruction process
   - Save results

### Option 2: Command Line Script

1. **Process your image:**
   ```bash
   source venv/bin/activate
   python process_user_image.py path/to/your/image.jpg
   ```

2. **With custom parameters:**
   ```bash
   python process_user_image.py path/to/your/image.jpg --threshold 220 --size 512 512 --output ./my_results
   ```

### Option 3: Test with Sample

Run the test script to see how it works:
```bash
source venv/bin/activate
python test_reconstruction.py
```

## Parameters

- `--threshold, -t`: White mask detection threshold (0-255, default: 240)
  - Lower values detect more pixels as mask
  - Higher values are more selective

- `--size, -s`: Target processing size (width height, optional)
  - Example: `--size 512 512`
  - Larger sizes may give better quality but take longer

- `--output, -o`: Output directory (default: ./output)

## Input Requirements

Your image should have:
- White or very light colored regions that need to be inpainted
- Good contrast between the mask and the surrounding areas
- Preferably facial images for best results

## Output Files

The script generates:
- `*_reconstructed.jpg`: Final inpainted result
- `*_mask.jpg`: Detected mask regions
- `*_edges.jpg`: Edge detection visualization
- `*_comparison.jpg`: Before vs after comparison

## Tips for Better Results

1. **Adjust the threshold** if mask detection is not working:
   ```bash
   python process_user_image.py your_image.jpg --threshold 200
   ```

2. **Use larger image sizes** for better quality:
   ```bash
   python process_user_image.py your_image.jpg --size 512 512
   ```

3. **Ensure good lighting** and contrast in your input image

4. **For complex masks**, consider manual editing of the detected mask

## Example Usage

```bash
# Process the image with nose mask
python process_user_image.py /path/to/nose_masked_face.jpg

# Process with custom threshold for lighter masks
python process_user_image.py /path/to/face.jpg --threshold 220

# Process with high resolution
python process_user_image.py /path/to/face.jpg --size 512 512 --output ./high_res_results
```

## Troubleshooting

1. **"No white regions detected"**:
   - Lower the threshold value (try 200-220)
   - Check if your image actually has white masks

2. **Poor reconstruction quality**:
   - Try different threshold values
   - Use larger image sizes
   - Ensure good image quality

3. **Errors with dependencies**:
   - Reactivate virtual environment: `source venv/bin/activate`
   - Reinstall dependencies: `pip install -r requirements_updated.txt`

## Files Overview

- `face_reconstruction.ipynb`: Interactive Jupyter notebook
- `test_reconstruction.py`: Test script with sample data
- `process_user_image.py`: Command-line processing script
- `requirements_updated.txt`: Updated dependencies
- `output/`: Results directory
- `input_images/`: Sample input images

## Advanced Usage

For more advanced features, see the Jupyter notebook which includes:
- Visualization of the reconstruction process
- Parameter tuning examples
- Comparison of different methods
- Tips for optimization