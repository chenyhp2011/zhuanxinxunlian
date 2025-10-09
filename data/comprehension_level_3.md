Problem_ID:: 301
Difficulty_Level:: 3
Problem_Text::
一项工程，如果由甲队单独施工，需要`30`天完成；如果由乙队单独施工，需要`20`天完成。
现在，两队合作施工，但在工程完成的前`5`天，乙队被调走，由甲队单独完成剩余工作。
请问，这项工程总共耗时多少天？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 甲队的工作效率|B. 两队合作了多少天|C. 完成工程所需的总天数|D. 乙队单独工作了多少天
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 甲队的效率是每天`1/30`|B. 乙队的效率是每天`1/20`|C. 甲队最后单独工作了`5`天|D. 两队合作期间的效率是`(1/30 + 1/20)`
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 可以将抽象的“总工程量”看作一个具体的单位“1”|B. (合作天数 × 合作效率) + (甲单独天数 × 甲效率) = 1|C. 合作效率 = 甲效率 + 乙效率|D. 总天数 = 合作天数 + 甲单独工作天数
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最有效的策略是什么？
Strategy_Options:: A. 设总天数为`x`天，列出方程 `(x-5)×(1/30+1/20) + 5×(1/30) = 1` 并求解|B. 先计算出甲队最后5天完成的工作量，再计算剩余工作量需要两队合作多少天，最后将天数相加|C. 假设工程总量为`60`个单位（20和30的最小公倍数）进行计算|D. 简单地用平均工时 `(20+30)/2` 来估算
Strategy_Answer:: B
Feedback_Column:: {"Extraction_C":"题目描述‘完成前5天乙队被调走’，这是一个关键的隐含叙述，意味着最后5天是甲队单独工作。","Rule_A":"将总工程量设为单位‘1’，是解决所有工程问题的基础和核心思想，它将具体问题抽象化为数学模型。","Strategy_A":"这个方程的逻辑是正确的，但对于解题步骤而言，策略B（先算部分，再算整体）的思路更清晰，不易出错。策略C也是一种非常有效的技巧。"}

---
Problem_ID:: 302
Difficulty_Level:: 3
Problem_Text::
一个商店购进了一批成本为每件`100`元的商品，并以期望`20%`利润率的价格作为标价。
在销售了`80%`的商品后，店主为了清仓，将剩余的商品打`5`折出售。
请问，该商店售完这批商品后的实际总利润率是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 商品的标价|B. 剩余商品的售价|C. 这批商品的总销售额|D. 整批商品的最终利润率
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 成本是100元/件|B. 标价是`100 × (1+20%) = 120`元|C. `80%`的商品按标价出售|D. 剩余`20%`的商品按标价的`5`折出售
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. `利润率 = (总售价 - 总成本) ÷ 总成本`|B. “打5折”意味着售价是标价的`50%`|C. 总成本和总售价的计算必须基于商品的总量|D. 必须加权计算两个阶段的销售额
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最有效的策略是什么？
Strategy_Options:: A. 直接用 `(20% - 50%) ÷ 2` 计算平均利润率|B. 假设总共有`100`件商品，分别计算两个阶段的销售额，再求总利润率|C. 只计算一件商品的平均售价来估算利润率|D. 假设所有商品都打折出售
Strategy_Answer:: B
Feedback_Column:: {"Goal_C":"总销售额是计算最终利润率的必要中间步骤，但不是最终要求解的目标。","Rule_A":"这是利润率的核心定义，必须清楚最终利润率是基于‘总成本’计算的，而非部分成本或销售额。","Strategy_A":"不同销售阶段的商品数量不同（80% vs 20%），不能简单地对利润率或折扣率取算术平均，必须考虑数量的权重。","Strategy_B":"对于涉及百分比和比例的问题，‘假设一个具体的总数’（如100）是一种非常强大且能简化问题的策略。"}

