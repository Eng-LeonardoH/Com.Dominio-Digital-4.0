package Java_POO;

public class calculadora {
	public static void main(String[] args) {
		int a;
		int b;
		int c;
		int soma1;
		int soma2;
		int multiplicar1;
		int multiplicar2;
		
		a = 5;
		b = 3;
		c = 2;
		
		SomarMetodos calc = new SomarMetodos();
		
		soma1 = calc.somar(a, b);
		soma2 = calc.somar(a, b, c);
		
		System.out.println(soma1);
		System.out.println(soma2);
		
		multiplicar1 = calc.multiplicar(a, b);
		multiplicar2 = calc.multiplicar(a, b, c);
		
		System.out.println(multiplicar1);
		System.out.println(multiplicar2);
		}
	}
