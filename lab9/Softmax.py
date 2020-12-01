# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:45:47 2020

@author: Vasilica
"""
import numpy as np

class Softmax:
  def __init__(self, input_len, nodes):
    self.weights = np.random.randn(input_len, nodes) / input_len
    self.biases = np.zeros(nodes)

  def forward(self, input):
    self.last_input_shape = input.shape

    input = input.flatten()
    self.last_input = input

    input_len, nodes = self.weights.shape

    totals = np.dot(input, self.weights) + self.biases
    self.last_totals = totals

    exp = np.exp(totals)
    return exp / np.sum(exp, axis=0)

  def backprop(self, loss_gradient, learn_rate):
    for i, gradient in enumerate(loss_gradient):
      if gradient == 0:
        continue

      t_exp = np.exp(self.last_totals)

      S = np.sum(t_exp)

      out_gradients = -t_exp[i] * t_exp / (S ** 2)
      out_gradients[i] = t_exp[i] * (S - t_exp[i]) / (S ** 2)

      w_gradients = self.last_input
      b_gradients = 1
      d_t_d_inputs = self.weights

      t_gradients = gradient * out_gradients

      w_gradients = w_gradients[np.newaxis].T @ t_gradients[np.newaxis]
      b_L_gradients = t_gradients * b_gradients
      d_L_d_inputs = d_t_d_inputs @ t_gradients

      self.weights -= learn_rate * w_gradients
      self.biases -= learn_rate * b_L_gradients

      return d_L_d_inputs.reshape(self.last_input_shape)
