import java.io.*;

public class RegexMatching{
    public static boolean isMatch(String s, String p) {
        //first make sure that they are both empty.
        //At the end, it should be empty
        if( p.isEmpty() ) return s.isEmpty();
        
        //we can make a variable to check if the first part matches
        //we'll combine this variable with the answers from other combinations
        boolean firstMatch = (!s.isEmpty() && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.') );
        
        //Now we have to check if the next char in the pattern is a star
        if(p.length() > 1 && p.charAt(1) == '*'){
            //there is a branch if it is true
            //1. either firstMatch is true and we can repeat the firstMatch process above
            //  but make sure that one of the char in s is removed
            //2. we can skip this pair entirely
            return (firstMatch && isMatch(s.substring(1), p)) || (isMatch(s, p.substring(2)));
        }else{
            return firstMatch && isMatch(s.substring(1), p.substring(1));
        }
    }

    //to learn
    public static boolean isMatchDP(String s, String p) {
        return false;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new FileReader("RegexMatching.in"));
        PrintWriter pw = new PrintWriter(new FileWriter("out"));
        for(String line = in.readLine();line != null; line = in.readLine()){
            String sp[] = line.split(" ");
            pw.println(isMatchDP(sp[0], sp[1]));
        }
        in.close(); pw.close();
    }
}