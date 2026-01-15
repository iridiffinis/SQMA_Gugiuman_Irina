import org.junit.Test;
import static org.junit.Assert.*;

public class StringTest {
    @Test
    public void testUpperCase() {
        assertEquals("HELLO", "hello".toUpperCase());
    }

    @Test
    public void testConcatenation() {
        assertEquals("Hello World", "Hello" + " " + "World");
    }
}