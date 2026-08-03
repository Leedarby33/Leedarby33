#!/usr/bin/env python3
import json, os

# ===== ALL DATA =====

# Weight data (all daily records)
weight_data = [
    {"date":"2026-05-26","weight":89.85,"note":"晚称"},
    {"date":"2026-05-31","weight":87.40,"note":"标准基准"},
    {"date":"2026-06-03","weight":87.9},
    {"date":"2026-06-06","weight":88.45,"note":"不可信"},
    {"date":"2026-06-07","weight":87.8,"bf":31.1,"bmi":28.9,"bmr":1737,"muscle":57.4,"ffm":60.5,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.1,"bone":3.1},
    {"date":"2026-06-09","weight":87.65},
    {"date":"2026-06-14","weight":87.2,"bf":31.1,"bmi":28.8,"bmr":1729,"muscle":57.0,"ffm":60.1,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.1,"bone":3.1},
    {"date":"2026-06-15","weight":88.6},
    {"date":"2026-06-19","weight":87.65},
    {"date":"2026-06-21","weight":87.5,"bf":31.0,"bmi":28.9,"bmr":1733,"muscle":57.3,"ffm":60.4,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.2,"bone":3.1},
    {"date":"2026-06-25","weight":87.1},
    {"date":"2026-06-26","weight":86.75},
    {"date":"2026-06-28","weight":86.5,"bf":30.6,"bmi":28.5,"bmr":1718,"muscle":57.0,"ffm":60.0,"vf":13,"sf":20.4,"protein":12.4,"sm":38.9,"water":49.4,"bone":3.1},
    {"date":"2026-06-29","weight":86.65},
    {"date":"2026-06-30","weight":86.85},
    {"date":"2026-07-01","weight":86.9},
    {"date":"2026-07-02","weight":86.65},
    {"date":"2026-07-03","weight":86.6},
    {"date":"2026-07-04","weight":86.25},
    {"date":"2026-07-05","weight":86.05,"bf":30.4,"bmi":28.4,"bmr":1711,"muscle":56.8,"ffm":59.9,"vf":13,"sf":20.3,"protein":12.4,"sm":39.0,"water":49.6,"bone":3.1},
    {"date":"2026-07-12","weight":83.9,"bf":29.4,"bmi":27.7,"bmr":1679,"muscle":56.3,"ffm":59.2,"vf":12},
    {"date":"2026-07-13","weight":84.1},
    {"date":"2026-07-14","weight":84.15,"note":"非空腹"},
    {"date":"2026-07-15","weight":84.15},
    {"date":"2026-07-16","weight":84.6},
    {"date":"2026-07-17","weight":84.55},
    {"date":"2026-07-18","weight":84.05},
    {"date":"2026-07-19","weight":84.7,"bf":29.6,"bmi":27.9,"bmr":1691,"muscle":56.7,"ffm":59.6,"vf":12,"sf":19.7,"protein":12.7,"sm":39.4,"water":50.1,"bone":3.0},
    {"date":"2026-07-20","weight":86.55,"note":"欺骗餐后"},
    {"date":"2026-07-21","weight":85.8},
    {"date":"2026-07-22","weight":85.05},
    {"date":"2026-07-23","weight":84.85},
    {"date":"2026-07-24","weight":84.5},
    {"date":"2026-07-25","weight":84.65,"note":"补觉后校正"},
    {"date":"2026-07-26","weight":84.45,"bf":29.6,"bmi":27.8,"bmr":1687,"muscle":56.5,"ffm":59.5,"vf":12,"sf":19.7,"protein":12.7,"sm":39.4,"water":50.1,"bone":3.0},
    {"date":"2026-07-27","weight":85.35},
    {"date":"2026-07-28","weight":84.7},
    {"date":"2026-07-29","weight":84.05},
    {"date":"2026-07-30","weight":84.75},
    {"date":"2026-07-31","weight":84.6},
    {"date":"2026-08-01","weight":84.1},
    {"date":"2026-08-02","weight":83.4,"bf":29.2,"bmi":27.5,"bmr":1672,"muscle":56.1,"ffm":59.0,"vf":12,"sf":19.5,"protein":12.7,"sm":39.6,"water":50.4,"bone":3.0},
]

