class Solution:
  def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]: # type: ignore
    @lru_cache(None) # type: ignore
    def height(root: TreeNode | None) -> int: # type: ignore
      if not root:
        return 0
      return 1 + max(height(root.left), height(root.right))
    
    valToMaxHeight = {}
    
    def dfs(root: TreeNode | None, depth: int, maxHeight: int) -> None: # type: ignore
      if not root:
        return
      valToMaxHeight[root.val] = maxHeight
      dfs(root.left, depth + 1, max(maxHeight, depth + height(root.right)))
      dfs(root.right, depth + 1, max(maxHeight, depth + height(root.left)))

    dfs(root, 0, 0)
    return [valToMaxHeight[query] for query in queries]
  