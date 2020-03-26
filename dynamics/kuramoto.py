# kuramoto model describes synchronization of large set of coupled oscillators
# d_phi_i / d_t = omega_i + (k/n)*( sin(phi_j) - sin(phi_i)

import sympy as sym
phi, omega = sym.symbols('phi', 'omega')


def kuramoto(n, m, k):
    for i in range(n):
        for j in range(i):
            pass
