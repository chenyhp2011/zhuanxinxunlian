Problem_ID:: 201
Difficulty_Level:: 2
Problem_Text::
小明去商店买文具，他买了一本`5`元钱的笔记本和`3`支每支`2`元钱的圆珠笔。商店里还有售价`20`元的书包。
如果小明付给收银员`20`元钱，应找回多少钱？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 小明购买文具的总花费|B. 一支圆珠笔的价格|C. 收银员应该找回的钱|D. 商店里书包的价格
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 笔记本单价5元|B. 圆珠笔单价2元，买了3支|C. 小明付了20元|D. 商店里书包售价20元
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 总花费 = 物品1价格 + 物品2总价|B. 找零 = 支付金额 - 总花费|C. 物品2总价 = 单价 × 数量|D. A、B和C都需要
Rule_Answer:: D
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 计算所有购买物品的总花费|B. 计算笔记本比一支圆珠笔贵多少|C. 询问书包是否打折|D. 用支付金额减去笔记本的价格
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"书包的价格与小明已购买的物品和找零无关，是一个干扰信息。","Strategy_B":"计算价格差对于求解‘总花费’和‘找零’没有帮助。","Strategy_D":"只减去笔记本的价格，漏掉了3支圆珠笔的费用，会导致计算错误。"}

---
Problem_ID:: 202
Difficulty_Level:: 2
Problem_Text::
一个农场里有 **30** 只鸡和 **20** 只兔子，农场主是`50`岁的王大伯。
如果每只鸡每天下一个蛋，每只兔子每天吃`2`根胡萝卜，那么这些鸡和兔子在`7`天里，总共能提供多少个鸡蛋？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 7天消耗的胡萝卜总量|B. 7天产出的鸡蛋总量|C. 鸡和兔子的总数量|D. 农场主的年龄
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 有30只鸡|B. 每只鸡每天下一个蛋|C. 任务是计算7天的鸡蛋量|D. 有20只兔子，每只每天吃2根胡萝卜
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 每日总产量 = 单个产量 × 数量|B. 几日总产量 = 每日总产量 × 天数|C. A和B都需要|D. 兔子数量 > 鸡数量
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 先计算出农场里所有动物的总数|B. 先计算出所有鸡一天能产多少个蛋|C. 先计算出所有兔子一天吃多少胡萝卜|D. 将鸡的数量和天数相加
Strategy_Answer:: B
Feedback_Column:: {"Extraction_D":"兔子的数量和它们的食量对于计算鸡蛋产量是完全无关的信息，属于干扰项。","Strategy_A":"计算动物总数对解决问题没有帮助。","Strategy_C":"计算胡萝卜消耗量回答的是另一个问题，不符合本题要求。"}

---
Problem_ID:: 203
Difficulty_Level:: 2
Problem_Text::
一个图书馆上午借出了`150`本书，下午借出的书比上午多`30`本。这个图书馆共有藏书**50000**册。
请问这个图书馆今天一共借出了多少本书？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 下午借出了多少本书|B. 图书馆还剩多少本书|C. 全天总共借出了多少本书|D. 图书馆的藏书总量
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 上午借出150本|B. 下午比上午多借30本|C. 图书馆总藏书50000册|D. 问题是求全天借出的总数
Extraction_Answer:: A|B|D
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 下午数量 = 上午数量 + 差额|B. 全天总量 = 上午数量 + 下午数量|C. A和B都需要|D. 剩余数量 = 总量 - 借出数量
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 先用总藏书量减去上午借出的数量|B. 先计算出下午借出了多少本书|C. 直接将150和30相加|D. 评估图书馆的规模
Strategy_Answer:: B
Feedback_Column:: {"Extraction_C":"图书馆的总藏书量对于计算‘今天一共借出多少本’是无用信息，属于干扰项。","Strategy_A":"这个步骤是用来计算图书馆还剩多少书，而不是今天借出了多少。","Strategy_C":"直接将150和30相加（180本）是下午借出的数量，但这只是一个中间结果，不是最终答案。"}

