package pregunta1;

public class Organizer extends Member{
    public Organizer(String nombre) {
        super(nombre);
    }
    //asi esta clase puede organizar torneos porque lo que las clases vip y premium
    //heredan esta clase
    @Override
    public void joinTournament() {
        System.out.println("Organizer members can join a tournament");
    }


    public void organizeTournament() {
        System.out.println("Organizing tournament as an organizer");
    }


}
