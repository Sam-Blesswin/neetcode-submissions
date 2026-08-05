class Solution {
    private Boolean inBound(int m,int n, int i, int j){
        return Math.min(i,j)>=0 && i<m && j<n;
    }
    public void islandsAndTreasure(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        Queue<List<Integer>> queue = new LinkedList<>();
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == 0){
                    queue.offer(Arrays.asList(i,j));
                }
            }
        }

        int count = 0;
        int[][] neigh = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};


 
        while(!queue.isEmpty()){
            int s = queue.size();
            count++;

            for(int i=0;i<s;i++){
                List<Integer> pair = queue.poll();
                int x = pair.get(0);
                int y = pair.get(1);

                for(int[] nb: neigh){
                    if(inBound(m,n,x+nb[0],y+nb[1]) && 
                    grid[x+nb[0]][y+nb[1]] == Integer.MAX_VALUE){
                        grid[x+nb[0]][y+nb[1]] = count;
                        queue.offer(Arrays.asList(x+nb[0],y+nb[1]));
                    }
                }
            }
        }
    }
}
