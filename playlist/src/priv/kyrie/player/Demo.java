package priv.kyrie.player;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Demo {

	public void mainMenu() {
		System.out.println("***********************************************************");
		System.out.println("\t**Main Menu**");
		System.out.println("\t**1--Music Play List Management**");
		System.out.println("\t**2--Music Player Management**");
		System.out.println("\t**0--Exit**");
		System.out.println("***********************************************************");
	}
	
	public void playListMenu() {
		System.out.println("***********************************************************");
		System.out.println("\t**Music Play List Management**");
		System.out.println("\t**1--Add a song into main play list**");
		System.out.println("\t**2--Add a song into other play list**");
		System.out.println("\t**3--Search the song from a play list by ID**");
		System.out.println("\t**4--Search the song from a play list by name**");
		System.out.println("\t**5--Change the song from a play list**");
		System.out.println("\t**6--Delete the song from a play list**");
		System.out.println("\t**7--Display all songs in a play list**");
		System.out.println("\t**9--Back to previous menu**");
		System.out.println("***********************************************************");
	}
	
	public void playerMenu() {
		System.out.println("***********************************************************");
		System.out.println("\t**Music Player Management**");
		System.out.println("\t**1--Add a play list into the player**");
		System.out.println("\t**2--Delete a play list from the player**");
		System.out.println("\t**3--Search the play list from player by name**");
		System.out.println("\t**4--Display all play lists in the player**");
		System.out.println("\t**9--Back to previous menu**");
		System.out.println("***********************************************************");
	}
	
	/**
	 * Main Process
	 */
	public void test() {
		Demo d = new Demo();
		Scanner sc = new Scanner(System.in);
		String opt = "0",opt1 = "0",opt2 = "0";
		PlayList favouritePlayList = null;
		
		//Construct a player (play list connection)
		PlayListCollection plc = new PlayListCollection();
		//Construct a main play list (default)
		PlayList mainPlayList = new PlayList("Main");
		//Add the main play list into the player
		plc.addPlayList(mainPlayList);
		
		while(true) {
			d.mainMenu();
			System.out.println("Please input given number to operate: ");
			opt = sc.next();			
			if (opt.equals("0")) {
				System.out.println("Exit Successfully!");
				break;
			}
			switch(opt) {
			case "1":
				//Music Play List Management
				while(true) {
					d.playListMenu();
					System.out.println("Please input given number to manage the play list:");
					opt1 = sc.next();
					if (opt1.equals("9")) {
						break;
					}
					switch(opt1) {
						case "1":
							System.out.println("***********************************************************");
							System.out.println("Add a song into main play list");
							System.out.println("***********************************************************");
							System.out.println("How many songs do you want to add?");
							int count = 0;
							try {
								count = sc.nextInt();
								for (int i=1;i<=count;i++) {
									System.out.println("Please input No."+i+" song: ");
									System.out.println("***Notice: use _ as blankspace***");
									System.out.println("Please input song's ID:");
									String songId = sc.next();
									System.out.println("Please input song's name:");
									String songName = sc.next();
									System.out.println("Please input song's singer:");
									String songSinger = sc.next();
									// construct Sing Object
									Song song = new Song(songId,songName,songSinger);
									mainPlayList.addToPlayList(song);
								}
							}catch(InputMismatchException e) {
								System.out.println("Please input correct operand!");
								sc.next();
							}
//							mainPlayList.displayAllSongs();
							break;
						case "2":
							System.out.println("***********************************************************");
							System.out.println("Add a song into other play list");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName = sc.next();
							// Judge whether the play list has already existed
							favouritePlayList = plc.searchPlayListByName(playListName);
							if (favouritePlayList == null) {
								System.out.println("This play list does not exist, please add this play list into the player first!");
							}else {
								System.out.println("How many songs do you want to add?");
								try {
									int count1 = sc.nextInt();
									for (int i=1;i<=count1;i++) {
										System.out.println("Please input No."+i+" song: ");
										System.out.println("***Notice: use _ as blankspace***");
										System.out.println("Please input song's ID:");
										String songId = sc.next();
										// Judge whether the song has existed in Main play list
										
										Song song = mainPlayList.searchSongById(songId);
										if (song==null) {
											// if not, needs to add new song into the Main play list first
											System.out.println("This song does not exist in the Main play list");
											System.out.println("Please continue to input the name of the song:");
											System.out.println("***Notice: use _ as blankspace***");
											String songName = sc.next();
											System.out.println("Please continue to input the singer of the song:");
											System.out.println("***Notice: use _ as blankspace***");
											String songSinger = sc.next();
											// Construct a new Sing object
											song = new Song(songId,songName,songSinger);
											// Add the song into the Main play list and other chosen play list
											mainPlayList.addToPlayList(song);
											favouritePlayList.addToPlayList(song);
										}
										else {
											// if exists, add the song into the chosen play list directly
											favouritePlayList.addToPlayList(song);
										}
										System.out.println("Songs in Main List:");
										mainPlayList.displayAllSongs();
										System.out.println("Songs in" + favouritePlayList.getPlayListName());
										favouritePlayList.displayAllSongs();
									}
								}	catch(InputMismatchException e) {
									System.out.println("Please input correct operand!");
									sc.next();
								}
							}
							break;
						case "3":
							System.out.println("***********************************************************");
							System.out.println("Search the song from a play list by ID");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName1 = sc.next();
							// check whether the play list is existed
							PlayList pl = plc.searchPlayListByName(playListName1);
							if (pl==null) {
								System.out.println(playListName1 +" does not exist in the player");break;
							}else {
								System.out.println("Please input the ID of the song:");
								String strId1 = sc.next();
								Song s = pl.searchSongById(strId1);
								if (s==null) {
									System.out.println("The song in" + playListName1 + "does not exist!");
								}else {
									System.out.println("The info of the song is:");
									System.out.println(s);
								}
							}
							break;
						case "4":
							System.out.println("***********************************************************");
							System.out.println("Search the song from a play list by name");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName2 = sc.next();
							// check whether the play list is existed
							PlayList pl1 = plc.searchPlayListByName(playListName2);
							if (pl1==null) {
								System.out.println(playListName2 +" does not exist in the player");break;
							}else {
								System.out.println("Please input the name of the song:");
								String strName = sc.next();
								Song s = pl1.searchSongByName(strName);
								if (s==null) {
									System.out.println("The song in" + playListName2 + "does not exist!");
								}else {
									System.out.println("The info of the song is:");
									System.out.println(s);
								}
							}
							break;
						case "5":
							System.out.println("***********************************************************");
							System.out.println("Change the song from a play list");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName3 = sc.next();
							// check whether the play list is existed
							PlayList pl2 = plc.searchPlayListByName(playListName3);
							if (pl2==null) {
								System.out.println(playListName3 +" does not exist in the player");break;
							}else {
								System.out.println("Please input the ID of the song that wants to be replaced:");
								String strId = sc.next();
								Song song = pl2.searchSongById(strId);
								if (song == null) {
									System.out.println("The song in " + playListName3 + " does not exist!");
								}else {
									System.out.println("Please input the ID of the new song:");
									System.out.println("***Notice: use _ as blankspace***");
									String newid = sc.next();
									System.out.println("Please input the name of the new song:");
									System.out.println("***Notice: use _ as blankspace***");
									String newName = sc.next();
									System.out.println("Please input the singer of the new song:");
									System.out.println("***Notice: use _ as blankspace***");
									String newSinger = sc.next();
									Song newSong = new Song(newid,newName,newSinger);
									pl2.updateSong(strId, newSong);
									System.out.println("Change Successfully!");
								}
							}
							break;
						case "6":
							System.out.println("***********************************************************");
							System.out.println("Delete the song from a play list");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName4 = sc.next();
							// check whether the play list is existed
							PlayList pl3 = plc.searchPlayListByName(playListName4);
							if (pl3==null) {
								System.out.println(playListName4 +" does not exist in the player");break;
							}else {
								System.out.println("Please input the ID of the song that wants to be deleted:");
								String strId = sc.next();
								Song song = pl3.searchSongById(strId);
								if (song == null) {
									System.out.println("The song in " + playListName4 + " does not exist!");
								}else {
									pl3.deleteSong(strId);
									System.out.println("Delete Successfully!");
								}
							}
							break;
						case "7":
							System.out.println("***********************************************************");
							System.out.println("Display all songs in a play list");
							System.out.println("***********************************************************");
							System.out.println("Please input the name of the play list");
							String playListName5 = sc.next();
							// check whether the play list is existed
							PlayList pl4 = plc.searchPlayListByName(playListName5);
							if (pl4==null) {
								System.out.println(playListName5 +" does not exist in the player");break;
							}else {
								pl4.displayAllSongs();
							}
							break; 
						default:
							System.out.println("No related operation! ");
							break;
					}
				}
				break;
			case "2":
				//Music Player Management
				while(true) {
					d.playerMenu();
					System.out.println("Please input given number to manage the player:");
					opt2 = sc.next();
					if (opt2.equals("9")) {
						break;
					}
					switch(opt2) {
						case "1":
							System.out.println("***********************************************************");
							System.out.println("Add a play list into the player");
							System.out.println("***********************************************************");
							System.out.println("Please add the name of the play list:");
							String playListName=sc.next();
							// Construct a new play list object
							favouritePlayList = new PlayList(playListName);
							// Add play list into the Map of the player
							plc.addPlayList(favouritePlayList);
							break;
						case "2":
							System.out.println("***********************************************************");
							System.out.println("Delete a play list from the player");
							System.out.println("***********************************************************");
							System.out.println("Please add the name of the play list:");
							String playListName1=sc.next();
							if (playListName1.equals("Main")) {
								System.out.println("Main list cannot be deleted!");
								break;
							}
							// Check whether the playlist does exist
							PlayList playList1 = plc.searchPlayListByName(playListName1);
							if(playList1 == null) {
								System.out.println("The playlist is not existed!");
							}else {
								plc.deletePlayList(playList1);
							}
							break;
						case "3":
							System.out.println("***********************************************************");
							System.out.println("Search the play list from player by name");
							System.out.println("***********************************************************");
							System.out.println("Please add the name of the play list:");
							String playListName2=sc.next();
							PlayList playList2 = plc.searchPlayListByName(playListName2);
							if(playList2 == null) {
								System.out.println("The playlist is not existed!");
							}else {
								System.out.println("The playlist is existed!");
								System.out.println("The name of the play list is "+playListName2);
								playList2.displayAllSongs();
							}
							break;
						case "4":
							System.out.println("***********************************************************");
							System.out.println("Display all play lists in the player");
							System.out.println("***********************************************************");
							plc.displayAllPlayListName();
							break;
						default:
							System.out.println("No related operation! ");
							break;
					}
				}
				break;
			default:
				System.out.println("No related operation! ");
				break;
			}
		}
	}
	
	public static void main(String[] args) {
		Demo td = new Demo();
		td.test();
	}

}
