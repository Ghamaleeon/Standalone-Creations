public class main {
    public static void main(String[] args)
    {
       // Somente tive uma dúvida que é o que precisava fazer na linha de texto a frente:
       // Campo Aluno --- Validar se o aluno já esta cadastrado na geração do relatório (IF)
       // Rogério é um estudante comum da 1º série, tendo seus altos e baixos com suas notas, ele se esforça nos estudos.
       // Alberto no entanto, era para ser um estudante da 2º série, porém ele apenas se importa com artes. (Teve sorte com Português)
       // Eu adicionei um sistema que conta se o aluno reprovou em 4 ou mais matérias para saber se ele passou do ano letivo ou não.
       // Também ia adicionar um sistema de faltas, porém ia demorar muito mais.
       // Quanto ao design, mantive o do código original, tive alguns problemas com números e letras fazendo o design quebrar um pouco.
       // Espero que tenha ficado bom! Abraços~
    	
    	String esp = "   "; //espaço entre as notas
        String aluno1 = "Rogério         "; 
        String série1 = "1º     ";
        String aluno2 = "Alberto         ";
        String série2 = "2º     ";
        String port = "L.Portuguesa      ";
        String mate = "                       Matemática        ";
        String biol = "                       Biologia          ";
        String quim = "                       Química           ";
        String fisi = "                       Física            ";
        String hist = "                       História          ";
        String geog = "                       Geografia         ";
        String filo = "                       Filosofia         ";
        String soci = "                       Sociologia        ";
        String edfi = "                       Ed.Física         ";
        String arte = "                       Artes             ";
        String ingl = "                       Inglês            ";
        
        int apr1 = 0;
        int apr2 = 0;	
        
        Double port11 = 5.5;
        Double port12 = 7.0;
        Double port13 = 6.5;
        Double port14 = 5.0;
        Double port1med = 0.0;
        port1med = (port11 + port12 + port13 + port14)/4;
        String port1apr = "Reprovado";
        if (port1med >= 6) {
        	port1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double mate11 = 7.0;
        Double mate12 = 9.5;
        Double mate13 = 7.0;
        Double mate14 = 8.5;
        Double mate1med = 0.0;
        mate1med = (mate11 + mate12 + mate13 + mate14)/4;
        String mate1apr = "Reprovado";
        if (mate1med >= 6) {
        	mate1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double biol11 = 7.5;
        Double biol12 = 6.5;
        Double biol13 = 8.5;
        Double biol14 = 7.5;
        Double biol1med = 0.0;
        biol1med = (biol11 + biol12 + biol13 + biol14)/4;
        String biol1apr = "Reprovado";
        if (biol1med >= 6) {
        	biol1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double quim11 = 8.5;
        Double quim12 = 7.0;
        Double quim13 = 6.0;
        Double quim14 = 6.5;
        Double quim1med = 0.0;
        quim1med = (quim11 + quim12 + quim13 + quim14)/4;
        String quim1apr = "Reprovado";
        if (quim1med >= 6) {
        	quim1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double fisi11 = 5.0;
        Double fisi12 = 8.0;
        Double fisi13 = 6.0;
        Double fisi14 = 7.0;
        Double fisi1med = 0.0;
        fisi1med = (fisi11 + fisi12 + fisi13 + fisi14)/4;
        String fisi1apr = "Reprovado";
        if (fisi1med >= 6) {
        	fisi1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double hist11 = 8.0;
        Double hist12 = 9.0;
        Double hist13 = 9.5;
        Double hist14 = 9.5;
        Double hist1med = 0.0;
        hist1med = (hist11 + hist12 + hist13 + hist14)/4;
        String hist1apr = "Reprovado";
        if (hist1med >= 6) {
        	hist1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double geog11 = 8.5;
        Double geog12 = 8.0;
        Double geog13 = 9.0;
        Double geog14 = 8.5;
        Double geog1med = 0.0;
        geog1med = (geog11 + geog12 + geog13 + geog14)/4;
        String geog1apr = "Reprovado";
        if (geog1med >= 6) {
        	geog1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double filo11 = 6.5;
        Double filo12 = 6.0;
        Double filo13 = 8.0;
        Double filo14 = 7.5;
        Double filo1med = 0.0;
        filo1med = (filo11 + filo12 + filo13 + filo14)/4;
        String filo1apr = "Reprovado";
        if (filo1med >= 6) {
        	filo1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double soci11 = 8.5;
        Double soci12 = 9.5;
        Double soci13 = 6.0;
        Double soci14 = 8.0;
        Double soci1med = 0.0;
        soci1med = (soci11 + soci12 + soci13 + soci14)/4;
        String soci1apr = "Reprovado";
        if (soci1med >= 6) {
        	soci1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double edfi11 = 9.5;
        Double edfi12 = 9.5;
        Double edfi13 = 9.5;
        Double edfi14 = 9.5;
        Double edfi1med = 0.0;
        edfi1med = (edfi11 + edfi12 + edfi13 + edfi14)/4;
        String edfi1apr = "Reprovado";
        if (edfi1med >= 6) {
        	edfi1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double arte11 = 6.0;
        Double arte12 = 8.5;
        Double arte13 = 7.5;
        Double arte14 = 6.0;
        Double arte1med = 0.0;
        arte1med = (arte11 + arte12 + arte13 + arte14)/4;
        String arte1apr = "Reprovado";
        if (arte1med >= 6) {
        	arte1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        Double ingl11 = 4.5;
        Double ingl12 = 5.5;
        Double ingl13 = 7.0;
        Double ingl14 = 9.0;
        Double ingl1med = 0.0;
        ingl1med = (ingl11 + ingl12 + ingl13 + ingl14)/4;
        String ingl1apr = "Reprovado";
        if (ingl1med >= 6) {
        	ingl1apr = "Aprovado";
        } else {
        	apr1 += 1;
        }
        
        //layout do relatorio
        System.out.println("+------------------------------------------------------------------------------------+" );
        System.out.println("|Nome            Série  Disciplinas       1ºB   2ºB   3ºB   4ºB   Média   Status     |" );
        System.out.println("|"+ aluno1 + série1 + port + port11 + esp + port12 + esp + port13 + esp + port14 + esp + port1med + esp + "  " + port1apr + "   |");
        System.out.println("|"+ mate + mate11 + esp + mate12 + esp + mate13 + esp + mate14 + esp + mate1med + esp + "  " + mate1apr + "   |");
        System.out.println("|"+ biol + biol11 + esp + biol12 + esp + biol13 + esp + biol14 + esp + biol1med + esp + "  " + biol1apr + "   |");
        System.out.println("|"+ quim + quim11 + esp + quim12 + esp + quim13 + esp + quim14 + esp + quim1med + esp + "  " + quim1apr + "   |");
        System.out.println("|"+ fisi + fisi11 + esp + fisi12 + esp + fisi13 + esp + fisi14 + esp + fisi1med + esp + "  " + fisi1apr + "   |");
        System.out.println("|"+ hist + hist11 + esp + hist12 + esp + hist13 + esp + hist14 + esp + hist1med + esp + "  " + hist1apr + "   |");
        System.out.println("|"+ geog + geog11 + esp + geog12 + esp + geog13 + esp + geog14 + esp + geog1med + esp + "  " + geog1apr + "   |");
        System.out.println("|"+ filo + filo11 + esp + filo12 + esp + filo13 + esp + filo14 + esp + filo1med + esp + "  " + filo1apr + "   |");
        System.out.println("|"+ soci + soci11 + esp + soci12 + esp + soci13 + esp + soci14 + esp + soci1med + esp + "  " + soci1apr + "   |");
        System.out.println("|"+ edfi + edfi11 + esp + edfi12 + esp + edfi13 + esp + edfi14 + esp + edfi1med + esp + "  " + edfi1apr + "   |");
        System.out.println("|"+ arte + arte11 + esp + arte12 + esp + arte13 + esp + arte14 + esp + arte1med + esp + "  " + arte1apr + "   |");
        System.out.println("|"+ ingl + ingl11 + esp + ingl12 + esp + ingl13 + esp + ingl14 + esp + ingl1med + esp + "  " + ingl1apr + "   |");
        System.out.println("+------------------------------------------------------------------------------------+" );

        Double port21 = 6.0;
        Double port22 = 8.0;
        Double port23 = 6.0;
        Double port24 = 6.0;
        Double port2med = 0.0;
        port2med = (port21 + port22 + port23 + port24)/4;
        String port2apr = "Reprovado";
        if (port2med >= 6) {
        	port2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double mate21 = 2.5;
        Double mate22 = 8.5;
        Double mate23 = 6.5;
        Double mate24 = 4.5;
        Double mate2med = 0.0;
        mate2med = (mate21 + mate22 + mate23 + mate24)/4;
        String mate2apr = "Reprovado";
        if (mate2med >= 6) {
        	mate2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double biol21 = 5.5;
        Double biol22 = 5.5;
        Double biol23 = 5.5;
        Double biol24 = 5.5;
        Double biol2med = 0.0;
        biol2med = (biol21 + biol22 + biol23 + biol24)/4;
        String biol2apr = "Reprovado";
        if (biol2med >= 6) {
        	biol2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double quim21 = 2.0;
        Double quim22 = 3.0;
        Double quim23 = 6.0;
        Double quim24 = 9.0;
        Double quim2med = 0.0;
        quim2med = (quim21 + quim22 + quim23 + quim24)/4;
        String quim2apr = "Reprovado";
        if (quim2med >= 6) {
        	quim2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double fisi21 = 5.0;
        Double fisi22 = 3.0;
        Double fisi23 = 2.5;
        Double fisi24 = 1.5;
        Double fisi2med = 0.0;
        fisi2med = (fisi21 + fisi22 + fisi23 + fisi24)/4;
        String fisi2apr = "Reprovado";
        if (fisi2med >= 6) {
        	fisi2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double hist21 = 2.0;
        Double hist22 = 4.0;
        Double hist23 = 6.0;
        Double hist24 = 6.0;
        Double hist2med = 0.0;
        hist2med = (hist21 + hist22 + hist23 + hist24)/4;
        String hist2apr = "Reprovado";
        if (hist2med >= 6) {
        	hist2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double geog21 = 6.0;
        Double geog22 = 3.0;
        Double geog23 = 1.0;
        Double geog24 = 0.0;
        Double geog2med = 0.0;
        geog2med = (geog21 + geog22 + geog23 + geog24)/4;
        String geog2apr = "Reprovado";
        if (geog2med >= 6) {
        	geog2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double filo21 = 1.5;
        Double filo22 = 1.5;
        Double filo23 = 4.5;
        Double filo24 = 0.5;
        Double filo2med = 0.0;
        filo2med = (filo21 + filo22 + filo23 + filo24)/4;
        String filo2apr = "Reprovado";
        if (filo2med >= 6) {
        	filo2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double soci21 = 5.0;
        Double soci22 = 5.0;
        Double soci23 = 4.0;
        Double soci24 = 2.0;
        Double soci2med = 0.0;
        soci2med = (soci21 + soci22 + soci23 + soci24)/4;
        String soci2apr = "Reprovado";
        if (soci2med >= 6) {
        	soci2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double edfi21 = 3.0;
        Double edfi22 = 3.5;
        Double edfi23 = 5.5;
        Double edfi24 = 4.0;
        Double edfi2med = 0.0;
        edfi2med = (edfi21 + edfi22 + edfi23 + edfi24)/4;
        String edfi2apr = "Reprovado";
        if (edfi2med >= 6) {
        	edfi2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double arte21 = 9.0;
        Double arte22 = 9.0;
        Double arte23 = 8.0;
        Double arte24 = 8.0;
        Double arte2med = 0.0;
        arte2med = (arte21 + arte22 + arte23 + arte24)/4;
        String arte2apr = "Reprovado";
        if (arte2med >= 6) {
        	arte2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        Double ingl21 = 0.0;
        Double ingl22 = 3.0;
        Double ingl23 = 4.0;
        Double ingl24 = 3.0;
        Double ingl2med = 0.0;
        ingl2med = (ingl21 + ingl22 + ingl23 + ingl24)/4;
        String ingl2apr = "Reprovado";
        if (ingl2med >= 6) {
        	ingl2apr = "Aprovado";
        } else {
        	apr2 += 1;
        }
        
        System.out.println("|Nome            Série  Disciplinas       1ºB   2ºB   3ºB   4ºB   Média   Status     |" );
        System.out.println("|"+ aluno2 + série2 + port + port21 + esp + port22 + esp + port23 + esp + port24 + esp + port2med + esp + "  " + port2apr + "   |");
        System.out.println("|"+ mate + mate21 + esp + mate22 + esp + mate23 + esp + mate24 + esp + mate2med + esp + "  " + mate2apr + "   |");
        System.out.println("|"+ biol + biol21 + esp + biol22 + esp + biol23 + esp + biol24 + esp + biol2med + esp + "  " + biol2apr + "   |");
        System.out.println("|"+ quim + quim21 + esp + quim22 + esp + quim23 + esp + quim24 + esp + quim2med + esp + "  " + quim2apr + "   |");
        System.out.println("|"+ fisi + fisi21 + esp + fisi22 + esp + fisi23 + esp + fisi24 + esp + fisi2med + esp + "  " + fisi2apr + "   |");
        System.out.println("|"+ hist + hist21 + esp + hist22 + esp + hist23 + esp + hist24 + esp + hist2med + esp + "  " + hist2apr + "   |");
        System.out.println("|"+ geog + geog21 + esp + geog22 + esp + geog23 + esp + geog24 + esp + geog2med + esp + "  " + geog2apr + "   |");
        System.out.println("|"+ filo + filo21 + esp + filo22 + esp + filo23 + esp + filo24 + esp + filo2med + esp + "  " + filo2apr + "   |");
        System.out.println("|"+ soci + soci21 + esp + soci22 + esp + soci23 + esp + soci24 + esp + soci2med + esp + "  " + soci2apr + "   |");
        System.out.println("|"+ edfi + edfi21 + esp + edfi22 + esp + edfi23 + esp + edfi24 + esp + edfi2med + esp + "  " + edfi2apr + "   |");
        System.out.println("|"+ arte + arte21 + esp + arte22 + esp + arte23 + esp + arte24 + esp + arte2med + esp + "  " + arte2apr + "   |");
        System.out.println("|"+ ingl + ingl21 + esp + ingl22 + esp + ingl23 + esp + ingl24 + esp + ingl2med + esp + "  " + ingl2apr + "   |");
        System.out.println("+------------------------------------------------------------------------------------+" );
        
        String reapr1 = "Aprovado no ano letivo";
        if (apr1 >= 4) {
        	reapr1 = "Reprovado no ano letivo";
        }
        String reapr2 = "Aprovado no ano letivo";
        if (apr2 >= 4) {
        	reapr2 = "Reprovado no ano letivo";
        }	
        
        System.out.println("|Nome            Reprovações     Aluno foi:                                          |");
        System.out.println("|"+ aluno1 + apr1 + esp + esp + esp + esp + esp + reapr1 + "                              |");
        System.out.println("|"+ aluno2 + apr2 + esp + esp + esp + esp + esp + reapr2 + "                              |");
        System.out.println("+------------------------------------------------------------------------------------+" );
    }
}