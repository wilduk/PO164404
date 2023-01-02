package pl.uwm.wmii.kmmi.luckiewicz;

public class TestAdres {
	public static void main(String[] args)
	{
		Adres jeden = new Adres("Dybowskiego","9","405p","Olsztyn","10-723");
		Adres dwa = new Adres("Kolobrzeska","13k","29","Olsztyn","10-445");

		jeden.pokaz();
		dwa.pokaz();

		if(dwa.przed(jeden)){
			System.out.println("tak");
		}
		else{
			System.out.println("nie");
		}
	}
}