---
Problem_ID:: 303
Difficulty_Level:: 3
Problem_Text::
在一个有`40`道题的考试中，答对一题得`5`分，不答得`0`分，答错一题倒扣`3`分。
小张回答了所有的题目，最终得分为`88`分。
请问小张答对了多少道题？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 小张答错了多少题|B. 小张答对了多少题|C. 小张的总得分|D. 如果全答对能得多少分
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 总共有40道题|B. 答对得5分，答错扣3分|C. 小张回答了所有题目|D. 小张的总分是88分
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. `答对题数 + 答错题数 = 40`|B. `(答对题数 × 5) - (答错题数 × 3) = 88`|C. 这是一个典型的“鸡兔同笼”问题的变体|D. 答错题的扣分效应是总分减少`5 - (-3) = 8`分
Rule_Answer:: A|B|C
Strategy_Question:: 要解出此题，最有效的策略是什么？
Strategy_Options:: A. 从40题开始，一题一题地尝试，直到分数等于88|B. 设答对`x`题，答错`y`题，联立方程组求解|C. 假设全部答对，看总分与实际得分的差距，再用分数差除以每错一题的影响分数|D. 设答对`x`题，则答错`(40-x)`题，建立一元一次方程求解
Strategy_Answer:: D
Feedback_Column:: {"Rule_D":"这个关系是‘假设法’（策略C）的核心，即每将一个‘对’换成‘错’，总分会减少8分。","Strategy_B":"联立二元一次方程组是完全正确的，但将其中一个方程代入另一个，就转化为了策略D的一元一次方程，后者步骤更直接。","Strategy_C":"假设法非常巧妙：` (40×5 - 88) / (5 - (-3)) ` 即可算出答错题数。`(200 - 88) / 8 = 112 / 8 = 14`题答错，所以`40-14=26`题答对。"}

---
Problem_ID:: 304
Difficulty_Level:: 3
Problem_Text::
一个容器中装有浓度为`10%`的盐水`500`克。
首先，倒出了`100`克盐水，然后又加入了`100`克纯水。
请问此时容器中盐水的浓度是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 倒出的盐水中含多少盐|B. 加入了多少水|C. 容器中盐的总量变化|D. 容器中最终的盐水浓度
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 初始盐水500克，浓度10%|B. 倒出了100克溶液|C. 加入了100克纯水（溶质为0）|D. 最终溶液的总质量仍然是500克
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. `溶质质量 = 溶液质量 × 浓度`|B. 倒出的溶液，其浓度与原溶液相同|C. 最终浓度 = `最终溶质质量 ÷ 最终溶液总质量`|D. 倒出溶液会使溶质减少，加入纯水不会增加溶质
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 先计算出初始时盐的总质量，再计算倒出的100克盐水带走了多少盐，从而得到剩余的盐量，最后除以最终总质量|B. 简单地认为浓度不变，因为总质量没变|C. 用初始浓度减去一个估算值|D. 假设最终浓度为x，建立方程求解
Strategy_Answer:: A
Feedback_Column:: {"Extraction_D":"这是一个关键的隐含推断：`500 - 100 + 100 = 500`克，总质量不变，但成分已发生改变。","Rule_B":"这是一个核心概念，均匀溶液中任何一部分的浓度都和整体相同。","Strategy_B":"这是一个非常具有迷惑性的错误想法。虽然总质量不变，但溶质（盐）的质量减少了，所以浓度必然降低。"}

