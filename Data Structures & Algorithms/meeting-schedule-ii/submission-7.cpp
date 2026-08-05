/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if(intervals.empty()){
            return 0;
        }

        sort(intervals.begin(), intervals.end(), [](auto& A, auto& B){
            return A.start < B.start;
        });

        priority_queue<int, vector<int>, greater<int>> minheap;

        int days = 0;

        for(int i=0; i<intervals.size(); i++){
            if(minheap.empty() || intervals[i].start < minheap.top()){
                days++;
            }else{
                minheap.pop();
            }

            minheap.push(intervals[i].end);
        }

        return days;
    }
};
