#include <iostream>

int fatorial(int valor){
	if(valor > 0){
		return valor * fatorial(valor - 1);
	}else{
		return 1;
	}
}

int elevacao(int valor, int vezes){
	if(vezes > 1){
		return valor * elevacao(valor, vezes - 1);
	}else{
		return valor;
	}
}

int main(int argc, char** argv) {
	float numero1 = 0, numero2 = 0;
	int sinal = 0;
	printf("Digite numero1 \n");
	scanf("%f", &numero1);
	printf("Digite numero2 \n");
	scanf("%f", &numero2);
	printf("Escolha o numero correspondente ao sinal \n 0 = Soma \n 1 = Reducao \n 2 = Divisao \n 3 = Multiplicacao \n 4 = Fatoracao \n 5 = Elevacao \n 6 = Contagem \n");
	scanf("%d", &sinal);
	switch (sinal)
	{
		case 0:
			numero1 += numero2;
			break;
		case 1:
			numero1 -= numero2;
			break;
		case 2:
			numero1 /= numero2;
			break;
		case 3:
			numero1 *= numero2;
			break;
		case 4:
			numero1 = fatorial(numero1);
			break;
		case 5:
			numero1 = elevacao(numero1, numero2);
			break;
		case 6:
			if(numero2 > numero1){
				for(int i = numero1; i <= numero2; i += 1) {
					printf("%d ", i);
				}
				break;
			} else if(numero2 < numero1) {
				for(int i = numero1; i >= numero2; i -= 1) {
					printf("%d ", i);
				}
				break;
			} else {
				printf("%f\n", numero1);
			}
	}
	
	if(sinal >= 0 && sinal <= 5){
		printf("\nResultado: %f\n", numero1);
		scanf("%c", &sinal);
	} else if(sinal == 6) {
		printf("\n");
		scanf("%c", &sinal);
	} else {
		printf("\nSinal inexistente.\n");
	}
	
	return 0;
}