---
Problem_ID:: 305
Difficulty_Level:: 3
Problem_Text::
甲、乙两车同时从相距`420`公里的A、B两地出发，相向而行。`3`小时后，两车在途中相遇。
已知甲车的速度是乙车速度的`1.5`倍。
请问甲车比乙车每小时多行驶多少公里？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 甲车的速度|B. 乙车的速度|C. 甲乙两车的速度和|D. 甲乙两车的速度差
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 总路程420公里|B. 两车同时出发，相向而行|C. 相遇时间是3小时|D. `速度_甲 = 1.5 × 速度_乙`
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 相遇问题中，`(速度_甲 + 速度_乙) × 相遇时间 = 总路程`|B. 两车同时出发到相遇，所用时间相等|C. 速度差 = `速度_甲 - 速度_乙`|D. `速度_甲 + 速度_乙 = 420 ÷ 3`
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最有效的策略是什么？
Strategy_Options:: A. 先根据相遇公式计算出甲乙两车的速度之和，再结合两车速度的倍数关系，解出各自的速度，最后求差|B. 猜测乙车的速度，然后计算甲车速度是否满足条件|C. 设甲车的速度为`x`，乙车的速度为`y`，建立二元一次方程组求解|D. 仅通过速度倍数关系来估算
Strategy_Answer:: A
Feedback_Column:: {"Goal_C":"速度和是解题的第一个关键中间步骤，但题目最终问的是速度‘差’。","Rule_B":"‘同时出发并相遇’是本题最重要的隐含条件，它确保了时间变量是相同的，从而可以利用路程和与速度和的关系。","Strategy_C":"建立二元一次方程组是可行的，但策略A的思路更直接：先求出`x+y`这个整体的值，再结合`x=1.5y`来求解，计算上更简便。"}

---

Problem_ID:: 306
Difficulty_Level:: 3
Problem_Text::
一个项目，甲工程队单独做需要20天完成。甲队先单独工作了5天后，乙工程队加入，两个队一起合作了6天，正好完成了剩余的工程。
请问，如果让乙工程队单独完成整个项目，需要多少天？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 乙队的工作效率|B. 乙队单独完成项目所需的天数|C. 两队合作完成项目所需的天数|D. 甲队完成了多少比例的工程
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 甲队单独完成需要20天|B. 甲队先工作了5天|C. 甲乙两队合作了6天完成了剩余部分|D. 项目最终被完成了
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 可以将整个项目的工作总量看作单位“1”|B. 甲队的工作效率是每天 1/20|C. (甲队效率 + 乙队效率) × 合作天数 = 合作完成的工作量|D. 甲队先完成的部分 + 两队合作完成的部分 = 1
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 先算出甲队5天完成了多少工作量，进而得到剩余工作量，然后根据合作情况建立关于乙队效率的方程|B. 假设乙队和甲队效率一样|C. 猜测一个乙队的天数再代入验算|D. 先计算甲乙合作的效率
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"将抽象的“工程”量化为具体的数字“1”，是解决此类工程问题的关键隐含前提。","Strategy_D":"无法直接计算出合作效率，因为乙队的效率是未知的，这也是最终要求解的目标。"}

---

Problem_ID:: 307
Difficulty_Level:: 3
Problem_Text::
一位商人进了一批服装，他以25%的利润率卖掉了其中的40%。剩下的服装，他以10%的亏损率全部卖掉。
交易完成后，他总共获利160元。请问这批服装的总成本是多少元？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 销售这批服装的总收入|B. 第一次销售的利润|C. 第二次销售的亏损|D. 这批服装的总成本
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 40%的服装以25%的利润率售出|B. 剩下的60%的服装以10%的亏损率售出|C. 最终总利润为160元
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 利润和亏损的计算基准都是相应部分服装的成本|B. 总利润 = 第一部分利润 - 第二部分亏损|C. “剩下的服装”是指总量的 1−40%=60%|D. 利润 = 售价 - 成本
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 假设总成本为x，用x表示出两部分的利润和亏损，然后建立总利润方程|B. 假设总共有100件衣服|C. 先计算25%和10%的平均值|D. 计算总收入
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"这是一个核心的隐含条件，如果把利润率或亏损率的计算基准搞错（例如误用总成本或售价），将导致完全错误的答案。"}

---

