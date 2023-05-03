from base_model import BaseModel
import pynvml
import time
import random
import os
import json


class AutoRunAvailableGPU(BaseModel):
    def __init__(self, mode="root"):
        # pip install nvidia-ml-py
        super().__init__(mode=mode)
        self.gpu_log = 'gpu_info.json'
        self.gpu_info = {
            '0': '0',
            '1': '0',
            '2': '0',
            '3': '0',
            '4': '0',
            '5': '0',
            '6': '0',
            '7': '0',
        }
        if not os.path.exists(os.path.join(self.log_dir, self.gpu_log)):
            self.log2file(self.gpu_info, self.gpu_log)
        self.allow_time_thres = 60 * 3
        pynvml.nvmlInit()
        pass

    def get_gpu_free(self, gpu_id):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)
        gpu_memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        free = gpu_memory_info.free
        return free
    
    def list2str(self, var):
        result = ",".join([str(elem) for elem in var])
        return result

    def parse_gpu_info(self, gpus=[4, 5, 6, 7], mode='r'):
        gpu_available = []
        with open(os.path.join(self.log_dir, self.gpu_log), mode='r') as f:
            self.gpu_info = json.load(f)
            
        if mode == 'r':
            # read and find gpus available now (> 1min)
            for gpu in gpus:
                time_now = int(time.time())
                time_gpu = int(self.gpu_info[str(gpu)])
                if time_now - time_gpu > self.allow_time_thres:
                    gpu_available.append(gpu)
            return gpu_available
        elif mode == 'w':
            for gpu in gpus:
                time_now = int(time.time())
                self.gpu_info[str(gpu)] = time_now
            self.log2file(self.gpu_info, self.gpu_log)

    def run(self, gpus=[0], need=1, delay=10, thres='20G', allow_times=3, type='int', delay_times_thres=5, info=""):
        gpu_allow = [0] * len(gpus)
        delay_times = 0
        while True:
            self.log(f"Search {need} gpus in {gpus}, delay={delay}s, thres={self.unit_conversion(thres, output_unit='G')}G.")
            if delay_times < delay_times_thres:
                delay_times += 1
            else:
                delay_times = 0
                wait_time = round(random.uniform(1, delay_times_thres), 2)
                self.log(f"Search too many times, wait {wait_time} min. Info: {info}")
                time.sleep(wait_time * 60)

            for i, gpu in enumerate(gpus):
                free = self.get_gpu_free(gpu)
                mem_thres = self.unit_conversion(thres, 'B')

                # cycle allow_times to check gpu is available
                if free >= mem_thres:
                    gpu_allow[i] += 1
                else:
                    gpu_allow[i] = 0

            # check the number of available gpus 
            num_available = 0
            for allow in gpu_allow:
                if allow >= allow_times:
                    num_available += 1

            # get available gpus id now
            if num_available >= need:
                gpus_available = []
                for i, allow in enumerate(gpu_allow):
                    if allow >= allow_times:
                        gpus_available.append(gpus[i])
                    # if len(gpus_available) == need:
                    #     break
                # check available gpus id 
                gpu_info = self.parse_gpu_info(gpus_available, mode='r')
                if len(gpu_info) >= need:
                    gpu_info = gpu_info[:need]
                    self.parse_gpu_info(gpu_info, mode='w')

                    pynvml.nvmlShutdown()
                    if type == 'str':
                        gpu_info = self.list2str(gpu_info)
                    elif type == 'int':
                        # for 1 gpu
                        gpu_info = gpu_info[0]
                
                    self.log(gpu_info)
                    return gpu_info

            # time for waiting
            time.sleep(delay)



if __name__ == "__main__":
    import sys
    sys.path.append("/media/l/b/wjpan/202207_asdtools/asdTools/")
    from auto_run_available_gpu import AutoRunAvailableGPU 
    # print(AutoRunAvailableGPU().run(gpus=[5,6,7], need=2, thres='15G'))
    # # output: [5, 6]
    # print(AutoRunAvailableGPU().run(gpus=[0,1,2,3,4], need=1, thres='9G'))
    # # output: [0]
    # print(AutoRunAvailableGPU().run(gpus=[5,6,7], need=2, thres='22G', type=str))
    # output: '5,6'
    
    print(AutoRunAvailableGPU().run(gpus=[7,6,5,4,3,2,1,0], delay=1, need=2, thres='22G', type='str'))