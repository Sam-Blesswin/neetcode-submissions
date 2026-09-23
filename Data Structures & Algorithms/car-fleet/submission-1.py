class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort()

        time = [(target - p)/s for p,s in pair]

        fleet = 0
        val = 0.0
        for i in range(len(time)-1,-1,-1):
            if time[i] > val:
                val= time[i]
                fleet+=1

        return fleet
        