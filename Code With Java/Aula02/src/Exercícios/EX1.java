package Exercícios;
import java.util.Scanner;
public class EX1 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite um numero: ");
		double resp = entrada.nextDouble();
		System.out.println (resp%2);
		if (resp % 2 == 1) {
			System.out.println("Numero impar");
		} else {
			System.out.println("Numero par");
		}
	}
}