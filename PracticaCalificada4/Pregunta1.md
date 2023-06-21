Parte 1:
creamos el metodo countClumps para poder contabilizazr los clumps en un arreglo contando con la mayor cobertura

    ```java
    public class Strings {

    public static int CountClumps(String nums) {
        int count = 0;
        int i = 0;
        int count_size=1;
        //este bucle recorre todo el arreglo
        if (nums.length() == 0) {
            return 0;
        }
        if (nums == null) {
            return 0;
        }

        while (i < nums.length()-1) {
            //si encuentra caracteres iguales aumenta el contador de caracteres y el indice
            if (nums.charAt(i) == nums.charAt(i + 1)) {
                i++;
                count_size++;

            //si 2 caracteres juntos no son iguales, entonces se encontro un grupo
                // se aumenta el contador de clumps y se reinicia el contador de caracteres
            } else if (count_size >= 2) {
                count++;
                count_size=1;
                i++;
            }
            else {
                i++;
            }
        }
        //retorna el contador de clumps
        return count;
    }
    }```
        

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
            assert Strings.CountClumps(null) == 0;}

        @Test
        public void TestArrayslength1(){
            assert Strings.CountClumps("a") == 0;
        }
        @Test
        public void TestArrays(){
            assert Strings.CountClumps("aabb") == 2;
        }
    }```

en esta parte nos muestra errores el TestnotNull y en TestArrays 
ya que en el segundo solo encuentra 1 clump por lo que modificamos el metodo countclumps() :
                
            ```java
                   public class Strings {

                public static int CountClumps(String nums) {
                    int count = 0;
                    int i = 0;
                    int count_size=1;
                    //este bucle recorre todo el arreglo
                    if (nums.length() == 0) {
                        return 0;
                    }
                    if (nums == null) {
                        return 0;
                    }

                    while (i < nums.length()-1) {
                        //si encuentra caracteres iguales aumenta el contador de caracteres y el indice
                        if (nums.charAt(i) == nums.charAt(i + 1)) {
                            i++;
                            count_size++;
                            if (count_size >= 2 && i == nums.length()-1) {
                                count++;
                            }
                        //si 2 caracteres juntos no son iguales, entonces se encontro un grupo
                            // se aumenta el contador de clumps y se reinicia el contador de caracteres
                        } else if (count_size >= 2) {
                            count++;
                            count_size=1;
                            i++;
                        }
                        else {
                            i++;
                        }
                    }
                    //retorna el contador de clumps
                    return count;
                }
                }```

Configurado esto ya no hay errores en los tests 

Parte 4:
Para esto escribimos 2 test que vean un clump que esta al inicio y al final del arreglo :

 
     ```java
            @Test
        public void Testfirtclump(){
            assert Strings.CountClumps("aaabdfghdhdc") == 1;
        }
        @Test
        public  void Testlastclump(){
            assert Strings.CountClumps("asfhjeiosfdsaaaa") == 1;
        }```



lo ejecutamos y vemos que los test son correctos , no ocurre error alguno 

![image](https://github.com/peg1163/CC-3S2/assets/92898224/e1b99900-d410-443a-bdb4-e6da7f1738cd)




    
    

