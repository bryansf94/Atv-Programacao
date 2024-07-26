#include <stdio.h>
#include <string.h>

// ----------------------- Algoritmo para calcular número de CPF -------------- //

int main() {
    char cpf[9]; // Para armazenar o CPF (11 dígitos + 1 caractere nulo)
    int noveNumeroCPF[9] = {};
    int mult = 0;
    int somaNumCPF = 0;
    int somaDoSegundoNumCPF = 0;
    int multCPF[9] = {};
    int multCPF_02[9] = {};

    printf("Qual é o número do seu CPF?: \n");
    scanf("%9s", cpf); // Lê a string do CPF com no máximo 11 caracteres

    // Convertendo os primeiros 9 caracteres do CPF para inteiros
    for (int i = 0; i < 9; i++) {
        noveNumeroCPF[i] = cpf[i] - '0';
    }

    // Loop for para multiplicar cpf
    for (int i = 0; i < 9; i++) {
        mult++;
        multCPF[i] = noveNumeroCPF[i] * mult;
        //printf("%d\n", multCPF[i]);
    }

    // Somando os 9 primeiros números
    for (int i = 0; i < 9; i++) {
        somaNumCPF += multCPF[i];
    }

    printf("%d\n", somaNumCPF);
    int PrimeiroNum = somaNumCPF % 11;
    printf("%d\n", PrimeiroNum);

    // Loop for para multiplicar cpf(2)
    mult = 0;
    int multCPFprimeiroNum = PrimeiroNum * 9;

    for (int i = 0; i < 9; i++) {
        mult++;
        multCPF_02[i] = noveNumeroCPF[i] * mult;
        //printf("%d\n", multCPF_02[i]);
    }

    somaDoSegundoNumCPF = multCPFprimeiroNum;
    for (int i = 0; i < 9; i++) {
        somaDoSegundoNumCPF += multCPF_02[i];
    }

    // printf("%d\n", somaNumCPF);
    int segundoNum = somaDoSegundoNumCPF % 11;
    printf("%d\n", segundoNum);

    return 0;
}