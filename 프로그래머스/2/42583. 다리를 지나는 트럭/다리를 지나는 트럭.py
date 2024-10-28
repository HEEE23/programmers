from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    # 다리에 있는 트럭의 무게 
    bridge_truck_weights = 0
    while bridge:
        answer += 1
        
        # 지나간 트럭의 무게 제외
        bridge_truck_weights -= bridge.popleft()
        
        if truck_weights:
            if bridge_truck_weights + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge_truck_weights += t
                bridge.append(t)
            else:
                bridge.append(0)

    return answer