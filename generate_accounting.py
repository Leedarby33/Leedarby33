
import json

# ========== ALL TRANSACTIONS ==========
# Format: (date_str, category_key, item_name, amount)
# category_key maps to the 11 categories

transactions = []

# ====== JUNE TRANSACTIONS ======
# 餐饮
transactions.append(("2026-06-01", "餐饮", "袁记云饺鸡肉云吞12个", 16.10))
transactions.append(("2026-06-02", "餐饮", "沙县鸡腿饭", 18.20))
transactions.append(("2026-06-07", "餐饮", "晚饭：钵钵鸡+酸菜土豆+米饭", 79.70))
transactions.append(("2026-06-08", "餐饮", "午餐外卖（金枪鱼滑蛋轻蔬碗）", 23.20))
transactions.append(("2026-06-09", "餐饮", "午餐外卖（刘家牛肉饭·广东菜心牛肉盖饭+拉丝鸡蛋炒番茄）", 21.18))
transactions.append(("2026-06-11", "餐饮", "午餐外卖（七碗湘·小炒黄牛肉盖码饭+煎蛋+小菜）", 20.00))
transactions.append(("2026-06-12", "餐饮", "午餐外卖（滑蛋炒牛肉+番茄炒蛋+米饭）", 20.80))
transactions.append(("2026-06-14", "餐饮", "晚餐外卖（钵钵鸡套餐+米饭+肉汁萝卜+例汤）", 25.90))
transactions.append(("2026-06-15", "餐饮", "午餐外卖（西芹炒牛肉+清炒莴笋丝+白灼菜心+糙米饭）", 24.80))
transactions.append(("2026-06-16", "餐饮", "午餐外卖（春野·小炒黄牛肉+西红柿炒蛋+米饭）", 27.80))
transactions.append(("2026-06-17", "餐饮", "午餐外卖（口水鸡+虾仁滑蛋+糙米饭）", 21.80))
transactions.append(("2026-06-18", "餐饮", "午餐：袁记云饺（玉米鲜肉9个+黑猪肉9个=18个）", 23.90))
# 6/18 牛肉拌面碗 SKIPPED - price missing
transactions.append(("2026-06-19", "娱乐", "剑网三凌波赴九幽外观", 279.90))
transactions.append(("2026-06-19", "娱乐", "剑网三110橙武拓印券", 330.89))
transactions.append(("2026-06-19", "娱乐", "剑网三120大橙武拓印券", 269.90))
transactions.append(("2026-06-19", "娱乐", "剑网三点卡充值", 15.00))
transactions.append(("2026-06-21", "餐饮", "午餐外卖（黔家阿婆·招牌鲜牛肉+7种配菜+蘸水+米饭）", 21.90))
transactions.append(("2026-06-22", "餐饮", "午餐外卖（烤牛肉拌饭）", 22.30))
transactions.append(("2026-06-23", "餐饮", "午餐外卖（蒜蓉粉丝虾套餐）", 24.10))
transactions.append(("2026-06-24", "餐饮", "午餐外卖", 20.30))
transactions.append(("2026-06-25", "餐饮", "午餐外卖", 21.00))
transactions.append(("2026-06-26", "餐饮", "午餐外卖（广东菜心牛肉+苦瓜牛肉+番茄炒蛋+牛骨清汤）", 24.08))
transactions.append(("2026-06-27", "个人生活", "咖啡豆", 190.00))
transactions.append(("2026-06-29", "餐饮", "午餐外卖（蔓味轻食·原切菲力鸡胸牛排配蔬果沙拉）", 18.00))
transactions.append(("2026-06-30", "餐饮", "午餐外卖（原切眼肉牛排+太阳蛋+土豆泥+时蔬）", 37.02))

