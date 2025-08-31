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