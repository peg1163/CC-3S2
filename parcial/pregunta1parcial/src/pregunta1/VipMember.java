package pregunta1;

import pregunta1.Member;

public class VipMember extends Organizer {
    public VipMember(String nombre) {
        super(nombre);
    }
    @Override
    public void joinTournament() {
        System.out.println("Joining tournament as a vip member");
    }
    @Override
    public void organizeTournament() {
        System.out.println("Organizing tournament as a vip member");
    }
}