# 交通
transactions.append(("2026-05-31", "交通", "峨眉岭停车费", 45.50))
transactions.append(("2026-06-01", "交通", "停车费", 10.50))
transactions.append(("2026-06-08", "交通", "停车费", 11.50))
transactions.append(("2026-06-08", "交通", "周末停车费（两天）", 87.00))
transactions.append(("2026-06-09", "交通", "昨晚停车费", 9.00))
transactions.append(("2026-06-09", "交通", "上班停车费", 8.50))
transactions.append(("2026-06-09", "交通", "车辆充电充值", 200.00))
transactions.append(("2026-06-11", "交通", "晚上停车费", 11.50))
transactions.append(("2026-06-12", "交通", "早上停车费", 7.50))
transactions.append(("2026-06-12", "交通", "单位停车费", 11.50))
transactions.append(("2026-06-15", "交通", "停车费", 11.50))
transactions.append(("2026-06-16", "交通", "停车费", 11.50))
transactions.append(("2026-06-17", "交通", "停车费", 8.50))
transactions.append(("2026-06-22", "交通", "停车费", 11.50))
transactions.append(("2026-06-22", "交通", "充电费", 25.50))
transactions.append(("2026-06-23", "交通", "停车费", 11.50))
transactions.append(("2026-06-24", "交通", "停车费（早上，家没车位停前面停车场）", 10.50))
transactions.append(("2026-06-24", "交通", "停车费（下班）", 11.50))
transactions.append(("2026-06-25", "交通", "停车费（一趟）", 8.50))
transactions.append(("2026-06-29", "交通", "停车费", 10.50))
transactions.append(("2026-06-30", "交通", "停车费", 8.50))

# 娱乐
transactions.append(("2026-06-01", "娱乐", "B站UP主充电包月", 10.00))
transactions.append(("2026-06-01", "娱乐", "B站充电会员", 10.00))
transactions.append(("2026-06-01", "娱乐", "京东Plus年卡", 99.00))
transactions.append(("2026-06-02", "娱乐", "剑网三璀璨钱途礼盒", 387.80))
transactions.append(("2026-06-02", "娱乐", "剑网三120级小铁×200", 50.00))
transactions.append(("2026-06-02", "娱乐", "剑网三奇遇后续代练", 18.00))
transactions.append(("2026-06-24", "娱乐", "WPS全年会员", 243.00))
transactions.append(("2026-06-26", "娱乐", "扣子旗舰版续费", 178.90))
transactions.append(("2026-06-26", "娱乐", "剑网三买积分", 99.90))

# 固定支出
transactions.append(("2026-06-01", "固定支出", "党费（6月）", 30.00))
transactions.append(("2026-06-15", "固定支出", "房贷净支出", 6071.17))

# 补剂
transactions.append(("2026-06-14", "补剂", "MyProtein分离乳清蛋白粉抹茶拿铁味1kg", 379.03))
transactions.append(("2026-06-14", "补剂", "欧德堡东方PRO4.0脱脂牛奶", 71.68))
transactions.append(("2026-06-17", "补剂", "Now Foods ADAM男士多维90粒×2", 456.80))
transactions.append(("2026-06-17", "补剂", "海力生95%高纯EPA鱼油5送3（690粒）", 912.65))
transactions.append(("2026-06-30", "补剂", "普通乳清柔滑巧克力5kg蛋白粉", 1088.00))

# 训练
transactions.append(("2026-06-17", "训练", "多德士TK605哑铃凳（家用尊享款全折叠）", 179.55))
transactions.append(("2026-06-17", "训练", "BlenderBottle Pro28钢铁侠800ml摇摇杯", 114.69))

# 个人护理
transactions.append(("2026-06-01", "个人护理", "博朗CCR清洗液16盒装", 261.36))

