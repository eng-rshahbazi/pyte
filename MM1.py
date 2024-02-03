import random
import simpy
import numpy
from random import seed
import statistics
seed(29384)  # for seed of randint function
random_seed = 42  # for seed of other random generators
new_customers = 10  # Total number of customers in the system
interarrival = numpy.random.poisson(6, size=None)  # Generate new customers roughly every x seconds
waitingTimes = []
serviceTimes = []
interarrivalTimes = []

def generator(env, number, interval, server):  # customer generator with interarrival times.
    """generator generates customers randomly"""
    for i in range(number):
        c = customer(env, 'Customer%02d' % i, server, service_time=random.expovariate(0.15))
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)  # adds time to the counter, does not delete from the memory

def customer(env, name, server, service_time):
    # customer arrives to the system, waits and leaves
    arrive = env.now
    print('%7.4f : Arrival time of %s' % (arrive, name))
    with server.request() as req:
        results = yield req | env.timeout(arrive)
        
        if req in results:
            servertime = service_time
            yield env.timeout(servertime)
            serviceTimes.append(servertime)
            print('%7.4f Departure Time of %s' % (env.now, name))
            print('%7.4f Time Spent in the system of %s' % (env.now - arrive, name))
        else:
            waiting_time = env.now - arrive
            waitingTimes.append(waiting_time)
            print('%6.3f Waiting time of %s' % (waiting_time, name))

random.seed(random_seed)
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)  # capacity changes the number of generators in the system.
env.process(generator(env, new_customers, interarrival, server))
env.run()
interarrivalTimes.append(interarrival)
average_interarrival = statistics.mean(interarrivalTimes)
average_waitingTime = statistics.mean(waitingTimes)
average_serviceTime = statistics.mean(serviceTimes)
print("Average Interravial Time Is : %7.4f" % (average_interarrival))
print("Average Waiting Time Is : %7.4f" % (average_waitingTime))
print("Average Service Time Is : %7.4f" % (average_serviceTime))

print("Elements of given array: ")
for i in range(0, len(interarrivalTimes)):
    print(interarrivalTimes[i]),
