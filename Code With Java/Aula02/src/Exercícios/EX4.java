package Exercícios;
import java.util.Scanner;
public class EX4 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite as notas do aluno: ");
		float nota1 = entrada.nextFloat();
		float nota2 = entrada.nextFloat();
		float media = (nota1 + nota2) / 2;
		System.out.println(media);
	}
}
