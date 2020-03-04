import java.io.*;

public class Sample{

    public static String method(){
        return "answer!";
    }

    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new FileReader("Sample.in"));
        PrintWriter pw = new PrintWriter(new FileWriter("out"));
        for(String line = in.readLine();line != null; line = in.readLine()){
            pw.println(method());
        }
        in.close(); pw.close();
    }
}