// tip: each public class is put in its own file
public class main
{
	// tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        int x = 100;
        int y = 5;
        int t = 4;
        int n = 2;
        System.out.println("INICIO");
        System.out.println("Pegar celular");
        System.out.println("Verificar bateria");
        if (y > x) {
            System.out.println("Bateria esgotada");
            System.out.println("Guardar celular");
            System.out.println("FIM");
        } else {
            System.out.println("Bateria OK!");
            System.out.println("Verificar sinal");
                if (n > t) {
                System.out.println("Sem sinal");
                System.out.println("Guardar celular");
                System.out.println("FIM");
            } else {
                System.out.println("Sinal OK!");
                System.out.println("Digitar número");
			    System.out.println("Aguardar ligação ser completada");
			    System.out.println("Falar com interlocutor");
			    System.out.println("Terminar ligação");
			    System.out.println("Guardar celular");
                System.out.println("FIM");
            }
        }
    }
}