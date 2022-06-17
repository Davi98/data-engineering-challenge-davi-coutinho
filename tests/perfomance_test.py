import requests
from src.utils.log import log
import queue
import threading
import sys
import time

body = [{
    "region": "Rio",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2018-05-28 09:03:40",
    "datasource": "funny_car"
  }]

queue_results = queue.Queue()
start_time = 0
event_time_up = threading.Event()

def stats():
    # request per second
    rps_mean = 0
    total_tested_requests = 0
    total_pass_requests = 0    
    # time per request
    tpr_min = 999
    tpr_mean = 0
    tpr_max = 0
    sum_response_time = 0
    # failures
    total_fail_requests = 0      
    total_exception_requests = 0  

    global start_time
    end_time = time.time()
    # get the approximate queue size
    qsize = queue_results.qsize()
    loop = 0
    for i in range(qsize):
        try:
            result=queue_results.get_nowait()
            loop +=1
        except :
            break
        # calc stats
        if result[1] == 'exception':
            total_exception_requests += 1
        elif result[1] == 'fail':
            total_fail_requests += 1
        elif result[1] == 'pass':
            total_pass_requests += 1
            sum_response_time += result[2]
            # update min and max time per request
            if result[2] < tpr_min:
                tpr_min = result[2]
            if result[2] > tpr_max:
                tpr_max = result[2]
        
    total_tested_requests += loop   
    # time per requests - mean (avg)
    if total_pass_requests != 0:
        tpr_mean = sum_response_time / total_pass_requests
    
    # requests per second - mean
    if start_time == 0:
        print('stats: start_time is not set, skipping rps stats.')
    else:
        tested_time = end_time - start_time
        rps_mean = total_pass_requests / tested_time
        
    print_stats(total_tested_requests, total_pass_requests, total_fail_requests, total_exception_requests,rps_mean,tpr_mean,tpr_min,tpr_max)


def print_stats(total_tested_requests, total_pass_requests, total_fail_requests, total_exception_requests,rps_mean,tpr_mean,tpr_min,tpr_max):
    print('\n-----------------Test Statistics---------------')
    print(time.asctime())
    print(f'Total requests: {total_tested_requests}, pass: {total_pass_requests}, fail: {total_fail_requests}, exception: {total_exception_requests}')
    if total_pass_requests > 0:
        print('For pass requests:') 
        print(f'Request per Second - mean: {rps_mean:.2f}')
        print(f'Time per Request   - mean: {tpr_mean:.6f}, min: {tpr_min:.6f}, max: {tpr_max:.6f}')
              
    


def test_mock_service():
    url = 'http://192.168.0.42:8080/insert'    
    resp = requests.post(url,json=body)
    if resp.status_code != 200:
        log().error(f"Test failed with response status code {resp.status_code}")
        return 'fail', resp.elapsed.total_seconds()
    else:
        log().info('Test passed.')
        return 'pass', resp.elapsed.total_seconds()
    

def loop_test(loop_wait=0, loop_times=sys.maxsize):
    looped_times = 0        
    while (looped_times < loop_times 
        and not event_time_up.is_set()):          
        test_result, elapsed_time = test_mock_service()           
        queue_results.put(['test_mock_service', test_result, elapsed_time])
        looped_times += 1
        time.sleep(loop_wait)   
                          
def set_event_time_up():
    if not event_time_up.is_set():
        event_time_up.set()

if __name__ == '__main__':
    ### Test Settings ###
    concurrent_users = 20
    loop_times = 1000
    test_time = 5
    
    workers = []
    start_time = time.time()
    log().info('Tests started at %s.' % start_time )
    
    # start concurrent user threads
    for i in range(concurrent_users):
        thread = threading.Thread(target=loop_test, kwargs={'loop_times': loop_times}, daemon=True)         
        thread.start()
        workers.append(thread)
    
    timer = threading.Timer(test_time, set_event_time_up)
    timer.start()

    # Block until all threads finish.
    for w in workers:
        w.join()       
    
    if not event_time_up.is_set():
        timer.cancel()
        
    end_time = time.time()
    stats()
    print("\n")
    log().info('Tests ended at %s.' % end_time )
    log().info('Total test time: %s seconds.' %  (end_time - start_time) )