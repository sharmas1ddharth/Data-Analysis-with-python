import numpy as np

def mean(matrix):
    mean_ax1 = np.mean(matrix, axis=0)
    mean_ax2 = np.mean(matrix, axis=1)
    mean_flat = np.mean(matrix)
    result = [mean_ax1.tolist(), mean_ax2.tolist(), mean_flat]
    return result

def variance(matrix):
    var_ax1 = np.var(matrix, axis=0)
    var_ax2 = np.var(matrix, axis=1)
    var_flat = np.var(matrix)
    result = [var_ax1.tolist(), var_ax2.tolist(), var_flat]
    return result

def std(matrix):
    std_ax1 = np.std(matrix, axis=0)
    std_ax2 = np.std(matrix, axis=1)
    std_flat = np.std(matrix)
    result = [std_ax1.tolist(), std_ax2.tolist(), std_flat]
    return result

def max(matrix):
    ax1 = np.max(matrix, axis=0)
    ax2 = np.max(matrix, axis=1)
    flat = np.max(matrix)
    result = [ax1.tolist(), ax2.tolist(), flat]
    return result

def min(matrix):
    ax1 = np.min(matrix, axis=0)
    ax2 = np.min(matrix, axis=1)
    flat = np.min(matrix)
    result = [ax1.tolist(), ax2.tolist(), flat]
    return result

def sum(matrix):
    ax1 = np.sum(matrix, axis=0)
    ax2 = np.sum(matrix, axis=1)
    flat = np.sum(matrix)
    result = [ax1.tolist(), ax2.tolist(), flat]
    return result

def calculate(arr):
    if len(arr) >= 9:
        np_arr = np.array(arr)
        matrix = np_arr.reshape(3,3)
        calculations = {
                        'mean': mean(matrix),
                        'variance': variance(matrix),
                        'standard deviation' : std(matrix),
                        'max' : max(matrix),
                        'min' : min(matrix),
                        'sum' : sum(matrix)
                                        }
        return calculations

    else:
        # return  "List must contain nine numbers."
        raise ValueError("List must contain nine numbers.")

