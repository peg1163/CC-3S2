package test;

import static org.junit.Assert.*;

import org.example.tictactoe;
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
        assertThrows(RuntimeException.class, () -> game.juego(5,1));
    }

}
