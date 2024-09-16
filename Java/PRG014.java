// tip: each public class is put in its own file
import java.time.temporal.ChronoUnit;
import java.time.LocalDate;  
import java.time.format.DateTimeFormatter;
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
    double VlrElevado = 3;
    double novoElevado = 0;
    LocalDate dBefore = LocalDate.parse("2021-10-13", DateTimeFormatter.ISO_LOCAL_DATE);
    LocalDate dAfter  = LocalDate.parse("2021-10-15", DateTimeFormatter.ISO_LOCAL_DATE);
    long diff = ChronoUnit.DAYS.between(dBefore, dAfter);
    System.out.println("Diferença : "+ diff);
    novoElevado = (VlrElevado) * (diff);
     System.out.println("novoElevado : "+novoElevado);
    } 
}