// tip: each public class is put in its own file
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        double Montante = 950;
        double Capital = 800;
        double Juros = 0;
        int Tempo = 1;
        Juros = Montante/Capital - 1;
        System.out.println("Novo saldo              :  " + Juros * 100 + "%");
    }
}