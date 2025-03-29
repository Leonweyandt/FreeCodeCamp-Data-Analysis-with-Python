import numpy as np

def calculate(liste):
    if len(liste) != 9:
        raise ValueError("List must contain nine numbers.")  # Raise the exception here
    array = np.reshape(liste, [3, 3])
    functions = {'mean': np.mean,  # save functions in a dictionary to execute them all later
                 'variance': np.var,
                 'standard deviation': np.std,
                 'max': np.max,
                 'min': np.min,
                 'sum': np.sum}
    calculations = {}  # create empty dictionary for the results
    for test_name, tests in functions.items():  # start loop with objects from dictionary
        axis1 = tests(array, axis=0).tolist()  # test for axis 1
        axis2 = tests(array, axis=1).tolist()  # test for axis 2
        flattened = float(tests(np.reshape(array, [1, 9]))) # test for flattened arra
        together = [axis1, axis2, flattened]  # put in one list
        calculations[test_name] = together  # add to dictionary with name of the test
    return calculations
