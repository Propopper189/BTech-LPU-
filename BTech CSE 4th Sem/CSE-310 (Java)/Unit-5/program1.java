import java.io.IOException;
import java.lang.classfile.TypeAnnotation.LocalVarTargetInfo;
import java.time.*;
import java.time.format.*;
public class program1 {
    // Write a program to create a console based digital clock
    public static void main(String args[]) throws Exception
    {
        while(true)
        {
            LocalTime t = LocalTime.now(ZoneId.of("Asia/Kolkata"));
            DateTimeFormatter f = DateTimeFormatter.ofPattern("HH:mm:ss");
            System.out.print("\rCurrent Time : " + t.format(f)); // "\r" => refresh the particular line
            Thread.sleep(1000);
        }
    }
}
