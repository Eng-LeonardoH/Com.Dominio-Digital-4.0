package Exercícios;
import java.util.Scanner;
public class EX3 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite um numero: ");
		int dia_semana = entrada.nextInt();
		
		if (dia_semana == 1) {
			System.out.println("Domingo");
		} if (dia_semana == 2) {
			System.out.println("Segundo-Feira");
		} if (dia_semana == 3) {
			System.out.println("Terça-Feira");
		} if (dia_semana == 4) {
			System.out.println("Quarta-Feira");
		} if (dia_semana == 5) {
			System.out.println("Quinta-Feira");
		} if (dia_semana == 6) {
			System.out.println("Sexta-Feira");
		} if (dia_semana == 7) {
			System.out.println("Sa*bado");
		} 

		}
	}