Problem_ID:: 308
Difficulty_Level:: 3
Problem_Text::
一位化学家有500毫升浓度为**20%**的酸性溶液。她希望能将溶液的浓度提高到50%。
为了达到这个目标，她需要加入多少毫升的纯酸？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 最终溶液的总容积|B. 原始溶液中纯酸的含量|C. 需要加入的纯酸的量|D. 最终溶液的浓度
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 原始溶液500ml，浓度20%|B. 目标浓度是50%|C. 加入物是纯酸
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 溶液中的溶质（酸）= 溶液总量 × 浓度|B. 加入的“纯酸”其自身的浓度应按100%计算|C. 混合后，总溶质 = 原始溶质 + 加入的溶质|D. 混合后，总溶液 = 原始溶液 + 加入的溶液
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 假设需要加入x毫升纯酸，根据“最终的酸量 ÷ 最终的溶液量 = 最终浓度”来建立方程|B. 计算原始溶液里有多少水|C. 假设最终溶液的总量为y|D. 用50%减去20%
Strategy_Answer:: A
Feedback_Column:: {"Rule_B":"“纯酸”浓度为100%是化学常识，也是本题的隐含条件，如果不能识别这一点，将无法正确计算加入的酸量。"}

---

Problem_ID:: 309
Difficulty_Level:: 3
Problem_Text::
一艘船从甲港顺流而下到达乙港，用了3小时。从乙港逆流返回甲港，则用了5小时。
已知水流的速度是每小时4公里。请问这艘船在静水中的速度是多少公里/小时？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 甲乙两港的距离|B. 船的顺流速度|C. 船的逆流速度|D. 船在静水中的速度
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 顺流时间3小时|B. 逆流时间5小时|C. 水速是4公里/小时
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 从甲到乙和从乙到甲的“路程”是相等的|B. 顺流速度 = 静水船速 + 水速|C. 逆流速度 = 静水船速 - 水速|D. 路程 = 速度 × 时间
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 假设静水船速为v，利用“顺流路程 = 逆流路程”建立关于v的方程并求解|B. 假设甲乙两港距离为d，用d表示出顺流和逆流的速度|C. 用5小时减去3小时，得到时间差|D. 先计算平均速度
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"“往返”意味着路程相等，这是本题最关键的隐含条件，是建立等式的基础。"}

---

Problem_ID:: 310
Difficulty_Level:: 3
Problem_Text::
一个长方形花园的周长是80米。其长度比其宽度的两倍还多4米。花园的正中央有一个圆形喷泉。
请问这个花园的面积是多少平方米？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 花园的周长|B. 花园的长度|C. 花园的宽度|D. 花园的面积
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 花园周长80米|B. 长度 = 2 × 宽度 + 4米|C. 花园里有喷泉
Extraction_Answer:: A|B
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 长方形周长 = 2 × (长 + 宽)|B. 长方形面积 = 长 × 宽|C. 题目中关于喷泉的信息与求解面积无关
Rule_Answer:: A|B|C
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 设宽度为w，利用周长信息建立关于w的一元一次方程并求解|B. 先计算出长和宽的和是40米|C. 假设这是一个正方形|D. 计算喷泉的面积
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"周长公式是解决所有周长问题的基础，属于必须掌握的常识性条件。","Extraction_C":"喷泉信息是干扰项，对解题没有帮助。"}

---

Problem_ID:: 311
Difficulty_Level:: 3
Problem_Text::
一个农场里只养了鸡和兔子。从上面数，一共有35个头；从下面数，一共有94条腿。
请问农场里有多少只兔子？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 鸡的数量|B. 兔子的数量|C. 鸡和兔子数量的总和|D. 腿和头的总和
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 动物总数是35只|B. 腿的总数是94条|C. 农场里只有鸡和兔子两种动物
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 每只动物都只有1个头|B. 每只鸡有2条腿|C. 每只兔子有4条腿|D. 鸡的数量 + 兔子的数量 = 35
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 设立鸡和兔子数量两个未知数，根据头和腿的数量建立二元一次方程组并求解|B. 假设全部都是鸡，计算腿的数量，然后通过差值来替换兔子|C. A和B都是有效且常见的策略|D. 挨个尝试兔子的数量
Strategy_Answer:: C
Feedback_Column:: {"Rule_B":"“鸡有2条腿，兔子有4条腿”是解决此类问题的生物学常识，题目中不会明确给出，是必须利用的隐含条件。"}

