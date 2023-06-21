import org.junit.jupiter.api.Test;
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
    @Test
    public void Testfirtclump(){
        assert Strings.CountClumps("aaabdfghdhdc") == 1;
    }
    @Test
    public  void Testlastclump(){
        assert Strings.CountClumps("asfhjeiosfdsaaaa") == 1;
    }
}
