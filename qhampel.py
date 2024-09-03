# Author: Mughni Yumashar
# Contact: mughnimail@gmail.com
# Any non-commercial usage shall include credit to the author.
# Commercial usages are prohibited without consent from the author.

import pandas as pd
import numpy as np
from scipy.stats import norm

try:
    print("Starting the calculation")
    print("Please wait...")
    print("")

    # Load data from CSV file
    data = pd.read_csv('data.csv', header=None)

    # Convert the data into a list of arrays for each lab
    values = [data.iloc[i].dropna().values for i in range(len(data))]  # List of arrays for each lab

    def calculate_pairwise_differences(lab_values):
        differences = []
        for i in range(len(lab_values)):
            for j in range(i + 1, len(lab_values)):
                for val1 in lab_values[i]:
                    for val2 in lab_values[j]:
                        differences.append(abs(val1 - val2))
        return np.array(differences)

    def H1(x, differences, p):
        count = np.sum(differences <= x)
        return (2 * count) / (p * (p - 1))

    def G1(differences, p):
        unique_differences = np.sort(np.unique(differences))
        G_values = []
        
        H1_values = [H1(x_i, differences, p) for x_i in unique_differences]
        
        for i, x_i in enumerate(unique_differences):
            if i == 0:
                G_value = 0.5 * H1_values[i]
            else:
                G_value = 0.5 * (H1_values[i] + H1_values[i - 1])
            G_values.append(G_value)
        
        return unique_differences, G_values

    def Psi(q):
        if q <= -4.5:
            return 0
        elif -4.5 < q <= -3:
            return -4.5 - q
        elif -3 < q <= -1.5:
            return -1.5
        elif -1.5 < q <= 1.5:
            return q
        elif 1.5 < q <= 3:
            return 1.5
        elif 3 < q <= 4.5:
            return 4.5 - q
        else:
            return 0

    def hampel_estimator(lab_values, s_star):
        p_means = np.array([np.mean(lab) for lab in lab_values])
        p = len(p_means)

        # Step 1: Calculate interpolation nodes
        d = []
        for mean in p_means:
            d.extend([mean - 4.5 * s_star, mean - 3 * s_star, mean - 1.5 * s_star,
                      mean + 1.5 * s_star, mean + 3 * s_star, mean + 4.5 * s_star])
        
        d = np.sort(d)

        # Step 2: Calculate p_m for each interpolation node
        p_m_values = []
        for m in range(len(d)):
            p_m = sum(Psi((mean - d[m]) / s_star) for mean in p_means)
            p_m_values.append(p_m)

        # Step 3: Find solutions to the equation
        solutions = []
        for m in range(len(d) - 1):
            if p_m_values[m] == 0:
                solutions.append(d[m])
            elif p_m_values[m + 1] == 0:
                solutions.append(d[m + 1])
            elif p_m_values[m] * p_m_values[m + 1] < 0:
                # Linear interpolation to find the root
                x_m = d[m] - (p_m_values[m] * (d[m + 1] - d[m])) / (p_m_values[m + 1] - p_m_values[m])
                solutions.append(x_m)

        # Step 4: Select the solution nearest to the median
        median_value = np.median(p_means)
        if solutions:
            x_star = min(solutions, key=lambda x: abs(x - median_value))
        else:
            x_star = median_value  # Fallback to median if no solutions found

        return x_star

    def q_method(data):
        p = len(data)
        differences = calculate_pairwise_differences(data)
        x_values, G_values = G1(differences, p)
        H1_0 = H1(0, differences, p)
        q_value = 0.25 + 0.75 * H1_0
        G_inv_value = np.interp(q_value, G_values, x_values)
        phi_inv_value = norm.ppf(0.625 + 0.375 * H1_0)
        s_star = G_inv_value / (np.sqrt(2) * phi_inv_value)
        return s_star

    # Calculate robust standard deviation
    robust_std_dev = q_method(values)

    # Calculate robust mean using the Hampel estimator
    robust_mean = hampel_estimator(values, robust_std_dev)

    # Print results
    print("RESULT")
    print("=============================================")
    print("Robust Mean:", robust_mean)
    print("Robust Standard Deviation:", robust_std_dev)
    print("=============================================")
    print("")
    print("Author: Mughni Yumashar")
    print("Contact: mughnimail@gmail.com")
    print("Any non-commercial usage shall include credit to the author.")
    print("Commercial usages are prohibited, contact the author for license.")
    print("")

except Exception as e:
    print("An error occurred during the execution of the script.")
    print("Error message:", str(e))
    print("Please check the input data file (data.csv) is exist in the same folder and in correct format.")
    print("")

# Pause the console window so it doesn't close immediately
input("Press Enter to exit...")
