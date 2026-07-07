#!/usr/bin/env python3
"""
Generate a right-angled triangle diagram showing sin, cos, and tan definitions.
Outputs to right-triangle.png in the same directory.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(8, 8), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 4)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

# Add axis labels
ax.set_xlabel('x', fontsize=12, fontweight='bold')
ax.set_ylabel('y', fontsize=12, fontweight='bold')

# Define triangle vertices
# Right angle at origin for simplicity
angle_phi = np.pi / 6  # 30 degrees
hyp_length = 4
opposite_length = hyp_length * np.sin(angle_phi)
adjacent_length = hyp_length * np.cos(angle_phi)

# Triangle vertices
A = np.array([0, 0])  # Angle φ
B = np.array([adjacent_length, 0])  # Right angle
C = np.array([adjacent_length, opposite_length])  # Opposite end

# Draw triangle
triangle = patches.Polygon([A, B, C], linewidth=2.5, edgecolor='black', 
                           facecolor='lightblue', alpha=0.3)
ax.add_patch(triangle)

# Draw right angle indicator
square_size = 0.3
square = patches.Rectangle((adjacent_length - square_size, 0), square_size, square_size, 
                           linewidth=1.5, edgecolor='black', facecolor='none')
ax.add_patch(square)

# Label sides
# Adjacent side (bottom)
ax.plot([A[0], B[0]], [A[1], B[1]], 'g-', linewidth=3, alpha=0.8)
ax.text((A[0] + B[0]) / 2, -0.3, r'$\mathrm{adjacent}$', fontsize=12, 
        color='green', fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# Opposite side (right)
ax.plot([B[0], C[0]], [B[1], C[1]], color='darkorange', linewidth=3, alpha=0.8)
ax.text(adjacent_length + 0.1, opposite_length / 2, r'$\mathrm{opposite}$', 
        fontsize=12, color='darkorange', fontweight='bold', ha='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Hypotenuse (diagonal)
ax.plot([A[0], C[0]], [A[1], C[1]], 'r-', linewidth=2.5, alpha=0.8)
mid_x = C[0] / 2
mid_y = C[1] / 2
ax.text(mid_x - 0.4, mid_y + 0.3, r'$\mathrm{hypotenuse}$', fontsize=12, 
        color='red', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8))

# Draw angle φ
arc_radius = 0.8
arc_angles = np.linspace(0, angle_phi, 50)
ax.plot(arc_radius * np.cos(arc_angles), arc_radius * np.sin(arc_angles), 
        'b--', linewidth=1.5)
ax.text(0.95, 0.1, r'$\phi$', fontsize=14, color='blue', fontweight='bold')

# Set ticks
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_yticks([0, 1, 2, 3])
ax.tick_params(labelsize=10)

plt.tight_layout()
plt.savefig('right-triangle.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: right-triangle.png")
plt.close()
