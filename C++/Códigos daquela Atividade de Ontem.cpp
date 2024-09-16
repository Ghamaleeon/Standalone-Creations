#include <stdio.h>

// questão 4

int questao4()
{
    int num[3], I; // não precisa usar vetor aqui, é só declarar mais variáveis
	
    for(I = 0; I <= 2; I += 1) { // muito menos usar for aqui, é só encher o código de scanf e printf.
        printf("Insira o valor %d \n", I + 1);
        scanf("%d", &num[I]);
    }
	
    for(I = 2; I >= 0; I -= 1) {
        printf("%d ", num[I]);
    }
	// mas eu usei para resumir o código, muito mais limpo e cheiroso.
}

// questão 5

int questao5()
{
	int num[3], I, igual = 0; // a variável igual pode ser removida caso não use a DLC.
	// novamente, não precisa de vetor, nem for, mas fiz para o código ficar mais limpinho.
	for(I = 0; I <= 2; I += 1) {
        printf("Insira o valor %d \n", I + 1);
        scanf("%d", &num[I]);
    }
	
	if(num[0] > num[1] && num[0] > num[2]){ // aqui não tem muito segredo, é só comparar variável por variável para ver qual é maior.
		printf("Maior valor: %d", num[0]);
	}
	
	if(num[1] > num[0] && num[1] > num[2]){
		printf("Maior valor: %d", num[1]);
	}
	
	if(num[2] > num[0] && num[2] > num[1]){
		printf("Maior valor: %d", num[2]);
	}
	
	// DLC (Conteúdo adicional, apenas serve para dizer se todos os números são iguais)
	for(I = 0; I <= 2; I += 1) {
		int J = 0;
        for(J = 0; J <= 2; J += 1) {
			if(num[I] == num[J]){
				igual += 1;
			}
		}
		if(igual == 9){
			printf("Os numeros sao todos iguais");
		}
    }
	//
}

// questão 6

int questao6()
{
	float salario, resultado;
	printf("Insira o salario\n");
	scanf("%f", &salario);
	
	if(salario >= 1000 && salario <= 1500){
		resultado = salario + (salario * 0.1); // salário multiplicado por 0.1 dá 10% do salário original, daí é só somar com o salário.
		printf("Aumento de 10 porcento\nTotal com aumento:\n %.2f", resultado);
	}else if(salario >= 1501 && salario <= 2500){
		resultado = salario + (salario * 0.07); // salário multiplicado por 0.07 dá 7% do salário original.
		printf("Aumento de 7 porcento\nTotal com aumento:\n %.2f", resultado);
	}else if(salario >= 2501 && salario <= 3000){
		resultado = salario + (salario * 0.06); // Iden
		printf("Aumento de 6 porcento\nTotal com aumento:\n %.2f", resultado);
	}else if(salario > 3000){
		resultado = salario + (salario * 0.02); // Iden
		printf("Aumento de 2 porcento\nTotal com aumento:\n %.2f", resultado);
	}
	// também tem como utilizar a formula salario * 1.1 que adicionaria direto o valor correto.
	// mas eu tenho o costume de multiplicar por 0.1 e adicionar, porque? não sei.
	// se bem que agora deu uma vontade de limpar esse código...
	
}

// questão 6 (limpo)

int questao6L()
{
	float salario;
	printf("Insira o salario\n");
	scanf("%f", &salario);
	
	if(salario >= 1000 && salario <= 1500){
		printf("Aumento de 10 porcento\nTotal com aumento:\n %.2f", salario * 1.1); // sim, dá para colocar o valor aqui e fazer a multiplicação no printf.
	}else if(salario >= 1501 && salario <= 2500){
		printf("Aumento de 7 porcento\nTotal com aumento:\n %.2f", salario * 1.07);
	}else if(salario >= 2501 && salario <= 3000){
		printf("Aumento de 6 porcento\nTotal com aumento:\n %.2f", salario * 1.06);
	}else if(salario > 3000){
		printf("Aumento de 2 porcento\nTotal com aumento:\n %.2f", salario * 1.02);
	}
	// assim que é bom, daqui a pouco vou oferecer tosa também.
}

// questão 7

int questao7()
{
	float num[2]; // vetor, não foi pedido, então só colocar um monte de variável
	int I;
	
	for(I = 0; I <= 1; I += 1) { // for também não foi pedido, só dar scanf e printf.
        printf("Insira o valor %d \n", I + 1);
        scanf("%f", &num[I]);
    }
	
	for(I = 0; I <= 1; I += 1) {
		printf("%.2f / 2 = %.2f \n", num[I] ,num[I] / 2); // printf com divisão inclusa.
	}
}

// questão 8

int questao8()
{
	float num[5]; // só declarar cinco variáveis...
	int I;
	
	for(I = 0; I <= 4; I += 1) { // eh, aqui vai ter que usar for mesmo, foi pedido.
        printf("Insira o valor %d \n", I + 1);
        scanf("%f", &num[I]);
		printf("%.2f \n", num[I] / 2); // deixou a alternativa de printar o valor logo após ser inserido, então só colocar o printf no mesmo for do scanf.
    }
	
}

// questão 9

int questao9()
{
    int num[5]; // aqui não tem escapatória, vai ter que usar vetor, foi pedido.
	// como só pode declarar uma variável vetor, não vou usar I também, então não haverá for. 
	// (Posso colocar o I no vetor em forma de num[6]? Posso, mas não quero).
    printf("Insira o valor 1 \n");
    scanf("%d", &num[0]);
	printf("Insira o valor 2 \n");
    scanf("%d", &num[1]);
	printf("Insira o valor 3 \n");
    scanf("%d", &num[2]);
	printf("Insira o valor 4 \n");
    scanf("%d", &num[3]);
	printf("Insira o valor 5 \n");
    scanf("%d", &num[4]);
	
    printf("%d ", num[4]); // não se esqueça: ordem inversa!
	printf("%d ", num[3]);
	printf("%d ", num[2]);
	printf("%d ", num[1]);
	printf("%d ", num[0]);
	
	// O motivo de eu usar tanto for deve estar claro agora. 
	// não gosto de ficar usando tanto ctrl c ctrl v 
	//(ou escrevendo no papel tanto printf, parece que estou fazendo tabuada!)
}

// questão 10

int questao10()
{
    char nome[50]; // vou deixar em 50, quando conhecer alguém com o primeiro nome com mais de 50 caracteres, me chama.
    
    printf("Insira seu nome \n");
    scanf("%50s", nome);
    
    printf("Uma boa tarde, %s!", nome);
	// na minha opinião, o código mais simples de todas as questões.
}

int main(){ // isso daqui é para caso queira testar os códigos, sinta-se a vontade para colocar em um compilador e testar!
	int questao;
	printf("Qual questao gostaria de testar?");
	scanf("%d", &questao);
	
	switch(questao){
		case 4:
			questao4();
		break;
		case 5:
			questao5();
		break;
		case 6:
			questao6L();
		break;
		case 7:
			questao7();
		break;
		case 8:
			questao8();
		break;
		case 9:
			questao9();
		break;
		case 10:
			questao7();
		break;
		default:
			printf("Questao de numero %d nao existe!", questao);
	}
}

