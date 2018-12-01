yxf_yixue_py : 易学数术推演
=========================================================

1.历法（万年历）。  
2.各数术模块（已完成：八字、六爻、小成图、金口诀，未来可添加：紫微斗数、风水、中医气运分析）。  
3.预测应用（探索性代码，暂时无用）。  

## 待解决

自动分析代码——内容太多，时间太少。  
预测的理论性理解——超出物质科学范围，悟。如果硬要对照现代科学，则应与信息论、分形、全息、混沌、复杂科学、量子力学等门类有关。（信息感应，量子数，自旋场，分形几何）  
预测实战的可靠性——缺少大批量实验，难以量化；占卜术预测准确性受意识状态影响忽高忽低;个人气运、意识的参与会影响结果，比如以预测牟利；命理术较为客观容易实现。  
数字预测。  

## 代码结构

    /utils——通用代码
    /wannianli——万年历（农历与节气无法逻辑推算，需要数据库，目前只得到200年数据）
    /bazi——八字
    /jinkoujue——金口诀
    /liuyao——六爻
    /xiaochengtu——小成图
    /#ziweidoushu——（紫微斗数，希望未来能够加入）  
	/#app_yixuececai——（易学测彩的初步探索，暂时无用）
	/#app_yixuecegu——（易学测股的初步探索，暂时无用）

## 环境依赖（此项目非常依赖中文和统一编码，2版本对中文非常不友好，必须使用3版本）

python==3.6  
openpyxl  
web.py==0.40.dev0  

python3解决方案：  
安装python3（已整理安装脚本）。  
在项目的所有代码文件开头加上这两句：  

	#!/usr/bin/python3   
	# -*- coding: utf-8 -*-

## 使用方法1：安装为Python系统模块

install:   

	python3 setup.py install
	
uninstall:   

	pip3 uninstall yxf-yixue
	
## 使用方法2：作为服务运行

runserver:   

	python3 server.py  或者  sh start_server.sh

## 输出内容

### API可定制输出  

例（金口诀）：  

	{
		'占时': {
			'占时': {'干支': '干支：戊戌 戊午 己丑 甲戌 空亡（辰巳 子丑 午未 申酉）'}, 
			'月将': {'干支': '未'}
		}, 
		'盘': {
			'1': {'地盘': '子', '天盘': '酉', '将神': '从魁', '神盘': '未', '贵神': '太常'}, 
			'2': {'地盘': '丑', '天盘': '戌', '将神': '河魁', '神盘': '申', '贵神': '白虎'}, 
			'3': {'地盘': '寅', '天盘': '亥', '将神': '登明', '神盘': '戌', '贵神': '天空'}, 
			'4': {'地盘': '卯', '天盘': '子', '将神': '神后', '神盘': '寅', '贵神': '青龙'}, 
			'5': {'地盘': '辰', '天盘': '丑', '将神': '大吉', '神盘': '辰', '贵神': '勾陈'}, 
			'6': {'地盘': '巳', '天盘': '寅', '将神': '功曹', '神盘': '卯', '贵神': '六合'}, 
			'7': {'地盘': '午', '天盘': '卯', '将神': '太冲', '神盘': '午', '贵神': '朱雀'}, 
			'8': {'地盘': '未', '天盘': '辰', '将神': '天罡', '神盘': '巳', '贵神': '腾蛇'}, 
			'9': {'地盘': '申', '天盘': '巳', '将神': '太乙', '神盘': '丑', '贵神': ' 贵人'}, 
			'10': {'地盘': '酉', '天盘': '午', '将神': '胜光', '神盘': '子', '贵神': '天后'}, 
			'11': {'地盘': '戌', '天盘': '未', '将神': '小吉', '神盘': '酉', '贵神': '太阴'}, 
			'12': {'地盘': '亥', '天盘': '申', '将神': '传送', '神盘': '亥', '贵神': '玄武'}}, 
		'课': {
			'人元': {'用神': '  ', '干支': '癸', '五行': '水', '阴阳': '阴', '旺衰': '旺'}, 
			'贵神': {'用神': '  ', '干支': '甲子（天后）', '五行': '水', '阴阳': '阳', '旺衰': '旺', '纳音': '纳音海中金'}, 
			'将神': {'用神': '用', '干支': '庚午（胜光）', '五行': '火', '阴阳': '阳', '旺衰': '死', '纳音': '纳音路旁土'}, 
			'地分': {'用神': '  ', '干支': '酉', '五行': '金', '阴阳': '阴', '旺衰': '休'}
		}
	}

