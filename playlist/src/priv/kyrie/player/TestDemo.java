package priv.kyrie.player;

public class TestDemo {

	public void test1(){
		Song song1 = new Song("S001","My heart will go on","Celine Dion");
		Song song2 = new Song("S002","Love Story","Taylor Swift");
		Song song3 = new Song("S001","My heart will go on","Celine Dion");
		// test  toString() overwrite 
		System.out.println(song1);
		System.out.println(song2);
		// test equals() overwrite
		boolean isEqual1 = song1.equals(song2);
		boolean isEqual2 = song1.equals(song3);
		System.out.println(isEqual1);
		System.out.println(isEqual2);
	}
	
	public void test2() {
		Song song1 = new Song("S001","My heart will go on","Celine Dion");
		Song song2 = new Song("S002","Love Story","Taylor Swift");
		Song song3 = new Song("S001","My heart will go on","Celine Dion");
		PlayList playlist1 = new PlayList("My favourite");
		playlist1.addToPlayList(song1);
		playlist1.addToPlayList(song2);
		playlist1.addToPlayList(song3);
		playlist1.displayAllSongs();
	}
	
	public void test3() {
		Song song1 = new Song("S001","My heart will go on","Celine Dion");
		Song song2 = new Song("S002","Love Story","Taylor Swift");
		Song song3 = new Song("S003","Attention","Charlie Puth");
		PlayList playlist1 = new PlayList("My Favourite");
		playlist1.addToPlayList(song1);
		playlist1.addToPlayList(song2);
		playlist1.addToPlayList(song3);
		playlist1.displayAllSongs();
		System.out.println("-------------------------------------------------");
		Song song = playlist1.searchSongByName("Attention");
		if (song != null) {
			System.out.println("The song you searched is:\n"+song);
		}else {
			System.out.println("This song is not existed in "+playlist1.getPlayListName());
		}
		System.out.println("-------------------------------------------------");
		song = playlist1.searchSongById("S001");
		if (song != null) {
			System.out.println("The song you searched is:\n"+song);
		}else {
			System.out.println("This song is not existed in "+playlist1.getPlayListName());
		}
		System.out.println("-------------------------------------------------");
		song = playlist1.searchSongById("S005");
		if (song != null) {
			System.out.println("The song you searched is:\n"+song);
		}else {
			System.out.println("This song is not existed in playList: "+playlist1.getPlayListName());
		}	
	}
	
	public void test4(){
		Song song1 = new Song("S001","My heart will go on","Celine Dion");
		Song song2 = new Song("S002","Love Story","Taylor Swift");
		Song song3 = new Song("S003","Attention","Charlie Puth");
		Song song5 = new Song("S005","All of me","John Legend");
		PlayList playlist1 = new PlayList("My Favourite");
		playlist1.addToPlayList(song1);
		playlist1.addToPlayList(song2);
		playlist1.addToPlayList(song3);
		playlist1.displayAllSongs();
		System.out.println("-------------------------------------------------");
		playlist1.updateSong("S002", song5);
		playlist1.displayAllSongs();
		System.out.println("-------------------------------------------------");
		playlist1.deleteSong("S007");
		playlist1.displayAllSongs();
	}
	
	public void test5() {
		Song song1 = new Song("S001","My heart will go on","Celine Dion");
		Song song2 = new Song("S002","Love Story","Taylor Swift");
		Song song3 = new Song("S003","Attention","Charlie Puth");
		Song song5 = new Song("S005","All of me","John Legend");
		PlayList mainPlayList = new PlayList("Main");
		mainPlayList.addToPlayList(song1);
		mainPlayList.addToPlayList(song2);
		mainPlayList.addToPlayList(song3);
		mainPlayList.addToPlayList(song5);
		mainPlayList.displayAllSongs();
		System.out.println("-------------------------------------------------");
		PlayList favoritePlayList = new PlayList("My Favourite");
		favoritePlayList.addToPlayList(song1);
		favoritePlayList.addToPlayList(song2);
		favoritePlayList.addToPlayList(song3);
		favoritePlayList.displayAllSongs();
		System.out.println("-------------------------------------------------");
		PlayListCollection plc = new PlayListCollection();
		plc.addPlayList(mainPlayList);
		plc.addPlayList(favoritePlayList);
		plc.displayAllPlayListName();
		plc.deletePlayList(mainPlayList);
		plc.displayAllPlayListName();
		plc.searchPlayListByName("My Favourite").displayAllSongs();
	}
	
	public static void main(String[] args) {
		TestDemo td = new TestDemo();
		td.test5();

	}

}
