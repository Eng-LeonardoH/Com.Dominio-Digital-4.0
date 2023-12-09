package Exercícios;
import java.util.StringTokenizer;
import java.util.Scanner;
public class EX3 {
public static void main(String[] args) {
	Scanner entrada = new Scanner(System.in);
	System.out.println("Digite um texto: ");
	String texto = entrada.nextLine();
	System.out.println(texto);
	StringTokenizer qtd_palavras_texto = new StringTokenizer(texto);
	System.out.println(qtd_palavras_texto.countTokens());
	
}
}