---
Problem_ID:: 204
Difficulty_Level:: 2
Problem_Text::
一辆火车共有`12`节车厢，每节车厢有`100`个座位。火车从A站出发时，载有`1000`名乘客。
在途径的B站，有`200`名乘客下车，同时有`150`名乘客上车。火车上有`10`名乘务员。
请问火车从B站开出时，车上有多少名乘客？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 火车总共的座位数|B. 在B站下车的人数|C. 火车离开B站时的乘客人数|D. 火车上的乘务员人数
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 出发时有1000名乘客|B. B站下车200人，上车150人|C. 火车共有12节车厢，每节100个座位|D. 问题求离开B站时的乘客数
Extraction_Answer:: A|B|D
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 现有数量 = 初始数量 - 减少数量 + 增加数量|B. 总容量 = 单节容量 × 节数|C. 乘客数 < 总座位数|D. A和C都需要
Rule_Answer:: A
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 先计算出火车的总座位数|B. 先计算出B站上下车后净增加或减少的乘客数|C. 用初始乘客数减去下车人数，再加上上车人数|D. 将所有数字相加
Strategy_Answer:: C
Feedback_Column:: {"Extraction_C":"火车的总座位数（1200个）是干扰信息，虽然与背景相关，但对于计算当前乘客数是无用的。","Strategy_A":"计算总座位数对于求解当前乘客人数没有帮助。","Strategy_B":"计算净变化（-200+150 = -50人）是一个有效的方法，但最直接的策略是按顺序计算，即C选项。"}

---
Problem_ID:: 205
Difficulty_Level:: 2
Problem_Text::
为了准备学校的运动会，体育老师买了`8`个篮球和`6`个足球。每个篮球`50`元，运动会将在**10月1日**举行。
如果老师总共花了`580`元，那么每个足球的价格是多少元？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 每个篮球的价格|B. 买球的总花费|C. 买篮球的总花费|D. 每个足球的价格
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 买了8个篮球，单价50元|B. 买了6个足球|C. 总花费580元|D. 运动会在10月1日举行
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 足球总价 = 总花费 - 篮球总价|B. 篮球总价 = 篮球单价 × 篮球数量|C. 足球单价 = 足球总价 ÷ 足球数量|D. A、B和C都需要
Rule_Answer:: D
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出购买篮球一共花了多少钱|B. 用总花费除以购买的球的总数|C. 用总花费减去篮球的单价|D. 规划运动会日程
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"运动会举办的日期是一个与数学计算完全无关的干扰信息。","Strategy_B":"因为篮球和足球的单价不同，所以不能用总花费除以总数量来计算平均价格，这无法求出足球的单价。","Strategy_C":"总花费减去的是篮球的‘总价’，而不是‘单价’。"}

---

Problem_ID:: 206
Difficulty_Level:: 2
Problem_Text::
一家商店的笔记本每本卖3元，钢笔每支卖5元。李华有20元钱，她买了4本笔记本。
商店里还有50本一样的笔记本库存。请问她会找回多少钱？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 购买笔记本的总花费|B. 李华剩下的钱（找零）|C. 钢笔的价格|D. 商店的库存
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 笔记本的单价是3元|B. 李华的总钱数是20元|C. 李华买了4本笔记本|D. 商店的库存是50本
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 总花费 = 单价 × 数量|B. 找零 = 总钱数 - 总花费|C. A和B都需要|D. 库存 > 购买数量
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出4本笔记本的总价格|B. 先用20元减去笔记本的单价|C. 确认库存是否足够|D. 计算买钢笔需要多少钱
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"商店的库存数量对于计算李华的找零是无关信息，属于干扰项。","Strategy_B":"直接用总钱数减单价是错误的，因为购买了不止一本。"}

---

Problem_ID:: 207
Difficulty_Level:: 2
Problem_Text::
一个长方形客厅长6米，宽4米，高为3米。现在要用边长为1米的正方形地砖铺满整个地面。
请问需要多少块这样的地砖？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 客厅的体积|B. 客厅地面的周长|C. 铺满地面需要的地砖数量|D. 墙壁的面积
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 客厅长6米|B. 客厅宽4米|C. 客厅高3米|D. 地砖是边长1米的正方形
Extraction_Answer:: A|B|D
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 总面积 = 单块面积 × 数量|B. 长方形面积 = 长 × 宽|C. A和B都需要|D. 体积 = 长 × 宽 × 高
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算客厅的体积|B. 先计算客厅地面的面积|C. 先计算一块地砖的周长|D. 先计算客厅地面的周长
Strategy_Answer:: B
Feedback_Column:: {"Extraction_C":"客厅的高度是用来计算体积或者墙壁面积的，对于铺地面这个任务是无关信息，属于干扰项。","Strategy_A":"题目要求的是铺地砖，只和地面的面积有关，计算体积是多余的步骤。"}

