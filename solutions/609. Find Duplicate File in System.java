class Solution {
public List<List<String>> findDuplicate(String[] paths) {
    Map<String,List<String>> map = new HashMap<>();
    for(String path : paths)
    {
        String[] pathComponents = path.split(" ");
        String root = pathComponents[0];
        for(int i = 1; i < pathComponents.length; i++)
        {
            int startIndex = pathComponents[i].indexOf("(");
            int endIndex = pathComponents[i].lastIndexOf(")");
            String content = pathComponents[i].substring(startIndex, endIndex);
            
            map.putIfAbsent(content, new ArrayList<>());
            map.get(content).add(root+"/"+pathComponents[i].substring(0,startIndex));
        }
    }
    
    List<List<String>> result = new ArrayList<List<String>>();
    for(List<String> list : map.values())
    {
        if(list.size() > 1) result.add(list);
    }
    
    return result;
}
}
