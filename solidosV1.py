import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definimos la variable simbólica
x = sp.Symbol('x', real=True)

# ==============================================================================
# 1. MÉTODO DE DISCOS
# Ejemplo: Rotar f(x) = sqrt(x) alrededor del eje X en el intervalo [0, 4]
# Fórmula: V = pi * integral( [f(x)]^2 dx )
# ==============================================================================
f_disco = sp.sqrt(x)
a_d, b_d = 0, 4
vol_disco = sp.pi * sp.integrate(f_disco**2, (x, a_d, b_d))

# ==============================================================================
# 2. MÉTODO DE ARANDELAS (ANILLOS)
# Ejemplo: Área entre f(x) = x (exterior) y g(x) = x^2 (interior) en [0, 1]
# Alrededor del eje X. Fórmula: V = pi * integral( ([f(x)]^2 - [g(x)]^2) dx )
# ==============================================================================
f_ext = x
g_int = x**2
a_a, b_a = 0, 1
vol_arandela = sp.pi * sp.integrate(f_ext**2 - g_int**2, (x, a_a, b_a))

# ==============================================================================
# 3. MÉTODO DE CASCARONES CILÍNDRICOS
# Ejemplo: Rotar f(x) = -x^2 + 4x alrededor del eje Y en [0, 4]
# Fórmula: V = 2 * pi * integral( x * f(x) dx )
# ==============================================================================
f_cascaron = -x**2 + 4*x
a_c, b_c = 0, 4
vol_cascaron = 2 * sp.pi * sp.integrate(x * f_cascaron, (x, a_c, b_c))

# Mostrar resultados exactos y aproximados en consola
print(f"1. Volumen (Discos):     {vol_disco} ≈ {float(vol_disco):.4f}")
print(f"2. Volumen (Arandelas):  {vol_arandela} ≈ {float(vol_arandela):.4f}")
print(f"3. Volumen (Cascarones): {vol_cascaron} ≈ {float(vol_cascaron):.4f}")

# ==============================================================================
# VISUALIZACIÓN EN 3D CON MATPLOTLIB
# ==============================================================================
fig = plt.figure(figsize=(16, 5))
theta = np.linspace(0, 2 * np.pi, 60) # Ángulo de revolución (0 a 360 grados)

# --- Gráfica 1: Método de Discos (Revolución en eje X) ---
ax1 = fig.add_subplot(131, projection='3d')
x_d = np.linspace(a_d, b_d, 50)
X_d, Theta_d = np.meshgrid(x_d, theta)
R_d = np.sqrt(X_d)
Y_d = R_d * np.cos(Theta_d)
Z_d = R_d * np.sin(Theta_d)

ax1.plot_surface(X_d, Y_d, Z_d, cmap='viridis', alpha=0.85, edgecolor='none')
ax1.set_title(f'Discos: $y = \\sqrt{{x}}$\nVolumen = ${sp.latex(vol_disco)}$')
ax1.set_xlabel('X (Eje de giro)')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# --- Gráfica 2: Método de Arandelas (Revolución en eje X) ---
ax2 = fig.add_subplot(132, projection='3d')
x_a = np.linspace(a_a, b_a, 50)
X_a, Theta_a = np.meshgrid(x_a, theta)

# Superficie exterior (y = x)
R_ext = X_a
Y_ext = R_ext * np.cos(Theta_a)
Z_ext = R_ext * np.sin(Theta_a)

# Superficie interior (y = x^2)
R_int = X_a**2
Y_int = R_int * np.cos(Theta_a)
Z_int = R_int * np.sin(Theta_a)

ax2.plot_surface(X_a, Y_ext, Z_ext, color='cyan', alpha=0.4, edgecolor='none')
ax2.plot_surface(X_a, Y_int, Z_int, color='crimson', alpha=0.9, edgecolor='none')
ax2.set_title(f'Arandelas: $y=x$ y $y=x^2$\nVolumen = ${sp.latex(vol_arandela)}$')
ax2.set_xlabel('X (Eje de giro)')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# --- Gráfica 3: Método de Cascarones (Revolución en eje Y) ---
ax3 = fig.add_subplot(133, projection='3d')
r_c = np.linspace(a_c, b_c, 50) # El radio corresponde a la variable x
R_c, Theta_c = np.meshgrid(r_c, theta)
X_c = R_c * np.cos(Theta_c)
Z_c = R_c * np.sin(Theta_c)
Y_c = -R_c**2 + 4*R_c # La altura corresponde a f(x)

ax3.plot_surface(X_c, Y_c, Z_c, cmap='plasma', alpha=0.85, edgecolor='none')
ax3.set_title(f'Cascarones: $y = -x^2+4x$\nVolumen = ${sp.latex(vol_cascaron)}$')
ax3.set_xlabel('X')
ax3.set_ylabel('Y (Eje de giro)')
ax3.set_zlabel('Z')

plt.tight_layout()
plt.show()
