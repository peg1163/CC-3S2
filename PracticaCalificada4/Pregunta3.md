Primero nos pide que creemos una clase que nos reserve una hora : 
   ```JAVA
      public class Reserva {
      private static final List<String> horasreservadas=new ArrayList<>();
      public static void reservar(String hora) {
          if (horasreservadas.contains(hora)) {
              System.out.println("Hora no disponible");
          }
          else {
              horasreservadas.add(hora);
          }
      }
      public static String get_reservas() {
          for (String hora : horasreservadas) {
              System.out.println(hora);
          }
          return horasreservadas.toString();
      
      }
      }
```
      
luego nos dice que modifiquemos para poder reservar en aulas, entonces creamos un diccionario para podera asignar  un aua y cierta hora ,para esto use
diccionarios anidados , el primer diccionario unira un salon con el diccionario de hora ,y este diccionario de hora hara tendra una llave que sera la hora de inicio de reserva y la hora final 

 ```JAVA
public class Reserva {
   //genera un diccionario anidado con las aulas y horas
private static final Map<String, Map<Integer,Integer>> reservas =new HashMap<>();
   //el diccionario anidado guardando las horas
private static final Map<Integer,Integer> horasreservadas = new HashMap<>();
   
public static void reservar(final String aula,final int hora,final int hora2) {
    if (reservas.containsKey(aula) && reservas.get(aula).containsKey(hora)) {
        System.out.println("Hora no disponible");
    }
    else {
        horasreservadas.put(hora,hora2);
        reservas.put(aula, horasreservadas);
        System.out.println("Reserva realizada");
    }
}
public static String get_reservas() {
    return reservas.toString();

}
```

finalmente nos pide que aumentemos requerimmientos y la capacidad del aula , por lo que cambiamos la anidacion de diccionarios y aumentamos uno ,
hacemos que la entrada de hora sea string y asi asignar un diccionario mas para la capacidad y los requerimientos 

 ```JAVA
public class Reserva {
private static final Map<String, Map<String,Map<Integer,String>>> reservas =new HashMap<>();
private static final Map<String,Map<Integer,String>> horasreservadas = new HashMap<>();
private static final Map<Integer,String> requerimientos = new HashMap<>();
   //si no nos dan requerimmientos de capacidad o de proyectores , etc :ponemos una capacidad de 20 y null para los extras
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

```


