import java.util.HashMap;

class FileSystem {
    HashMap<String,Integer> paths;

    public FileSystem() {
        paths = new HashMap<String,Integer>();
        paths.put("/", 0);  // Initialize root path
    }
    
    public boolean createPath(String path, int value) {
        if (path.isEmpty() || path.equals("/") || paths.containsKey(path)) {
            return false; // Invalid path or path already exists
        }
        int delimIndex = path.lastIndexOf("/");
        String parent = path.substring(0, delimIndex);
        if (parent.length() > 0 && !paths.containsKey(parent)) {
            return false; // Parent path does not exist
        }
        paths.put(path, value);
        return true;
    }
    
    public int get(String path) {
        return paths.getOrDefault(path, -1);
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * boolean param_1 = obj.createPath(path, value);
 * int param_2 = obj.get(path);
 */

