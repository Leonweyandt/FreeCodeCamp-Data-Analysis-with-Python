# MEAN-VARIANCE-STANDARD-DEVIATION-CALCULATOR

# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance,
# standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# The input of the function should be a list containing 9 digits. The function should convert the list
# into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation,
# max, min, and sum along both axes and for the flattened matrix.
# The returned dictionary should follow this format:
# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }
# If a list containing less than 9 elements is passed into the function, it should raise
# a ValueError exception with the message: "List must contain nine numbers."
# The values in the returned dictionary should be lists and not Numpy arrays.
# For example, calculate([0,1,2,3,4,5,6,7,8]) should return:
# {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
#   'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }
# Development
# Write your code in mean_var_std.py. For development, you can use main.py to test your code.
# In order to run your code, type python3 main.py into the GitPod terminal and hit enter.
# This will cause the included CPython interpreter to run the main.py file.
#
# Testing
# The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience.
#
# Submitting
# Copy your project's URL and submit it to freeCodeCamp.


import numpy as np

liste_9 =[0,1,2,3,4,5,6,7,8]
liste_8 =[0,1,2,3,4,5,6,7]

def calculate(liste):
    if len(liste) != 9:
        print('List must contain nine numbers.')
        return
    array = np.reshape(liste, [3, 3])
    functions = {'mean': np.mean,  # save functions in a dictionary to execute them all later
                 'variance': np.var,
                 'standard deviation': np.std,
                 'max': np.max,
                 'min': np.min,
                 'sum': np.sum}
    results = {}  # create empty dictionary for the results
    for test_name, tests in functions.items():  # start loop with objects from dictionary
        axis1 = list(tests(array, axis=0))  # test for axis 1
        axis2 = list(tests(array, axis=1))  # test for axis 2
        flattened = tests(np.reshape(array, [1, 9]))  # test for flattened array
        together = [axis1, axis2, flattened]  # put in one list
        results[test_name] = together  # add to dictionary with name of the test

    print(results)
calculate(liste_8)
calculate(liste_9)