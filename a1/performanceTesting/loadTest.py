import requests
import time
import matplotlib.pyplot as plt

url = "http://localhost:8080/?short=short&long=long"
num_requests = 1000
response_times = []

for i in range(num_requests):
    start_time = time.time()
    response = requests.put(url)
    end_time = time.time()
    response_times.append(end_time - start_time)
    print(f"Request {i + 1}/{num_requests}: {response.status_code} in {end_time - start_time:.4f} seconds")
    time.sleep(0.1)

plt.figure(figsize=(10, 6))
plt.plot(response_times, marker='o')
plt.title('Response Times for PUT Requests')
plt.xlabel('Request Number')
plt.ylabel('Response Time (seconds)')
plt.grid()
plt.savefig('response_times.png')
plt.close()