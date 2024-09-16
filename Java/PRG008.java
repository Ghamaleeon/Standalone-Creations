// tip: each public class is put in its own file
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        double Montante = 0;
        double Capital = 20000.00;
        double Novosaldo;
        double Juros = 6;
        int Tempo = 3;
        Montante = Capital * (1 + (Juros/100 * Tempo));
        System.out.println("Novo saldo              :  " + Montante);
    }
}