# Body measurements
dimension_data = [
    {"date":"2026-06-07","waist":101.5,"hip":101.5,"chest":108.5,"thigh":62.5,"armFlex":37.5,"armRelax":31.5,"note":"晚饭后,腰围虚高"},
    {"date":"2026-06-21","waist":98.5,"hip":101.5,"chest":108.5,"thigh":48.5,"armFlex":34.5,"armRelax":29.5,"note":"空腹晨测,大腿新标准"},
    {"date":"2026-07-26","waist":94.5,"hip":102.5,"chest":104.5,"thigh":50.5,"armFlex":35.5,"armRelax":31.5,"note":"空腹晨测"},
]

# Daily diet data (5/31 - 8/2)
diet_data = [
    {"date":"2026-06-01","meals":{"breakfast":"4荷包蛋+酱牛肉+燕麦米40g+希腊酸奶+美式","lunch":"外卖(估算)","dinner":"彩椒炒牛腱+凉拌毛豆+蒜蓉菠菜+秋木耳+燕麦饭"},"total":{"cal":1800,"protein":148,"satFat":16,"fructose":5,"carbs":35}},
    {"date":"2026-06-02","meals":{"breakfast":"4荷包蛋+拿铁(全脂奶)+美式","lunch":"沙县去皮鸡腿饭","dinner":"水煮牛腱200g+凉拌菠菜+彩椒+黑木耳+毛豆+海参+米饭0"},"total":{"cal":1321,"protein":139,"satFat":8,"fructose":4,"carbs":30}},
    {"date":"2026-06-03","meals":{"breakfast":"水煮牛肉200g+4荷包蛋+拿铁","lunch":"麻辣烫(肥牛+乌鸡+鸭血+菠菜+木耳+香菇+金针菇+鹌鹑蛋)","dinner":"黑虎虾120g+尖椒牛排100g+蒜苗炒蛋+香菇油麦菜+毛豆+彩椒蘑菇+长豇豆+香蕉1根"},"total":{"cal":1570,"protein":179,"satFat":22,"fructose":6,"carbs":40}},
    {"date":"2026-06-04","meals":{"breakfast":"4荷包蛋+150g牛肉+拿铁","lunch":"Subway鸡肉三明治6寸全麦","dinner":"西兰花+50g牛肉+番茄炖排骨+菌菇+咖喱排骨土豆+彩椒"},"total":{"cal":1602,"protein":136,"satFat":19,"fructose":5,"carbs":80}},
    {"date":"2026-06-05","meals":{"breakfast":"Subway牛肉三明治","lunch":"麻辣烫(牛肉+鸡肉+鹌鹑蛋+菠菜+木耳+海带+鸭血+豆腐)","dinner":"彩椒洋葱炒鸡肉+凉拌卤牛肉+水煮毛豆+半碗白米饭"},"total":{"cal":1380,"protein":120,"satFat":10,"fructose":3,"carbs":70}},
    {"date":"2026-06-06","meals":{"breakfast":"2根香蕉+150g牛肉+4荷包蛋+拿铁","dinner":"窑鸡去皮肉300g+酱牛肉150g+清炒四季豆80g"},"total":{"cal":1690,"protein":193,"satFat":22,"fructose":12,"carbs":30}},
    {"date":"2026-06-07","meals":{"breakfast":"牛排150g+4蛋+拿铁","lunch":"辛香汇钵钵鸡大份+辣味酸菜小土豆+米饭+自烫菠菜250g"},"total":{"cal":1550,"protein":125,"satFat":20,"fructose":5,"carbs":80}},
    {"date":"2026-06-08","meals":{"breakfast":"4荷包蛋+150g牛肉+拿铁","lunch":"金枪鱼滑蛋轻蔬碗","dinner":"虾+毛豆+酸奶+香蕉"},"total":{"cal":1450,"protein":130,"satFat":18,"fructose":8,"carbs":60}},
    {"date":"2026-06-09","meals":{"breakfast":"4蛋+拿铁+150g牛肉","lunch":"刘家牛肉饭+拉丝鸡蛋炒番茄","dinner":"卤牛肉+蔬菜+蛋白粉"},"total":{"cal":1500,"protein":155,"satFat":15,"fructose":5,"carbs":55}},
    {"date":"2026-06-10","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"外卖","dinner":"龙虾应酬"},"total":{"cal":1600,"protein":130,"satFat":15,"fructose":5,"carbs":60}},
    {"date":"2026-06-11","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"外卖","dinner":"正常晚餐"},"total":{"cal":1500,"protein":140,"satFat":14,"fructose":5,"carbs":60}},
    {"date":"2026-06-12","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"外卖","dinner":"烧烤"},"total":{"cal":1600,"protein":135,"satFat":18,"fructose":5,"carbs":60}},
    {"date":"2026-06-13","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"外卖","dinner":"蛋白奶昔"},"total":{"cal":1300,"protein":110,"satFat":12,"fructose":5,"carbs":50}},
    {"date":"2026-06-14","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"外卖","dinner":"正常晚餐"},"total":{"cal":1500,"protein":140,"satFat":14,"fructose":5,"carbs":60}},
    {"date":"2026-06-15","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"西芹炒牛肉+清炒莴笋丝+白灼菜心+糙米饭","dinner":"蛋白粉+卤牛肉"},"total":{"cal":1290,"protein":124,"satFat":15,"fructose":3,"carbs":50}},
    {"date":"2026-06-16","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"小炒黄牛肉+西红柿炒蛋+米饭","dinner":"蛋白粉+三文鱼"},"total":{"cal":1380,"protein":161,"satFat":16,"fructose":3,"carbs":45}},
    {"date":"2026-06-17","meals":{"breakfast":"4蛋+拿铁+牛肉","lunch":"口水鸡+虾仁滑蛋+糙米饭","dinner":"蛋白粉+牛肉+蔬菜"},"total":{"cal":1410,"protein":147,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-06-18","meals":{"breakfast":"袁记云饺18个","lunch":"牛肉拌面碗","dinner":"蛋白粉+蔬菜"},"total":{"cal":1532,"protein":126,"satFat":12,"fructose":3,"carbs":80}},
    {"date":"2026-06-19","meals":{"lunch":"白酒应酬","dinner":"白酒4壶+菜"},"total":{"cal":4892,"protein":116,"satFat":20,"fructose":10,"carbs":80}},
    {"date":"2026-06-20","meals":{"breakfast":"皮蛋瘦肉粥","lunch":"虾饺","dinner":"简单晚餐"},"total":{"cal":1359,"protein":143,"satFat":11,"fructose":3,"carbs":50}},
    {"date":"2026-06-21","meals":{"note":"称重日"}, "total":{"cal":0,"protein":0,"satFat":0,"fructose":0,"carbs":0}},
    {"date":"2026-06-22","meals":{"lunch":"外卖"},"total":{"cal":1450,"protein":135,"satFat":13,"fructose":4,"carbs":60}},
    {"date":"2026-06-23","meals":{"lunch":"蒜蓉粉丝虾套餐"},"total":{"cal":1450,"protein":135,"satFat":13,"fructose":4,"carbs":60}},
    {"date":"2026-06-24","meals":{"lunch":"外卖"},"total":{"cal":1450,"protein":135,"satFat":13,"fructose":4,"carbs":60}},
    {"date":"2026-06-25","meals":{"lunch":"外卖"},"total":{"cal":1450,"protein":135,"satFat":13,"fructose":4,"carbs":60}},
    {"date":"2026-06-26","meals":{"lunch":"广东菜心牛肉+苦瓜牛肉+番茄炒蛋+牛骨清汤"},"total":{"cal":1450,"protein":140,"satFat":14,"fructose":4,"carbs":60}},
    {"date":"2026-06-27","meals":{"lunch":"外卖"},"total":{"cal":1450,"protein":135,"satFat":13,"fructose":4,"carbs":60}},
    {"date":"2026-06-28","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":135,"satFat":13,"fructose":4,"carbs":55}},
    {"date":"2026-06-29","meals":{"lunch":"原切菲力鸡胸牛排配蔬果沙拉"},"total":{"cal":1400,"protein":135,"satFat":13,"fructose":4,"carbs":55}},
    {"date":"2026-06-30","meals":{"lunch":"原切眼肉牛排+太阳蛋+土豆泥+时蔬"},"total":{"cal":1400,"protein":135,"satFat":13,"fructose":4,"carbs":55}},
    {"date":"2026-07-01","meals":{"lunch":"嫩煎鸡胸能量碗+卤牛肉120g","dinner":"卤牛肉150g+西红柿炒蛋+香菇+海参+杂粮饭+菠菜"},"total":{"cal":1453,"protein":142,"satFat":10,"fructose":3,"carbs":55}},
    {"date":"2026-07-02","meals":{"breakfast":"卤牛肉100-140g","lunch":"熏牛肉120g+沙拉碗","dinner":"米饭+菠菜+卤牛腱180g+虾150g+菌菇+芹菜+彩椒"},"total":{"cal":1450,"protein":160,"satFat":8,"fructose":3,"carbs":55}},
    {"date":"2026-07-03","meals":{"lunch":"外卖","dinner":"卤牛肉+蔬菜+蛋白粉"},"total":{"cal":1400,"protein":145,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-04","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-05","meals":{"lunch":"双倍鸡胸鲜蔬杂粮饭","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":145,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-06","meals":{"lunch":"双倍鸡胸鲜蔬杂粮饭"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-07","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-08","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-09","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-10","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-11","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-12","meals":{"lunch":"外卖","dinner":"蛋白粉+蔬菜"},"total":{"cal":1400,"protein":140,"satFat":12,"fructose":3,"carbs":55}},
    {"date":"2026-07-13","meals":{"breakfast":"拿铁+蛋白粉3勺","pre":"蛋白粉1勺+精氨酸瓜氨酸12g","dinner":"蛋白粉1勺+盐水卤牛肉200g+西兰花60g"},"total":{"cal":871,"protein":168,"satFat":7,"fructose":14,"carbs":15}},
    {"date":"2026-07-14","meals":{"breakfast":"美式咖啡","lunch":"烤牛肉拌饭+额外牛肉粒+配菜","dinner":"蛋白粉1勺+三文鱼200g","snack":"蛋白粉半勺"},"total":{"cal":1552,"protein":121,"satFat":15,"fructose":8,"carbs":60}},
    {"date":"2026-07-15","meals":{"breakfast":"美式咖啡","lunch":"延边辣牛肉汤+米饭一半+辣白菜","dinner":"三文鱼240g+蛋白粉2勺","snack":"精氨酸瓜氨酸"},"total":{"cal":1603,"protein":114,"satFat":10,"fructose":5,"carbs":55}},
    {"date":"2026-07-16","meals":{"breakfast":"美式咖啡","lunch":"CrazyCat能量碗(牛肉+鸡胸+烤时蔬+低GI谷物饭)","dinner":"盐水卤牛腱子220g+西兰花70g","snack":"蛋白粉3勺"},"total":{"cal":1468,"protein":145,"satFat":10,"fructose":5,"carbs":50}},
    {"date":"2026-07-17","meals":{"breakfast":"美式咖啡2杯+蛋白粉2勺+精氨酸瓜氨酸12g","lunch":"蛋白粉2勺","dinner":"日料刺身拼盘+沙拉+芝士卷×2"},"total":{"cal":1065,"protein":132,"satFat":13,"fructose":8,"carbs":30}},
    {"date":"2026-07-18","meals":{"lunch":"清汤牛肉面+辣椒油+煎蛋+烤羊肉小串×5","snack":"蛋白粉1勺","dinner":"黑椒朗姆厚牛排200g","snack2":"蛋白粉1勺"},"total":{"cal":1467,"protein":148,"satFat":12,"fructose":3,"carbs":50}},
    {"date":"2026-07-19","meals":{"lunch":"手枪炸鸡腿×1+琵琶腿×2+鸡柳×1(欺骗餐)","snack":"蛋白粉2勺","dinner":"馄饨20个+必胜客烤肉披萨1/4"},"total":{"cal":2956,"protein":174,"satFat":25,"fructose":5,"carbs":135}},
    {"date":"2026-07-20","meals":{"lunch":"嫩滑蛋羹鸡胸肉鲜蔬杂粮饭+白灼西兰花","dinner":"菠菜+黄瓜+三文鱼100g+蛋白粉1勺+精氨酸瓜氨酸"},"total":{"cal":1456,"protein":106,"satFat":13,"fructose":2,"carbs":55}},
    {"date":"2026-07-21","meals":{"lunch":"嫩煎鸡胸肉100g+应季烤时蔬175g+低GI谷物饭150g","dinner":"卤牛肉200g+西红柿+海参+西兰花70g+海带"},"total":{"cal":1270,"protein":135,"satFat":7,"fructose":8,"carbs":45}},
    {"date":"2026-07-22","meals":{"lunch":"香煎鱼柳配杂蔬饭","dinner":"盐水卤牛肉200g+毛豆100g","snack":"蛋白粉2勺"},"total":{"cal":1311,"protein":132,"satFat":14,"fructose":7,"carbs":50}},
    {"date":"2026-07-23","meals":{"lunch":"炙烤黑椒鸡胸肉时蔬糙米谷物饭+金枪鱼","dinner":"盐水卤牛腱子167.5g+毛豆100g+蛋白粉2勺"},"total":{"cal":1436,"protein":151,"satFat":7,"fructose":5,"carbs":50}},
    {"date":"2026-07-24","meals":{"lunch":"双倍鸡胸鲜蔬杂粮饭","dinner":"卤鸭舌35根+西兰花+黄瓜+盐水豆腐+香菇"},"total":{"cal":1240,"protein":109,"satFat":10,"fructose":3,"carbs":45}},
    {"date":"2026-07-25","meals":{"lunch":"猪肉片150g+青椒+洋葱+米饭+紫菜蛋花汤","snack":"蛋白粉2勺+精氨酸瓜氨酸","dinner":"三文鱼刺身106.8g+盐水卤牛腱子88.7g","snack2":"卤鸭舌40根"},"total":{"cal":1358,"protein":154,"satFat":9,"fructose":6,"carbs":45}},
    {"date":"2026-07-26","meals":{"dinner":"牛蛙米线+里脊肉串2串+黑咖啡","snack":"蛋白粉3勺+A2牛奶150ml"},"total":{"cal":1139,"protein":122,"satFat":12,"fructose":0,"carbs":25}},
    {"date":"2026-07-27","meals":{"lunch":"嫩滑蛋羹鸡胸肉杂粮拌饭+白灼西兰花×1.2","dinner":"卤鸭舌30根+炒青菜","snack":"蛋白粉3勺"},"total":{"cal":1316,"protein":135,"satFat":12,"fructose":0,"carbs":40}},
    {"date":"2026-07-28","meals":{"lunch":"鸡胸肉180g+圣女果+黄瓜+玉米+菠菜鸡肉丸+奇亚籽酸奶","snack":"星巴克抹茶拿铁大杯+蛋白粉1勺","dinner":"青菜200g+黄瓜200g+虾仁3个+卤牛肉87g"},"total":{"cal":1164,"protein":155,"satFat":10,"fructose":3,"carbs":45}},
    {"date":"2026-07-29","meals":{"breakfast":"卤牛肉139.5g","lunch":"杭椒牛肉套餐(×1.5)","dinner":"西兰花炒鸡胸肉+豆腐虾仁菌菇汤+杂粮饭半碗","snack":"蛋白粉1勺"},"total":{"cal":1802,"protein":148,"satFat":11,"fructose":0,"carbs":80}},
    {"date":"2026-07-30","meals":{"lunch":"葱香杏鲍菇鸡胸肉+清炒小青菜+豆芽炒韭菜+糙米饭","dinner":"大蒜榨菜拌油麦菜+水煮菠菜+番茄炒蛋","snack":"蛋白粉3勺"},"total":{"cal":1262,"protein":115,"satFat":6,"fructose":0,"carbs":71}},
    {"date":"2026-07-31","meals":{"lunch":"自选寿司套餐10枚","dinner":"青菜150g+菌菇豆腐+卤牛肉184.8g","snack":"蛋白粉2勺"},"total":{"cal":1138,"protein":130,"satFat":8,"fructose":0,"carbs":56}},
    {"date":"2026-08-01","meals":{"lunch":"毛豆+牛肉50g+洋葱+鸡胸肉100g+番茄炒蛋+米饭+红薯+三文鱼100g","dinner":"洋葱炒鸡胸肉+番茄炒蛋+毛豆+红薯+米饭+西红柿","snack":"蛋白粉2勺"},"total":{"cal":1146,"protein":126,"satFat":6,"fructose":0,"carbs":79}},
    {"date":"2026-08-02","meals":{"dinner":"小龙虾虾仁20个+爆炒花蛤20个+面条130g","snack":"蛋白粉3勺"},"total":{"cal":1295,"protein":119,"satFat":9,"fructose":0,"carbs":100}},
]

# Training data (from 5/31 onwards)
training_data = [
    {"date":"2026-05-27","type":"力量+柔韧","duration":29,"dynCal":154,"totalCal":200},
    {"date":"2026-05-29","type":"力量+有氧","duration":55,"dynCal":371,"totalCal":500},
    {"date":"2026-06-02","type":"有氧日","duration":24,"dynCal":60,"totalCal":78},
    {"date":"2026-06-04","type":"力量日","duration":45,"dynCal":280,"totalCal":400},
    {"date":"2026-06-09","type":"拉力+有氧","duration":50,"dynCal":300,"totalCal":420},
    {"date":"2026-06-10","type":"下肢日","duration":45,"dynCal":280,"totalCal":400},
    {"date":"2026-06-11","type":"上肢推日","duration":40,"dynCal":250,"totalCal":350},
    {"date":"2026-06-15","type":"推力日","duration":50,"dynCal":326,"totalCal":450},
    {"date":"2026-06-16","type":"拉力+有氧","duration":45,"dynCal":288,"totalCal":400},
    {"date":"2026-06-17","type":"下肢+核心","duration":55,"dynCal":461,"totalCal":600},
    {"date":"2026-06-20","type":"有氧+柔韧","duration":30,"dynCal":407,"totalCal":500},
    {"date":"2026-07-01","type":"下肢+核心","duration":74,"dynCal":538,"totalCal":676},
    {"date":"2026-07-02","type":"肩臂专项","duration":60,"dynCal":350,"totalCal":480},
    {"date":"2026-07-03","type":"推力日","duration":55,"dynCal":320,"totalCal":440},
    {"date":"2026-07-04","type":"拉力日","duration":60,"dynCal":380,"totalCal":510},
    {"date":"2026-07-05","type":"下肢+核心","duration":55,"dynCal":350,"totalCal":470},
    {"date":"2026-07-06","type":"推力日","duration":55,"dynCal":330,"totalCal":450},
    {"date":"2026-07-07","type":"拉力日","duration":60,"dynCal":380,"totalCal":510},
    {"date":"2026-07-09","type":"下肢","duration":60,"dynCal":400,"totalCal":540},
    {"date":"2026-07-13","type":"推力日","duration":114,"dynCal":815,"totalCal":1022},
    {"date":"2026-07-14","type":"拉力日","duration":99,"dynCal":723,"totalCal":904},
    {"date":"2026-07-15","type":"下肢+核心","duration":76,"dynCal":473,"totalCal":611},
    {"date":"2026-07-16","type":"肩臂专项","duration":83,"dynCal":538,"totalCal":689},
    {"date":"2026-07-17","type":"全身整合","duration":95,"dynCal":722,"totalCal":903},
    {"date":"2026-07-20","type":"推力日","duration":57,"dynCal":358,"totalCal":462},
    {"date":"2026-07-21","type":"拉力日","duration":90,"dynCal":683,"totalCal":867},
    {"date":"2026-07-22","type":"下肢+肩胛","duration":78,"dynCal":527,"totalCal":669},
    {"date":"2026-07-23","type":"肩臂+核心","duration":80,"dynCal":447,"totalCal":594},
    {"date":"2026-07-25","type":"有氧整合+核心","duration":82,"dynCal":662,"totalCal":811},
    {"date":"2026-07-27","type":"推力日","duration":94,"dynCal":649,"totalCal":820},
    {"date":"2026-07-28","type":"拉力日","duration":98,"dynCal":880,"totalCal":1059},
    {"date":"2026-07-30","type":"拉力日","duration":87,"dynCal":561,"totalCal":719},
    {"date":"2026-08-01","type":"下肢+肩胛+HIIT","duration":128,"dynCal":1051,"totalCal":1285},
    {"date":"2026-08-02","type":"Zone2有氧","duration":70,"dynCal":350,"totalCal":450},
]

# Expense data (health-related only: supplements, equipment, guards)
expense_data = [
    {"date":"2026-06-14","item":"MyProtein分离乳清蛋白粉1kg","amount":379.03,"category":"补剂"},
    {"date":"2026-06-17","item":"Now Foods ADAM男士多维90粒×2","amount":456.80,"category":"补剂"},
    {"date":"2026-06-17","item":"多德士TK605哑铃凳","amount":179.55,"category":"训练器材"},
    {"date":"2026-06-17","item":"BlenderBottle摇摇杯800ml","amount":114.69,"category":"训练器材"},
    {"date":"2026-06-17","item":"海力生95%EPA鱼油690粒","amount":912.65,"category":"补剂"},
    {"date":"2026-06-30","item":"普通乳清蛋白粉5kg","amount":1088,"category":"补剂"},
    {"date":"2026-07-05","item":"小米Clip耳夹式耳机","amount":799,"category":"训练器材"},
    {"date":"2026-07-09","item":"哈他天然橡胶瑜伽垫5mm","amount":209,"category":"训练器材"},
    {"date":"2026-07-13","item":"惯爱他达拉非5mg×3盒","amount":251,"category":"补剂"},
    {"date":"2026-07-13","item":"Nutricost KSM-66 600mg×2盒","amount":286.94,"category":"补剂"},
    {"date":"2026-07-23","item":"鸭舌头(周黑鸭)","amount":280,"category":"补剂"},
    {"date":"2026-07-26","item":"剪头发","amount":150,"category":"其他"},
]

# Weekly review data
weekly_reviews = {
    "W29 (7/20-7/26)": {
        "period": "7/20-7/26",
        "weightStart": 84.70, "weightEnd": 84.45, "weightChange": -0.25,
        "bfStart": 29.6, "bfEnd": 29.6,
        "trainingDays": 5, "trainingHours": 6.6,
        "avgCal": 1365, "avgProtein": 139,
        "summary": "正常减脂方案重启第一周。欺骗餐后水钠潴留从86.55回落至84.45，7天降2.10kg。日均摄入1365kcal精准贴合目标。训练执行5/6天。"
    },
    "W31 (7/27-8/2)": {
        "period": "7/27-8/2",
        "weightStart": 85.35, "weightEnd": 83.4, "weightChange": -1.95,
        "bfStart": 29.6, "bfEnd": 29.2,
        "trainingDays": 4, "trainingHours": 6.8,
        "avgCal": 1305, "avgProtein": 135,
        "summary": "V7首周执行。体脂率开始下降0.4%。周减重1.95kg。训练执行率80%。总动态消耗3141kcal。"
    }
}

# Monthly summary data
monthly_reviews = {
    "6月": {
        "trainingDays": 12, "totalHours": 10.5,
        "weightStart": 87.4, "weightEnd": 87.5,
        "avgCal": 1550, "dietCompliance": 0.7,
        "summary": "第一个月试验期。重在建立习惯和校准基线。体重从87.4→87.5基本持平。训练频率43%。6/19白酒事件抵消一周缺口。"
    },
    "7月": {
        "trainingDays": 22, "totalHours": 28.5,
        "weightStart": 86.9, "weightEnd": 83.4,
        "avgCal": 1380, "dietCompliance": 0.85,
        "summary": "正式执行期。猛冲期(7/13-7/20)+降档恢复期+正常减脂。体重从86.9→83.4降3.5kg。训练频率71%。体脂从30.4%→29.2%。"
    }
}

# Current training plan (action cards summary for Tab 1)
action_cards = {
    "周一": {
        "name": "推力量 + HIIT",
        "duration": "~67min",
        "warmup": "快速小碎步→臀桥→猫牛式→弓步压腿+同侧转体→站立腘绳肌拉伸→手臂画圈→站姿提膝触肘→快速深蹲起立+踮脚尖",
        "main": [
            {"name":"哑铃卧推","sets":"4组×10-12次","weight":"7.5-10kg/手","tip":"肩胛骨全程后缩下沉贴凳，离心3-4秒"},
            {"name":"哑铃肩推","sets":"4组×10-12次","weight":"7.5kg/手","tip":"背部贴紧靠背不后仰"},
            {"name":"标准俯卧撑","sets":"4组×力竭","weight":"自重","tip":"末组可改跪姿，核心收紧夹臀"},
            {"name":"仰卧臂屈伸","sets":"4组×12次","weight":"5kg","tip":"大臂固定不动"},
        ],
        "hiit": "弓步+弯举40s→弓步+转体40s→仰卧蹬车40s→休息60s ×5轮",
        "cooldown": "胸肌门框拉伸+三头肌拉伸+踝关节画圈",
        "notes": "组间休息60-75秒。❌禁止折腕/过度后仰/塌腰/大臂摆动"
    },
    "周二": {
        "name": "拉力量 + HIIT + 肩胛协议",
        "duration": "~87min",
        "warmup": "同周一",
        "main": [
            {"name":"弹力带直臂下压","sets":"4组×12-15次","weight":"弹力带15磅","tip":"站姿，手臂伸直从头顶往下压，顶峰挤压1-2秒"},
            {"name":"单臂哑铃划船","sets":"4组×12-15次","weight":"12.5kg/手","tip":"离心5-6秒，组间60秒"},
            {"name":"面拉","sets":"4组×15次","weight":"弹力带10磅","tip":"对准面部，顶峰挤压1-2秒"},
            {"name":"哑铃弯举","sets":"4组×12次","weight":"5-7.5kg/手","tip":"坐姿靠凳"},
        ],
        "hiit": "深蹲+肩上推40s→快速俯卧撑40s→哑铃摇摆40s→休息60s ×5轮",
        "cooldown": "背阔肌侧向幼犬式+直臂二头拉伸+跨胸后束拉伸+踝关节画圈",
        "notes": "含肩胛协议完整版20min。含肩袖激活。"
    },
    "周三": {
        "name": "休息日",
        "duration": "—",
        "warmup": "—",
        "main": [],
        "hiit": "—",
        "cooldown": "—",
        "notes": "完全休息。如需补课，补周一/周二缺席的力量模块。"
    },
    "周四": {
        "name": "拉力量 + HIIT",
        "duration": "~57min",
        "warmup": "同周一",
        "main": [
            {"name":"弹力带直臂下压","sets":"4组×12-15次","weight":"弹力带15磅","tip":"站姿，顶峰挤压1-2秒"},
            {"name":"单臂哑铃划船","sets":"4组×12-15次","weight":"12.5kg/手","tip":"离心5-6秒"},
            {"name":"面拉","sets":"4组×15次","weight":"弹力带10磅","tip":"对准面部，顶峰挤压"},
            {"name":"哑铃弯举","sets":"4组×12次","weight":"5-7.5kg/手","tip":"坐姿靠凳"},
        ],
        "hiit": "深蹲+肩上推40s→快速俯卧撑40s→哑铃摇摆40s→休息60s ×5轮",
        "cooldown": "背阔肌拉伸+直臂二头拉伸+跨胸后束拉伸+踝关节画圈",
        "notes": "精力等级：低（最疲惫日）"
    },
    "周五": {
        "name": "推力量 + HIIT + 肩胛协议",
        "duration": "~87min",
        "warmup": "同周一",
        "main": [
            {"name":"哑铃卧推","sets":"4组×10-12次","weight":"7.5-10kg/手","tip":"肩胛骨全程后缩下沉贴凳"},
            {"name":"哑铃肩推","sets":"4组×10-12次","weight":"7.5kg/手","tip":"背部贴紧靠背不后仰"},
            {"name":"标准俯卧撑","sets":"4组×力竭","weight":"自重","tip":"末组可改跪姿"},
            {"name":"仰卧臂屈伸","sets":"4组×12次","weight":"5kg","tip":"大臂固定不动"},
        ],
        "hiit": "弓步+弯举40s→弓步+转体40s→仰卧蹬车40s→休息60s ×5轮",
        "cooldown": "胸肌门框拉伸+三头肌拉伸+踝关节画圈",
        "notes": "含肩胛协议完整版20min。"
    },
    "周六": {
        "name": "下肢 + 肩胛协议 + HIIT",
        "duration": "~90min",
        "warmup": "同周一",
        "main": [
            {"name":"高脚杯深蹲","sets":"4组×12次","weight":"10kg哑铃","tip":"膝盖追脚尖"},
            {"name":"保加利亚分腿蹲","sets":"4组×10次/侧","weight":"5kg/手","tip":"先做右腿"},
            {"name":"单腿臀桥","sets":"4组×12次/侧","weight":"自重","tip":"顶峰挤压1秒，骨盆不旋转"},
        ],
        "core": [
            {"name":"死虫式","sets":"3组×每侧10次","tip":"腰贴地面"},
            {"name":"鸟狗式","sets":"3组×每侧8次","tip":"顶端停2秒"},
            {"name":"空心体保持","sets":"2组×30-45秒","tip":"下背压实"},
        ],
        "hiit": "快速俯卧撑40s→登山者40s→平板支撑起落40s→休息60s ×7轮",
        "cooldown": "股四头肌拉伸+腘绳肌拉伸+髋屈肌拉伸+踝关节画圈",
        "notes": "最重训练日。含核心训练10min+肩胛协议20min。"
    },
    "周日": {
        "name": "休息日",
        "duration": "—",
        "warmup": "—",
        "main": [],
        "hiit": "—",
        "cooldown": "—",
        "notes": "完全休息。饮食提示：休息日碳水≤50g。"
    }
}

# Supplements list
supplements = [
    "ADAM多维 2粒",
    "D3 2000IU",
    "K2 100mcg",
    "鱼油(海力生+Blackmores) 4粒",
    "Move Free 2片",
    "他达拉非 5mg",
    "氨糖钙片 2片",
    "精氨酸瓜氨酸 12g",
    "肌酸 5g",
    "CoQ10",
    "KSM-66 600mg",
    "甘氨酸镁 2粒(睡前)",
]

print("Data preparation complete. Generating HTML...")
print(f"Weight records: {len(weight_data)}")
print(f"Diet records: {len(diet_data)}")
print(f"Training records: {len(training_data)}")
print(f"Expense records: {len(expense_data)}")
