package Exercicios;
import java.util.Scanner;
public class EX1 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
 		System.out.println ("Digite um numero: ");
 		int dia_semana = entrada.nextInt();
 		 		
 		System.out.println((dia_semana == 1 ) ? "Domingo" : (dia_semana == 2) ? "Segunda" : (dia_semana == 3) ? "Terça" : (dia_semana == 4) ? "Quarta" : (dia_semana == 5) ? "Quinta" : (dia_semana == 6) ? "Sexta" : "Sábado" );
	}
}
