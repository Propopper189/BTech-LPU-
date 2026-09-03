import java.time.*;
import java.time.format.*;

public class practice26
{
    public static void main(String args[])
    {
        String dt = "15-05-2026 07:26:10 PM +0530";

        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy hh:mm:ss a Z");

        OffsetDateTime dati = OffsetDateTime.parse(dt, f);
        String l = dati.toString();
        System.out.println(l);
        System.out.println(dati);
    }
}