# ====== JULY TRANSACTIONS ======
# 餐饮
transactions.append(("2026-07-02", "餐饮", "午餐：鸡胸牛肉双拼沙拉碗", 18.62))
transactions.append(("2026-07-03", "餐饮", "午餐：毛豆米烧鸡+南京素什锦", 27.90))
transactions.append(("2026-07-06", "餐饮", "午餐：双倍鸡胸鲜蔬杂粮饭", 27.90))
transactions.append(("2026-07-07", "餐饮", "儿子晚餐（单人份）", 39.90))
transactions.append(("2026-07-10", "餐饮", "午餐外卖（给儿子点）", 49.40))
transactions.append(("2026-07-14", "餐饮", "午餐：海底捞海肠捞饭+50g烤牛肉粒", 33.20))
transactions.append(("2026-07-15", "餐饮", "午餐：延边辣牛肉汤单人餐", 22.50))
transactions.append(("2026-07-16", "餐饮", "午餐：CrazyCat失控猫能量碗", 28.80))
transactions.append(("2026-07-17", "餐饮", "请胡老师小孩吃饭·日料", 288.00))
transactions.append(("2026-07-18", "餐饮", "早餐：陈香贵（清汤牛肉面+5串羊肉小串+煎蛋）", 29.00))
transactions.append(("2026-07-18", "餐饮", "晚餐：牛排套餐（含儿子意面+沙拉）", 127.90))
transactions.append(("2026-07-19", "餐饮", "午餐：炸鸡外卖", 52.60))
transactions.append(("2026-07-19", "餐饮", "晚餐：馄饨外卖", 18.90))
transactions.append(("2026-07-20", "餐饮", "午餐：RYETURN轻食", 26.90))
transactions.append(("2026-07-21", "餐饮", "午餐：嫩煎鸡胸肉+应季烤时蔬+低GI谷物饭", 25.90))
transactions.append(("2026-07-22", "餐饮", "午餐：香煎鱼柳配杂蔬饭", 33.10))
transactions.append(("2026-07-23", "餐饮", "午餐：炙烤黑椒鸡胸肉时蔬糙米谷物饭+加料金枪鱼", 25.50))
transactions.append(("2026-07-24", "餐饮", "午餐", 27.90))
transactions.append(("2026-07-26", "餐饮", "晚饭（牛蛙米线+里脊肉串）", 48.00))
transactions.append(("2026-07-27", "餐饮", "午餐：嫩滑蛋羹（鸡胸肉）杂粮拌饭+白灼西兰花", 26.90))
transactions.append(("2026-07-28", "餐饮", "午餐：香煎鸡胸烤蔬杂粮饭+奇亚籽酸奶+菠菜鸡肉丸", 36.50))
transactions.append(("2026-07-29", "餐饮", "午餐：杭椒牛肉套餐", 30.30))
transactions.append(("2026-07-30", "餐饮", "午餐：葱香杏鲍菇鸡胸肉+清炒小青菜+豆芽炒韭菜+糙米饭", 24.10))
transactions.append(("2026-07-31", "餐饮", "午餐：寿司", 22.90))

