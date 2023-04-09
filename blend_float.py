"""
4190.308 Computer Architecture                                                          Spring 2023

Image blending (float)

This module implements a function that blends two images together (floating point version)

@author:
    Your Name <your@email.com>

@changes:
    2023/MM/DD Your Name Comment

"""



def blend(img1, img2, height, width, channels, overlay, alpha):
    """
    Alpha-blends two images of size heightxwidth. The image data must contain an alpha
    channel, i.e., 'channels' must be four

    Args:
        img1:         image 1 data (multi-level list), BGRA
        img2:         image 2 data (multi-level list), BGRA
        height:       image height
        width:        image width
        channels:     number of channels (must be 4)
        overlay:      if 1, overlay the second image over the first
                      if 0, merge the two images
        alpha:        alpha blending factor (0.0-1.0)

    Returns:
        A tuple containing the following elements:
        - blended:    blended image data (multi-level list), BGRA
        - bheight:    blended image height (=height)
        - bwidth:     blended image width (=width)
        - bchannels:  blended image channels (=channels)

    """

    if channels != 4:
        raise ValueError('Invalid number of channels')


    # TODO
    # Your work goes here

    # For now, we simply copy the input parameters into the output parameters.
    # Fix/adjust once you have implemented your solution.
    bheight   = height
    bwidth    = width
    bchannels = channels
    blended   = img1


    return blended, bheight, bwidth, bchannels



