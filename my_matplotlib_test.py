# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------
# Plot 1: Multiple Sine Waves with Enhancements
# ---------------------------------------------

# Generate 1000 points from 0 to 10
x = np.linspace(0, 10, 1000)

# Start a new figure with custom size
plt.figure(figsize=(10, 5))

# Plot basic sine wave with label and color
plt.plot(x, np.sin(x), label='sin(x)', color='black', linewidth=2)

# Scatter plot of sine with tiny dots
plt.scatter(x, np.sin(x), s=1, alpha=0.3, label='scatter sin(x)')

# Additional sine curves with phase shifts
plt.plot(x, np.sin(x - 0), color='blue', label='sin(x-0)', linewidth = 2, linestyle='--')   # dashed
plt.plot(x, np.sin(x - 1), color='green', label='sin(x-1)', linestyle='-.')  # dash-dot
plt.plot(x, np.sin(x - 2), color='red', label='sin(x-2)', linestyle=':')     # dotted

# Add x and y axis labels
plt.xlabel("X-axis: Time or Angle (radians)")
plt.ylabel("Y-axis: Sine Value")

# Add title and legend
plt.title("Sine Waves with Phase Shifts", fontdict ={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.legend(loc='upper right')  # legend position

# Add annotation (text on the plot)
plt.annotate("Peak", xy=(1.5, 1), xytext=(2, 1.2),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add grid and limits
plt.grid(True)
plt.xlim(0, 10)  # Set x-axis range
plt.ylim(-1.5, 1.5)  # Set y-axis range

# Save the plot to an image file (optional)
plt.savefig("sine_waves_plot.png")

# Show the plot
plt.show()


# ---------------------------------------------
# Plot 2: Line Style Demonstration
# ---------------------------------------------

# New figure
plt.figure(figsize=(8, 5))

# Various line styles
plt.plot(x, x + 0, '-g', label='x (solid green)', linewidth = 2)
plt.plot(x, x + 1, '--c', label='x+1 (dashed cyan)')
plt.plot(x, x + 2, '-.k', label='x+2 (dash-dot black)')
plt.plot(x, x + 3, ':r', label='x+3 (dotted red)')

# Set labels, title, and grid
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Style Variations")
plt.legend()
plt.grid(True)
plt.show()

# Sample data points for x and y axes
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Resize the graph window: figsize sets the width and height in inches
# dpi stands for dots per inch; higher dpi gives better resolution
plt.figure(figsize=(8, 5), dpi=100)

# Plotting Line 1 using keyword arguments
# label      : text shown in the legend
# color      : line color
# linewidth  : width of the line
# marker     : shape of the data point markers
# linestyle  : style of the connecting line
# markersize : size of the marker symbols
# markeredgecolor : edge color of the markers
plt.plot(x, y,
         label='2x',
         color='red',
         linewidth=2,
         marker='.',
         linestyle='--',
         markersize=10,
         markeredgecolor='blue')

# Plotting Line 2 using shorthand notation (fmt = '[color][marker][line]')
# This line will appear blue (b), triangle-up marker (^), and dashed line (--)
plt.plot(x, y, 'b^--', label='2x (shorthand)')

# Add a title with custom font and size
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# Label the X and Y axes
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Define custom tick marks on the X-axis
plt.xticks([0, 1, 2, 3, 4])
# Uncomment below if you want to customize Y-axis ticks as well
# plt.yticks([0, 2, 4, 6, 8, 10])

# Display the legend to differentiate between lines
plt.legend()

# Display the graph
plt.show()

# ---------------------------------------------
# Plot 3: Subplots Example
# ---------------------------------------------

# Create a figure with 2 rows and 2 columns of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# First subplot: sin(x)
axs[0, 0].plot(x, np.sin(x), 'b')
axs[0, 0].set_title("sin(x)")

# Second subplot: cos(x)
axs[0, 1].plot(x, np.cos(x), 'g')
axs[0, 1].set_title("cos(x)")

# Third subplot: tan(x)
axs[1, 0].plot(x, np.tan(x), 'r')
axs[1, 0].set_title("tan(x)")
axs[1, 0].set_ylim(-10, 10)  # Limit to prevent extreme values

# Fourth subplot: sin(x)*cos(x)
axs[1, 1].plot(x, np.sin(x) * np.cos(x), 'm')
axs[1, 1].set_title("sin(x) * cos(x)")

# Set a super-title for the whole figure
fig.suptitle("Trigonometric Functions")

# Add spacing between subplots
plt.tight_layout()
plt.show()
