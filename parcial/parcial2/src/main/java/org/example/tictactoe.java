package org.example;

public class tictactoe {
    public enum Cell {EMPTY, CROSS, NOUGHT}
    public enum GameState {PLAYING, DRAW, CROSS_WON, NOUGHT_WON}

    private static final int TOTALROWS = 3;
    private static final int TOTALCOLUMNS = 3;

    private Cell[][] grid;
    private char turn;

    private GameState currentGameState;
    // comenzmos con el metodo jugar siendo un metodo que cambiara sus funcionalidad con el tiempo
    //public void juego(int row, int column) {
    // 1er intento
    // if(row > 0 && row <= TOTALROWS ){
    //       System.out.println("Posicion correcta");}
    // else{ thorw new RuntimeException("Posicion incorrecta");}
    //-----------------------------------------------
    //2do intento -> ahora no solo vemos las filas sino tambien las columnas
    // if(row > 0 && row <= TOTALROWS && column > 0 && column <= TOTALCOLUMNS){
    //       System.out.println("Posicion correcta");}
    // else{ thorw new RuntimeException("Posicion incorrecta");}
    //-----------------------------------------------
    //3r intento -> tenemos que comprobar si el espacio donde pondremos la ficha esta vacio
    // if(row > 0 && row <= TOTALROWS && column > 0 && column <= TOTALCOLUMNS
    // && grid[row-1][column-1] == Cell.EMPTY){
    //       System.out.println("Posicion correcta");}
    // else{ thorw new RuntimeException("Posicion incorrecta");}

    //puede que sea confuso con todas las fncionalidades que posee asi que lo dividiremos en metodos
    public void posicion_columna(int row) {


    }
    public void posicion_fila(int column) {


    }
    public void posicion_vacia(int row, int column) {


    }
}
