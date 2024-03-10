import random, requests, json, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def generate_test_file(num_tests=500, seed=None) -> None:
    file = open('testfile.json', 'w')
    file.write('{\n\t"requestType": "tour",')
    file.write('\n\t"earthRadius": 1234,')
    file.write('\n\t"response": 1,')
    file.write('\n\t"places": [')
    
    random.seed(seed) #change seed or remove
    for i in range(num_tests):
        latitude = random.randint(-90, 90)
        longitude = random.randint(-180, 180)
        
        file.write('\n\t\t{\n')
        file.write(f'\t\t\t"latitude": "{latitude}",\n')
        file.write(f'\t\t\t"longitude": "{longitude}"\n')
        
        if i == num_tests - 1: 
            file.write('\t\t}\n')
            break
        
        file.write('\t\t},\n')
    
    file.write('\t]\n')
    file.write('}\n')

def generate_distances(num=20, seed=None) -> None:
    random.seed(seed)
    file = open('distances.json', 'w')
    file.write('{\n\t"places": [')
    
    for i in range(num):
        latitude = random.randint(-90, 90)
        longitude = random.randint(-180, 180)
        
        file.write('\n\t\t{\n')
        file.write(f'\t\t\t"latitude": "{latitude}",\n')
        file.write(f'\t\t\t"longitude": "{longitude}",\n')
        file.write(f'\t\t\t"name": "{i}",\n')
        file.write(f'\t\t\t"municipality": "{i}",\n')
        file.write(f'\t\t\t"region": "{i}"\n')
        if i == num - 1: 
            file.write('\t\t}\n')
            break
        file.write('\t\t},\n')
    
    file.write('\t]\n')
    file.write('}\n')

def send_to_server(verbose=False, timeout=15) -> tuple[int, float]:
    # url = 'https://black-bottle.cs.colostate.edu:31412/api/tour'
    url = 'http://127.0.0.1:41312/api/tour'
    
    with open('testfile.json', 'r') as file:
        json_data = json.load(file)
    
    session = requests.Session()
    start = time.time()
    response = session.post(url, json=json_data, verify='cs314.pem', timeout=timeout)
    end = time.time()
    response_time = end - start 
    response_status = response.status_code
    
    if verbose:
        print(f'SERVER RESPONSE:')
        print(f'STATUS CODE: {response_status}')
        print(f'TIME ELAPSED: {response_time}s')
        
        pretty_json = json.loads(response.text)
        with open('server_response.json', 'w') as file:
            file.write(json.dumps(pretty_json, indent=2))
            
    return (response_status, response_time)

def cubic_polynomial_func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def compute_average_function(x, y) -> None:
    a = []; b = []; c = []; d = []
    
    for i in range(10): #increase if needed
        params, _ = curve_fit(cubic_polynomial_func, x, y)  #covariance will not be calculated when 
        ai, bi, ci, di = params                             #there are not enough values or they are really small
        a.append(ai); b.append(bi); c.append(ci); d.append(di)
        
    a_mean = np.mean(a); b_mean = np.mean(b); c_mean = np.mean(c); d_mean = np.mean(d)
    print(f'Equation: {a_mean:.10f}x^3 + {b_mean:.10f}x^2 + {c_mean:.10f}x + {d_mean:0.10f}')

def benchmark(iterations=1, intervals=50, max_tests=1000, max_seconds=1, verbose=False) -> None:
    results = []
    for iter in range(iterations):
        for i in range(0, max_tests, intervals):
            generate_test_file(i)
            try:
                status, time = send_to_server()
            except:
                continue
            print(f'Completed {iter}:{i}')
            if status >= 400: raise Exception #could be because server returned 500 for 0 places
            results.append([i, time])
    results = np.array(results, dtype=np.float32)
    
    results_mean = []
    for i in range(0, max_tests, intervals):
        filtered_row = results[results[:,0] == i]
        results_mean.append([i, np.mean(filtered_row[:,1])])
    results_mean = np.array(results_mean, dtype=np.float32)        
       
    if verbose:
        for r in results:
            print(f'Num tests: {r[0]}; Time: {r[1]:.5f}')
            
        plt.plot(results_mean[:,0], results_mean[:, 1])
        plt.axhline(max_seconds, color='r')
        plt.xlabel("Num Tests")    
        plt.ylabel("Seconds to Complete")
        plt.savefig('results.png')
    
    compute_average_function(results_mean[:, 0], results_mean[:, 1])
    
if __name__ == '__main__':
    # generate_test_file(num_tests=1200)
    # send_to_server(verbose=True)
    # benchmark(iterations=3, max_tests=2000, verbose=True) #sometimes gets stuck if app's terminal isn't opened
    generate_distances(1000)
    