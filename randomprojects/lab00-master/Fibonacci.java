public class Fibonacci {
	
	public int p;
    public static int fibonacci(int n) {
        if (n == 0){ return 0;}
      else  if (n <= 2){ return 1;}
        else 
        	return (fibonacci(n-1) + fibonacci(n-2));
    }

    // NO MODIFICAR A PARTIR DE AQUI

    public static void main(String[] args) {
        if(args.length > 0) {
            int n = Integer.parseInt(args[0]);
            System.out.println("Fibonacci de " + n + ": " + fibonacci(n));
        } else {
            System.err.println("No se paso ningun argumento");
        }
    }

}
