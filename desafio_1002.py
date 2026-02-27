"""
Beecrowd 1002 - Área do Círculo

A fórmula para calcular a área de uma circunferência é: area = π . raio².
Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e
  multiplicando por π.

Entrada: O arquivo de entrada contém um valor de ponto flutuante (dupla precisão),
no caso, a variável raio.

Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme
exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão
(double).
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1002

# Escreva sua solução abaixo

#include <iostream>
#include <iomanip> // Necessário para configurar as casas decimais

using namespace std;

int main() {
    double raio, area;
    double pi = 3.14159;

    // Leitura do valor de entrada
    cin >> raio;

    // Cálculo da área
    area = pi * (raio * raio);

    // Configuração da saída: 4 casas decimais
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}
