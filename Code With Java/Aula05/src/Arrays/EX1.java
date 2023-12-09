package Arrays;

public class EX1 {
public static void main(String[] args) {
	int contador=0;
	int[] intarray = {3, 5, 46, 12, 34};
	int intarrayb[] = new int[5];
	for(int i=0; i<intarray.length; i++) {
		System.out.print(intarray[i] + " ");
	}
	System.out.println();
	for(int i=intarray.length-1; i>=0; i--) {
		System.out.print(intarray[i] + " ");
		intarrayb[contador] = intarray[i];
		contador++;
	}
	
	System.out.println();
	for(int i=0; i<intarrayb.length; i++) {
		System.out.print(intarrayb[i] + " ");
	}

}
}
