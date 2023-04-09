"""
4190.308 Computer Architecture                                                          Spring 2023

Image blurring (float)

This module implements a function that blurs an image with a 3x3 filter (floating point version)

@author:
    Your Name <your@email.com>

@changes:
    2023/MM/DD Your Name Comment

"""



def blur(image, height, width, channels, kernel_size=5):
    """
    Blurs an image with a kernel and returns the blurred image.

    Args:
        image:        image data (multi-level list)
        height:       image height
        width:        image width
        channels:     number of channels (BGR or BGRA)
        kernel_size:  size of blurring kernel

    Returns:
        A tuple containing the following elements:
        - blurred:    blurred image data
        - bheight:    blurred image height
        - bwidth:     blurred image width
        - bchannels:  blurred image channels

    """

    # TODO
    # Your work goes here

    # For now, we simply copy the input parameters into the output parameters.
    # Fix/adjust once you have implemented your solution.
    bheight   = height
    bwidth    = width
    bchannels = channels
    blurred   = image


    return blurred, bheight, bwidth, bchannels



