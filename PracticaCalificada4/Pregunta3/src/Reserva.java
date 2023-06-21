import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Reserva {
private static final Map<String, Map<String,Map<Integer,String>>> reservas =new HashMap<>();
private static final Map<String,Map<Integer,String>> horasreservadas = new HashMap<>();
private static final Map<Integer,String> requerimientos = new HashMap<>();

    public static void reservar(final String aula,final String hora,final String requerimiento) {
    reservar(aula, hora, 20, null);
}

    public static void reservar(final String aula, final String hora, final int personas, final String requerimiento) {
    if (reservas.containsKey(aula) && reservas.get(aula).containsKey(hora)) {
        System.out.println("Hora no disponible");
    }
    else {
        requerimientos.put(personas, requerimiento);
        horasreservadas.put(hora, requerimientos);
        reservas.put(aula, horasreservadas);
        System.out.println("Reserva realizada");
    }
}
public static String get_reservas() {
    return reservas.toString();

}
}