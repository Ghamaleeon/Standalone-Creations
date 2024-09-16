public class main {
    public static void main(String[] args)
    {
        double vlr_nota    = 0; 
        int    qtde_faltas  = 22; 
        int    inf_presenca = 85; 
        double mover_faltas  = 0; 
        int abonada = 0;
        mover_faltas = (qtde_faltas - abonada);
        if (qtde_faltas - abonada > ( inf_presenca * 0.25))  {   
            System.out.println("Aluno reprovado com " + (qtde_faltas - abonada) + " faltas");
        } else { 
            System.out.println("Aluno aprovado com " + (qtde_faltas - abonada) + " faltas"); 
             }
        System.out.println("Porcentagem de faltas: " + (mover_faltas/inf_presenca)*100 + "%");
    }
}