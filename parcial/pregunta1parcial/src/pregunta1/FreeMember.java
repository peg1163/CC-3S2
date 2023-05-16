package pregunta1;

public class FreeMember extends Member {
    public FreeMember(String nombre) {
        super(nombre);
    }
    @Override
    public void joinTournament() {
        System.out.println("Joining tournament as a free member");
    }


}
