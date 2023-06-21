Parte 1:
creamos el metodo countClumps para poder contabilizazr los clumps en un arreglo contando con la mayor cobertura

![image](https://github.com/peg1163/CC-3S2/assets/92898224/6186887a-0477-47cd-8a0e-180eb750ee06)

Parte 2:

escribiremos primero las pruebas que delimitan el contador ,con los casos  :

longitud arreglo = 0

arreglo = null

longitud arreglo = 1

y uno extra :

arreglo = aabb 

Parte 3:

Con las pruebas ya escritas , las pasamos a codigo :

```java
public class StringTest {
    @Test
    public void testNotVoid() {
          assert Strings.CountClumps("") == 0;
    }
    @Test
    public void TestnotNull(){
        assert Strings.CountClumps(null) == 0;
    }
    @Test
    public void TestArrays(){
        assert Strings.CountClumps("aabb") == 2;
    }```
    

