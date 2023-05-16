
import static org.junit.Assert.*;


import org.junit.After;
import org.junit.Before;
import org.junit.Test;
public class testtictactoe {
    private tictactoe game;
    @Before
    public void setUp() throws Exception {
        game = new tictactoe();
    }

    @Test
    public void testPosicionFila(){
        //cambiando los datos , vemos que ahora nos arroja la excepcion
        assertThrows(RuntimeException.class, () -> game.fila(6,0));
    }
    @Test
    public void testPosicionColumna() {
        assertThrows(RuntimeException.class, () -> game.columna(1, 6));
    }
    @Test
    public void testPosicionVacia() {
        game.makeMove(1, 1);
        assertThrows(RuntimeException.class, () -> game.posicion_vacia(1, 1));
    }
    @Test
    public void testsigjugador(){
        //podemos saber que jugador sigue sin implementar el metodo proximojugador
        //ya que existe una variable que nos dice que jugador tiene el turno
        //por lo que
        assertEquals("", game.getTurn(), 'X');
        //poniendo una jugada cambia de turno
        game.makeMove(1, 1);
        assertEquals("", game.getTurn(), 'O');
    }
    @Test
    public void testnoganador(){
        //ponemos la prueba pero no implementamos el metodo ganador
        assertEquals("", game.getGameState(), "NOUGHT_WON");
    }
    @Test
    public void testganador(){
        //aqui ponemos una prueba gandora
        game.makeMove(2, 2);
        game.makeMove(0, 0);
        game.makeMove(1, 1);
        game.makeMove(0, 1);
        game.makeMove(1, 0);
        game.makeMove(0, 2);
        assertEquals("", game.getGameState(), tictactoe.GameState.NOUGHT_WON);
    }
    @Test
    public void testXWon() {
        game.makeMove(0, 0);
        game.makeMove(1, 1);
        game.makeMove(0, 1);
        game.makeMove(1, 0);
        game.makeMove(0, 2);
        assertEquals("", game.getGameState(), tictactoe.GameState.CROSS_WON);
}
}
