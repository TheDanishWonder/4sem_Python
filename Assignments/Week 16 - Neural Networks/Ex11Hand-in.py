import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib
import matplotlib.pyplot as plt

# weight;height;type
# 233.4799204165095;23.514129929623852;rat
# 231.32446731816555;26.03382997978225;rat
# 17.906954059999567;6.846576762459397;mouse
# 230.276522831171;24.077799766119398;rat
# 20.36059265800554;6.6059829255227;mouse
# 21.60538751773697;6.812460032530713;mouse

# So we want to predict if its a rat or mouse, based on weight and height.
# So we have to split off the rat / mouse column

with open("rodents.csv", "r") as f:

    df = pd.read_csv(f, sep=";")
    print("Dataframe")
    print(df.head())
    # Splitting the data
    weightHeight = df.values[:, 0:2]
    rodentType = df.values[:, 2]
    # print("\nWeight and Height\n", weightHeight)
    # print("\ntype of rodent\n", rodentType)
    # Make a new scatter plot with datapoints of weights vs heights. Choose different colors for rats and mice

    # Mice
    mice = df.loc[df["type"] == "mouse"]
    plt.scatter(mice["weight"], mice["height"], c="red", label="Mice")
    # Rats
    rats = df.loc[df["type"] == "rat"]
    plt.scatter(rats["weight"], rats["height"], c="blue", label="Rats")
    plt.xlabel("weight")
    plt.ylabel("height")
    plt.title("Rodents")
    # Manually find the optimal linear function to divide the 2 groups (y = aX+b). Plot it on the scatter plot
    x = np.linspace(0, 250, 1000)
    # https://www.mathsisfun.com/equation_of_line.html
    y = 0 * x + 9.9
    plt.plot(x, y, "-r", label="Manual Perceptron")
    plt.legend(loc="upper left")
    # plt.grid()
    # plt.show()
    # What is the slope and intercept of the linear function?
    # What is "Slope" and "intercept"?
    # https://www.purplemath.com/modules/slopyint.htm
    # So I guess the slope is "flat" and the intercept is 9.9?
    # Now change the 'type' column to represent rats as 1 and mice as -1
    def ratOrMice(rodent):
        # Why did I make this?
        if rodent == "rat":
            return 1
        else:
            return -1

    df["type"].replace("rat", 1, inplace=True)
    df["type"].replace("mouse", -1, inplace=True)
    print("Replaced Head")
    print(df.head())
    df.dropna(
        axis=0
    )  # 0 = Row , 1 = column, so this means, drop all rows which contains a null value

    def perceptron(input, weights):
        dot_product = np.dot(input, weights)
        return ratOrMice(dot_product)

    # Use these weights herè [40,-190] to determine if the following 3 animals are mice or rats:

    taskSix = [
        [231.32446731816555, 26.03382997978225],
        [17.906954059999567, 6.846576762459397],
        [230.276522831171, 24.077799766119398],
    ]

    sixWeights = [40, -190]
    for rodent in taskSix:
        print("")
        print("Rat == 1")
        print("Mice == -1")
        print("New Rodent:")
        print(rodent)
        print("Is it a Mouse or Rat?")
        print(perceptron(rodent, sixWeights))

    # Find the (approximately) optimal weights using the perceptron learning algorithm

    def pla(training_data, no_iterations=10000, eta=0.5):
        """
        Find the proper weights to use in the perceptron based on data and target
        Parameters:
        training_data: list of vectors, as predictors zipped with a target value
        no_iterations: number of times to adjust the weights to get them as close as possible to the optimal number
        eta: the learning rate (prevent learning to go pendulum from one extreme error to the opposite)
        """

        dim = len(training_data[0][0])
        weights = np.random.random(
            dim
        )  # error and weights (for x and y) start out as random numbers

        # initial_error
        error = np.random.random()
        weight_history = [np.copy(weights)]

        for i in range(no_iterations):

            # breakpoint()
            inp_vec, expected_label = training_data[
                i % len(training_data)
            ]  # expected labels are 1 or -1
            perceptron_output = perceptron(
                inp_vec, weights
            )  # perceptron output id a decimal between 0 and 1
            error = expected_label - perceptron_output  # error
            weights += eta * error * inp_vec  # accumulate the weights
            weight_history.append(np.copy(weights))

        return weights, weight_history

    learned_weights, weight_history = pla(df)
    # print(weight_history)
    print("LEARNED WEIGHTS", learned_weights)

    # Plot the weightline
    # Plot the division line

# ? ? ?? ?
def activation_function(x):
    """
    Step function to respond with y = 1 or -1
    Parameter:
    x: An x (numeric) value that will have a corresponding y value of 1 or -1
    """
    # Look at the activation_function and plot the y-values for each x from -5,5 spaced with 0.5
    if x < 0:
        return -1
    else:
        return 1


rnge = np.linspace(-5.5, 5.5, num=23)
# print("rnge:", rnge)
values = [activation_function(i) for i in rnge]
# print("values: ", values)
# plt.plot(values)
# plt.axis([-10, 9, -2, 2])
# plt.show()


def perceptron(inp, weights):
    """
    Given a list of input (x) values and a list of weights, 
    calculates the dot product of the 2 lists and returns 1 or -1 (fire or don't)
    Parameters:
    inp: vector of input predictors
    weights: vector of weights to be ajusted for precise prediction of output.
    """
    # Change the perceptron method from the notebook to use the numpy.dot() method in line 12 instead of the lengthy sum() function
    dot_product = np.dot(inp, weights)
    output = activation_function(dot_product)
    return output
