import random
import heapq

class Client:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time  # Time when the client arrives
        self.service_time = service_time  # Time taken to serve the client

def simulate_bank():
    # Initialize variables
    time = 0
    queue1 = []
    queue2 = []
    event_queue = []  # Min-heap for events
    total_clients_served = 0
    simulation_time = 80  # Run the simulation for 80 minutes

    # Schedule the first client arrival
    first_arrival_time = random.randint(1, 3)
    heapq.heappush(event_queue, (first_arrival_time, 'arrival'))

    while event_queue and time < simulation_time:
        # Get the next event
        time, event_type = heapq.heappop(event_queue)

        if event_type == 'arrival':
            # Create a new client
            service_time = random.randint(1, 10)
            new_client = Client(time, service_time)

            # Place the client in the shortest queue
            if len(queue1) <= len(queue2):
                queue1.append(new_client)
            else:
                queue2.append(new_client)

            print(f"Client arrives at {time} minutes. Assigned to {'Teller 1' if len(queue1) <= len(queue2) else 'Teller 2'}.")

            # Schedule the next client arrival
            next_arrival_time = time + random.randint(1, 3)
            heapq.heappush(event_queue, (next_arrival_time, 'arrival'))

            # Check if a teller can serve a client
            if len(queue1) == 1 and len(queue2) == 0:
                completion_time = time + queue1[0].service_time
                heapq.heappush(event_queue, (completion_time, 'departure_teller1'))
            elif len(queue2) == 1 and len(queue1) == 0:
                completion_time = time + queue2[0].service_time
                heapq.heappush(event_queue, (completion_time, 'departure_teller2'))
            elif len(queue1) > 0 and len(queue2) > 0:
                # Check both queues and serve the next client
                if queue1[0].arrival_time <= queue2[0].arrival_time:
                    completion_time = time + queue1[0].service_time
                    heapq.heappush(event_queue, (completion_time, 'departure_teller1'))
                else:
                    completion_time = time + queue2[0].service_time
                    heapq.heappush(event_queue, (completion_time, 'departure_teller2'))

        elif event_type == 'departure_teller1':
            if queue1:
                finished_client = queue1.pop(0)  # Serve the client
                total_clients_served += 1
                print(f"Client served at Teller 1 and leaves at {time} minutes.")
                
                # Check if the last client in queue2 can switch to queue1
                if queue2:
                    last_client_queue2 = queue2[-1]
                    if last_client_queue2.arrival_time + last_client_queue2.service_time < time:
                        queue2.pop()
                        queue1.append(last_client_queue2)
                        print(f"Client from queue 2 moves to queue 1 at {time} minutes.")

                # Schedule next departure if queue1 is not empty
                if queue1:
                    completion_time = time + queue1[0].service_time
                    heapq.heappush(event_queue, (completion_time, 'departure_teller1'))

        elif event_type == 'departure_teller2':
            if queue2:
                finished_client = queue2.pop(0)  # Serve the client
                total_clients_served += 1
                print(f"Client served at Teller 2 and leaves at {time} minutes.")
                
                # Check if the last client in queue1 can switch to queue2
                if queue1:
                    last_client_queue1 = queue1[-1]
                    if last_client_queue1.arrival_time + last_client_queue1.service_time < time:
                        queue1.pop()
                        queue2.append(last_client_queue1)
                        print(f"Client from queue 1 moves to queue 2 at {time} minutes.")

                # Schedule next departure if queue2 is not empty
                if queue2:
                    completion_time = time + queue2[0].service_time
                    heapq.heappush(event_queue, (completion_time, 'departure_teller2'))

    # End of simulation
    print(f"\nSimulation ended. Total clients served: {total_clients_served}")

# Run the simulation
simulate_bank()
