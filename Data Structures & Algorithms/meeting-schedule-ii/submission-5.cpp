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
        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b){
            return a.start < b.start;
        });

        vector<int> days(intervals.size(), 0);

        for(int i=0; i<intervals.size(); i++){
            for(int j=0; j<days.size(); j++){
                if(intervals[i].start >= days[j]){
                    days[j] = intervals[i].end;
                    break;
                }
            }
        }
        
        int res = 0;
        for(int i=0; i<days.size(); i++){
            if(days[i] != 0){
                res++;
            }
        }
        return res;
    }
};
