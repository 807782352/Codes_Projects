package priv.kyrie.player;

import java.util.ArrayList;
import java.util.List;

/**
 * Class PlayList 
 * @author kyrie
 *
 */
public class PlayList {
		private String playListName;	//the name of playlist
		private List<Song> musicList;	//the musicList to collect Songs.
		
		public PlayList() {
			
		}
		
		/**
		 * Constructor, automatically create an ArrayList for musicList
		 * @param playListName
		 */
		public PlayList(String playListName) {
			this.setPlayListName(playListName);
			musicList = new ArrayList<Song>();
		}

		public String getPlayListName() {
			return playListName;
		}

		public void setPlayListName(String playListName) {
			this.playListName = playListName;
		}
		
		/**
		 * Add songs to the playlist
		 * @param song -- the song that should be added
		 */
		public void addToPlayList(Song song) {
			// need to exclude the situation of adding repeated songs
			boolean flag = false; // Judge whether the given song is in the musicList
			for (Song song1:musicList) {
				if (song1.equals(song)) {
					flag=true;break;
				}
			}
			if (flag) {
				System.out.println("The song has already existed in the music list.\nAdd the song unsuccessfully!");
			}else {
				musicList.add(song);
//				System.out.println("Add the song successfully!");
			}
		}
		
		/**
		 * Display all songs in the playlist
		 */
		public void displayAllSongs() {
			System.out.println("Songs in the music list: "+ this.getPlayListName());
			for (Song song:musicList) {
				System.out.println(song);
			}
		}
		
		/**
		 * Search the song given by ID
		 * @param id -- given ID
		 * @return searched Song's info or null if not found
		 */
		public Song searchSongById(String id) {
			Song song = null;
			for (Song song1:musicList) {
				if (song1.getId().equals(id)) {
					song = song1;break;
				}
			}
			return song;
		}
		
		/**
		 * Search the song given by Song's name
		 * @param name -- given Song's name
		 * @return searched Song's info or null if not found
		 */
		public Song searchSongByName(String name) {
			Song song = null;
			for (Song song1:musicList) {
				if (song1.getName().equals(name)) {
					song = song1;break;
				}
			}
			return song;
		}
		
		/**
		 * Change the song with its id by another given song
		 * @param id -- the Song's ID that wants to be changed
		 * @param song -- the new Song that wants to replace for
		 */
		public void updateSong(String id,Song song) {
			Song song1 = searchSongById(id);
			if (song1 == null) {
				System.out.println("The song with ID"+id+ " is not existed in the music list:"+getPlayListName());
				System.out.println("Change the song unsuccessfullly!");
			} else {
				musicList.remove(song1);
				musicList.add(song);
			}
		}
		
		/**
		 * Delete the song with its ID from the musicList
		 * @param id -- the Song's ID that wants to be deleted
		 */
		public void deleteSong(String id) {
			Song song1 = searchSongById(id);
			if (song1 == null) {
				System.out.println("The song with ID "+id+ " is not existed in the music list:"+getPlayListName());
				System.out.println("Delete the song unsuccessfullly!");
			} else {
				musicList.remove(song1);
			}
		}

}
