public class Perm {

    // Asuma que todos los parametros son validos
    public static String permutation(String message, int spaces) {
        // Su codigo aqui
        return "";
    }

    // NO MODIFICAR A PARTIR DE AQUI

    public static void main(String[] args) {
        if(args.length > 0) {
            String entry = args[0];
            int spaces = Integer.parseInt(args[1]);
            System.out.println(permutation(entry, spaces));
        } else {
            System.err.println("No se paso ningun argumento");
        }
    }

}
