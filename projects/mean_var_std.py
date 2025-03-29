import numpy as np

liste_9 =[0,1,2,3,4,5,6,7,8]
liste_8 =[0,1,2,3,4,5,6,7]

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
    results = {}  # create empty dictionary for the results
    for test_name, tests in functions.items():  # start loop with objects from dictionary
        axis1 = tests(array, axis=0).tolist()  # test for axis 1
        axis2 = tests(array, axis=1).tolist()  # test for axis 2
        flattened = float(tests(np.reshape(array, [1, 9]))) # test for flattened array
        together = [axis1, axis2, flattened]  # put in one list
        results[test_name] = together  # add to dictionary with name of the test
    print(results)
    print(type(axis1), type(flattened))
calculate(liste_8)
calculate(liste_9)
