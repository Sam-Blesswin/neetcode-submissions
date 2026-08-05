/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if(intervals.isEmpty()){
            return 0;
        }

        intervals.sort(Comparator.comparingInt(
            (interval)->interval.start));

        PriorityQueue<Integer> minheap = new PriorityQueue<>();
        minheap.add(intervals.get(0).end);

        int days = 1;

        for(int i=1; i<intervals.size(); i++){
            if(intervals.get(i).start < minheap.peek()){
                days++;
            }
            else{
                minheap.remove();
            }

            minheap.add(intervals.get(i).end);
        }
        
        return days;
    }
}
