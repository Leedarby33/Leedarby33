#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os

# ===== DATA =====
weight_data = [
    {"date":"2026-05-26","weight":89.85},{"date":"2026-05-31","weight":87.40},
    {"date":"2026-06-03","weight":87.9},{"date":"2026-06-06","weight":88.45},
    {"date":"2026-06-07","weight":87.8,"bf":31.1,"bmi":28.9,"bmr":1737,"muscle":57.4,"ffm":60.5,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.1,"bone":3.1},
    {"date":"2026-06-09","weight":87.65},
    {"date":"2026-06-14","weight":87.2,"bf":31.1,"bmi":28.8,"bmr":1729,"muscle":57.0,"ffm":60.1,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.1,"bone":3.1},
    {"date":"2026-06-15","weight":88.6},{"date":"2026-06-19","weight":87.65},
    {"date":"2026-06-21","weight":87.5,"bf":31.0,"bmi":28.9,"bmr":1733,"muscle":57.3,"ffm":60.4,"vf":13,"sf":20.7,"protein":12.3,"sm":38.6,"water":49.2,"bone":3.1},
    {"date":"2026-06-25","weight":87.1},{"date":"2026-06-26","weight":86.75},
    {"date":"2026-06-28","weight":86.5,"bf":30.6,"bmi":28.5,"bmr":1718,"muscle":57.0,"ffm":60.0,"vf":13,"sf":20.4,"protein":12.4,"sm":38.9,"water":49.4,"bone":3.1},
    {"date":"2026-06-29","weight":86.65},{"date":"2026-06-30","weight":86.85},
    {"date":"2026-07-01","weight":86.9},{"date":"2026-07-02","weight":86.65},
    {"date":"2026-07-03","weight":86.6},{"date":"2026-07-04","weight":86.25},
    {"date":"2026-07-05","weight":86.05,"bf":30.4,"bmi":28.4,"bmr":1711,"muscle":56.8,"ffm":59.9,"vf":13,"sf":20.3,"protein":12.4,"sm":39.0,"water":49.6,"bone":3.1},
    {"date":"2026-07-12","weight":83.9,"bf":29.4,"bmi":27.7,"bmr":1679,"muscle":56.3,"ffm":59.2,"vf":12},
    {"date":"2026-07-13","weight":84.1},{"date":"2026-07-14","weight":84.15},
    {"date":"2026-07-15","weight":84.15},{"date":"2026-07-16","weight":84.6},
    {"date":"2026-07-17","weight":84.55},{"date":"2026-07-18","weight":84.05},
    {"date":"2026-07-19","weight":84.7,"bf":29.6,"bmi":27.9,"bmr":1691,"muscle":56.7,"ffm":59.6,"vf":12,"sf":19.7,"protein":12.7,"sm":39.4,"water":50.1,"bone":3.0},
    {"date":"2026-07-20","weight":86.55},{"date":"2026-07-21","weight":85.8},
    {"date":"2026-07-22","weight":85.05},{"date":"2026-07-23","weight":84.85},
    {"date":"2026-07-24","weight":84.5},{"date":"2026-07-25","weight":84.65},
    {"date":"2026-07-26","weight":84.45,"bf":29.6,"bmi":27.8,"bmr":1687,"muscle":56.5,"ffm":59.5,"vf":12,"sf":19.7,"protein":12.7,"sm":39.4,"water":50.1,"bone":3.0},
    {"date":"2026-07-27","weight":85.35},{"date":"2026-07-28","weight":84.7},
    {"date":"2026-07-29","weight":84.05},{"date":"2026-07-30","weight":84.75},
    {"date":"2026-07-31","weight":84.6},{"date":"2026-08-01","weight":84.1},
    {"date":"2026-08-02","weight":83.4,"bf":29.2,"bmi":27.5,"bmr":1672,"muscle":56.1,"ffm":59.0,"vf":12,"sf":19.5,"protein":12.7,"sm":39.6,"water":50.4,"bone":3.0},
]

dimension_data = [
    {"date":"2026-06-07","waist":101.5,"hip":101.5,"chest":108.5,"thigh":62.5,"armFlex":37.5,"armRelax":31.5,"note":"晚饭后,腰围虚高"},
    {"date":"2026-06-21","waist":98.5,"hip":101.5,"chest":108.5,"thigh":48.5,"armFlex":34.5,"armRelax":29.5,"note":"空腹晨测"},
    {"date":"2026-07-26","waist":94.5,"hip":102.5,"chest":104.5,"thigh":50.5,"armFlex":35.5,"armRelax":31.5,"note":"空腹晨测"},
]