---

Problem_ID:: 208
Difficulty_Level:: 2
Problem_Text::
一列火车以平均每小时80公里的速度行驶，需要行驶240公里的路程。这列火车共有5节车厢。
如果火车早上9:00出发，请问它将在什么时间到达目的地？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 火车行驶的总时间|B. 火车的平均速度|C. 火车到达的时间点|D. 火车行驶的总路程
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 平均速度是80公里/小时|B. 总路程是240公里|C. 出发时间是早上9:00|D. 火车有5节车厢
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 时间 = 路程 ÷ 速度|B. 到达时间 = 出发时间 + 行驶时间|C. A和B都需要|D. 速度 = 路程 × 时间
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出火车需要行驶多长时间|B. 将速度和路程相乘|C. 用出发时间加上车厢数量|D. 确认火车的型号
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"火车的车厢数量与计算到达时间无关，属于干扰项。"}

---

Problem_ID:: 209
Difficulty_Level:: 2
Problem_Text::
一件夹克的原价是200元，现在商店进行促销活动，打七五折（即25%的折扣）出售。
这件夹克有3种不同的颜色可供选择。请问折后这件夹克的售价是多少元？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 节省的金额|B. 夹克的原价|C. 夹克的折后售价|D. 折扣的百分比
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 原价是200元|B. 折扣是25%|C. 夹克有3种颜色
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 折扣金额 = 原价 × 折扣率|B. 售价 = 原价 - 折扣金额|C. 售价 = 原价 × (1 - 折扣率)|D. 以上都可以
Rule_Answer:: D
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出25%的折扣具体是多少钱|B. 用原价除以25%|C. 确认要买哪种颜色|D. 用原价乘以3
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"夹克的颜色数量对于计算其价格是无关信息，属于干扰项。","Strategy_B":"用原价除以折扣率是错误的计算方法。"}

---

Problem_ID:: 210
Difficulty_Level:: 2
Problem_Text::
在一个4人的学习小组中，他们的身高分别是150厘米、155厘米、158厘米和161厘米。
他们的班主任是一位35岁的男老师。请问这个学习小组的平均身高是多少厘米？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 他们的身高总和|B. 他们的平均身高|C. 他们的最高身高|D. 班主任的年龄
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 小组有4个人|B. 四个人的具体身高数据|C. 班主任的年龄是35岁
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 平均数 = 数据总和 ÷ 数据个数|B. 数据总和 = 所有数据相加|C. A和B都需要|D. 35大于4
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 将所有身高数据加起来求总和|B. 找出最高和最矮的身高|C. 将身高数据和老师年龄相加|D. 将身高数据从小到大排序
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"班主任的年龄与计算学生的平均身高无关，属于干扰项。","Strategy_C":"错误地将无关信息（老师年龄）納入计算，会导致错误的平均值。"}

---

Problem_ID:: 211
Difficulty_Level:: 2
Problem_Text::
一位面包师做一个蛋糕需要200克面粉。她今天计划做5个蛋糕。
商店售卖的面粉都是1公斤一袋的。请问她做这5个蛋糕总共需要多少克面粉？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 需要买几袋面粉|B. 一袋面粉有多重|C. 做所有蛋糕需要的面粉总克数|D. 一个蛋糕需要的面粉克数
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 每个蛋糕需要200克面粉|B. 计划做5个蛋糕|C. 面粉是1公斤一袋卖的
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 总需求量 = 单个需求量 × 数量|B. 1公斤 = 1000克|C. 只需要A|D. A和B都需要
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 将单个蛋糕所需面粉乘以要做的数量|B. 先将1公斤换算成1000克|C. 用1000克除以200克|D. 将200克和5相加
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"面粉的包装规格（1公斤一袋）对于计算总共需要多少克面粉是无关信息，属于干扰项。如果问题是“需要买几袋”，这个信息才有用。"}

---

