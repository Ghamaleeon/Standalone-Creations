#include <stdio.h>

int main()
{
    struct pessoa {
    int idade, nota[4];
    } pessoa;
    
    float resultado;
    
    printf("Digite uma idade: ");
    scanf("%d", &pessoa.idade);
    
    printf("\n");
    
    for(int i = 0; i < 4; i += 1){
        printf("Digite nota n %d: ", i + 1);
        scanf("%d", &pessoa.nota[i]);
    }
    
    resultado = (pessoa.nota[0] + pessoa.nota[1] + pessoa.nota[2] + pessoa.nota[3]);
    
    printf("\nIdade: %d\n", pessoa.idade);
    printf("Media: %.2f", resultado / 4);
    
    return 0;
}
