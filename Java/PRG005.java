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
        System.out.println("Pegar");
        System.out.println("Avaliar");
		System.out.println("OK?");
        if (y > x) {
            System.out.println("Pegar outra");
            System.out.println("Avaliar");
            System.out.println("OK!");
			System.out.println("Lavar");
			System.out.println("Cortar?");
			if (n > t) {
                System.out.println("Comer");
                System.out.println("FIM");
            } else {
                System.out.println("Fatiar");
                System.out.println("Recipiente");
			    System.out.println("Comer");
			    System.out.println("FIM");
            }
        } else {
            System.out.println("OK!");
            System.out.println("Lavar");
			System.out.println("Cortar?");
                if (n > t) {
                System.out.println("Comer");
                System.out.println("FIM");
            } else {
                System.out.println("Fatiar");
                System.out.println("Recipiente");
			    System.out.println("Comer");
			    System.out.println("FIM");
            }
        }
    }
}