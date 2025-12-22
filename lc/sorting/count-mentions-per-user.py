class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # sorting
        # time O(nlogn + n^2), space O(n)
        def cmp(a, b):
            int_a = int(a[1])
            int_b = int(b[1])
            if int_a == int_b:
                return -1 if a[0] == 'OFFLINE' else 1
            return 1 if int_a > int_b else -1
            
        events.sort(key = cmp_to_key(cmp))
        res = [0] * numberOfUsers
        time_online = [-1] * numberOfUsers
        for msg,time,ids in events:
            time = int(time)
            if msg == "MESSAGE":
                if ids == "ALL":
                    for i in range(numberOfUsers):
                        res[i] += 1
                elif ids == "HERE":
                    for i in range(numberOfUsers):
                        if time_online[i] <= time:
                            res[i] += 1
                else:
                    ids_list = ids.split(" ")
                    for id in ids_list:
                        idx = int(id[2:])
                        res[idx] += 1
            elif msg == "OFFLINE":
                time_online[int(ids)] = time + 60
        return res
