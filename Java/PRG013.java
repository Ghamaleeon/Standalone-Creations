// tip: each public class is put in its own file
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        int fatorial = 1;
        for(int i = 1; i <= 10; ++i) {
            fatorial = fatorial * i;
			System.out.println("O valor do contador é " + fatorial);
		}
    }
}