Problem_ID:: 212
Difficulty_Level:: 2
Problem_Text::
小明独自粉刷一面墙需要4小时。他的朋友小刚的工作效率和他完全相同。他们从早上8点开始一起工作。
如果他们两人一起粉刷这面墙，需要多长时间？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 他们开始工作的时间|B. 他们完成工作的时间|C. 他们完成工作需要花费的总时长|D. 小明的工作效率
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 一个人完成工作需要4小时|B. 有两个人一起工作|C. 他们的工作效率相同|D. 他们早上8点开始工作
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 工作总量 = 工作效率 × 工作时间|B. 两人合作时间 = 单人时间 ÷ 2|C. 合作效率 = 个人效率之和|D. B或C都可以推导出答案
Rule_Answer:: D
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 假设墙的面积为具体数值|B. 将单人所需时间除以合作人数|C. 用结束时间减去开始时间|D. 将4小时乘以2
Strategy_Answer:: B
Feedback_Column:: {"Extraction_D":"什么时候开始工作，对于计算“需要多长时间”这个时长是无关的，属于干扰项。"}

---

Problem_ID:: 213
Difficulty_Level:: 2
Problem_Text::
一个等腰三角形的一个顶角是100度。这个三角形的周长是25厘米。
请问它的一个底角是多少度？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 三角形的周长|B. 三角形的面积|C. 三角形一个底角的大小|D. 三角形一条边的长度
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 这是一个等腰三角形|B. 其中一个角是100度|C. 三角形的周长是25厘米
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 三角形内角和为180度|B. 等腰三角形两底角相等|C. A和B都需要|D. 三角形周长等于三边之和
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 用180度减去已知的100度|B. 用180度除以3|C. 用周长25厘米除以3|D. 判断100度是顶角还是底角
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"三角形的周长对于求解其内角大小是无关信息，属于干扰项。","Strategy_D":"等腰三角形中不可能有两个100度的角（因为100+100=200>180），所以100度一定是顶角，这一步是必要的逻辑判断。但计算的第一步是A。"}

---

Problem_ID:: 214
Difficulty_Level:: 2
Problem_Text::
电影院的成人票每张12元，儿童票每张8元。电影院共有200个座位。
一个家庭购买了2张成人票和3张儿童票。请问他们购买门票的总花费是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 买成人票的花费|B. 买儿童票的花费|C. 买所有票的总花费|D. 电影院的总座位数
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 成人票单价12元，买了2张|B. 儿童票单价8元，买了3张|C. 电影院有200个座位
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 各类总价 = 单价 × 数量|B. 最终总价 = 各类总价之和|C. A和B都需要|D. 购买数量 < 座位数
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 分别计算成人票的总价和儿童票的总价|B. 将所有票的单价相加|C. 将购买的票数相加|D. 用座位数乘以单价
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"电影院的座位总数对于计算一个家庭的购票花费是无关信息，属于干扰项。"}

---

Problem_ID:: 215
Difficulty_Level:: 2
Problem_Text::
一个长方体水箱长5米，宽2米，深3米。这个水箱是用钢板焊接而成的。
如果水箱里装了一半的水，请问水箱里水的体积是多少立方米？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 水箱的容积|B. 水箱的表面积|C. 水箱里水的体积|D. 水的深度
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 水箱的长、宽、深尺寸|B. 水箱装了一半的水|C. 水箱是用钢板做的
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 长方体体积 = 长 × 宽 × 高|B. 一半的体积 = 总体积 ÷ 2|C. A和B都需要|D. 钢板的密度
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出整个水箱的总容积|B. 先计算水箱的底面积|C. 先将水的深度算出来 (3米 ÷ 2)|D. 考虑钢板的厚度
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"水箱的制作材料对于计算水的体积是无关信息，属于干扰项。"}

---

Problem_ID:: 216
Difficulty_Level:: 2
Problem_Text::
一位店主以500元的总价购买了10把相同的椅子。他用一张1000元的支票支付了货款。
之后，他以每把70元的价格卖掉了全部10把椅子。请问他卖掉所有椅子赚了多少利润？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 销售总收入|B. 购买总成本|C. 总利润|D. 找回的钱
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 10把椅子的总成本是500元|B. 每把椅子的售价是70元|C. 店主卖掉了所有10把椅子|D. 店主用1000元的支票支付
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 总收入 = 单价 × 数量|B. 利润 = 总收入 - 总成本|C. A和B都需要|D. 成本 = 500元
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 计算卖掉10把椅子的总收入|B. 计算每把椅子的成本|C. 计算用1000元支付后找回多少钱|D. 将售价减去成本
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"店主用多大面额的支票支付货款，对于计算他最终的销售利润是无关信息，属于干扰项。"}

