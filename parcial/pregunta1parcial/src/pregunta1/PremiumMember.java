package pregunta1;

import pregunta1.Member;

public class PremiumMember extends Organizer {
    public PremiumMember(String nombre) {
        super(nombre);
    }
    @Override
    public void joinTournament() {
        System.out.println("Joining tournament as a premium member");
    }
    @Override
    public void organizeTournament() {
        System.out.println("Organizing tournament as a premium member");
    }
}
