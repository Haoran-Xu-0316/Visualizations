import matplotlib.pyplot as plt
from SALib.analyze import sobol
from SALib.sample import saltelli


def ET(X):
    # column 0 = x1, column 1 = x2, column 2 = x3
    return(0.0031*X[:,0]*(X[:,1]+209)*(X[:,2]*(X[:,2]+15))**-1)

problem = {'num_vars': 3,
      'names': ['x1', 'x2', 'x3'],
      'bounds': [[10, 100],
        [3, 7],
        [-10, 30]]
      }

# Generate samples
param_values = saltelli.sample(problem, 1000, calc_second_order=False)

# Run model (example)
Y = ET(param_values)

# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True)

# Print the first-order sensitivity indices
print (Si['S1'])
plt.subplots(figsize=(9, 9)) # 设置画面大小
plt.barh(range(len(Si['S1'])), Si['S1'])
plt.show()
