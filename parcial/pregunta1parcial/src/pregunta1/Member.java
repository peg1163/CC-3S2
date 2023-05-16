package pregunta1;

public abstract class Member {
    private  String nombre;
    public Member(String nombre) {
        this.nombre = nombre;
    }
    //dejaoms que la clase miembro solo tenga el metodo de unirse al torneo ,
    //y creamos uha clase organizador que hara que cada miembro pueda organizar un torneo
    public abstract void joinTournament();


}