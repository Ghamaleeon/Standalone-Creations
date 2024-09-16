// tip: each public class is put in its own file
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        double saldo = 6000;
        double saque =  500;
        double depositado = 1200;
        double novo_saldo;

        System.out.println("Saldo Atual             :  " + saldo);
        System.out.println("Valor do saque          :  " + saque);
        System.out.println("Valor do depósito       :  " + depositado);
        novo_saldo = depositado + (saldo - saque);
        System.out.println("Novo saldo              :  " + novo_saldo);
    }
}