---

Problem_ID:: 312
Difficulty_Level:: 3
Problem_Text::
某股票的价格在一月份上涨了20%。到了二月份，价格又下跌了20%。
如果该股票的初始价格为100元，请问二月底时该股票的最终价格是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 股票价格的总变化率|B. 一月份结束时的价格|C. 二月份结束时的价格|D. 股票的初始价格
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 初始价格100元|B. 一月份上涨20%|C. 二月份下跌20%
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 百分比的变化总是基于一个“基准值”|B. 第二次价格变化（二月份）的基准值是第一次变化后（一月底）的价格|C. 上涨20%后变为原来的1.2倍，下跌20%后变为原来的0.8倍|D. 两次变化的基准值是不同的
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 依次计算，先算出一月底的价格，再以此为基础计算二月底的价格|B. 认为上涨20%和下跌20%相互抵消，价格不变|C. 将两个百分比相加减|D. 将两个百分比相乘
Strategy_Answer:: A
Feedback_Column:: {"Rule_B":"这是一个极易出错的地方，也是本题的核心考点。第二次变化的基准（分母）不再是初始价格，而是变化后的新价格。这个隐含的逻辑关系必须被识别。"}

---

Problem_ID:: 313
Difficulty_Level:: 3
Problem_Text::
一开始，爱丽丝和鲍勃的钱数之比是 5:3。后来爱丽丝给了鲍勃20元，他们俩的钱数就变得一样多了。
请问爱丽丝一开始有多少钱？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 鲍勃一开始有多少钱|B. 爱丽丝一开始有多少钱|C. 他们两人总共有多少钱|D. 爱丽丝后来有多少钱
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 初始钱数比为5:3|B. 爱丽丝给了鲍勃20元|C. 最终两人钱数相等
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 两人钱数相等，意味着新的比例是1:1|B. 在传递过程中，两个人的总钱数保持不变|C. 可以设初始钱数为5x和3x|D. 爱丽丝的钱数变化为-20，鲍勃的钱数变化为+20
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 设初始钱数为5x和3x，根据变化后的相等关系建立方程 5x−20=3x+20|B. 假设爱丽丝最初有50元进行尝试|C. 从选项反向代入验证|D. 计算出爱丽丝比鲍勃多出来的钱是两份，这两份钱的一半给了鲍勃
Strategy_Answer:: A
Feedback_Column:: {"Rule_B":"总钱数守恒是这类交易问题的核心隐含条件，它保证了我们的方程能够平衡。"}

---

Problem_ID:: 314
Difficulty_Level:: 3
Problem_Text::
一个人将总共10000元的资金投入到A和B两个理财账户中。A账户的年化简单利率是5%，B账户的年化简单利率是7%。
一年后，他从两个账户总共获得了620元的利息。请问他在A账户中投入了多少资金？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 在B账户的投资额|B. 在A账户的投资额|C. A账户获得的利息|D. B账户获得的利息
Goal_Answer:: B
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 总投资额10000元|B. A账户利率5%，B账户利率7%|C. 总利息620元|D. 投资时间为一年
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 简单利息 = 本金 × 利率 × 时间|B. A账户的本金 + B账户的本金 = 10000元|C. A账户的利息 + B账户的利息 = 620元
Rule_Answer:: A|B|C
Strategy_Question:: 要解出此题，最关键的步骤是什么？
Strategy_Options:: A. 设A账户投资额为x，则B账户为(10000-x)，根据总利息建立关于x的方程|B. 计算一个平均利率|C. 假设在A和B中各投5000元|D. 用总利息除以总本金
Strategy_Answer:: A
Feedback_Column:: {"Rule_B":"两个账户本金之和为总投资额，这个关系是建立一元一次方程的基础，是题目中间接给出的隐含条件。"}

---

