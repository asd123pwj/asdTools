from base_model import BaseModel
import os
import json


class ForTianqi(BaseModel):
    r"""


    """
    def __init__(self):
        super(ForTianqi, self).__init__()
        pass

    def run(self):
        period_path = "data/Tianqi/period.txt"
        weather_path = "data/Tianqi/weather.txt"
        period_path = "/media/l/b/wjpan/0_mmcls/mmclassification/log/t31/pred.txt"
        weather_path = "/media/l/b/wjpan/0_mmcls/mmclassification/log/t32/pred.txt"
        period_id = ["Morning", "Afternoon", "Dawn", "Dusk"]
        weather_id = ["Cloudy", "Sunny", "Rainy"]
        info = {}
        with open(period_path, 'r') as f:
            content_period = f.readlines()
            for content in content_period:
                content = content.split()
                period = period_id[int(content[1])]
                info[content[0]] = [period]
        
        with open(weather_path, 'r') as f:
            content_weather = f.readlines()
            for content in content_weather:
                content = content.split()
                weather = weather_id[int(content[1])]
                info[content[0]].append(weather)

        res = {"annotations": []}
        for k, v in info.items():
            infer_res = {
                "filename": k.replace(r"/", "\\"),
                "period": v[0],
                "weather": v[1]
            }
            res["annotations"].append(infer_res)

        self.log2file(res, "infer.json", show=True)
        self.log("done")


if __name__ == "__main__":
    ForTianqi().run()