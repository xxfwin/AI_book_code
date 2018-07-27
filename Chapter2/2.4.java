List<String> rt = new ArrayList<String>();
List<Integer> path = new ArrayList<Integer>();

public List<String> binaryTreePaths(TreeNode root) 
{
    findPath(root);
    return rt;
}

void findPath(TreeNode root) 
{

    if (root == null) 
    {
        return;
    }

    path.add(root.val);

    if (root.left == null && root.right == null) 
    {
        StringBuffer sb = new StringBuffer();
        sb.append(path.get(0));
        for (int i = 1; i < path.size(); i++) 
        {
            sb.append("->" + path.get(i));
        }
        rt.add(sb.toString());
    }

    findPath(root.left);
    findPath(root.right);

    path.remove(path.size() - 1);
}