Problem_ID:: 315
Difficulty_Level:: 3
Problem_Text::
一个三位数，它的百位数字是它个位数字的两倍，它的十位数字比百位数字小3。
如果这个三位数的各位数字之和为17，请问这个三位数是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 各位数字之和|B. 个位数字|C. 十位数字|D. 这个三位数本身
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 百位 = 2 × 个位|B. 十位 = 百位 - 3|C. 百位 + 十位 + 个位 = 17|D. 这是一个三位数
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 数字的值与其所在的位置（place value）有关|B. 各位上的数字都必须是0到9的整数|C. 可以将所有未知数用一个未知数（例如个位u）来表示
Rule_Answer:: B|C
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 设个位为u，将百位和十位都用u的表达式代替，代入数字和为17的等式中求解|B. 从100到999逐个数字尝试|C. 假设百位是8，进行推算|D. 将17分成三份
Strategy_Answer:: A
Feedback_Column:: {"Rule_B":"数字是0-9的整数是一个基础常识，这个隐含条件可以用来验证解的合理性（例如，如果解出个位是4.5，则说明计算错误）。"}

---

Problem_ID:: 316
Difficulty_Level:: 3
Problem_Text::
一名骑行者在上午9:00以每小时15公里的恒定速度离开小镇。上午10:00，一名摩托车手以每小时40公里的速度从同一个小镇出发，沿同一条路追赶骑行者。
请问摩托车手在什么时间能追上骑行者？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 摩托车手需要多长时间追上|B. 骑行者行驶了多远|C. 摩托车手追上骑行者的具体时间点|D. 两者的速度差
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 骑行者9点出发，速度15km/h|B. 摩托车手10点出发，速度40km/h|C. 骑行者比摩托车手早出发1小时
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 当摩托车手追上骑行者时，他们行驶的“路程”是相等的|B. 骑行者行驶的时间比摩托车手多1小时|C. 路程 = 速度 × 时间|D. 追及时间 = 路程差 ÷ 速度差
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 设摩托车手行驶时间为t，根据“路程相等”建立方程 40t=15(t+1)|B. 先计算出10点时，骑行者领先的距离，然后用“追及问题”公式求解|C. A和B都是解决此问题的核心策略|D. 猜测一个追上的时间
Strategy_Answer:: C
Feedback_Column:: {"Rule_A":"“追上”的数学含义就是两者从起点出发的位移（路程）相等，这是解决所有追及问题的关键隐含条件。"}

---

Problem_ID:: 317
Difficulty_Level:: 3
Problem_Text::
一块长方形土地需要用栅栏围起来。这块土地的长度比其宽度的两倍少5米。
以每米10元的价格计算，整个栅栏的总造价为2000元。请问这块土地的面积是多少平方米？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 土地的周长|B. 土地的宽度|C. 土地的长度|D. 土地的面积
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 长度 = 2 × 宽度 - 5|B. 栅栏单价10元/米|C. 栅栏总价2000元
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 围起来的“栅栏”总长度就是长方形的“周长”|B. 周长 = 总造价 ÷ 单价|C. 周长 = 2 × (长 + 宽)|D. 面积 = 长 × 宽
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最关键的第一步是什么？
Strategy_Options:: A. 先根据总造价和单价计算出土地的周长|B. 设宽度为w，然后建立关于面积的方程|C. 猜测土地的尺寸|D. 用总造价除以2
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"必须能将实际问题（造栅栏）转化为数学模型（求周长），这个转化是本题的隐含要求。"}

---

