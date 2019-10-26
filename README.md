# Deep-Learning
basics of deep learning concepts with few examples




# Examples

## Style Transfer
<p align = 'center'>
<a href = 'Examples/fast-style-transfer-master/examples/results/stata_udnie.jpg'><img src = 'examples/results/stata_udnie_header.jpg' width = '627px'></a>
</p>

### Dependencies
```
conda create -n style-transfer python=3
conda activate style-transfer
conda install tensorflow scipy pillow
pip install moviepy
python -c "import imageio; imageio.plugins.ffmpeg.download()"
```
### Transferring styles cmd
```
python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg
```

