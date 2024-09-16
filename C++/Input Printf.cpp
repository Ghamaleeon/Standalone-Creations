#include <iostream>

int main()
{
    char nome[50], endereco[50], telefone[10];
    
    printf("Insira seu nome \n");
    scanf("%50s", nome);
    printf("Insira seu endereco \n");
    scanf("%50s", endereco);
    printf("Insira seu telefone (separadores inclusos) \n");
    scanf("%10s", telefone);
    
    printf("\n %s \n %s \n %s", nome, endereco, telefone);
}
