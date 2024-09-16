// tip: each public class is put in its own file
public class main
{
	// tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        int x = 10;
        int y = 5;
        int t = 10;
        int n = 5;
        System.out.println("INICIO");
        System.out.println("Café da manhã");
        System.out.println("Verificar material");
        if (x > y) {
            System.out.println("Material OK!");
        } else {
            System.out.println("Verifique o material novamente");
        }
        System.out.println("Ir para a escola.");
            System.out.println("Transporte?");
        if (t > n) {
            System.out.println("Usar transporte");
        } else {
            System.out.println("Caminhar até a escola");
        }
        System.out.println("Escola!");
        System.out.println("FIM");
    }
}