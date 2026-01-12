import numpy as np  # Importing the numpy library for numerical operations
import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting graphs

# Constants
epsilon = 1.0  # Depth of the potential well, which determines how strongly two particles attract each other at the minimum potential energy
A = 1.0        # Characteristic distance, the distance at which the potential energy is zero
r_cutoff = 2.5 # Cutoff distance, beyond which the Lennard-Jones potential is set to zero

# Define the Lennard-Jones potential function with cutoff
def lennard_jones_potential(r, epsilon, A, r_cutoff):
    # Calculate the Lennard-Jones potential U(r) for a given distance r
    U = 4 * epsilon * ((A / r)**12 - (A / r)**6)
   
    # Apply the cutoff: for distances greater than r_cutoff, set U(r) to zero
    U[r > r_cutoff] = 0  
   
    # Return the calculated potential U(r)
    return U

# Generate an array of r values (avoid r=0 to prevent division by zero)
r_values = np.linspace(0.8, 3, 500)  
# np.linspace(0.8, 3, 500) generates 500 equally spaced values between 0.8 and 3.0.
# The range starts from 0.8 to avoid division by zero issues at r=0.

# Calculate the potential U(r) for each r value in r_values
U_values = lennard_jones_potential(r_values, epsilon, A, r_cutoff)

# Plot U(r) versus r with cutoff
plt.figure(figsize=(8, 6))  # Create a figure with a specific size
plt.plot(r_values, U_values,
         label=r'$U(r) = 4\epsilon\left[\left(\frac{A}{r}\right)^{12} - \left(\frac{A}{r}\right)^{6}\right]$',
         color='blue')  
# Plot the Lennard-Jones potential curve, labeling it with the formula and coloring it blue.

plt.axhline(0, color='black', linestyle='--')  # Add a horizontal dashed line at U=0
plt.axvline(A, color='red', linestyle='--', label='r = A')  # Add a vertical dashed line at r=A with a label
plt.axvline(r_cutoff, color='green', linestyle='--', label=r'Cutoff at $r = 2.5$')  
# Add a vertical dashed line at the cutoff distance (r=2.5) with a label.

plt.xlabel(r'Distance $r$')  # Label the x-axis as 'Distance r'
plt.ylabel(r'Potential $U(r)$')  # Label the y-axis as 'Potential U(r)'
plt.title('Lennard-Jones Potential with Cutoff')  # Set the title of the plot
plt.legend()  # Add a legend to the plot
plt.grid(True)  # Enable grid lines for better visualization of the plot
plt.savefig("lj.pdf")  # Save the plot as a PDF file named "lj.pdf"
plt.show()  # Display the plot
