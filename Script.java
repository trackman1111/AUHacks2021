import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Script {
	static List<List<String>> lines = new ArrayList<>();
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String fileName = "CountyData.csv";
		File file = new File(fileName);
		System.out.println("Attempting to read from file in: " + file.getCanonicalPath());
		
		
		Scanner inputStream;
		try {
			inputStream = new Scanner(file);
			
			while(inputStream.hasNext()) {
				String line = inputStream.nextLine();
				String[] values = line.split(",");
				List<String> csvPieces = new ArrayList<String>();
				for(String piece: values) {
				csvPieces.add(piece);
				}
				lines.add(csvPieces);
			}
			inputStream.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		maskDelete();
		
		int lineNo = 1;
		for(List<String> line: lines) {
			int columnNo = 1;
			for (String value: line) {
				System.out.println("Line " + lineNo + " Column " + columnNo + ": " + value);
				columnNo++;
			}
			lineNo++;
			
		}
		
		//Testing getData method
		System.out.println(getData(lines, 4, 2));
	}
	
	

	public static String getData(List<List<String>> list,int rowNum, int columnNum) {
		return list.get(rowNum).get(columnNum);
	}
	
	public static void maskDelete() {
		
		for(int i = 0; i < lines.size() - 1; i++) {
			if (getData(lines, i, 2).contains("No")) {
				//System.out.println("noted");
				lines.remove(i);
				i--;
			}
		}
		
	}

}
