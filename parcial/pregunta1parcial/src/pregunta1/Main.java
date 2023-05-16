package pregunta1;

import pregunta1.FreeMember;

import java.util.List;

public class Main {
    public void joinTournament(List<Member> miembros) {
        for (var miembro : miembros) {
            miembro.joinTournament();
        }
    }

    public static void main(String[] args) {


    List<Member> miembros = List.of(
            new PremiumMember("Abejita Azul"),
            new VipMember("Kaperucita Feliz"),
            new FreeMember("Inspectora Motita")
    );
    miembros.forEach(miembro -> {
        miembro.joinTournament();
    });

    }
}