# 交通
transactions.append(("2026-07-01", "交通", "停车费", 8.50))
transactions.append(("2026-07-02", "交通", "停车费", 8.50))
transactions.append(("2026-07-06", "交通", "停车费", 45.50))
transactions.append(("2026-07-06", "交通", "停车费（单位）", 8.50))
transactions.append(("2026-07-06", "交通", "货拉拉出门停车", 7.00))
transactions.append(("2026-07-07", "交通", "打车（停车换地方）", 12.90))
transactions.append(("2026-07-07", "交通", "出门办事停车", 37.00))
transactions.append(("2026-07-10", "交通", "打车（帮老婆取电瓶车）", 12.50))
transactions.append(("2026-07-13", "交通", "停车费（早×2）", 63.50))
transactions.append(("2026-07-13", "交通", "停车费（下班）", 8.50))
transactions.append(("2026-07-14", "交通", "停车费", 11.50))
transactions.append(("2026-07-15", "交通", "停车费", 11.50))
transactions.append(("2026-07-16", "交通", "停车费", 11.50))
transactions.append(("2026-07-17", "交通", "停车费", 45.50))
transactions.append(("2026-07-18", "交通", "停车费", 45.50))
transactions.append(("2026-07-18", "交通", "停车费（接老婆孩子）", 12.00))
transactions.append(("2026-07-20", "交通", "停车费", 11.50))
transactions.append(("2026-07-21", "交通", "停车费", 8.50))
transactions.append(("2026-07-22", "交通", "停车费", 11.50))
transactions.append(("2026-07-23", "交通", "停车费", 11.50))
transactions.append(("2026-07-24", "交通", "汽车保养", 588.00))
transactions.append(("2026-07-24", "交通", "打车", 22.30))
transactions.append(("2026-07-25", "交通", "停车费", 8.50))
transactions.append(("2026-07-26", "交通", "停车费", 49.00))
transactions.append(("2026-07-26", "交通", "停车费（7/27补报，属7/26）", 6.00))
transactions.append(("2026-07-27", "交通", "停车费", 11.50))
transactions.append(("2026-07-27", "交通", "充电（预充50退23.38）", 26.62))
transactions.append(("2026-07-28", "交通", "机场停车费", 13.50))
transactions.append(("2026-07-28", "交通", "停车费", 11.50))
transactions.append(("2026-07-28", "交通", "交通罚款补交", 350.00))
transactions.append(("2026-07-29", "交通", "停车费", 8.50))
transactions.append(("2026-07-30", "交通", "停车费", 11.50))
transactions.append(("2026-07-31", "交通", "打车（回家）", 35.00))
transactions.append(("2026-07-31", "交通", "停车费", 11.50))

# 固定支出
transactions.append(("2026-07-13", "固定支出", "党费", 30.00))
transactions.append(("2026-07-15", "固定支出", "房贷净支出", 6525.07))

# 补剂
transactions.append(("2026-07-13", "补剂", "惯爱他达拉非5mg×3盒", 251.00))
transactions.append(("2026-07-13", "补剂", "Nutricost KSM-66 600mg×2盒", 286.94))

# 训练
transactions.append(("2026-07-09", "训练", "哈他天然橡胶PU瑜伽垫183×68cm/5mm", 209.00))

# 数码产品
transactions.append(("2026-07-05", "数码产品", "小米Clip耳夹式耳机", 799.00))

# 娱乐
transactions.append(("2026-07-05", "娱乐", "百度网盘24小时会员", 9.90))
transactions.append(("2026-07-07", "娱乐", "观夏昆仑煮雪藤条香薰（200ml）", 293.00))  # WAIT - 香薰→个人生活
# Actually: 家居-香薰 → 个人生活. Let me fix this.

# Remove the wrong one and add correct
transactions.pop()  # remove the last one
transactions.append(("2026-07-07", "个人生活", "观夏昆仑煮雪藤条香薰（200ml）", 293.00))

transactions.append(("2026-07-08", "娱乐", "剑网三代练：凌波争铸吴钩", 15.00))
transactions.append(("2026-07-08", "娱乐", "剑网三代练：凌波塞外宝驹包赛季", 6.00))
transactions.append(("2026-07-08", "娱乐", "Coze积分充值10万", 100.00))
transactions.append(("2026-07-11", "娱乐", "Coze积分充值", 100.00))
transactions.append(("2026-07-13", "娱乐", "Coze积分充值", 100.00))
transactions.append(("2026-07-17", "娱乐", "Coze积分充值", 100.00))
transactions.append(("2026-07-20", "娱乐", "B站充电", 19.00))
transactions.append(("2026-07-21", "娱乐", "B站充电充值卡", 200.00))
transactions.append(("2026-07-22", "娱乐", "Coze积分充值", 100.00))
transactions.append(("2026-07-26", "娱乐", "游戏捆绑包（侠影录+地府有点忙）", 82.26))
transactions.append(("2026-07-31", "娱乐", "扣子积分充值", 100.00))
transactions.append(("2026-07-31", "娱乐", "App Store订阅", 27.00))