Problem_ID:: 318
Difficulty_Level:: 3
Problem_Text::
一个30人的班级，某次考试的平均分是80分。后来老师复查时发现，有两名学生的成绩被记错了：甲同学的80分被误记为50分，乙同学的70分被误记为60分。
请问，修正错误后，这个班的正确平均分是多少？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 错误的考试总分|B. 正确的考试总分|C. 成绩被记错的学生人数|D. 班级正确的平均分
Goal_Answer:: D
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 班级人数30人|B. 错误的平均分是80分|C. 甲同学成绩：错误50，正确80|D. 乙同学成绩：错误60，正确70
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 平均分 = 总分 ÷ 总人数|B. 要修正平均分，必须先修正总分|C. 修正总分 = 原始总分 - 错误分数 + 正确分数
Rule_Answer:: A|B|C
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 先用错误平均分乘以人数得到错误总分，然后修正总分，最后除以人数得到正确平均分|B. 计算出总的误差分数，求出平均分的误差，然后修正原平均分|C. A和B都是可行的正确策略|D. 重新计算30个学生的平均分
Strategy_Answer:: C
Feedback_Column:: {"Rule_A":"平均分、总分、人数三者的关系是解决此类问题的基础，是隐含的公式条件。"}

---

Problem_ID:: 319
Difficulty_Level:: 3
Problem_Text::
如果6名工人10个月可以建造2栋同样的房子。
那么，请问9名工人建造3栋同样的房子需要多少个月？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 每栋房子需要多少工人|B. 每个工人每个月能完成多少工作|C. 9名工人建3栋房子需要的时间|D. 总共需要多少工作量
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 6个工人10个月建2栋房子|B. 目标是9个工人建3栋房子|C. 所有工人的效率相同，所有房子都一样
Extraction_Answer:: A|B|C
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. 可以用“人·月”来作为一个衡量工作总量的单位|B. 总工作量 = 工人数 × 时间|C. 每栋房子的工作量是恒定的|D. 完成一定工作量所需的时间与工人数成反比
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 先计算出建造一栋房子需要多少“人·月”的工作量，再计算3栋房子的总工作量，最后除以新的工人数|B. 假设一个工人一个月能完成的工作量为w|C. 设需要的时间为x，建立比例式|D. 猜测一个时间
Strategy_Answer:: A
Feedback_Column:: {"Rule_A":"“人·月”或“工时”是解决工程量问题的核心概念，是一种将工作、效率、时间统一起来的度量，是解决此类问题的隐含工具。"}

---

Problem_ID:: 320
Difficulty_Level:: 3
Problem_Text::
一件商品在会员日为持卡会员提供九折优惠。在国庆节期间，商场又在会员价的基础上再提供八折优惠。
一位会员在国庆节期间购买这件商品，最终支付了144元。请问这件商品的原始标价是多少元？
Goal_Question:: 这道题最终要求解的是什么？
Goal_Options:: A. 最终支付的金额|B. 会员价是多少|C. 商品的原始标价|D. 总共的折扣是多少
Goal_Answer:: C
Extraction_Question:: 根据题目，以下哪些信息是已知的或可以推断的？
Extraction_Options:: A. 第一次折扣是10% (九折)|B. 第二次折扣是20% (八折)|C. 最终支付144元|D. 第二次折扣是在第一次折扣后的价格基础上计算的
Extraction_Answer:: A|B|C|D
Rule_Question:: 解决此题，必须识别并利用哪些核心关系或隐含条件？
Rule_Options:: A. “在...基础上再...”意味着连续折扣，而非折扣的叠加|B. 九折意味着价格变为原价的90% (0.9倍)|C. 八折意味着价格变为当前价格的80% (0.8倍)|D. 原始标价 = 最终价格 ÷ (折扣率1 × 折扣率2)
Rule_Answer:: A|B|C|D
Strategy_Question:: 要解出此题，最优的策略是什么？
Strategy_Options:: A. 设原始标价为P，建立方程 P×0.9×0.8=144 并求解|B. 从最终价格144元出发，反向计算，即先除以0.8，再除以0.9|C. A和B的思路本质相同，都是正确的|D. 将两个折扣相加，认为总共打了七折
Strategy_Answer:: C
Feedback_Column:: {"Rule_A":"连续折扣的计算基准是变化后的价格，这是一个关键的隐含规则。如果错误地将折扣率相加（10%+20%=30%），会得出错误答案。"}