### 格式化输出  

#### 万年历

	公元：2018/11/28 23:58 星期三
	农历：2018年 十月 廿一 子时 四刻
	节气：小雪 第7天 功曹寅 射手座
	干支：戊戌 癸亥 甲子 甲子 空亡（辰巳 子丑 戌亥 戌亥）
	风水：下元艮运 年九紫右弼 月五黄廉贞 日六白武曲 时九紫右弼
	中医：阳火运 太阳寒水司天 太阴湿土在泉 三阳太阳寒水 足少阳胆经
	皇极：元（坎卦午会） 会（大过卦） 运（姤卦） 世（鼎卦） 旬（蛊卦） 年（随卦）
	
#### 八字

	乾造：丙子 乙未 庚戌 壬午 空亡（申酉 辰巳 寅卯 申酉）
	公元：1996/7/12 12:40 星期五
	农历：1996年 五月 廿七 午时 七刻
	节气：小暑第6日

	涧下水          沙中金          钗钏金          杨柳木
	七杀            正财            日干            食神
	丙              乙              庚              壬
	子              未              戌              午
	癸伤官          己正印          戊偏印          丁正官
					丙七杀          庚比肩
					乙正财          丁正官
	死              冠带            衰              沐浴

	天干五合：
	地支六冲：子午
	地支六合：
	地支三会：
	地支三合：
	地支生半合：
	地支墓半合：午戌

	大运：
	2004            2014            2024            2034            2044            2054            2064            2074            2084            2094
	9               19              29              39              49              59              69      		79              89              99
	丙申            丁酉            戊戌            己亥            庚子            辛丑            壬寅            癸卯            甲辰            乙巳
	七杀            正官            偏印            正印            比肩            劫财            食神            伤官            偏财            正财
	山下火          山下火          平地木          平地木          壁上土          壁上土          金箔金          金箔金          佛灯火          佛灯火
	临官            帝旺            衰              病              死              墓              绝              胎              养              长生

#### 金口诀

	地盘：子丑寅卯辰巳午未申酉戌亥
	天盘：酉戌亥子丑寅卯辰巳午未申
	神盘：未申戌寅辰卯午巳丑子酉亥
	月将：未
	占时：干支：戊戌 戊午 己丑 甲戌 空亡（辰巳 子丑 午未 申酉）
	人元：癸        水-旺
	贵神：甲子（天后）      水+旺 纳音海中金
	将神：庚午（胜光）用    火+死 纳音路旁土
	地分：酉        金-休

#### 六爻
	
	上巽下艮 风山渐(艮宫)  之  上乾下艮 天山遁(乾宫) 日空亡：午未
	青龙▅▅▅▅▅  官鬼辛卯木应     ▅▅▅▅▅ 兄弟壬戌土
	玄武▅▅▅▅▅  父母辛巳火       ▅▅▅▅▅ 子孙壬申金应
	白虎▅▅  ▅▅ X兄弟辛未土       ▅▅▅▅▅ 父母壬午火
	腾蛇▅▅▅▅▅  子孙丙申金世     ▅▅▅▅▅ 子孙丙申金
	勾陈▅▅  ▅▅  父母丙午火       ▅▅  ▅▅ 父母丙午火世
	朱雀▅▅  ▅▅  兄弟丙辰土       ▅▅  ▅▅ 兄弟丙辰土

#### 小成图

	4艮山地剥↑↓阳上|9坎水地比↓↓阳中|2坤山地剥↑↓阴下|
	------  ------  ------  ------  ------  ------
	3坎坎为水↓↓阳中|5坎水雷屯↓↑阳中|7坎坎为水↓↓阳中|
	------  ------  ------  ------  ------  ------
	8艮山雷颐↑↑阳上|1坤水地比↓↓阴下|6震山雷颐↑↑阳下|
	------  ------  ------  ------  ------  ------

