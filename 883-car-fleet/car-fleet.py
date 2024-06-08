class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       
       cars = sorted(zip(position, speed), reverse=True)
       times = [(target - p) / s for p, s in cars]

       fleets = 0
       slowestTime = 0 

       for time in times:
           if time > slowestTime:
            fleets += 1
            slowestTime = time

       return fleets
       

          

                