diet_data = [
    {"date":"2026-06-01","m":{"b":"4蛋+酱牛肉+燕麦+酸奶+美式","l":"外卖","d":"彩椒牛腱+毛豆+菠菜+木耳+燕麦饭"},"t":{"cal":1800,"p":148,"sf":16,"fr":5,"c":35}},
    {"date":"2026-06-02","m":{"b":"4蛋+拿铁+美式","l":"沙县去皮鸡腿饭","d":"牛腱200g+菠菜+彩椒+木耳+毛豆+海参"},"t":{"cal":1321,"p":139,"sf":8,"fr":4,"c":30}},
    {"date":"2026-06-03","m":{"b":"牛腱200g+4蛋+拿铁","l":"麻辣烫(肥牛+鸭血+菠菜+木耳+香菇)","d":"虾120g+牛排100g+毛豆+彩椒+香蕉"},"t":{"cal":1570,"p":179,"sf":22,"fr":6,"c":40}},
    {"date":"2026-06-04","m":{"b":"4蛋+150g牛肉+拿铁","l":"Subway鸡肉三明治6寸","d":"西兰花+牛肉+番茄排骨+菌菇+咖喱土豆+彩椒"},"t":{"cal":1602,"p":136,"sf":19,"fr":5,"c":80}},
    {"date":"2026-06-05","m":{"b":"Subway牛肉三明治","l":"麻辣烫(牛鸡鹌鹑蛋+菠菜+木耳+海带+鸭血+豆腐)","d":"彩椒洋葱炒鸡+卤牛肉+毛豆+半碗米饭"},"t":{"cal":1380,"p":120,"sf":10,"fr":3,"c":70}},
    {"date":"2026-06-06","m":{"b":"2香蕉+150g牛肉+4蛋+拿铁","d":"窑鸡300g+酱牛肉150g+四季豆80g"},"t":{"cal":1690,"p":193,"sf":22,"fr":12,"c":30}},
    {"date":"2026-06-07","m":{"b":"牛排150g+4蛋+拿铁","d":"钵钵鸡大份+酸菜土豆+米饭+菠菜250g"},"t":{"cal":1550,"p":125,"sf":20,"fr":5,"c":80}},
    {"date":"2026-06-08","m":{"b":"4蛋+150g牛肉+拿铁","l":"金枪鱼滑蛋轻蔬碗","d":"虾+毛豆+酸奶+香蕉"},"t":{"cal":1450,"p":130,"sf":18,"fr":8,"c":60}},
    {"date":"2026-06-09","m":{"b":"4蛋+拿铁+150g牛肉","l":"刘家牛肉饭+鸡蛋炒番茄","d":"卤牛肉+蔬菜+蛋白粉"},"t":{"cal":1500,"p":155,"sf":15,"fr":5,"c":55}},
    {"date":"2026-06-10","m":{"b":"4蛋+拿铁+牛肉","l":"外卖","d":"龙虾应酬"},"t":{"cal":1600,"p":130,"sf":15,"fr":5,"c":60}},
    {"date":"2026-06-11","m":{"b":"4蛋+拿铁+牛肉","l":"外卖","d":"正常晚餐"},"t":{"cal":1500,"p":140,"sf":14,"fr":5,"c":60}},
    {"date":"2026-06-12","m":{"b":"4蛋+拿铁+牛肉","l":"外卖","d":"烧烤"},"t":{"cal":1600,"p":135,"sf":18,"fr":5,"c":60}},
    {"date":"2026-06-13","m":{"b":"4蛋+拿铁+牛肉","l":"外卖","d":"蛋白奶昔"},"t":{"cal":1300,"p":110,"sf":12,"fr":5,"c":50}},
    {"date":"2026-06-14","m":{"b":"4蛋+拿铁+牛肉","l":"外卖","d":"正常晚餐"},"t":{"cal":1500,"p":140,"sf":14,"fr":5,"c":60}},
    {"date":"2026-06-15","m":{"b":"4蛋+拿铁+牛肉","l":"西芹炒牛肉+莴笋+菜心+糙米","d":"蛋白粉+卤牛肉"},"t":{"cal":1290,"p":124,"sf":15,"fr":3,"c":50}},
    {"date":"2026-06-16","m":{"b":"4蛋+拿铁+牛肉","l":"小炒黄牛肉+西红柿炒蛋+米饭","d":"蛋白粉+三文鱼"},"t":{"cal":1380,"p":161,"sf":16,"fr":3,"c":45}},
    {"date":"2026-06-17","m":{"b":"4蛋+拿铁+牛肉","l":"口水鸡+虾仁滑蛋+糙米","d":"蛋白粉+牛肉+蔬菜"},"t":{"cal":1410,"p":147,"sf":12,"fr":3,"c":55}},
    {"date":"2026-06-18","m":{"b":"袁记云饺18个","l":"牛肉拌面碗","d":"蛋白粉+蔬菜"},"t":{"cal":1532,"p":126,"sf":12,"fr":3,"c":80}},
    {"date":"2026-06-19","m":{"l":"白酒应酬","d":"白酒4壶+菜"},"t":{"cal":4892,"p":116,"sf":20,"fr":10,"c":80}},
    {"date":"2026-06-20","m":{"b":"皮蛋瘦肉粥","l":"虾饺","d":"简单晚餐"},"t":{"cal":1359,"p":143,"sf":11,"fr":3,"c":50}},
    {"date":"2026-06-21","m":{"note":"称重日"},"t":{"cal":0,"p":0,"sf":0,"fr":0,"c":0}},
    {"date":"2026-06-22","m":{"l":"外卖"},"t":{"cal":1450,"p":135,"sf":13,"fr":4,"c":60}},
    {"date":"2026-06-23","m":{"l":"蒜蓉粉丝虾套餐"},"t":{"cal":1450,"p":135,"sf":13,"fr":4,"c":60}},
    {"date":"2026-06-24","m":{"l":"外卖"},"t":{"cal":1450,"p":135,"sf":13,"fr":4,"c":60}},
    {"date":"2026-06-25","m":{"l":"外卖"},"t":{"cal":1450,"p":135,"sf":13,"fr":4,"c":60}},
    {"date":"2026-06-26","m":{"l":"广东菜心牛肉+苦瓜牛肉+番茄炒蛋+牛骨清汤"},"t":{"cal":1450,"p":140,"sf":14,"fr":4,"c":60}},
    {"date":"2026-06-27","m":{"l":"外卖"},"t":{"cal":1450,"p":135,"sf":13,"fr":4,"c":60}},
    {"date":"2026-06-28","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":135,"sf":13,"fr":4,"c":55}},
    {"date":"2026-06-29","m":{"l":"菲力鸡胸牛排沙拉"},"t":{"cal":1400,"p":135,"sf":13,"fr":4,"c":55}},
    {"date":"2026-06-30","m":{"l":"眼肉牛排+太阳蛋+土豆泥+时蔬"},"t":{"cal":1400,"p":135,"sf":13,"fr":4,"c":55}},
    {"date":"2026-07-01","m":{"l":"鸡胸能量碗+卤牛肉120g","d":"卤牛肉150g+西红柿炒蛋+香菇+海参+杂粮饭+菠菜"},"t":{"cal":1453,"p":142,"sf":10,"fr":3,"c":55}},
    {"date":"2026-07-02","m":{"b":"卤牛肉120g","l":"熏牛肉120g+沙拉碗","d":"米饭+菠菜+牛腱180g+虾150g+菌菇+芹菜+彩椒"},"t":{"cal":1450,"p":160,"sf":8,"fr":3,"c":55}},
    {"date":"2026-07-03","m":{"l":"外卖","d":"卤牛肉+蔬菜+蛋白粉"},"t":{"cal":1400,"p":145,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-04","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-05","m":{"l":"双倍鸡胸鲜蔬杂粮饭","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":145,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-06","m":{"l":"双倍鸡胸鲜蔬杂粮饭"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-07","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-08","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-09","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-10","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-11","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-12","m":{"l":"外卖","d":"蛋白粉+蔬菜"},"t":{"cal":1400,"p":140,"sf":12,"fr":3,"c":55}},
    {"date":"2026-07-13","m":{"b":"拿铁+蛋白粉3勺","pre":"蛋白粉1勺+精氨酸瓜氨酸","d":"蛋白粉1勺+卤牛肉200g+西兰花60g"},"t":{"cal":871,"p":168,"sf":7,"fr":14,"c":15}},
    {"date":"2026-07-14","m":{"b":"美式咖啡","l":"烤牛肉拌饭+牛肉粒","d":"蛋白粉1勺+三文鱼200g","s":"蛋白粉半勺"},"t":{"cal":1552,"p":121,"sf":15,"fr":8,"c":60}},
    {"date":"2026-07-15","m":{"b":"美式咖啡","l":"延边辣牛肉汤+米饭一半","d":"三文鱼240g+蛋白粉2勺","s":"精氨酸瓜氨酸"},"t":{"cal":1603,"p":114,"sf":10,"fr":5,"c":55}},
    {"date":"2026-07-16","m":{"b":"美式咖啡","l":"CrazyCat能量碗","d":"卤牛腱子220g+西兰花","s":"蛋白粉3勺"},"t":{"cal":1468,"p":145,"sf":10,"fr":5,"c":50}},
    {"date":"2026-07-17","m":{"b":"美式2杯+蛋白粉2勺+精氨酸瓜氨酸","l":"蛋白粉2勺","d":"日料刺身+沙拉+芝士卷×2"},"t":{"cal":1065,"p":132,"sf":13,"fr":8,"c":30}},
    {"date":"2026-07-18","m":{"l":"牛肉面+辣椒油+煎蛋+羊肉串×5","s":"蛋白粉1勺","d":"牛排200g","s2":"蛋白粉1勺"},"t":{"cal":1467,"p":148,"sf":12,"fr":3,"c":50}},
    {"date":"2026-07-19","m":{"l":"炸鸡腿+琵琶腿×2+鸡柳(欺骗餐)","s":"蛋白粉2勺","d":"馄饨20个+披萨1/4"},"t":{"cal":2956,"p":174,"sf":25,"fr":5,"c":135}},
    {"date":"2026-07-20","m":{"l":"蛋羹鸡胸鲜蔬杂粮饭+西兰花","d":"菠菜+黄瓜+三文鱼100g+蛋白粉+精氨酸瓜氨酸"},"t":{"cal":1456,"p":106,"sf":13,"fr":2,"c":55}},
    {"date":"2026-07-21","m":{"l":"鸡胸肉100g+烤时蔬+低GI饭","d":"卤牛肉200g+西红柿+海参+西兰花+海带"},"t":{"cal":1270,"p":135,"sf":7,"fr":8,"c":45}},
    {"date":"2026-07-22","m":{"l":"香煎鱼柳杂蔬饭","d":"卤牛肉200g+毛豆100g","s":"蛋白粉2勺"},"t":{"cal":1311,"p":132,"sf":14,"fr":7,"c":50}},
    {"date":"2026-07-23","m":{"l":"黑椒鸡胸糙米饭+金枪鱼","d":"卤牛腱167g+毛豆100g+蛋白粉2勺"},"t":{"cal":1436,"p":151,"sf":7,"fr":5,"c":50}},
    {"date":"2026-07-24","m":{"l":"双倍鸡胸鲜蔬杂粮饭","d":"卤鸭舌35根+西兰花+黄瓜+豆腐+香菇"},"t":{"cal":1240,"p":109,"sf":10,"fr":3,"c":45}},
    {"date":"2026-07-25","m":{"l":"猪肉150g+青椒洋葱+米饭+蛋花汤","s":"蛋白粉2勺+精氨酸瓜氨酸","d":"三文鱼107g+卤牛腱89g","s2":"卤鸭舌40根"},"t":{"cal":1358,"p":154,"sf":9,"fr":6,"c":45}},
    {"date":"2026-07-26","m":{"d":"牛蛙米线+里脊串+咖啡","s":"蛋白粉3勺+A2牛奶150ml"},"t":{"cal":1139,"p":122,"sf":12,"fr":0,"c":25}},
    {"date":"2026-07-27","m":{"l":"蛋羹鸡胸杂粮饭+西兰花×1.2","d":"卤鸭舌30根+炒青菜","s":"蛋白粉3勺"},"t":{"cal":1316,"p":135,"sf":12,"fr":0,"c":40}},
    {"date":"2026-07-28","m":{"l":"鸡胸180g+圣女果+黄瓜+玉米+酸奶","s":"抹茶拿铁+蛋白粉1勺","d":"青菜+黄瓜+虾仁+卤牛肉87g"},"t":{"cal":1164,"p":155,"sf":10,"fr":3,"c":45}},
    {"date":"2026-07-29","m":{"b":"卤牛肉140g","l":"杭椒牛肉套餐×1.5","d":"西兰花鸡胸+豆腐虾仁汤+杂粮饭","s":"蛋白粉1勺"},"t":{"cal":1802,"p":148,"sf":11,"fr":0,"c":80}},
    {"date":"2026-07-30","m":{"l":"杏鲍菇鸡胸+青菜+豆芽韭菜+糙米","d":"油麦菜+菠菜+番茄炒蛋","s":"蛋白粉3勺"},"t":{"cal":1262,"p":115,"sf":6,"fr":0,"c":71}},
    {"date":"2026-07-31","m":{"l":"寿司10枚","d":"青菜+菌菇豆腐+卤牛肉185g","s":"蛋白粉2勺"},"t":{"cal":1138,"p":130,"sf":8,"fr":0,"c":56}},
    {"date":"2026-08-01","m":{"l":"毛豆+牛肉50g+鸡胸100g+番茄炒蛋+米饭红薯+三文鱼100g","d":"洋葱鸡胸+番茄炒蛋+毛豆+红薯+米饭","s":"蛋白粉2勺"},"t":{"cal":1146,"p":126,"sf":6,"fr":0,"c":79}},
    {"date":"2026-08-02","m":{"d":"小龙虾20个+花蛤20个+面条130g","s":"蛋白粉3勺"},"t":{"cal":1295,"p":119,"sf":9,"fr":0,"c":100}},
]

training_data = [
    {"date":"2026-05-27","type":"力量+柔韧","dur":29,"dyn":154,"total":200},
    {"date":"2026-05-29","type":"力量+有氧","dur":55,"dyn":371,"total":500},
    {"date":"2026-06-02","type":"有氧日","dur":24,"dyn":60,"total":78},
    {"date":"2026-06-04","type":"力量日","dur":45,"dyn":280,"total":400},
    {"date":"2026-06-09","type":"拉力+有氧","dur":50,"dyn":300,"total":420},
    {"date":"2026-06-10","type":"下肢日","dur":45,"dyn":280,"total":400},
    {"date":"2026-06-11","type":"上肢推日","dur":40,"dyn":250,"total":350},
    {"date":"2026-06-15","type":"推力日","dur":50,"dyn":326,"total":450},
    {"date":"2026-06-16","type":"拉力+有氧","dur":45,"dyn":288,"total":400},
    {"date":"2026-06-17","type":"下肢+核心","dur":55,"dyn":461,"total":600},
    {"date":"2026-06-20","type":"有氧+柔韧","dur":30,"dyn":407,"total":500},
    {"date":"2026-07-01","type":"下肢+核心","dur":74,"dyn":538,"total":676},
    {"date":"2026-07-02","type":"肩臂专项","dur":60,"dyn":350,"total":480},
    {"date":"2026-07-03","type":"推力日","dur":55,"dyn":320,"total":440},
    {"date":"2026-07-04","type":"拉力日","dur":60,"dyn":380,"total":510},
    {"date":"2026-07-05","type":"下肢+核心","dur":55,"dyn":350,"total":470},
    {"date":"2026-07-06","type":"推力日","dur":55,"dyn":330,"total":450},
    {"date":"2026-07-07","type":"拉力日","dur":60,"dyn":380,"total":510},
    {"date":"2026-07-09","type":"下肢","dur":60,"dyn":400,"total":540},
    {"date":"2026-07-13","type":"推力日","dur":114,"dyn":815,"total":1022},
    {"date":"2026-07-14","type":"拉力日","dur":99,"dyn":723,"total":904},
    {"date":"2026-07-15","type":"下肢+核心","dur":76,"dyn":473,"total":611},
    {"date":"2026-07-16","type":"肩臂专项","dur":83,"dyn":538,"total":689},
    {"date":"2026-07-17","type":"全身整合","dur":95,"dyn":722,"total":903},
    {"date":"2026-07-20","type":"推力日","dur":57,"dyn":358,"total":462},
    {"date":"2026-07-21","type":"拉力日","dur":90,"dyn":683,"total":867},
    {"date":"2026-07-22","type":"下肢+肩胛","dur":78,"dyn":527,"total":669},
    {"date":"2026-07-23","type":"肩臂+核心","dur":80,"dyn":447,"total":594},
    {"date":"2026-07-25","type":"有氧整合+核心","dur":82,"dyn":662,"total":811},
    {"date":"2026-07-27","type":"推力日","dur":94,"dyn":649,"total":820},
    {"date":"2026-07-28","type":"拉力日","dur":98,"dyn":880,"total":1059},
    {"date":"2026-07-30","type":"拉力日","dur":87,"dyn":561,"total":719},
    {"date":"2026-08-01","type":"下肢+肩胛+HIIT","dur":128,"dyn":1051,"total":1285},
    {"date":"2026-08-02","type":"Zone2有氧","dur":70,"dyn":350,"total":450},
]

expense_data = [
    {"date":"2026-06-14","item":"MyProtein分离乳清蛋白粉1kg","amt":379.03,"cat":"补剂"},
    {"date":"2026-06-17","item":"ADAM男士多维90粒×2","amt":456.80,"cat":"补剂"},
    {"date":"2026-06-17","item":"多德士TK605哑铃凳","amt":179.55,"cat":"器材"},
    {"date":"2026-06-17","item":"BlenderBottle摇摇杯","amt":114.69,"cat":"器材"},
    {"date":"2026-06-17","item":"海力生EPA鱼油690粒","amt":912.65,"cat":"补剂"},
    {"date":"2026-06-30","item":"普通乳清蛋白粉5kg","amt":1088,"cat":"补剂"},
    {"date":"2026-07-05","item":"小米Clip耳夹耳机","amt":799,"cat":"器材"},
    {"date":"2026-07-09","item":"哈他橡胶瑜伽垫","amt":209,"cat":"器材"},
    {"date":"2026-07-13","item":"他达拉非5mg×3盒","amt":251,"cat":"补剂"},
    {"date":"2026-07-13","item":"KSM-66 600mg×2盒","amt":286.94,"cat":"补剂"},
    {"date":"2026-07-23","item":"鸭舌头周黑鸭","amt":280,"cat":"补剂"},
]

supplements = [
    "ADAM多维 2粒","D3 2000IU","K2 100mcg",
    "鱼油(海力生2+Blackmores2)","Move Free 2片",
    "他达拉非 5mg","氨糖钙片 2片","精氨酸瓜氨酸 12g",
    "肌酸 5g","CoQ10","KSM-66 600mg","甘氨酸镁 2粒(睡前)"
]

# Now generate the HTML
w_json = json.dumps(weight_data, ensure_ascii=False)
d_json = json.dumps(diet_data, ensure_ascii=False)
t_json = json.dumps(training_data, ensure_ascii=False)
e_json = json.dumps(expense_data, ensure_ascii=False)
dim_json = json.dumps(dimension_data, ensure_ascii=False)
sup_json = json.dumps(supplements, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#0f1115">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>健康管理工作台 | 大笔哥</title>
<link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoi5YaF562J566h55CG5bel5L2cIiwic2hvcnRfbmFtZSI6Iui3r+W+hCAiLCJzdGFydF91cmwiOiIuLyIsImRpc3BsYXkiOiJzdGFuZGFsb25lIiwiYmFja2dyb3VuZF9jb2xvciI6IiMwZjExMTUiLCJ0aGVtZV9jb2xvciI6IiMwZjExMTUifQ==">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
html{{font-size:16px;-webkit-text-size-adjust:100%}}
body{{font-family:-apple-system,'SF Pro Text','PingFang SC','Helvetica Neue',sans-serif;background:#0f1115;color:#e0e0e0;line-height:1.5;overflow-x:hidden;-webkit-font-smoothing:antialiased}}
:root{{--bg:#0f1115;--card:#1a1d24;--inset:#12141a;--t1:#e8e8e8;--t2:#8a8a8a;--t3:#555;--blue:#4a9eff;--green:#34c759;--orange:#ff9500;--red:#ff3b30;--purple:#af52de;--teal:#5ac8fa;--bdr:rgba(255,255,255,0.06);--bdr2:rgba(255,255,255,0.15);--r:14px;--rs:10px}}
.container{{max-width:480px;margin:0 auto;padding:0 16px 80px}}
.header{{position:sticky;top:0;z-index:100;background:rgba(15,17,21,0.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);padding:12px 16px;display:flex;align-items:center;justify-content:space-between}}
.header-left{{display:flex;align-items:center;gap:10px}}
.avatar{{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,var(--blue),var(--purple));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;color:#fff}}
.header-title{{font-size:15px;font-weight:600;color:var(--t1)}}
.header-sub{{font-size:11px;color:var(--t2);margin-top:1px}}
.header-date{{font-size:11px;color:var(--t3);text-align:right}}
.tab-bar{{position:sticky;top:60px;z-index:99;background:rgba(15,17,21,0.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);display:flex;gap:0;padding:10px 16px 8px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;border-bottom:1px solid var(--bdr)}}
.tab-bar::-webkit-scrollbar{{display:none}}
.tab-item{{flex-shrink:0;padding:7px 14px;border-radius:20px;font-size:12px;font-weight:500;color:var(--t2);background:transparent;border:1px solid transparent;transition:all 0.2s;white-space:nowrap;cursor:pointer}}
.tab-item.active{{color:var(--t1);background:var(--card);border-color:var(--bdr2)}}
.tab-content{{display:none;padding-top:16px}}
.tab-content.active{{display:block}}
.card{{background:var(--card);border-radius:var(--r);padding:18px;margin-bottom:12px;border:1px solid var(--bdr)}}
.card-title{{font-size:14px;font-weight:600;color:var(--t1);margin-bottom:14px}}
.big-num{{font-size:36px;font-weight:800;color:var(--t1);line-height:1.1}}
.big-num .unit{{font-size:14px;font-weight:400;color:var(--t2)}}
.big-sub{{font-size:12px;color:var(--t2);margin-top:4px}}
.kpi-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.kpi-item{{background:var(--inset);border-radius:var(--rs);padding:14px;text-align:center}}
.kpi-value{{font-size:24px;font-weight:700;color:var(--t1)}}
.kpi-value .unit{{font-size:11px;font-weight:400;color:var(--t2)}}
.kpi-label{{font-size:11px;color:var(--t2);margin-top:4px}}
.progress-bar{{height:8px;background:var(--inset);border-radius:4px;overflow:hidden;margin:8px 0}}
.progress-fill{{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--blue),var(--teal));transition:width 0.6s ease}}
.stage-row{{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--t2)}}
.stage-row .num{{font-size:20px;font-weight:700;color:var(--t1)}}
.check-group{{display:flex;gap:12px;flex-wrap:wrap}}
.check-item{{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--t2)}}
.check-box{{width:22px;height:22px;border-radius:6px;border:2px solid var(--t3);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.2s;font-size:14px}}
.check-box.checked{{background:var(--green);border-color:var(--green);color:#fff}}
.supplement-list{{display:flex;flex-wrap:wrap;gap:8px}}
.sup-tag{{background:var(--inset);border-radius:8px;padding:6px 12px;font-size:11px;color:var(--t2)}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{text-align:left;padding:8px 6px;color:var(--t3);font-weight:500;border-bottom:1px solid var(--bdr);font-size:11px}}
td{{padding:8px 6px;border-bottom:1px solid var(--bdr);color:var(--t2)}}
.chart-svg{{width:100%;height:auto}}
select,input[type="date"]{{background:var(--inset);color:var(--t1);border:1px solid var(--bdr);border-radius:8px;padding:8px 12px;font-size:13px;outline:none}}
select{{width:100%}}
.date-range{{display:flex;gap:8px;align-items:center}}
.date-range input{{flex:1}}
.date-range span{{color:var(--t3);font-size:12px}}
.meal-block{{background:var(--inset);border-radius:var(--rs);padding:12px;margin-bottom:8px}}
.meal-label{{font-size:11px;font-weight:600;color:var(--blue);margin-bottom:6px;text-transform:uppercase}}
.meal-items{{font-size:12px;color:var(--t2);line-height:1.6}}
.meal-macros{{font-size:11px;color:var(--t3);margin-top:4px}}
.action-card{{background:var(--inset);border-radius:var(--rs);padding:14px;margin-bottom:10px}}
.action-name{{font-size:14px;font-weight:600;color:var(--t1);margin-bottom:4px}}
.action-meta{{font-size:11px;color:var(--blue);margin-bottom:8px}}
.action-detail{{font-size:12px;color:var(--t2)}}
.action-tip{{font-size:11px;color:var(--orange);margin-top:4px}}
.hiit-box{{background:rgba(74,158,255,0.1);border-radius:var(--rs);padding:12px;margin-top:10px;border-left:3px solid var(--blue)}}
.warmup-box{{background:rgba(52,199,89,0.08);border-radius:var(--rs);padding:12px;margin-top:10px;border-left:3px solid var(--green)}}
.note-box{{background:rgba(255,149,0,0.08);border-radius:var(--rs);padding:10px;margin-top:8px;font-size:11px;color:var(--orange)}}
.flex-row{{display:flex;gap:8px;flex-wrap:wrap}}
.badge{{display:inline-block;padding:2px 8px;border-radius:6px;font-size:10px;font-weight:600}}
.badge-green{{background:rgba(52,199,89,0.15);color:var(--green)}}
.badge-blue{{background:rgba(74,158,255,0.15);color:var(--blue)}}
.badge-orange{{background:rgba(255,149,0,0.15);color:var(--orange)}}
.badge-red{{background:rgba(255,59,48,0.15);color:var(--red)}}
.review-section{{background:var(--inset);border-radius:var(--rs);padding:14px;margin-bottom:10px}}
.review-title{{font-size:13px;font-weight:600;color:var(--blue);margin-bottom:8px}}
.summary-text{{font-size:12px;color:var(--t2);line-height:1.7}}
svg text{{font-family:-apple-system,'PingFang SC',sans-serif}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<div class="header-left">
<div class="avatar">D</div>
<div><div class="header-title">健康管理工作台</div><div class="header-sub">减脂阶段 · V7计划</div></div>
</div>
<div class="header-date" id="headerDate">2026-08-02</div>
</div>
<div class="tab-bar" id="tabBar">
<div class="tab-item active" data-tab="nav">今日</div>
<div class="tab-item" data-tab="overview">总览</div>
<div class="tab-item" data-tab="training">训练</div>
<div class="tab-item" data-tab="diet">饮食</div>
<div class="tab-item" data-tab="body">体测</div>
<div class="tab-item" data-tab="expense">花费</div>
<div class="tab-item" data-tab="weekly">周复盘</div>
<div class="tab-item" data-tab="monthly">月复盘</div>
</div>

<!-- TAB 1: 今日导航 -->
<div class="tab-content active" id="tab-nav">
<div class="card" style="background:linear-gradient(135deg,#1a2332,#1a1d24)">
<div style="font-size:12px;color:var(--blue);margin-bottom:8px">📊 今日剩余额度</div>
<div class="big-num" id="remainCal">—<span class="unit"> kcal</span></div>
<div class="big-sub" id="remainProtein">—</div>
</div>
<div class="card">
<div class="card-title">🏋️ 凯格尔打卡</div>
<div class="check-group" id="kegelChecks">
<div class="check-item"><div class="check-box" onclick="toggleCheck(this)" data-k="am">✓</div><span>上午</span></div>
<div class="check-item"><div class="check-box" onclick="toggleCheck(this)" data-k="pm">✓</div><span>下午</span></div>
<div class="check-item"><div class="check-box" onclick="toggleCheck(this)" data-k="bed">✓</div><span>睡前(4-7-8)</span></div>
</div>
</div>
<div class="card">
<div class="card-title">🚶 步数</div>
<div style="display:flex;align-items:center;gap:12px">
<div class="big-num" style="font-size:28px" id="stepsDisplay">—</div>
<input type="number" id="stepsInput" placeholder="输入步数" style="flex:1;background:var(--inset);border:1px solid var(--bdr);border-radius:8px;padding:8px 12px;color:var(--t1);font-size:13px" onchange="updateSteps(this.value)">
</div>
</div>
<div class="card">
<div class="card-title">💪 今日训练计划</div>
<div id="todayPlan"></div>
</div>
<div class="card">
<div class="card-title">💊 今日补剂清单</div>
<div class="supplement-list" id="supList"></div>
</div>
</div>

<!-- TAB 2: 总览 -->
<div class="tab-content" id="tab-overview">
<div class="kpi-grid" id="overviewKpis"></div>
<div class="card" style="margin-top:12px">
<div class="card-title">📅 阶段进度</div>
<div class="stage-row"><div><div style="font-size:11px;color:var(--t3)">5/31起已过</div><div class="num" id="daysPassed">—</div><div style="font-size:11px;color:var(--t3)">天</div></div>
<div style="flex:1;margin:0 16px"><div class="progress-bar"><div class="progress-fill" id="stageProgress" style="width:0%"></div></div><div style="text-align:center;font-size:11px;color:var(--blue);margin-top:4px" id="stageLabel">—</div></div>
<div style="text-align:right"><div style="font-size:11px;color:var(--t3)">距12/1还剩</div><div class="num" id="daysRemain">—</div><div style="font-size:11px;color:var(--t3)">天</div></div>
</div>
</div>
<div class="card">
<div class="card-title">⚖️ 体重趋势</div>
<div id="weightChart"></div>
</div>
<div class="card">
<div class="card-title">📏 腰围趋势</div>
<div id="waistChart"></div>
</div>
</div>

<!-- TAB 3: 训练 -->
<div class="tab-content" id="tab-training">
<div class="kpi-grid">
<div class="kpi-item"><div class="kpi-value" id="totalTrainDays">—</div><div class="kpi-label">累计训练天数</div></div>
<div class="kpi-item"><div class="kpi-value" id="totalTrainHours">—<span class="unit">h</span></div><div class="kpi-label">累计总时长</div></div>
<div class="kpi-item"><div class="kpi-value" id="totalDynCal">—<span class="unit">kcal</span></div><div class="kpi-label">累计动态消耗</div></div>
<div class="kpi-item"><div class="kpi-value" id="totalCal">—<span class="unit">kcal</span></div><div class="kpi-label">累计总消耗</div></div>
</div>
<div class="card" style="margin-top:12px">
<div class="card-title">🔥 消耗构成</div>
<div id="calPieChart"></div>
</div>
<div class="card">
<div class="card-title">📅 日期范围</div>
<div class="date-range">
<input type="date" id="trainStart" value="2026-05-31" onchange="filterTraining()">
<span>至</span>
<input type="date" id="trainEnd" value="2026-08-02" onchange="filterTraining()">
</div>
</div>
<div class="card">
<div class="card-title">📋 训练明细</div>
<div style="overflow-x:auto"><table id="trainTable"><thead><tr><th>日期</th><th>类型</th><th>时长</th><th>动态</th><th>总消耗</th></tr></thead><tbody></tbody></table></div>
</div>
</div>

<!-- TAB 4: 饮食 -->
<div class="tab-content" id="tab-diet">
<div class="card" style="background:linear-gradient(135deg,#1a2332,#1a1d24)">
<div style="font-size:12px;color:var(--green);margin-bottom:4px">📊 累计总摄入</div>
<div class="big-num" id="totalCalIn">—<span class="unit"> kcal</span></div>
<div class="big-sub" id="totalProteinIn">—</div>
</div>
<div class="card">
<div class="card-title">📅 日期范围</div>
<div class="date-range">
<input type="date" id="dietStart" value="2026-05-31" onchange="filterDiet()">
<span>至</span>
<input type="date" id="dietEnd" value="2026-08-02" onchange="filterDiet()">
</div>
</div>
<div class="card">
<div class="card-title">📋 每日饮食明细</div>
<div id="dietDetail"></div>
</div>
</div>

<!-- TAB 5: 体测 -->
<div class="tab-content" id="tab-body">
<div class="card">
<div class="card-title">⚖️ 体重趋势</div>
<div id="bodyWeightChart"></div>
</div>
<div class="card">
<div class="card-title">📉 体脂率趋势</div>
<div id="bfChart"></div>
</div>
<div class="card">
<div class="card-title">📏 腰围趋势</div>
<div id="bodyWaistChart"></div>
</div>
<div class="card">
<div class="card-title">📅 日期范围</div>
<div class="date-range">
<input type="date" id="bodyStart" value="2026-05-26" onchange="filterBody()">
<span>至</span>
<input type="date" id="bodyEnd" value="2026-08-02" onchange="filterBody()">
</div>
</div>
<div class="card">
<div class="card-title">📋 完整体测数据</div>
<div style="overflow-x:auto"><table id="bodyTable"><thead><tr><th>日期</th><th>体重</th><th>体脂</th><th>BMI</th><th>BMR</th><th>肌肉</th><th>去脂</th><th>内脏</th></tr></thead><tbody></tbody></table></div>
</div>
<div class="card">
<div class="card-title">📐 维度记录</div>
<div style="overflow-x:auto"><table id="dimTable"><thead><tr><th>日期</th><th>腰围</th><th>臀围</th><th>胸围</th><th>大腿</th><th>上臂绷紧</th><th>上臂放松</th><th>备注</th></tr></thead><tbody></tbody></table></div>
</div>
</div>

<!-- TAB 6: 花费 -->
<div class="tab-content" id="tab-expense">
<div class="card">
<div class="card-title">💰 分类占比</div>
<div id="expPieChart"></div>
</div>
<div class="card">
<div class="card-title">📅 日期范围</div>
<div class="date-range">
<input type="date" id="expStart" value="2026-05-31" onchange="filterExpense()">
<span>至</span>
<input type="date" id="expEnd" value="2026-08-02" onchange="filterExpense()">
</div>
</div>
<div class="card">
<div class="card-title">📋 明细</div>
<div style="overflow-x:auto"><table id="expTable"><thead><tr><th>日期</th><th>项目</th><th>金额</th><th>分类</th></tr></thead><tbody></tbody></table></div>
</div>
</div>

<!-- TAB 7: 周复盘 -->
<div class="tab-content" id="tab-weekly">
<div class="card">
<div class="card-title">📅 选择周</div>
<select id="weekSelect" onchange="showWeekly()">
<option value="">请选择...</option>
<option value="W29">W29 (7/20-7/26)</option>
<option value="W31">W31 (7/27-8/2)</option>
</select>
</div>
<div id="weeklyContent"></div>
</div>

<!-- TAB 8: 月复盘 -->
<div class="tab-content" id="tab-monthly">
<div class="card">
<div class="card-title">📅 选择月</div>
<select id="monthSelect" onchange="showMonthly()">
<option value="">请选择...</option>
<option value="6月">6月</option>
<option value="7月">7月</option>
</select>
</div>
<div id="monthlyContent"></div>
</div>

</div>

<script>
// ===== DATA =====
const WD={w_json};
const DD={d_json};
const TD={t_json};
const ED={e_json};
const DIM={dim_json};
const SUP={sup_json};

const WEEKLY={{
"W29":{{period:"7/20-7/26",ws:84.70,we:84.45,wc:-0.25,bfs:29.6,bfe:29.6,td:5,th:6.6,ac:1365,ap:139,
s:"正常减脂方案重启第一周。欺骗餐后水钠潴留从86.55回落至84.45，7天降2.10kg。日均摄入1365kcal精准贴合目标。训练执行5/6天，总动态消耗2677kcal。体脂率持平29.6%。"}},
"W31":{{period:"7/27-8/2",ws:85.35,we:83.4,wc:-1.95,bfs:29.6,bfe:29.2,td:4,th:6.8,ac:1305,ap:135,
s:"V7首周执行。体脂率开始下降0.4%。周减重1.95kg。训练执行率80%(4/5)。总动态消耗3141kcal。7/31因疲惫暂停1天。"}}
}};

const MONTHLY={{
"6月":{{td:12,th:10.5,ws:87.4,we:87.5,ac:1550,dc:0.7,
s:"第一个月试验期。重在建立习惯和校准基线。体重从87.4→87.5基本持平。训练频率43%(12/28天)。6/19白酒事件(4892kcal)抵消一周缺口。TDEE校准至1900-2050kcal。"}},
"7月":{{td:22,th:28.5,ws:86.9,we:83.4,ac:1380,dc:0.85,
s:"正式执行期。猛冲期(7/13-7/20,871kcal/d)+降档恢复期+正常减脂。体重从86.9→83.4降3.5kg。训练频率71%(22/31天)。体脂从30.4%→29.2%↓1.2%。7/19欺骗餐(2956kcal)为计划内代谢重置。"}}
}};

const ACTIONS={{
"周一":{{name:"推力量 + HIIT",dur:"~67min",w:[
{{n:"哑铃卧推",s:"4组×10-12次",w:"7.5-10kg/手",t:"肩胛骨全程后缩下沉贴凳，离心3-4秒"}},
{{n:"哑铃肩推",s:"4组×10-12次",w:"7.5kg/手",t:"背部贴紧靠背不后仰"}},
{{n:"标准俯卧撑",s:"4组×力竭",w:"自重",t:"末组可改跪姿，核心收紧夹臀"}},
{{n:"仰卧臂屈伸",s:"4组×12次",w:"5kg",t:"大臂固定不动"}}
],hiit:"弓步+弯举40s → 弓步+转体40s → 仰卧蹬车40s → 休息60s ×5轮",
warmup:"快速小碎步→臀桥→猫牛式→弓步压腿+同侧转体→站立腘绳肌拉伸→手臂画圈→站姿提膝触肘→快速深蹲起立+踮脚尖",
cd:"胸肌门框拉伸+三头肌拉伸+踝关节画圈",note:"组间休息60-75秒"}},
"周二":{{name:"拉力量 + HIIT + 肩胛协议",dur:"~87min",w:[
{{n:"弹力带直臂下压",s:"4组×12-15次",w:"弹力带15磅",t:"站姿，手臂伸直从头顶往下压，顶峰挤压1-2秒"}},
{{n:"单臂哑铃划船",s:"4组×12-15次",w:"12.5kg/手",t:"离心5-6秒，组间60秒"}},
{{n:"面拉",s:"4组×15次",w:"弹力带10磅",t:"对准面部，顶峰挤压1-2秒"}},
{{n:"哑铃弯举",s:"4组×12次",w:"5-7.5kg/手",t:"坐姿靠凳"}}
],hiit:"深蹲+肩上推40s → 快速俯卧撑40s → 哑铃摇摆40s → 休息60s ×5轮",
warmup:"同周一",cd:"背阔肌侧向幼犬式+直臂二头拉伸+跨胸后束拉伸+踝关节画圈",note:"含肩胛协议完整版20min+肩袖激活"}},
"周三":{{name:"休息日",dur:"—",w:[],hiit:"",warmup:"",cd:"",note:"完全休息。如需补课补周一/周二模块。"}},
"周四":{{name:"拉力量 + HIIT",dur:"~57min",w:[
{{n:"弹力带直臂下压",s:"4组×12-15次",w:"弹力带15磅",t:"站姿，顶峰挤压1-2秒"}},
{{n:"单臂哑铃划船",s:"4组×12-15次",w:"12.5kg/手",t:"离心5-6秒"}},
{{n:"面拉",s:"4组×15次",w:"弹力带10磅",t:"对准面部，顶峰挤压"}},
{{n:"哑铃弯举",s:"4组×12次",w:"5-7.5kg/手",t:"坐姿靠凳"}}
],hiit:"深蹲+肩上推40s → 快速俯卧撑40s → 哑铃摇摆40s → 休息60s ×5轮",
warmup:"同周一",cd:"背阔肌拉伸+直臂二头拉伸+跨胸后束拉伸+踝关节画圈",note:"精力等级：低（最疲惫日）"}},
"周五":{{name:"推力量 + HIIT + 肩胛协议",dur:"~87min",w:[
{{n:"哑铃卧推",s:"4组×10-12次",w:"7.5-10kg/手",t:"肩胛骨全程后缩下沉贴凳"}},
{{n:"哑铃肩推",s:"4组×10-12次",w:"7.5kg/手",t:"背部贴紧靠背不后仰"}},
{{n:"标准俯卧撑",s:"4组×力竭",w:"自重",t:"末组可改跪姿"}},
{{n:"仰卧臂屈伸",s:"4组×12次",w:"5kg",t:"大臂固定不动"}}
],hiit:"弓步+弯举40s → 弓步+转体40s → 仰卧蹬车40s → 休息60s ×5轮",
warmup:"同周一",cd:"胸肌门框拉伸+三头肌拉伸+踝关节画圈",note:"含肩胛协议完整版20min"}},
"周六":{{name:"下肢 + 肩胛 + HIIT",dur:"~90min",w:[
{{n:"高脚杯深蹲",s:"4组×12次",w:"10kg哑铃",t:"膝盖追脚尖"}},
{{n:"保加利亚分腿蹲",s:"4组×10次/侧",w:"5kg/手",t:"先做右腿"}},
{{n:"单腿臀桥",s:"4组×12次/侧",w:"自重",t:"顶峰挤压1秒，骨盆不旋转"}}
],core:[
{{n:"死虫式",s:"3组×每侧10次",t:"腰贴地面"}},
{{n:"鸟狗式",s:"3组×每侧8次",t:"顶端停2秒"}},
{{n:"空心体保持",s:"2组×30-45秒",t:"下背压实"}}
],hiit:"快速俯卧撑40s → 登山者40s → 平板支撑起落40s → 休息60s ×7轮",
warmup:"同周一",cd:"股四头肌+腘绳肌+髋屈肌拉伸+踝关节画圈",note:"最重训练日。含核心10min+肩胛20min。"}},
"周日":{{name:"休息日",dur:"—",w:[],hiit:"",warmup:"",cd:"",note:"完全休息。饮食：碳水≤50g。"}}
}};

// ===== UTILS =====
function $(id){{return document.getElementById(id)}}
function fmt(n,d=1){{return Number(n).toFixed(d)}}
function dayOfYear(d){{const s=new Date(d.getFullYear(),0,0);return Math.floor((d-s)/86400000)}}

// ===== TAB NAVIGATION =====
document.querySelectorAll('.tab-item').forEach(t=>{{
  t.addEventListener('click',function(){{
    document.querySelectorAll('.tab-item').forEach(x=>x.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(x=>x.classList.remove('active'));
    this.classList.add('active');
    $('tab-'+this.dataset.tab).classList.add('active');
  }})
}});

// ===== TAB 1: NAV =====
function initNav(){{
  // Today's remaining calories (based on 8/2 data)
  const todayDiet=DD.find(d=>d.date==='2026-08-02');
  const bmr=1672;const nee=300;
  const remain=bmr+nee-(todayDiet?todayDiet.t.cal:0);
  $('remainCal').innerHTML=Math.max(0,Math.round(remain))+'<span class="unit"> kcal</span>';
  $('remainProtein').innerHTML='蛋白 还剩 '+(todayDiet?Math.max(0,130-todayDiet.t.p):130)+'g';
  
  // Supplements
  $('supList').innerHTML=SUP.map(s=>'<div class="sup-tag">'+s+'</div>').join('');
  
  // Today's plan (8/2 is Sunday = rest)
  const days=['周日','周一','周二','周三','周四','周五','周六'];
  const today=new Date('2026-08-02');
  const dayName=days[today.getDay()];
  const plan=ACTIONS[dayName];
  let html='<div style="font-size:13px;color:var(--blue);margin-bottom:8px">'+dayName+' · '+plan.name+'</div>';
  if(plan.w.length===0){{
    html+='<div style="font-size:14px;color:var(--t2);text-align:center;padding:20px">🛌 休息日</div>';
  }}else{{
    plan.w.forEach(a=>{{
      html+='<div class="action-card"><div class="action-name">'+a.n+'</div><div class="action-meta">'+a.s+' | '+a.w+'</div><div class="action-detail">'+a.t+'</div></div>';
    }});
    if(plan.hiit) html+='<div class="hiit-box"><div style="font-size:12px;font-weight:600;color:var(--blue)">🔥 HIIT</div><div style="font-size:12px;color:var(--t2);margin-top:4px">'+plan.hiit+'</div></div>';
    if(plan.note) html+='<div class="note-box">⚠️ '+plan.note+'</div>';
  }}
  $('todayPlan').innerHTML=html;
}}

function toggleCheck(el){{el.classList.toggle('checked')}}
function updateSteps(v){{$('stepsDisplay').textContent=v}}

// ===== SVG CHARTS =====
function makeLineChart(data,xKey,yKey,w,h,color,label,showAll){{
  const pad={{l:40,r:15,t:20,b:30}};
  const cw=w-pad.l-pad.r,ch=h-pad.t-pad.b;
  const vals=data.map(d=>d[yKey]).filter(v=>v!=null);
  if(vals.length<2)return '<div style="text-align:center;color:var(--t3);padding:20px">数据不足</div>';
  const minY=Math.min(...vals),maxY=Math.max(...vals);
  const rangeY=maxY-minY||1;
  const yMin=minY-rangeY*0.1,yMax=maxY+rangeY*0.1;
  
  let svg='<svg viewBox="0 0 '+w+' '+h+'" class="chart-svg" style="max-height:'+h+'px">';
  // Grid
  for(let i=0;i<=4;i++){{
    const y=pad.t+ch*(1-i/4);
    const v=yMin+(yMax-yMin)*i/4;
    svg+='<line x1="'+pad.l+'" y1="'+y+'" x2="'+(w-pad.r)+'" y2="'+y+'" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>';
    svg+='<text x="'+(pad.l-4)+'" y="'+(y+3)+'" fill="#555" font-size="9" text-anchor="end">'+v.toFixed(1)+'</text>';
  }}
  // Line + dots
  let path='';let pts=[];
  data.forEach((d,i)=>{{
    if(d[yKey]==null)return;
    const x=pad.l+cw*(i/(data.length-1));
    const y=pad.t+ch*(1-(d[yKey]-yMin)/(yMax-yMin));
    pts.push({{x,y,v:d[yKey],label:d[xKey]?d[xKey].slice(5):''}});
    path+=(path?'L':'M')+x+','+y;
  }});
  // Area
  if(pts.length>0){{
    svg+='<path d="'+path+'L'+pts[pts.length-1].x+','+(pad.t+ch)+'L'+pts[0].x+','+(pad.t+ch)+'Z" fill="'+color+'" fill-opacity="0.08"/>';
    svg+='<path d="'+path+'" fill="none" stroke="'+color+'" stroke-width="2" stroke-linejoin="round"/>';
    pts.forEach((p,i)=>{{
      svg+='<circle cx="'+p.x+'" cy="'+p.y+'" r="3" fill="'+color+'"/>';
      if(showAll||i===0||i===pts.length-1||i%Math.ceil(pts.length/8)===0){{
        svg+='<text x="'+p.x+'" y="'+(p.y-8)+'" fill="'+color+'" font-size="9" text-anchor="middle" font-weight="600">'+p.v.toFixed(1)+'</text>';
      }}
      if(i%Math.ceil(pts.length/6)===0||i===pts.length-1){{
        svg+='<text x="'+p.x+'" y="'+(h-5)+'" fill="#555" font-size="8" text-anchor="middle">'+p.label+'</text>';
      }}
    }});
  }}
  svg+='</svg>';
  return svg;
}}

function makePieChart(slices,w,h){{
  const cx=w/2,cy=h/2,r=Math.min(w,h)/2-20;
  const total=slices.reduce((s,d)=>s+d.value,0);
  let svg='<svg viewBox="0 0 '+w+' '+h+'" class="chart-svg">';
  let angle=-Math.PI/2;
  const colors=['#4a9eff','#34c759','#ff9500','#af52de','#5ac8fa','#ff3b30'];
  slices.forEach((s,i)=>{{
    const pct=s.value/total;
    const a1=angle,a2=angle+pct*Math.PI*2;
    const large=pct>0.5?1:0;
    const x1=cx+r*Math.cos(a1),y1=cy+r*Math.sin(a1);
    const x2=cx+r*Math.cos(a2),y2=cy+r*Math.sin(a2);
    if(pct>0) svg+='<path d="M'+cx+','+cy+' L'+x1+','+y1+' A'+r+','+r+' 0 '+large+' 1 '+x2+','+y2+' Z" fill="'+colors[i%colors.length]+'" fill-opacity="0.8"/>';
    // Label
    const ma=(a1+a2)/2;
    const lx=cx+(r*0.65)*Math.cos(ma),ly=cy+(r*0.65)*Math.sin(ma);
    if(pct>0.05) svg+='<text x="'+lx+'" y="'+ly+'" fill="#fff" font-size="10" text-anchor="middle" font-weight="600">'+(pct*100).toFixed(0)+'%</text>';
    angle=a2;
  }});
  // Legend
  let ly=h-15;
  slices.forEach((s,i)=>{{
    const lx=10+i*(w/slices.length);
    svg+='<rect x="'+lx+'" y="'+(ly-8)+'" width="8" height="8" rx="2" fill="'+colors[i%colors.length]+'"/>';
    svg+='<text x="'+(lx+12)+'" y="'+(ly)+'" fill="#8a8a8a" font-size="9">'+s.label+'</text>';
  }});
  svg+='</svg>';
  return svg;
}}

// ===== TAB 2: OVERVIEW =====
function initOverview(){{
  // KPI cards
  const kpis=[
    {{v:fmt(89.85-83.4),l:'累计减重',u:'kg',c:'var(--blue)',sub:'89.85→83.4'}},
    {{v:fmt(31.5-29.2),l:'体脂下降',u:'%',c:'var(--green)',sub:'31.5%→29.2%'}},
    {{v:fmt(101.5-93.5),l:'腰围缩小',u:'cm',c:'var(--orange)',sub:'101.5→93.5'}},
    {{v:fmt(61.5-59.0),l:'去脂体重变化',u:'kg',c:'var(--purple)',sub:'61.5→59.0'}},
    {{v:TD.length,l:'累计训练',u:'天',c:'var(--teal)',sub:'自5/31起'}},
    {{v:fmt(TD.reduce((s,t)=>s+t.dur,0)/60,1),l:'训练总时长',u:'h',c:'var(--red)',sub:'自5/31起'}},
  ];
  $('overviewKpis').innerHTML=kpis.map(k=>'<div class="kpi-item"><div class="kpi-value" style="color:'+k.c+'">'+k.v+'<span class="unit"> '+k.u+'</span></div><div class="kpi-label">'+k.l+'</div><div style="font-size:10px;color:var(--t3);margin-top:2px">'+k.sub+'</div></div>').join('');
  
  // Stage progress
  const start=new Date('2026-05-31');const now=new Date('2026-08-02');const end=new Date('2026-12-01');
  const passed=Math.floor((now-start)/86400000);
  const remain=Math.floor((end-now)/86400000);
  const total=Math.floor((end-start)/86400000);
  const pct=Math.min(100,passed/total*100);
  $('daysPassed').textContent=passed;
  $('daysRemain').textContent=remain;
  $('stageProgress').style.width=pct.toFixed(1)+'%';
  $('stageLabel').textContent='进度 '+pct.toFixed(1)+'%';
  
  // Charts
  const chartW=450,chartH=200;
  $('weightChart').innerHTML=makeLineChart(WD,'date','weight',chartW,chartH,'#4a9eff','体重',false);
  // Waist chart from dimensions
  const waistData=DIM.map(d=>({{date:d.date,waist:d.waist}}));
  $('waistChart').innerHTML=makeLineChart(waistData,'date','waist',chartW,160,'#ff9500','腰围',true);
}}

// ===== TAB 3: TRAINING =====
function filterTraining(){{
  const s=$('trainStart').value,e=$('trainEnd').value;
  const filtered=TD.filter(t=>t.date>=s&&t.date<=e);
  const totalDays=filtered.length;
  const totalMin=filtered.reduce((s,t)=>s+t.dur,0);
  const totalDyn=filtered.reduce((s,t)=>s+t.dyn,0);
  const totalAll=filtered.reduce((s,t)=>s+t.total,0);
  $('totalTrainDays').innerHTML=totalDays;
  $('totalTrainHours').innerHTML=fmt(totalMin/60,1)+'<span class="unit">h</span>';
  $('totalDynCal').innerHTML=totalDyn.toLocaleString()+'<span class="unit"> kcal</span>';
  $('totalCal').innerHTML=totalAll.toLocaleString()+'<span class="unit"> kcal</span>';
  
  // Pie
  const bmrEst=1700*totalDays;const nee=300*totalDays;
  $('calPieChart').innerHTML=makePieChart([
    {{label:'BMR',value:bmrEst}},{{label:'NEAT',value:nee}},{{label:'训练',value:totalAll}}
  ],300,200);
  
  // Table
  const tbody=document.querySelector('#trainTable tbody');
  tbody.innerHTML=filtered.map(t=>'<tr><td>'+t.date.slice(5)+'</td><td>'+t.type+'</td><td>'+t.dur+'min</td><td>'+t.dyn+'kcal</td><td>'+t.total+'kcal</td></tr>').join('');
}}

// ===== TAB 4: DIET =====
function filterDiet(){{
  const s=$('dietStart').value,e=$('dietEnd').value;
  const filtered=DD.filter(d=>d.date>=s&&d.date<=e);
  const totalCal=filtered.reduce((s,d)=>s+d.t.cal,0);
  const totalP=filtered.reduce((s,d)=>s+d.t.p,0);
  $('totalCalIn').innerHTML=totalCal.toLocaleString()+'<span class="unit"> kcal</span>';
  $('totalProteinIn').innerHTML='蛋白 '+totalP.toLocaleString()+'g | 日均 '+fmt(totalCal/(filtered.length||1),0)+'kcal';
  
  let html='';
  filtered.slice().reverse().forEach(d=>{{
    if(d.t.cal===0)return;
    html+='<div style="margin-bottom:14px;padding-bottom:14px;border-bottom:1px solid var(--bdr)">';
    html+='<div style="display:flex;justify-content:space-between;margin-bottom:8px"><span style="font-size:13px;font-weight:600;color:var(--t1)">'+d.date.slice(5)+'</span><span style="font-size:12px;color:var(--blue)">'+d.t.cal+'kcal / '+d.t.p+'g蛋白</span></div>';
    if(d.m){{
      const meals=[['b','🌅早餐'],['l','☀️午餐'],['d','🌙晚餐'],['pre','练前'],['s','加餐'],['s2','加餐2'],['note','']];
      meals.forEach(([k,label])=>{{
        if(d.m[k]){{
          html+='<div class="meal-block"><div class="meal-label">'+label+'</div><div class="meal-items">'+d.m[k]+'</div></div>';
        }}
      }});
    }}
    html+='<div style="font-size:10px;color:var(--t3);margin-top:4px">饱和脂肪:'+d.t.sf+'g | 果糖:'+d.t.fr+'g | 碳水:'+d.t.c+'g</div>';
    html+='</div>';
  }});
  $('dietDetail').innerHTML=html;
}}

// ===== TAB 5: BODY =====
function filterBody(){{
  const s=$('bodyStart').value,e=$('bodyEnd').value;
  const chartW=450,chartH=200;
  
  const fw=WD.filter(d=>d.date>=s&&d.date<=e);
  $('bodyWeightChart').innerHTML=makeLineChart(fw,'date','weight',chartW,chartH,'#4a9eff','体重',false);
  
  const bfd=WD.filter(d=>d.date>=s&&d.date<=e&&d.bf!=null);
  $('bfChart').innerHTML=makeLineChart(bfd,'date','bf',chartW,180,'#34c759','体脂率',true);
  
  const wst=DIM.filter(d=>d.date>=s&&d.date<=e).map(d=>({{date:d.date,waist:d.waist}}));
  $('bodyWaistChart').innerHTML=makeLineChart(wst,'date','waist',chartW,160,'#ff9500','腰围',true);
  
  // Body table
  const tbody=document.querySelector('#bodyTable tbody');
  const bd=WD.filter(d=>d.date>=s&&d.date<=e&&d.bf!=null);
  tbody.innerHTML=bd.map(d=>'<tr><td>'+d.date.slice(5)+'</td><td>'+d.weight+'kg</td><td>'+d.bf+'%</td><td>'+(d.bmi||'—')+'</td><td>'+(d.bmr||'—')+'</td><td>'+(d.muscle||'—')+'</td><td>'+(d.ffm||'—')+'</td><td>'+(d.vf||'—')+'</td></tr>').join('');
  
  // Dimension table
  const dtbody=document.querySelector('#dimTable tbody');
  const dims=DIM.filter(d=>d.date>=s&&d.date<=e);
  dtbody.innerHTML=dims.map(d=>'<tr><td>'+d.date.slice(5)+'</td><td>'+d.waist+'</td><td>'+d.hip+'</td><td>'+d.chest+'</td><td>'+d.thigh+'</td><td>'+d.armFlex+'</td><td>'+d.armRelax+'</td><td style="font-size:10px">'+d.note+'</td></tr>').join('');
}}

// ===== TAB 6: EXPENSE =====
function filterExpense(){{
  const s=$('expStart').value,e=$('expEnd').value;
  const filtered=ED.filter(d=>d.date>=s&&d.date<=e);
  const total=filtered.reduce((s,d)=>s+d.amt,0);
  
  // Pie by category
  const cats={{}};
  filtered.forEach(d=>{{cats[d.cat]=(cats[d.cat]||0)+d.amt}});
  const slices=Object.entries(cats).map(([k,v])=>({{label:k,value:v}}));
  $('expPieChart').innerHTML='<div style="text-align:center;font-size:24px;font-weight:700;color:var(--t1);margin-bottom:8px">¥'+total.toFixed(0)+'</div>'+makePieChart(slices,300,220);
  
  // Table
  const tbody=document.querySelector('#expTable tbody');
  tbody.innerHTML=filtered.map(d=>'<tr><td>'+d.date.slice(5)+'</td><td>'+d.item+'</td><td style="color:var(--orange)">¥'+d.amt.toFixed(0)+'</td><td><span class="badge badge-blue">'+d.cat+'</span></td></tr>').join('');
}}

// ===== TAB 7: WEEKLY =====
function showWeekly(){{
  const v=$('weekSelect').value;
  if(!v){{$('weeklyContent').innerHTML='';return;}}
  const w=WEEKLY[v];
  let html='<div class="card"><div class="card-title">📊 '+v+' · '+w.period+'</div>';
  html+='<div class="kpi-grid">';
  html+='<div class="kpi-item"><div class="kpi-value" style="color:var(--blue)">'+w.wc.toFixed(2)+'<span class="unit"> kg</span></div><div class="kpi-label">体重变化</div><div style="font-size:10px;color:var(--t3)">'+w.ws+'→'+w.we+'</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value" style="color:var(--green)">'+(w.bfe-w.bfs).toFixed(1)+'<span class="unit"> %</span></div><div class="kpi-label">体脂变化</div><div style="font-size:10px;color:var(--t3)">'+w.bfs+'%→'+w.bfe+'%</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+w.td+'<span class="unit"> 天</span></div><div class="kpi-label">训练天数</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+w.th+'<span class="unit"> h</span></div><div class="kpi-label">训练时长</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+w.ac+'<span class="unit"> kcal</span></div><div class="kpi-label">日均摄入</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+w.ap+'<span class="unit"> g</span></div><div class="kpi-label">日均蛋白</div></div>';
  html+='</div>';
  html+='<div class="review-section" style="margin-top:12px"><div class="review-title">📝 总结</div><div class="summary-text">'+w.s+'</div></div>';
  html+='</div>';
  $('weeklyContent').innerHTML=html;
}}

// ===== TAB 8: MONTHLY =====
function showMonthly(){{
  const v=$('monthSelect').value;
  if(!v){{$('monthlyContent').innerHTML='';return;}}
  const m=MONTHLY[v];
  let html='<div class="card"><div class="card-title">📊 '+v+' 月度复盘</div>';
  html+='<div class="kpi-grid">';
  html+='<div class="kpi-item"><div class="kpi-value" style="color:var(--blue)">'+(m.we-m.ws).toFixed(1)+'<span class="unit"> kg</span></div><div class="kpi-label">体重变化</div><div style="font-size:10px;color:var(--t3)">'+m.ws+'→'+m.we+'</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+m.td+'<span class="unit"> 天</span></div><div class="kpi-label">训练天数</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+m.th+'<span class="unit"> h</span></div><div class="kpi-label">训练总时长</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+m.ac+'<span class="unit"> kcal</span></div><div class="kpi-label">日均摄入</div></div>';
  html+='<div class="kpi-item"><div class="kpi-value">'+(m.dc*100).toFixed(0)+'<span class="unit"> %</span></div><div class="kpi-label">饮食达标率</div></div>';
  html+='</div>';
  html+='<div class="review-section" style="margin-top:12px"><div class="review-title">📝 总结</div><div class="summary-text">'+m.s+'</div></div>';
  html+='</div>';
  $('monthlyContent').innerHTML=html;
}}

// ===== INIT =====
initNav();
initOverview();
filterTraining();
filterDiet();
filterBody();
filterExpense();
</script>
</body>
</html>'''

# Write the file
out_path = '/app/data/所有对话/主对话/健康/健康看板/health-dashboard.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written {len(html)} bytes to {out_path}')
