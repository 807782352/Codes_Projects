package priv.kyrie.player;

/**
 * Class Song
 * 
 * @author kyrie
 *
 */

public class Song {
	private String id; // the ID of the Song
	private String name; // the name of the Song
	private String singer; // the Singer of the Song

	public Song() {

	}

	public Song(String id, String name, String singer) {
		this.setId(id);
		this.setName(name);
		this.setSinger(singer);
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSinger() {
		return singer;
	}

	public void setSinger(String singer) {
		this.singer = singer;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		result = prime * result + ((singer == null) ? 0 : singer.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		// Judge whether two objects are equaled, if equaled return true
		if (this == obj) {
			return true;
		}
		if (obj.getClass() == Song.class) {
			Song song = (Song) obj;
			return song.getId().equals(this.getId()) && song.getName().equals(this.getName())
					&& song.getSinger().equals(this.getSinger());
		}
		return false;
	}

	@Override
	public String toString() {
		return "Info of the Song: the ID is " + id + ", the Name is " + name + ", and the Singer is " + singer + ".";
	}

	
}
