package solutions.euler.problems;

import java.io.File;
import java.io.FileNotFoundException;
import java.text.Collator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Names_Scores {

	public static long getScore(String data) {

		File dataFile = new File(data);
		Pattern p = Pattern.compile("[\\w]+");
		long fileScore = 0;
		int multiplier = 1;

		List<String> sortedNames = new LinkedList<String>();

		try {
			Scanner scanFile = new Scanner(dataFile);
			while (scanFile.hasNext()) {
				String found = scanFile.findInLine(p);
				if (found == null) {
					break;
				}
				sortedNames.add(found);
			}

		} catch (

		FileNotFoundException e) {
			e.printStackTrace();
		}

		sortedNames.sort(Collator.getInstance());

		for (String name : sortedNames) {
			fileScore += multiplier * getNameScore(name);
			multiplier++;
		}
		return fileScore;
	}

	private static int getNameScore(String name) {
		final String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int nameScore = 0;
		for (char letter : name.toCharArray()) {
			nameScore += alphabet.indexOf(letter) + 1;
		}

		return nameScore;
	}

}
