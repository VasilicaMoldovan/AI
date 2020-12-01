# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:34:06 2020

@author: Vasilica
"""

import numpy as np

class Convolutional3x3:
  def __init__(self, num_filters):
    self.num_filters = num_filters

    self.filters = np.random.randn(num_filters, 3, 3) / 9

  def iterate_regions(self, image):
    h, w = image.shape

    for i in range(h - 2):
      for j in range(w - 2):
        im_region = image[i:(i + 3), j:(j + 3)]
        yield im_region, i, j

  def forward(self, input):
    self.last_input = input

    h, w = input.shape
    output = np.zeros((h - 2, w - 2, self.num_filters))

    for im_region, i, j in self.iterate_regions(input):
      output[i, j] = np.sum(im_region * self.filters, axis=(1, 2))

    return output

  def backprop(self, loss_gradient, learn_rate):
    filter_gradient = np.zeros(self.filters.shape)

    for im_region, i, j in self.iterate_regions(self.last_input):
      for f in range(self.num_filters):
        filter_gradient[f] += loss_gradient[i, j, f] * im_region

    self.filters -= learn_rate * filter_gradient

    return None
