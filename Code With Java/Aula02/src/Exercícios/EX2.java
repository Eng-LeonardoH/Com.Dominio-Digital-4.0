package Exercícios;
import java.util.Scanner;
public class EX2 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite o primeiro numero: ");
		double e1 = entrada.nextDouble();
		System.out.println ("Digite o segundo numero: ");
		double e2 = entrada.nextDouble();
		System.out.println ("Digite o terceiro numero: ");
		double e3 = entrada.nextDouble();
		System.out.println (e1);
		System.out.println (e2);
		System.out.println (e3);
		
		if (e1 > e2) {
			if (e1 > e3) {
				System.out.println("O primeiro numero e o maior");
			} 
		} else {
			if (e2 > e3) {
				System.out.println("O segundo numero e o maior");
			} else {
				System.out.println("O terceiro numero e o maior");
			}
		}
		if (e1 < e2) {
			if (e1 < e3) {
				System.out.println("O primeiro numero e o menor");
			} 
		} else {
			if (e2 < e3) {
				System.out.println("O segundo numero e o menor");
			} else {
				System.out.println("O terceiro numero e o menor");
			}
		}
	
	}
}