// tip: each public class is put in its own file
public class main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        String Announce = "Uma boa noite, pessoal do java!";
        int Ann_Qnt = 0;
        Ann_Qnt = Announce.length();
        System.out.println(Announce + " tem " + Ann_Qnt + " caracteres. (espaços inclusos)");
        System.out.println(Announce.toUpperCase());
        System.out.println(Announce.toLowerCase());
        System.out.println(Announce.substring(0,3).toLowerCase());
        System.out.println(Announce.substring(4,7).toUpperCase());
        System.out.println(Announce.substring(8,13).toLowerCase());
        System.out.println(Announce.substring(15,22).toUpperCase());
        System.out.println(Announce.substring(23,25).toLowerCase());
        System.out.println(Announce.substring(26,31).toUpperCase());
    }
}