# 个人护理
transactions.append(("2026-07-28", "个人护理", "宝拉珍选水杨酸身体乳+精华液", 365.49))
transactions.append(("2026-07-30", "个人护理", "碧柔UV水感防晒精华 50g×2", 88.29))

# 个人生活
transactions.append(("2026-07-17", "个人生活", "烟（两条+一包）", 483.00))
transactions.append(("2026-07-23", "个人生活", "鸭舌头（周黑鸭）", 280.00))
transactions.append(("2026-07-26", "个人生活", "烟", 23.00))
transactions.append(("2026-07-26", "个人生活", "剪头发", 150.00))
transactions.append(("2026-07-28", "个人生活", "茶叶（六妙一日茶老白茶龙珠300g）", 153.00))

# Income
income_records = [
    ("2026-06-01", "初始余额", 9475.65),
    ("2026-06-10", "工资", 11711.34),
    ("2026-07-10", "工资", 9023.48),
]

# ========== CALCULATIONS ==========
categories_config = {
    "固定支出": {"emoji": "🏠", "color": "#ff6b6b"},
    "餐饮": {"emoji": "🍜", "color": "#ffa502"},
    "补剂": {"emoji": "💊", "color": "#2ed573"},
    "训练": {"emoji": "🏋️", "color": "#1e90ff"},
    "个人护理": {"emoji": "🧴", "color": "#ff6b81"},
    "交通": {"emoji": "🚗", "color": "#747d8c"},
    "娱乐": {"emoji": "🎮", "color": "#a55eea"},
    "医疗": {"emoji": "💊", "color": "#ff4757"},
    "穿戴": {"emoji": "👟", "color": "#ff7f50"},
    "个人生活": {"emoji": "🚬", "color": "#57606f"},
    "数码产品": {"emoji": "📱", "color": "#3742fa"},
}

# Category totals
cat_totals = {}
for t in transactions:
    cat = t[1]
    amt = t[3]
    cat_totals[cat] = cat_totals.get(cat, 0) + amt

total_income = sum(r[2] for r in income_records)
total_expense = sum(t[3] for t in transactions)
balance = total_income - total_expense

# Monthly breakdown
june_expense = sum(t[3] for t in transactions if t[0].startswith("2026-06") or t[0].startswith("2026-05"))
july_expense = sum(t[3] for t in transactions if t[0].startswith("2026-07"))
june_income = sum(r[2] for r in income_records if r[0].startswith("2026-06"))
july_income = sum(r[2] for r in income_records if r[0].startswith("2026-07"))

print(f"Total income: {total_income:.2f}")
print(f"Total expense: {total_expense:.2f}")
print(f"Balance: {balance:.2f}")
print(f"June expense: {june_expense:.2f}, June income: {june_income:.2f}")
print(f"July expense: {july_expense:.2f}, July income: {july_income:.2f}")
print()
print("Category totals:")
for cat, total in sorted(cat_totals.items(), key=lambda x: -x[1]):
    cfg = categories_config[cat]
    print(f"  {cfg['emoji']} {cat}: ¥{total:.2f}")
print(f"\nTotal transactions: {len(transactions)}")

# Save as JSON for use in HTML generation
data = {
    "transactions": [{"date": t[0], "category": t[1], "item": t[2], "amount": t[3]} for t in transactions],
    "income": [{"date": r[0], "item": r[1], "amount": r[2]} for r in income_records],
    "categories_config": categories_config,
    "cat_totals": {k: round(v, 2) for k, v in cat_totals.items()},
    "total_income": round(total_income, 2),
    "total_expense": round(total_expense, 2),
    "balance": round(balance, 2),
}

with open('/app/data/所有对话/主对话/健康/健康看板/accounting_data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nData saved to accounting_data.json")
