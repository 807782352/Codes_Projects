package priv.kyrie.player;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * class PlayListCollection
 * @author kyrie
 *
 */
public class PlayListCollection {
		private Map <String,PlayList> playListMap; // use map to store play lists
		
		public PlayListCollection() {
			playListMap = new HashMap<String,PlayList>();
		}

		/**
		 * Add a play list in the playListCollection
		 * @param playList -- given play list wanted to be added
		 */
		public void addPlayList(PlayList playList) {
			// use PlayList Name as key
			// and use PlayList Object as value
			playListMap.put(playList.getPlayListName(), playList);
		}
		
		/**
		 * Delete the given play list in the playListCollection
		 * @param playList -- given play list wanted to be deleted
		 */
		public void deletePlayList(PlayList playList) {
			playListMap.remove(playList.getPlayListName());
			System.out.println("Delete Successfully!");
		}
		
		/**
		 * Search the play list by its name
		 * @param playListName -- name of the play list
		 * @return a PlayList object
		 */
		public PlayList searchPlayListByName(String playListName) {
			PlayList playlist = null;
			Set <String> playListSet = playListMap.keySet();
			for (String s:playListSet) {
				if (s.equals(playListName)) {
					playlist = playListMap.get(s);break;
				}
			}
			return playlist;
		}
		
		/**
		 * Show all names of play lists
		 */
		public void displayAllPlayListName() {
			System.out.println("List of playlists:");
			Set <String> playListSet = playListMap.keySet();
			for(String s:playListSet) {
				System.out.print(s+"        ");
			}
			System.out.println();
		}
		
		public Map<String, PlayList> getPlayListMap() {
			return playListMap;
		}

		public void setPlayListMap(Map<String, PlayList> playListMap) {
			this.playListMap = playListMap;
		}
		
		
		
		
}
