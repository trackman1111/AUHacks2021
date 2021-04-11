import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class CountySorter {
	private static List<List<String>> lines = new ArrayList<>();
	private static boolean maskPreference;
	
	
	public CountySorter(boolean m)
	{
		this.maskPreference = false;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String fileName = "CountyData.csv";
		String countyCenters = "county_centers.csv";
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
//		for(List<String> line: lines) {
//				System.out.println("Line " + lineNo + " Data:" + line);
//				lineNo++;
//			
//		}
		
		System.out.println(lines.size());
	}
	
	

	public static String getData(List<List<String>> list,int rowNum, int columnNum) {
		return list.get(rowNum).get(columnNum);
	}
	
	public static void maskDelete() {
		
		for(int i = 0; i < lines.size() - 1; i++) {
			if (getData(lines, i, 3).contains("No")) {
				System.out.println("noted");
				lines.remove(i);
				i--;
			}
		}
		System.out.println("Done");
		
	}

}
