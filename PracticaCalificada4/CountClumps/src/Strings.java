import static java.lang.String.*;

public class Strings {

    public static int CountClumps(String nums) {
        int count = 0;
        int i = 0;
        int count_size=1;
        //este bucle recorre todo el arreglo
        if (nums.length() == 0) {
            return 0;
        }
        if (nums == null) {
            return 0;
        }

        while (i < nums.length()-1) {
            //si encuentra caracteres iguales aumenta el contador de caracteres y el indice
            if (nums.charAt(i) == nums.charAt(i + 1)) {
                i++;
                count_size++;
                if (count_size >= 2 && i == nums.length()-1) {
                    count++;
                }
            //si 2 caracteres juntos no son iguales, entonces se encontro un grupo
                // se aumenta el contador de clumps y se reinicia el contador de caracteres
            } else if (count_size >= 2) {
                count++;
                count_size=1;
                i++;
            }
            else {
                i++;
            }
        }
        //retorna el contador de clumps
        return count;
    }
}