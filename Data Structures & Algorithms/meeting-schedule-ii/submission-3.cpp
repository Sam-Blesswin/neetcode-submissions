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
        if(intervals.size() == 0){
            return 0;
        }

        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b){
            return a.start < b.start;
        });

        vector<int> endTime;
        endTime.push_back(intervals[0].end);

        for(int i=1; i<intervals.size(); i++){
            bool newDay = true;
            for(int j=0; j<endTime.size(); j++){
                if(intervals[i].start >= endTime[j]){
                    endTime[j] = intervals[i].end;
                    newDay = false;
                    break;
                }
            }
            if(newDay){
                endTime.push_back(intervals[i].end);
            }
        }

        return endTime.size();
    }
};
