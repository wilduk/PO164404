package pl.uwm.wmii.kmmi.luckiewicz;

public class Adres {

	public Adres(String ulica, String nr_domu, String nr_mieszkania, String miasto, String kod_pocztowy){
		this.ulica = ulica;
		this.nr_domu = nr_domu;
		this.nr_mieszkania = nr_mieszkania;
		this.miasto = miasto;
		this.kod_pocztowy = Integer.parseInt(kod_pocztowy.substring(0,2)+kod_pocztowy.substring(3));
	}
	public Adres(String ulica, String nr_domu, String miasto, String kod_pocztowy){
		this.ulica = ulica;
		this.nr_domu = nr_domu;
		this.miasto = miasto;
		this.kod_pocztowy = Integer.parseInt(kod_pocztowy.substring(0,2)+kod_pocztowy.substring(3));
	}

	public void pokaz()
	{
		if(this.nr_mieszkania != null) {
			System.out.println(this.getKod_pocztowy()+" "+this.miasto+"\n"+this.ulica+" "+this.nr_domu+" "+this.nr_mieszkania);
		}
		else{
			System.out.println(this.getKod_pocztowy()+" "+this.miasto+"\n"+this.ulica+" "+this.nr_domu);
		}

	}

	public boolean przed(Adres inny){
		if(this.kod_pocztowy < inny.getKod_pocztowyInt()){
			return true;
		}
		return false;
	}

	public String getKod_pocztowy(){
		return (this.kod_pocztowy-this.kod_pocztowy%1000)/1000+"-"+this.kod_pocztowy%1000;
	}
	public int getKod_pocztowyInt(){
		return this.kod_pocztowy;
	}

	private String ulica;
	private String nr_domu;
	private String nr_mieszkania;
	private String miasto;
	private int kod_pocztowy;
}
