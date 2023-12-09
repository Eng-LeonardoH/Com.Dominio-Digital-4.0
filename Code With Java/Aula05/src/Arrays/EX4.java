package Arrays;
import java.util.Scanner;
public class EX4 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		float notas[] = new float[5];
		float media = 0;
		
		for(int i = 0; i < notas.length; i++) {
			System.out.printf("Digite a nota do %dº aluno: ", i+1);
			notas[i] = entrada.nextFloat();
		}
		
		for(float acumulador: notas) {
			media += acumulador;
		}
		media = media/notas.length;
		System.out.printf("A média é: %f", media);
	}
}
