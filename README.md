# Random-Erasing

Zhong, Z., Zheng, L., Kang, G., Li, S., & Yang, Y. (2017). Random erasing data augmentation. arXiv (Cornell University). https://doi.org/10.48550/arxiv.1708.04896

## How to use

This is for `YOLOv8 format` <br/>
There are three modes to use
1. IRE: random erasing a region in whole image
2. ORE: random erasing regions inside bounding boxes
3. I+ORE: random erasing regions in whole image and bounding boxes

The function `eraser` return numpy array, so if you want to save the image <br/>
you can use `Image.fromarray(numpy.array).save('filename.extension')`
