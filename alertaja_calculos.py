
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ALERTAJÁ - DIFFERENTIATED PROBLEM SOLVING
# Análise matemática da intensidade da chuva
# ==========================================

# 1. FUNÇÃO MATEMÁTICA
# f(t) = -2t² + 12t + 5

def intensidade(t):
    return -2 * t**2 + 12 * t + 5


# 2. PRIMEIRA DERIVADA
# f'(t) = -4t + 12

def derivada(t):
    return -4 * t + 12


# 3. SEGUNDA DERIVADA
# f''(t) = -4

def segunda_derivada(t):
    return -4


print("=" * 50)
print("ALERTAJÁ - ANÁLISE DA CHUVA")
print("=" * 50)


# 4. DERIVADA EM TRÊS MOMENTOS

print("\n1. DERIVADA EM TRÊS MOMENTOS")

for tempo in [1, 3, 5]:

    resultado = derivada(tempo)

    if resultado > 0:
        interpretacao = "A chuva está aumentando."

    elif resultado < 0:
        interpretacao = "A chuva está diminuindo."

    else:
        interpretacao = "Momento de intensidade máxima."

    print(f"\nTempo: {tempo} hora(s)")
    print(f"Derivada: {resultado} mm/h²")
    print(f"Interpretação: {interpretacao}")


# 5. PONTO CRÍTICO E INTENSIDADE MÁXIMA

print("\n2. PONTO CRÍTICO")

tempo_critico = 3

intensidade_maxima = intensidade(tempo_critico)

print("Derivada igual a zero:")
print("-4t + 12 = 0")
print(f"Tempo crítico: {tempo_critico} horas")

print(f"Segunda derivada: {segunda_derivada(tempo_critico)}")

print("Como a segunda derivada é negativa,")
print("o ponto crítico representa um máximo.")

print(f"Intensidade máxima: {intensidade_maxima} mm/h")


# 6. INTEGRAL - CHUVA ACUMULADA

print("\n3. INTEGRAL")

def primitiva(t):
    return (-2/3) * t**3 + 6 * t**2 + 5 * t


chuva_acumulada = primitiva(6) - primitiva(0)

print("Integral entre 0 e 6 horas:")
print(f"Chuva acumulada: {chuva_acumulada:.2f} mm")


# 7. LIMITE QUANDO t TENDE A 3

print("\n4. LIMITE")

limite = intensidade(3)

print(f"Limite quando t tende a 3: {limite} mm/h")


# 8. CONFERÊNCIA DOS VALORES

print("\n5. CONFERÊNCIA DO MODELO")

print(f"Intensidade inicial: {intensidade(0)} mm/h")
print(f"Intensidade final: {intensidade(6)} mm/h")

print("\nTodos os dados são simulados para fins acadêmicos.")


# 9. GRÁFICO DA INTENSIDADE DA CHUVA

tempos = np.linspace(0, 6, 300)

valores = intensidade(tempos)

plt.figure(figsize=(9, 5))

plt.plot(
    tempos,
    valores,
    label="f(t) = -2t² + 12t + 5",
    linewidth=2
)

plt.scatter(
    [1, 3, 5],
    [intensidade(1), intensidade(3), intensidade(5)],
    label="Pontos analisados"
)

plt.scatter(
    [3],
    [23],
    label="Intensidade máxima (3, 23)"
)

plt.title("AlertaJá - Intensidade da chuva")
plt.xlabel("Tempo (horas)")
plt.ylabel("Intensidade (mm/h)")

plt.xlim(0, 6)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("grafico_intensidade.png", dpi=300)

plt.show()


# 10. GRÁFICO DA DERIVADA

valores_derivada = derivada(tempos)

plt.figure(figsize=(9, 5))

plt.plot(
    tempos,
    valores_derivada,
    label="f'(t) = -4t + 12",
    linewidth=2
)

plt.axhline(
    0,
    linestyle="--",
    label="Derivada igual a zero"
)

plt.scatter(
    [1, 3, 5],
    [derivada(1), derivada(3), derivada(5)],
    label="Pontos analisados"
)

plt.title("AlertaJá - Taxa de variação da chuva")
plt.xlabel("Tempo (horas)")
plt.ylabel("Taxa de variação (mm/h²)")

plt.xlim(0, 6)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("grafico_derivada.png", dpi=300)

plt.show()


# 11. FINALIZAÇÃO

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!")
print("=" * 50)

print("Gráficos gerados:")
print("- grafico_intensidade.png")
print("- grafico_derivada.png")