---

Problem_ID:: 217
Difficulty_Level:: 2
Problem_Text::
一个班有30名学生，男女生的比例是 2:3。他们的数学老师今年40岁。
请问这个班有多少名女生？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 班级的总人数|B. 男生的人数|C. 女生的人数|D. 老师的年龄
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 班级总人数是30人|B. 男女比例是2:3|C. 数学老师40岁
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 按比例分配时，先求出总份数|B. 每份的数量 = 总量 ÷ 总份数|C. 女生数量 = 女生所占份数 × 每份的数量|D. 以上都需要
Rule_Answer:: D
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 将比例的数字2和3相加，求出总份数|B. 用30除以2|C. 用30乘以3/2|D. 将30和40相加
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"老师的年龄与计算班级学生人数的构成无关，属于干扰项。"}

---

Problem_ID:: 218
Difficulty_Level:: 2
Problem_Text::
日出时，山区的气温为零下4摄氏度。到了中午12点，气温上升了10摄氏度。从中午到日落，气温又下降了6摄氏度。
当天的天气预报说，降水概率为20%。请问日落时的气温是多少摄氏度？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 中午时的气温|B. 日落时的气温|C. 全天的总温差|D. 降水概率
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 日出时气温-4℃|B. 中午比日出上升10℃|C. 日落比中午下降6℃|D. 降水概率20%
Extraction_Answer:: A|B|C
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 在数轴上，上升表示向右（加），下降表示向左（减）|B. 最终值 = 初始值 + 变化量1 + 变化量2|C. A和B都需要|D. 20% < 100%
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先计算出中午时的气温|B. 直接用-4减去6|C. 将所有温度数值相加|D. 忽略负号进行计算
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"降水概率是天气信息，但与计算具体的温度数值无关，属于干扰项。"}

---

Problem_ID:: 219
Difficulty_Level:: 2
Problem_Text::
公交车时刻表显示，B路车在上午9:15从总站发车。从总站到市中心图书馆的行程需要25分钟。
每辆B路公交车上都有40个座位。如果你乘坐这班车，你将在什么时间到达市中心图书馆？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. B路车的发车时间|B. 行程需要的时间|C. 到达市中心图书馆的时间|D. 公交车的座位数
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. 发车时间是9:15|B. 行程用时25分钟|C. 公交车有40个座位
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 到达时间 = 出发时间 + 行程用时|B. 1小时 = 60分钟|C. A和B都需要|D. 40 > 1
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 将出发时间的小时和分钟数与行程的分钟数相加|B. 确认公交车是否有空座|C. 了解总站和图书馆的位置|D. 将9:15减去25分钟
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"公交车的座位数量对于计算单次行程的到达时间是无关信息，属于干扰项。"}

---

Problem_ID:: 220
Difficulty_Level:: 2
Problem_Text::
A商店的500克装麦片售价为4元。B商店的800克装同品牌麦片售价为6.4元。
A商店的麦片包装盒上有8份建议食用份量的标识。请问B商店的麦片每100克比A商店便宜多少元？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. A商店每100克的价格|B. B商店每100克的价格|C. 两家商店每100克的价格差|D. A商店麦片的建议食用份量
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的？
Extraction_Options:: A. A商店: 500克卖4元|B. B商店: 800克卖6.4元|C. A商店麦片有8份建议食用份量
Extraction_Answer:: A|B
Rule_Question:: 要解决这个问题，必须利用到的核心数学关系是什么？
Rule_Options:: A. 单价 = 总价 ÷ 数量|B. 价格差 = 价格1 - 价格2|C. A和B都需要|D. 800克 > 500克
Rule_Answer:: C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 分别计算出两家商店每100克麦片的价格|B. 比较两家的总价格|C. 计算两家每克的差价|D. 计算每份麦片多少克
Strategy_Answer:: A
Feedback_Column:: {"Extraction_C":"包装上的建议食用份量对于计算单位重量的价格是无关信息，属于干扰项。"}
