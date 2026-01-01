# class Solution:
#     def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
#         # find the longest existing free time
#         # find a slot to move the one of the left or right of this


#         #1st attempt
#         #find longest contiguous
        
#         free_time = (0, 0)
#         before_meeting = (0,0)
#         after_meeting = (0,0)
#         beginning = 0

#         free_periods = []
#         free_period_times = []

#         longest_free = 0

#         for i in range(len(startTime)):
#             start = startTime[i]
#             end = endTime[i]
            
#             if (start - beginning > 0):
#                 free_periods.append((beginning, start))
#                 free_period_times.append(start - beginning)

#             if (start - beginning) > (free_time[1] - free_time[0]):
#                 free_time = (beginning, start)
#                 if beginning != 0 and i != 0:
#                     before_meeting = (startTime[i - 1], endTime[i - 1])
#                 if end != eventTime and i != len(startTime):
#                     after_meeting = (startTime[i], endTime[i])

#             beginning = end


#         if endTime[-1] < eventTime:
#             free_periods.append((endTime[-1], eventTime))
#             free_period_times.append(eventTime - endTime[-1])
            
#         print(free_time)
#         print(free_periods)
#         print(free_period_times)

#         # no free time at all
#         if free_time == (0, 0):
#             return 0

#         if len(free_period_times) == 1:
#             return free_period_times[0] 

#         if len(free_periods) == 2:
#             return (free_periods[1][1] - free_periods[0][0]) - (free_periods[1][0] - free_periods[0][1])

#         index = free_periods.index(free_time)

#         if index == 0:
#             #only check right
#             time_to_check = free_periods[index + 1][0] - free_time[1]

#             for i in range(1, len(free_period_times)):
#                 if free_period_times[i] >= time_to_check:
#                     return free_period_times[index] + time_to_check + free_period_times[index + 1]
#                 if i == len(free_period_times):
#                     return free_period_times[index] - time_to_check + free_period_times[index + 1]

#         elif index == len(free_periods):
#             #only check left
#             time_to_check = free_periods[index - 1][1] - free_time[0]

#             for i in range(len(free_period_times) - 1):
#                 if free_period_times[i] >= time_to_check:
#                     return free_period_times[index] + time_to_check + free_period_times[index - 1]
#                 if i == len(free_period_times - 1):
#                     return free_period_times[index] - time_to_check + free_period_times[index - 1]
            
#         else:
#             #check both

#             #check left and right
#             time_to_check_left = free_periods[index - 1][1] - free_time[0]
#             time_to_check_right = free_periods[index + 1][0] - free_time[1]

#             longest_time = max(free_period_times[index] - time_to_check_left + free_period_times[index - 1], free_period_times[index] - time_to_check_right + free_period_times[index + 1])
            
#             for i in range(len(free_period_times)):
                
#                 if free_periods[i] != free_time and free_period_times[i] >= time_to_check_left:
#                     longest_time = max(longest_time, free_period_times[index] + time_to_check_left + free_period_times[index - 1])
#                 if free_periods[i] != free_time and free_period_times[i] >= time_to_check_right:
#                     longest_time = max(longest_time, free_period_times[index] + time_to_check_right + free_period_times[index + 1])

            
#             return longest_time


## fixed ans

class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2,
                (eventTime if i == 0 else startTime[n - i])
                - endTime[n - i - 1],
            )

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res
