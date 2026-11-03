import simpy
import random
import matplotlib.pyplot as plt

#Experimentieren Sie mit untershiedlichen Parametern, um das Systemsverhalten zu analysieren

ARRIVAL_RATE = 1.4
MIN_SERVICE = 0.6
MAX_SERVICE = 2.0
NUM_SERVERS = 2
MAX_WAIT = 3.3
SIM_DURATION = 30

queue_history = []
server_history = []
time_history = []


class ServerSimulation:
    def __init__(self, env):
        self.env = env
        self.server = simpy.Resource(env, capacity=NUM_SERVERS)

        self.processed = 0
        self.dropped = 0
        self.total_wait = 0

        self.busy = 0

    def request_generator(self):
        while True:
            yield self.env.timeout(random.expovariate(ARRIVAL_RATE))
            self.env.process(self.handle_request())

    def handle_request(self):
        request = self.server.request()
        arrival_time = self.env.now

        result = yield request | self.env.timeout(MAX_WAIT)

        wait_time = self.env.now - arrival_time

        if request in result:
            self.busy += 1

            service_time = random.uniform(MIN_SERVICE, MAX_SERVICE)
            yield self.env.timeout(service_time)

            self.server.release(request)
            self.busy -= 1

            self.total_wait += wait_time
            self.processed += 1
        else:
            self.server.release(request)
            self.dropped += 1


def monitor(env, sim):
    while True:
        queue_history.append(len(sim.server.queue))
        server_history.append(sim.busy)
        time_history.append(env.now)

        yield env.timeout(0.1)


def run_simulation():
    env = simpy.Environment()
    sim = ServerSimulation(env)

    env.process(sim.request_generator())
    env.process(monitor(env, sim))

    env.run(until=SIM_DURATION)

    avg_wait = sim.total_wait / sim.processed if sim.processed else 0
    throughput = sim.processed / SIM_DURATION

    max_queue = max(queue_history) if queue_history else 0

    total_capacity_time = NUM_SERVERS * SIM_DURATION
    utilization = (sum(server_history) * 0.1) / total_capacity_time * 100

    
    print("\n📊 FINAL REPORT")
    print("-------------------------")
    print(f"Servers: {NUM_SERVERS}")
    print(f"Processed requests: {sim.processed}")
    print(f"Dropped requests: {sim.dropped}")
    print(f"Average wait time: {avg_wait:.3f} s")
    print(f"Throughput: {throughput:.3f} req/s")
    print(f"Max queue length: {max_queue}")
    print(f"Server utilization: {utilization:.2f}%")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    ax1.set_title("Queue Length Over Time")
    ax1.set_xlabel("Simulation time")
    ax1.set_ylabel("Number of requests in queue")

    ax1.plot(time_history, queue_history, label="Queue Length", color="blue")
    ax1.grid(True)
    ax1.legend()

    ax2.set_title("Server Usage Over Time")
    ax2.set_xlabel("Simulation time")
    ax2.set_ylabel("Number of busy servers")

    ax2.plot(time_history, server_history, label="Busy Servers", color="green")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
