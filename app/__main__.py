# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:09:10 2020

@author: syunary
"""

import numpy as np
def rot_theta(axis,angleDeg):
    '''
    Inputs:
        axis: x, y, z for the axis about which the rotation is desired ( input as string)
        angle: magnitude of rotation (input as degrees) 
    Returns: Rotation/Transformation matrix
    '''
    angleRad = np.radians(angleDeg)
   
    if axis == 'X' or axis == 'x':
        R = np.array([[1, 0, 0], [0, np.cos(angleRad), np.sin(angleRad)], \
                      [0, -np.sin(angleRad), np.cos(angleRad)]])
    elif axis == 'Y' or axis == 'y':
        R = np.array([[np.cos(angleRad), 0, -np.sin(angleRad)], [0, 1, 0], \
                      [np.sin(angleRad), 0, np.cos(angleRad)]])
    elif axis == 'Z' or axis == 'z':
        R = np.array([[np.cos(angleRad), np.sin(angleRad), 0], \
                      [-np.sin(angleRad), np.cos(angleRad), 0], [0, 0, 1]])
    return R


def main():

    constant = -8
    array_A = np.arange(0,  50) * constant

    for i in range(len(array_A)):            
 
        a1 = rot_theta('x', 25)
        b1 = rot_theta('z', array_A[i])
        print('inside for loop after b1')
        
        temp = np.matmul(a1, b1)
        print('inside for loop after temp')
    
    print(f'first row of temp is {temp[0]}.')
