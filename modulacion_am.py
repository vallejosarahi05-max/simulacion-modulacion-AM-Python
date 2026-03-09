import numpy as np
import matplotlib.pyplot as plt

# Tiempo de simulación
fs = 1000
t = np.linspace(0, 1, fs)

# Señal de mensaje (baja frecuencia)
fm = 5
mensaje = np.sin(2 * np.pi * fm * t)

# Señal portadora (alta frecuencia)
fc = 50
portadora = np.sin(2 * np.pi * fc * t)

# Modulación en amplitud (AM)
senal_modulada = (1 + mensaje) * portadora

# Agregar ruido
ruido = 0.2 * np.random.randn(len(t))
senal_ruido = senal_modulada + ruido

# Gráfica señal de mensaje
plt.figure()
plt.plot(t, mensaje)
plt.title("Señal de mensaje")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

# Gráfica señal portadora
plt.figure()
plt.plot(t, portadora)
plt.title("Señal portadora")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

# Gráfica señal modulada
plt.figure()
plt.plot(t, senal_modulada)
plt.title("Señal modulada AM")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

# Gráfica señal con ruido
plt.figure()
plt.plot(t, senal_ruido)
plt.title("Señal modulada con ruido")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()
