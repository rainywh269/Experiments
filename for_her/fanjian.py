#coding:utf8
#author:ne.manman@gmail.com
#说明：
#    简繁体互换包
#    简体=>繁体 JtoF(str)
#    繁体=>简体 FtoJ(str)
#    传入的字符串(str)必须为utf8编码
#    已去掉了简繁体相同的字，减少字典大小


zh_dict={
'还':'還',
'气':'氣',
'铺':'鋪',
'锌':'鋅',
'谰':'讕',
'锋':'鋒',
'锈':'鏽',
'铲':'鏟',
'锄':'鋤',
'锅':'鍋',
'银':'銀',
'销':'銷',
'锁':'鎖',
'铸':'鑄',
'锚':'錨',
'铭':'銘',
'错':'錯',
'铣':'銑',
'锗':'鍺',
'铡':'鍘',
'谴':'譴',
'圆':'圓',
'锐':'銳',
'锑':'銻',
'键':'鍵',
'锯':'鋸',
'歼':'殲',
'锭':'錠',
'衬':'襯',
'麦':'麥',
'铜':'銅',
'锦':'錦',
'残':'殘',
'锤':'錘',
'锥':'錐',
'锣':'鑼',
'瘪':'癟',
'锡':'錫',
'双':'雙',
'卖':'賣',
'锻':'鍛',
'锹':'鍬',
'铃':'鈴',
'圣':'聖',
'铁':'鐵',
'药':'藥',
'誉':'譽',
'铱':'銥',
'锰':'錳',
'誊':'謄',
'聪':'聰',
'铰':'鉸',
'动':'動',
'捻':'撚',
'写':'寫',
'争':'爭',
'饮':'飲',
'衅':'釁',
'务':'務',
'亏':'虧',
'于':'於',
'云':'雲',
'赖':'賴',
'蜕':'蛻',
'势':'勢',
'隶':'隸',
'卜':'蔔',
'诀':'訣',
'农':'農',
'亚':'亞',
'换':'換',
'捣':'搗',
'劲':'勁',
'捡':'撿',
'捞':'撈',
'损':'損',
'聋':'聾',
'职':'職',
'当':'當',
'产':'產',
'线':'線',
'亩':'畝',
'聂':'聶',
'获':'獲',
'随':'隨',
'检':'檢',
'劝':'勸',
'办':'辦',
'亲':'親',
'讨':'討',
'骤':'驟',
'窥':'窺',
'联':'聯',
'讫':'訖',
'亿':'億',
'飞':'飛',
'强':'強',
'现':'現',
'洒':'灑',
'踊':'踴',
'铬':'鉻',
'赐':'賜',
'踌':'躊',
'洁':'潔',
'纶':'綸',
'弯':'彎',
'项':'項',
'张':'張',
'议':'議',
'鸭':'鴨',
'环':'環',
'鲤':'鯉',
'冈':'岡',
'确':'確',
'踪':'蹤',
'娱':'娛',
'洼':'窪',
'桥':'橋',
'坝':'壩',
'讲':'講',
'愿':'願',
'异':'異',
'弃':'棄',
'开':'開',
'瓮':'甕',
'坟':'墳',
'闲':'閑',
'场':'場',
'啮':'齧',
'鳞':'鱗',
'协':'協',
'壮':'壯',
'讶':'訝',
'鳖':'鼈',
'牺':'犧',
'壶':'壺',
'舰':'艦',
'壳':'殼',
'啸':'嘯',
'声':'聲',
'柜':'櫃',
'珐':'琺',
'众':'眾',
'启':'啓',
'支':'隻',
'灿':'燦',
'灾':'災',
'攒':'攢',
'柠':'檸',
'锨':'鍁',
'绸':'綢',
'婴':'嬰',
'灶':'竈',
'系':'係',
'军':'軍',
'与':'與',
'讼':'訟',
'灯':'燈',
'灭':'滅',
'萨':'薩',
'葱':'蔥',
'腊':'臘',
'泻':'瀉',
'设':'設',
'骚':'騷',
'矿':'礦',
'矾':'礬',
'焕':'煥',
'龋':'齲',
'龄':'齡',
'视':'視',
'内':'內',
'补':'補',
'妈':'媽',
'狞':'獰',
'龟':'龜',
'龙':'龍',
'龚':'龔',
'嘱':'囑',
'瘫':'癱',
'坏':'壞',
'妆':'妝',
'妇':'婦',
'摊':'攤',
'摈':'擯',
'莲':'蓮',
'绵':'綿',
'属':'屬',
'摆':'擺',
'摇':'搖',
'摄':'攝',
'维':'維',
'厨':'廚',
'茧':'繭',
'馒':'饅',
'绷':'繃',
'芜':'蕪',
'愤':'憤',
'抡':'掄',
'嘘':'噓',
'苹':'蘋',
'冻':'凍',
'疮':'瘡',
'疯':'瘋',
'冲':'沖',
'疡':'瘍',
'况':'況',
'腻':'膩',
'俩':'倆',
'盘':'盤',
'冯':'馮',
'绍':'紹',
'践':'踐',
'孙':'孫',
'樱':'櫻',
'计':'計',
'屉':'屜',
'讣':'訃',
'学':'學',
'讥':'譏',
'认':'認',
'槛':'檻',
'闯':'闖',
'问':'問',
'闭':'閉',
'绎':'繹',
'训':'訓',
'闪':'閃',
'讯':'訊',
'门':'門',
'闷':'悶',
'记':'記',
'讳':'諱',
'间':'間',
'册':'冊',
'疟':'瘧',
'闰':'閏',
'讹':'訛',
'许':'許',
'闽':'閩',
'论':'論',
'闻':'聞',
'闺':'閨',
'闹':'鬧',
'闸':'閘',
'欲':'慾',
'狰':'猙',
'犹':'猶',
'状':'狀',
'渔':'漁',
'渗':'滲',
'节':'節',
'礼':'禮',
'渐':'漸',
'报':'報',
'护':'護',
'筛':'篩',
'孪':'孿',
'华':'華',
'渊':'淵',
'筑':'築',
'层':'層',
'游':'遊',
'屿':'嶼',
'赏':'賞',
'祷':'禱',
'抚':'撫',
'筹':'籌',
'芦':'蘆',
'犊':'犢',
'签':'簽',
'须':'須',
'顺':'順',
'屡':'屢',
'顷':'頃',
'窜':'竄',
'烫':'燙',
'络':'絡',
'昼':'晝',
'汉':'漢',
'翘':'翹',
'獭':'獺',
'币':'幣',
'遥':'遙',
'郧':'鄖',
'铝':'鋁',
'伟':'偉',
'汇':'彙',
'师':'師',
'烬':'燼',
'忧':'憂',
'帐':'帳',
'皋':'臯',
'惊':'驚',
'窑':'窯',
'蓟':'薊',
'帘':'簾',
'蓝':'藍',
'带':'帶',
'据':'據',
'呛':'嗆',
'卢':'盧',
'呜':'嗚',
'评':'評',
'帮':'幫',
'污':'汙',
'翱':'翺',
'汤':'湯',
'汹':'洶',
'忆':'憶',
'惧':'懼',
'惨':'慘',
'惩':'懲',
'遗':'遺',
'惫':'憊',
'惭':'慚',
'惮':'憚',
'惯':'慣',
'俭':'儉',
'鲜':'鮮',
'数':'數',
'沉':'沈',
'虫':'蟲',
'离':'離',
'衔':'銜',
'独':'獨',
'涌':'湧',
'鲍':'鮑',
'唤':'喚',
'鲁':'魯',
'沟':'溝',
'虽':'雖',
'虾':'蝦',
'鲸':'鯨',
'顽':'頑',
'没':'沒',
'札':'劄',
'韩':'韓',
'术':'術',
'沤':'漚',
'监':'監',
'沪':'滬',
'订':'訂',
'敛':'斂',
'励':'勵',
'虑':'慮',
'粤':'粵',
'机':'機',
'难':'難',
'怜':'憐',
'粮':'糧',
'温':'溫',
'虚':'虛',
'劳':'勞',
'粪':'糞',
'朴':'樸',
'鹅':'鵝',
'哗':'嘩',
'钻':'鑽',
'痈':'癰',
'盏':'盞',
'袄':'襖',
'鹏':'鵬',
'钳':'鉗',
'钵':'缽',
'鹊':'鵲',
'咏':'詠',
'袜':'襪',
'撵':'攆',
'钠':'鈉',
'钡':'鋇',
'钢':'鋼',
'痪':'瘓',
'钥':'鑰',
'钦':'欽',
'盖':'蓋',
'袭':'襲',
'鹤':'鶴',
'国':'國',
'顶':'頂',
'哑':'啞',
'钞':'鈔',
'钟':'鐘',
'钒':'釩',
'围':'圍',
'号':'號',
'听':'聽',
'囱':'囪',
'嚣':'囂',
'钉':'釘',
'撑':'撐',
'鹰':'鷹',
'钎':'釺',
'涛':'濤',
'皱':'皺',
'团':'團',
'掷':'擲',
'谚':'諺',
'砾':'礫',
'掳':'擄',
'侣':'侶',
'谜':'謎',
'谓':'謂',
'鸯':'鴦',
'谐':'諧',
'谗':'讒',
'掺':'摻',
'卫':'衛',
'掸':'撣',
'谋':'謀',
'谊':'誼',
'钙':'鈣',
'帅':'帥',
'畴':'疇',
'谎':'謊',
'谍':'諜',
'莹':'瑩',
'玛':'瑪',
'谁':'誰',
'馆':'館',
'谆':'諄',
'谅':'諒',
'赡':'贍',
'穷':'窮',
'隐':'隱',
'饺':'餃',
'抬':'擡',
'饼':'餅',
'饿':'餓',
'饱':'飽',
'饰':'飾',
'砖':'磚',
'饲':'飼',
'饵':'餌',
'枢':'樞',
'饶':'饒',
'单':'單',
'谩':'謾',
'谨':'謹',
'饭':'飯',
'饯':'餞',
'谬':'謬',
'谣':'謠',
'谢':'謝',
'运':'運',
'饥':'饑',
'码':'碼',
'谤':'謗',
'绩':'績',
'宠':'寵',
'牵':'牽',
'绪':'緒',
'续':'續',
'浓':'濃',
'酿':'釀',
'浑':'渾',
'酱':'醬',
'绣':'繡',
'绢':'絹',
'绥':'綏',
'蝎':'蠍',
'懒':'懶',
'绦':'縧',
'浆':'漿',
'浇':'澆',
'浅':'淺',
'绽':'綻',
'综':'綜',
'绿':'綠',
'暂':'暫',
'济':'濟',
'绰':'綽',
'绳':'繩',
'浊':'濁',
'测':'測',
'营':'營',
'萤':'螢',
'抢':'搶',
'终':'終',
'阳':'陽',
'绊':'絆',
'酝':'醞',
'涩':'澀',
'经':'經',
'让':'讓',
'练':'練',
'戏':'戲',
'绅':'紳',
'组':'組',
'织':'織',
'细':'細',
'给':'給',
'绘':'繪',
'绚':'絢',
'绝':'絕',
'烟':'煙',
'统':'統',
'绞':'絞',
'绑':'綁',
'结':'結',
'绒':'絨',
'绕':'繞',
'宪':'憲',
'蹿':'躥',
'赶':'趕',
'识':'識',
'猪':'豬',
'羡':'羨',
'构':'構',
'献':'獻',
'举':'舉',
'逻':'邏',
'吴':'吳',
'涂':'塗',
'吗':'嗎',
'枫':'楓',
'涟':'漣',
'御':'禦',
'涝':'澇',
'弹':'彈',
'态':'態',
'怀':'懷',
'吨':'噸',
'怂':'慫',
'抠':'摳',
'帜':'幟',
'递':'遞',
'适':'適',
'巩':'鞏',
'画':'畫',
'蝉':'蟬',
'丽':'麗',
'涨':'漲',
'涧':'澗',
'润':'潤',
'涤':'滌',
'涣':'渙',
'吓':'嚇',
'涡':'渦',
'蔷':'薔',
'员':'員',
'径':'徑',
'阴':'陰',
'页':'頁',
'逊':'遜',
'债':'債',
'选':'選',
'吁':'籲',
'爷':'爺',
'齐':'齊',
'断':'斷',
'词':'詞',
'萝':'蘿',
'斩':'斬',
'帧':'幀',
'辈':'輩',
'晋':'晉',
'纫':'紉',
'奖':'獎',
'专':'專',
'兰':'蘭',
'晒':'曬',
'晓':'曉',
'体':'體',
'诈':'詐',
'奋':'奮',
'晕':'暈',
'贫':'貧',
'阎':'閻',
'树':'樹',
'硷':'鹼',
'蔼':'藹',
'斋':'齋',
'医':'醫',
'横':'橫',
'齿':'齒',
'颁':'頒',
'赌':'賭',
'类':'類',
'宾':'賓',
'奥':'奧',
'爱':'愛',
'赎':'贖',
'毁':'毀',
'货':'貨',
'账':'賬',
'样':'樣',
'仅':'僅',
'责':'責',
'财':'財',
'时':'時',
'从':'從',
'贮':'貯',
'购':'購',
'贬':'貶',
'险':'險',
'贪':'貪',
'贩':'販',
'质':'質',
'贷':'貸',
'丧':'喪',
'肿':'腫',
'肾':'腎',
'剥':'剝',
'仓':'倉',
'剧':'劇',
'贰':'貳',
'贿':'賄',
'伪':'僞',
'贼':'賊',
'贺':'賀',
'费':'費',
'贸':'貿',
'剑':'劍',
'剐':'剮',
'陇':'隴',
'栖':'棲',
'旷':'曠',
'荚':'莢',
'畅':'暢',
'缅':'緬',
'会':'會',
'伙':'夥',
'优':'優',
'仪':'儀',
'陈':'陳',
'肃':'肅',
'顿':'頓',
'陕':'陝',
'价':'價',
'标':'標',
'剂':'劑',
'猎':'獵',
'厩':'廄',
'蜡':'蠟',
'灵':'靈',
'栏':'欄',
'弥':'彌',
'栈':'棧',
'栋':'棟',
'拨':'撥',
'择':'擇',
'笋':'筍',
'称':'稱',
'尘':'塵',
'呕':'嘔',
'尔':'爾',
'拣':'揀',
'拥':'擁',
'拦':'攔',
'拧':'擰',
'蜗':'蝸',
'沧':'滄',
'顾':'顧',
'苏':'蘇',
'苍':'蒼',
'将':'將',
'丛':'叢',
'积':'積',
'笔':'筆',
'湿':'濕',
'业':'業',
'转':'轉',
'轮':'輪',
'软':'軟',
'轨':'軌',
'轩':'軒',
'尸':'屍',
'过':'過',
'陨':'隕',
'吕':'呂',
'车':'車',
'轧':'軋',
'担':'擔',
'载':'載',
'笺':'箋',
'轿':'轎',
'笼':'籠',
'赚':'賺',
'秃':'禿',
'轻':'輕',
'种':'種',
'尧':'堯',
'赛':'賽',
'轰':'轟',
'馁':'餒',
'邹':'鄒',
'纯':'純',
'纬':'緯',
'瞩':'矚',
'纪':'紀',
'风':'風',
'箩':'籮',
'约':'約',
'级':'級',
'纤':'纖',
'红':'紅',
'纠':'糾',
'骡':'騾',
'总':'總',
'纽':'紐',
'纺':'紡',
'舆':'輿',
'纸':'紙',
'纹':'紋',
'溃':'潰',
'纷':'紛',
'纵':'縱',
'纲':'綱',
'纳':'納',
'溅':'濺',
'纱':'紗',
'骑':'騎',
'舱':'艙',
'废':'廢',
'庙':'廟',
'骗':'騙',
'应':'應',
'躯':'軀',
'庐':'廬',
'库':'庫',
'峦':'巒',
'骂':'罵',
'骄':'驕',
'扬':'揚',
'峡':'峽',
'骇':'駭',
'庄':'莊',
'诲':'誨',
'庆':'慶',
'骋':'騁',
'验':'驗',
'骏':'駿',
'罚':'罰',
'丑':'醜',
'垦':'墾',
'烧':'燒',
'烦':'煩',
'烩':'燴',
'网':'網',
'罗':'羅',
'权':'權',
'杀':'殺',
'万':'萬',
'郸':'鄲',
'庞':'龐',
'竖':'豎',
'泞':'濘',
'烁':'爍',
'鱼':'魚',
'烃':'烴',
'烂':'爛',
'蚁':'蟻',
'蚀':'蝕',
'杨':'楊',
'蚂':'螞',
'哟':'喲',
'泪':'淚',
'来':'來',
'坞':'塢',
'条':'條',
'蚕':'蠶',
'渍':'漬',
'铂':'鉑',
'罢':'罷',
'烛':'燭',
'骆':'駱',
'泼':'潑',
'泽':'澤',
'杰':'傑',
'后':'後',
'兽':'獸',
'毕':'畢',
'垒':'壘',
'诅':'詛',
'兹':'茲',
'为':'為',
'养':'養',
'证':'證',
'兴':'興',
'诌':'謅',
'临':'臨',
'诊':'診',
'毙':'斃',
'关':'關',
'诉':'訴',
'瞒':'瞞',
'诗':'詩',
'试':'試',
'垄':'壟',
'个':'個',
'译':'譯',
'诞':'誕',
'瑶':'瑤',
'严':'嚴',
'话':'話',
'诚':'誠',
'诛':'誅',
'详':'詳',
'诧':'詫',
'窝':'窩',
'该':'該',
'询':'詢',
'诣':'詣',
'党':'黨',
'静':'靜',
'误':'誤',
'诬':'誣',
'语':'語',
'兑':'兌',
'诫':'誡',
'额':'額',
'挤':'擠',
'请':'請',
'说':'說',
'诵':'誦',
'调':'調',
'毡':'氈',
'三':'叁',
'诱':'誘',
'课':'課',
'诽':'誹',
'诺':'諾',
'读':'讀',
'诸':'諸',
'钱':'錢',
'钝':'鈍',
'揽':'攬',
'头':'頭',
'斗':'鬥',
'跃':'躍',
'挝':'撾',
'税':'稅',
'沦':'淪',
'区':'區',
'潍':'濰',
'沥':'瀝',
'稳':'穩',
'匀':'勻',
'垫':'墊',
'椭':'橢',
'铆':'鉚',
'谭':'譚',
'潜':'潛',
'响':'響',
'猫':'貓',
'础':'礎',
'丰':'豐',
'辑':'輯',
'辐':'輻',
'输':'輸',
'叠':'疊',
'辕':'轅',
'辗':'輾',
'辖':'轄',
'辙':'轍',
'咨':'諮',
'铅':'鉛',
'败':'敗',
'崭':'嶄',
'辞':'辭',
'鳃':'鰓',
'较':'較',
'贤':'賢',
'辅':'輔',
'叶':'葉',
'辆':'輛',
'辉':'輝',
'刘':'劉',
'叹':'歎',
'虏':'虜',
'范':'範',
'篓':'簍',
'参':'參',
'篮':'籃',
'侨':'僑',
'贡':'貢',
'边':'邊',
'辽':'遼',
'达':'達',
'丢':'丟',
'贯':'貫',
'发':'發',
'战':'戰',
'诡':'詭',
'肤':'膚',
'辩':'辯',
'辫':'辮',
'变':'變',
'篱':'籬',
'禄':'祿',
'咸':'鹹',
'淀':'澱',
'彻':'徹',
'肠':'腸',
'热':'熱',
'恋':'戀',
'彦':'彥',
'访':'訪',
'钩':'鈎',
'郑':'鄭',
'敌':'敵',
'录':'錄',
'颓':'頹',
'萧':'蕭',
'恼':'惱',
'归':'歸',
'彝':'彜',
'恳':'懇',
'恶':'惡',
'贵':'貴',
'墙':'牆',
'蕴':'蘊',
'传':'傳',
'阅':'閱',
'里':'裡',
'释':'釋',
'讽':'諷',
'疗':'療',
'贱':'賤',
'滞':'滯',
'伤':'傷',
'颊':'頰',
'娇':'嬌',
'娄':'婁',
'岗':'崗',
'鸟':'鳥',
'装':'裝',
'对':'對',
'蛰':'蟄',
'霉':'黴',
'炽':'熾',
'鹃':'鵑',
'紧':'緊',
'鸣':'鳴',
'鸡':'雞',
'鸦':'鴉',
'鸥':'鷗',
'馋':'饞',
'鸿':'鴻',
'裤':'褲',
'鸽':'鴿',
'鸳':'鴛',
'睁':'睜',
'着':'著',
'擞':'擻',
'鸵':'鴕',
'继':'繼',
'际':'際',
'驾':'駕',
'胶':'膠',
'赠':'贈',
'赢':'贏',
'赣':'贛',
'预':'預',
'刽':'劊',
'你':'妳',
'赵':'趙',
'桨':'槳',
'佣':'傭',
'仑':'侖',
'领':'領',
'删':'刪',
'档':'檔',
'颇':'頗',
'阶':'階',
'别':'別',
'寝':'寢',
'阵':'陣',
'资':'資',
'钨':'鎢',
'谦':'謙',
'阉':'閹',
'划':'劃',
'赁':'賃',
'赂':'賂',
'赃':'贓',
'阂':'閡',
'阀':'閥',
'阁':'閣',
'刚':'剛',
'创':'創',
'胜':'勝',
'则':'則',
'赔':'賠',
'胀':'脹',
'胁':'脅',
'胆':'膽',
'队':'隊',
'偿':'償',
'寻':'尋',
'狭':'狹',
'赞':'讚',
'阑':'闌',
'寿':'壽',
'们':'們',
'阔':'闊',
'导':'導',
'钮':'鈕',
'竞':'競',
'储':'儲',
'狮':'獅',
'伞':'傘',
'耻':'恥',
'颐':'頤',
'耸':'聳',
'两':'兩',
'梦':'夢',
'频':'頻',
'挡':'擋',
'挠':'撓',
'挣':'掙',
'挥':'揮',
'雾':'霧',
'坛':'壇',
'栅':'柵',
'挛':'攣',
'挚':'摯',
'勋':'勳',
'显':'顯',
'挟':'挾',
'挞':'撻',
'雏':'雛',
'干':'乾',
'盗':'盜',
'荧':'熒',
'杂':'雜',
'楼':'樓',
'钧':'鈞',
'儿':'兒',
'坚':'堅',
'颈':'頸',
'驴':'驢',
'滚':'滾',
'驶':'駛',
'驱':'驅',
'驰':'馳',
'驳':'駁',
'图':'圖',
'狱':'獄',
'驼':'駝',
'颂':'頌',
'碍':'礙',
'驹':'駒',
'颅':'顱',
'驻':'駐',
'岛':'島',
'题':'題',
'负':'負',
'颜':'顔',
'岁':'歲',
'岂':'豈',
'贞':'貞',
'驭':'馭',
'马':'馬',
'驯':'馴',
'驮':'馱',
'链':'鏈',
'贝':'貝',
'颖':'穎',
'颗':'顆',
'艰':'艱',
'艳':'豔',
'岳':'嶽',
'颠':'顛',
'艺':'藝',
'岿':'巋',
'颤':'顫',
'颧':'顴',
'滨':'濱',
'滩':'灘',
'癣':'癬',
'蒋':'蔣',
'碱':'堿',
'祸':'禍',
'满':'滿',
'堑':'塹',
'滤':'濾',
'陆':'陸',
'滦':'灤',
'窍':'竅',
'钓':'釣',
'矫':'矯',
'极':'極',
'赘':'贅',
'旧':'舊',
'无':'無',
'堕':'墮',
'尝':'嘗',
'皑':'皚',
'览':'覽',
'觉':'覺',
'夺':'奪',
'澜':'瀾',
'规':'規',
'夹':'夾',
'观':'觀',
'户':'戶',
'见':'見',
'针':'針',
'辊':'輥',
'枣':'棗',
'备':'備',
'处':'處',
'狈':'狽',
'蝇':'蠅',
'茎':'莖',
'园':'園',
'复':'複',
'秽':'穢',
'义':'義',
'触':'觸',
'够':'夠',
'阐':'闡',
'块':'塊',
'镊':'鑷',
'镍':'鎳',
'黄':'黃',
'镁':'鎂',
'镀':'鍍',
'铀':'鈾',
'慑':'懾',
'买':'買',
'乱':'亂',
'镇':'鎮',
'秸':'稭',
'琼':'瓊',
'镜':'鏡',
'岭':'嶺',
'镑':'鎊',
'镐':'鎬',
'书':'書',
'习':'習',
'乡':'鄉',
'飘':'飄',
'镭':'鐳',
'拢':'攏',
'丝':'絲',
'乔':'喬',
'镣':'鐐',
'婶':'嬸',
'乐':'樂',
'桩':'樁',
'滥':'濫',
'乌':'烏',
'么':'麼',
'坠':'墜',
'长':'長',
'镰':'鐮',
'欢':'歡',
'琐':'瑣',
'欧':'歐',
'镶':'鑲',
'击':'擊',
'宁':'甯',
'凿':'鑿',
'东':'東',
'脱':'脫',
'卤':'鹵',
'韧':'韌',
'韦':'韋',
'卧':'臥',
'脸':'臉',
'侥':'僥',
'痴':'癡',
'侧':'側',
'侦':'偵',
'凯':'凱',
'侠':'俠',
'凭':'憑',
'伦':'倫',
'韵':'韻',
'几':'幾',
'侩':'儈',
'宝':'寶',
'实':'實',
'凤':'鳳',
'凛':'凜',
'审':'審',
'趋':'趨',
'橱':'櫥',
'脓':'膿',
'脑':'腦',
'脐':'臍',
'湾':'灣',
'凑':'湊',
'宫':'宮',
'痉':'痙',
'脚':'腳',
'苇':'葦',
'倾':'傾',
'凉':'涼',
'减':'減',
'凌':'淩',
'脏':'髒',
'净':'淨',
'宽':'寬',
'脉':'脈',
'凄':'淒',
'厢':'廂',
'扰':'擾',
'厦':'廈',
'连':'連',
'迟':'遲',
'挂':'掛',
'谈':'談',
'厍':'厙',
'锎':'鐦',
'馑':'饉',
'鲓':'鮳',
'徕':'徠',
'芗':'薌',
'钣':'鈑',
'嘤':'嚶',
'骧':'驤',
'悫':'愨',
'弪':'弳',
'戬':'戩',
'犷':'獷',
'锵':'鏘',
'镎':'鎿',
'㧑':'撝',
'鼹':'鼴',
'鳓':'鰳',
'鹔':'鷫',
'麸':'麩',
'滟':'灧',
'饦':'飥',
'痫':'癇',
'沈':'沈',
'阏':'閼',
'缕':'縷',
'戗':'戧',
'赅':'賅',
'颛':'顓',
'峄':'嶧',
'吣':'唚',
'鲨':'鯊',
'薮':'藪',
'谳':'讞',
'纟':'糹',
'砻':'礱',
'赉':'賚',
'飐':'颭',
'绔':'絝',
'跞':'躒',
'靥':'靨',
'荭':'葒',
'䙓':'襬',
'轵':'軹',
'广':'廣',
'铔':'錏',
'缪':'繆',
'殇':'殤',
'缔':'締',
'蒙':'蒙',
'辟':'闢',
'谞':'諝',
'箧':'篋',
'鲩':'鯇',
'鸪':'鴣',
'鲳':'鯧',
'亵':'褻',
'馈':'饋',
'钹':'鈸',
'锸':'鍤',
'箪':'簞',
'诇':'詗',
'浈':'湞',
'鸼':'鵃',
'飑':'颮',
'䁖':'瞜',
'赋':'賦',
'鹪':'鷦',
'荬':'蕒',
'潴':'瀦',
'铹':'鐒',
'筼':'篔',
'鱾':'魢',
'袆':'褘',
'刍':'芻',
'厌':'厭',
'璎':'瓔',
'馐':'饈',
'骒':'騍',
'褛':'褸',
'饸':'餄',
'劢':'勱',
'颦':'顰',
'贳':'貰',
'鲾':'鰏',
'裆':'襠',
'克':'克',
'牍':'牘',
'铎':'鐸',
'嫒':'嬡',
'鹕':'鶘',
'诜':'詵',
'㱩':'殰',
'酽':'釅',
'廪':'廩',
'杯':'杯',
'卷':'捲',
'饻':'餏',
'驽':'駑',
'肮':'骯',
'鸨':'鴇',
'讱':'訒',
'锺':'鍾',
'讴':'謳',
'铏':'鉶',
'篑':'簣',
'渎':'瀆',
'鹨':'鷚',
'胫':'脛',
'锝':'鍀',
'撄':'攖',
'琏':'璉',
'骐':'騏',
'鲔':'鮪',
'镮':'鐶',
'谟':'謨',
'猡':'玀',
'咤':'吒',
'箦':'簀',
'缩':'縮',
'纨':'紈',
'悬':'懸',
'圹':'壙',
'䍁':'繸',
'鹓':'鵷',
'鳔':'鰾',
'䝙':'貙',
'镥':'鑥',
'铤':'鋌',
'绨':'綈',
'扫':'掃',
'腭':'齶',
'惬':'愜',
'饽':'餑',
'箫':'簫',
'忾':'愾',
'榇':'櫬',
'压':'壓',
'鲕':'鮞',
'鸮':'鴞',
'纩':'纊',
'缨':'纓',
'悭':'慳',
'鲪':'鮶',
'贴':'貼',
'制':'制',
'鸾':'鸞',
'苁':'蓯',
'䍀':'繿',
'觇':'覘',
'鳕':'鱈',
'㓥':'劏',
'镤':'鏷',
'躏':'躪',
'虮':'蟣',
'迳':'逕',
'鹾':'鹺',
'搅':'攪',
'锏':'鐧',
'缓':'緩',
'颒':'頮',
'昙':'曇',
'窦':'竇',
'鸩':'鴆',
'骜':'驁',
'谵':'譫',
'驵':'駔',
'涞':'淶',
'纾':'紓',
'摅':'攄',
'迈':'邁',
'镏':'鎦',
'穑':'穡',
'飒':'颯',
'赟':'贇',
'饧':'餳',
'鹩':'鷯',
'荫':'蔭',
'蛮':'蠻',
'诰':'誥',
'轳':'轤',
'铕':'銪',
'绾':'綰',
'搀':'攙',
'莅':'蒞',
'榉':'櫸',
'钋':'釙',
'阌':'閿',
'缒':'縋',
'妩':'嫵',
'枭':'梟',
'趱':'趲',
'讵':'詎',
'锶':'鍶',
'鲻':'鯔',
'帼':'幗',
'仇':'仇',
'铋':'鉍',
'飓':'颶',
'钸':'鈽',
'违':'違',
'面':'面',
'虬':'虯',
'轲':'軻',
'毵':'毿',
'饾':'餖',
'怃':'憮',
'缥':'縹',
'阘':'闒',
'眍':'瞘',
'鲐':'鮐',
'笕':'筧',
'骔':'騌',
'谛':'諦',
'躜':'躦',
'唡':'啢',
'蚬':'蜆',
'戯':'戱',
'玺':'璽',
'纼':'紖',
'裈':'褌',
'鳐':'鰩',
'锢':'錮',
'嫔':'嬪',
'䗖':'螮',
'觞':'觴',
'镡':'鐔',
'铠':'鎧',
'鹧':'鷓',
'饩':'餼',
'飨':'饗',
'闶':'閌',
'驿':'驛',
'秾':'穠',
'辇':'輦',
'缃':'緗',
'鲑':'鮭',
'馓':'饊',
'骕':'驌',
'唠':'嘮',
'点':'點',
'鳑':'鰟',
'鹒':'鶊',
'黪':'黲',
'诟':'詬',
'镠':'鏐',
'屦':'屨',
'饨':'飩',
'搁':'擱',
'栉':'櫛',
'榈':'櫚',
'阍':'閽',
'疠':'癘',
'鲚':'鱭',
'鳇':'鰉',
'缧':'縲',
'鲦':'鰷',
'媪':'媼',
'悮':'悞',
'谱':'譜',
'殴':'毆',
'钶':'鈳',
'潇':'瀟',
'镋':'鎲',
'胧':'朧',
'鼍':'鼉',
'远':'遠',
'赒':'賙',
'螨':'蟎',
'蔂':'虆',
'怄':'慪',
'同':'同',
'骓':'騅',
'馕':'饢',
'唢':'嗩',
'鲧':'鯀',
'缦':'縵',
'悯':'憫',
'飔':'颸',
'贲':'賁',
'钷':'鉕',
'纻':'紵',
'㶽':'煱',
'笾':'籩',
'潆':'瀠',
'郏':'郟',
'鹐':'鵮',
'镢':'钁',
'饪':'飪',
'铷':'銣',
'绻':'綣',
'籼':'秈',
'氇':'氌',
'阋':'鬩',
'锍':'鋶',
'钌':'釕',
'弑':'弒',
'颔':'頷',
'折':'折',
'荮':'葤',
'霡':'霢',
'蹰':'躕',
'骝':'騮',
'妪':'嫗',
'犸':'獁',
'帻':'幘',
'鲼':'鱝',
'觊':'覬',
'铌':'鈮',
'灏':'灝',
'绐':'紿',
'荙':'薘',
'赝':'贗',
'雠':'讎',
'轱':'軲',
'瑷':'璦',
'矶':'磯',
'出':'出',
'搂':'摟',
'栊':'櫳',
'钍':'釷',
'庑':'廡',
'箓':'籙',
'颕':'頴',
'蘖':'櫱',
'厣':'厴',
'傥':'儻',
'谇':'誶',
'氲':'氳',
'褴':'襤',
'喷':'噴',
'岽':'崬',
'镌':'鐫',
'飕':'颼',
'晖':'暉',
'进':'進',
'赜':'賾',
'槟':'檳',
'鹦':'鸚',
'诳':'誑',
'怅':'悵',
'了':'了',
'鬓':'鬢',
'鲒':'鮚',
'馔':'饌',
'伛':'傴',
'谝':'諞',
'椟':'櫝',
'珰':'璫',
'箨':'籜',
'锷':'鍔',
'赈':'賑',
'刹':'剎',
'邺':'鄴',
'尽':'盡',
'饷':'餉',
'仆':'僕',
'鹂':'鸝',
'鹑':'鶉',
'鳒':'鰜',
'硕':'碩',
'铢':'銖',
'鱽':'魛',
'栀':'梔',
'颋':'頲',
'铙':'鐃',
'缂':'緙',
'谘':'諮',
'鲣':'鰹',
'鸤':'鳲',
'邻':'鄰',
'锾':'鍰',
'哓':'嘵',
'鸻':'鴴',
'峣':'嶢',
'酦':'醱',
'闩':'閂',
'叽':'嘰',
'椁':'槨',
'帏':'幃',
'䴙':'鷿',
'辚':'轔',
'锩':'錈',
'踯':'躑',
'瘿':'癭',
'喾':'嚳',
'毂':'轂',
'髌':'髕',
'郐':'鄶',
'呓':'囈',
'赙':'賻',
'捝':'挩',
'齑':'齏',
'绤':'綌',
'镩':'鑹',
'铨':'銓',
'韪':'韙',
'蛴':'蠐',
'偻':'僂',
'闾':'閭',
'怆':'愴',
'蒉':'蕢',
'瘅':'癉',
'挜':'掗',
'颡':'顙',
'纥':'紇',
'缤':'繽',
'逦':'邐',
'谮':'譖',
'鲹':'鰺',
'鸺':'鵂',
'棁':'梲',
'秋':'秋',
'忏':'懺',
'荜':'蓽',
'铩':'鎩',
'镨':'鐠',
'豮':'豶',
'辄':'輒',
'缏':'緶',
'鲎':'鱟',
'锓':'鋟',
'阕':'闋',
'镴':'鑞',
'谙':'諳',
'骢':'驄',
'讬':'託',
'嬷':'嬤',
'钾':'鉀',
'蛊':'蠱',
'鳎':'鰨',
'镓':'鎵',
'鹥':'鷖',
'㑩':'儸',
'痨':'癆',
'绺':'綹',
'殁':'歿',
'谄':'諂',
'馍':'饃',
'鲏':'鮍',
'缎':'緞',
'玑':'璣',
'抛':'拋',
'纣':'紂',
'傧':'儐',
'匦':'匭',
'垩':'堊',
'锪':'鍃',
'莱':'萊',
'鸸':'鴯',
'钿':'鈿',
'荆':'荊',
'髋':'髖',
'鳏':'鰥',
'这':'這',
'祢':'禰',
'镪':'鏹',
'蛳':'螄',
'铿':'鏗',
'沄':'沄',
'颌':'頜',
'阓':'闠',
'锕':'錒',
'钔':'鍆',
'栗':'慄',
'枞':'樅',
'骠':'驃',
'鲝':'鮺',
'谯':'譙',
'家':'家',
'炼':'煉',
'颍':'潁',
'镕':'鎔',
'哔':'嗶',
'诖':'詿',
'余':'餘',
'鹣':'鶼',
'峤':'嶠',
'赓':'賡',
'䇲':'筴',
'酾':'釃',
'戆':'戇',
'钕':'釹',
'锔':'鋦',
'鲥':'鰣',
'谲':'譎',
'瘾':'癮',
'蝈':'蟈',
'鹎':'鵯',
'哕':'噦',
'镔':'鑌',
'馎':'餺',
'峥':'崢',
'牦':'氂',
'鲽':'鰈',
'绹':'綯',
'闿':'闓',
'滪':'澦',
'馌':'饁',
'厐':'龎',
'辘':'轆',
'缣':'縑',
'颢':'顥',
'钪':'鈧',
'鸹':'鴰',
'鲺':'鯴',
'锿':'鎄',
'棂':'欞',
'跄':'蹌',
'铍':'鈹',
'铗':'鋏',
'靓':'靚',
'荛':'蕘',
'臜':'臢',
'韨':'韍',
'铪':'鉿',
'谀':'諛',
'鲋':'鮒',
'邓':'鄧',
'厕':'廁',
'䴖':'鶄',
'抟':'摶',
'缢':'縊',
'踬':'躓',
'䩄':'靦',
'鳋':'鰠',
'鹌':'鵪',
'祎':'禕',
'呐':'吶',
'郓':'鄆',
'钏':'釧',
'滗':'潷',
'拟':'擬',
'镦':'鐓',
'姹':'奼',
'顸':'頇',
'铻':'鋙',
'韫':'韞',
'谔':'諤',
'辂':'輅',
'鳀':'鯷',
'缍':'綞',
'镬':'鑊',
'钐':'釤',
'猕':'獼',
'殚':'殫',
'鲠':'鯁',
'谫':'譾',
'樯':'檣',
'鸷':'鷙',
'㶶':'燶',
'刿':'劌',
'鳣':'鱣',
'䅉':'稏',
'绌':'絀',
'铐':'銬',
'鳠':'鱯',
'陧':'隉',
'烨':'燁',
'只':'只',
'轭':'軛',
'饹':'餎',
'壸':'壼',
'螀':'螿',
'㺍':'獱',
'缌':'緦',
'钑':'鈒',
'阒':'闃',
'谖':'諼',
'訚':'誾',
'鲡':'鱺',
'鸢':'鳶',
'傩':'儺',
'溆':'漵',
'夸':'誇',
'隽':'雋',
'县':'縣',
'赀':'貲',
'觃':'覎',
'渑':'澠',
'鹢':'鷁',
'衮':'袞',
'㲿':'瀇',
'胨':'腖',
'奸':'姦',
'驺':'騶',
'偾':'僨',
'龌':'齷',
'颎':'熲',
'向':'向',
'侬':'儂',
'掴':'摑',
'鲶':'鯰',
'赊':'賒',
'鹍':'鵾',
'饣':'飠',
'铦':'銛',
'曲':'曲',
'辁':'輇',
'榅':'榲',
'蒇':'蕆',
'颏':'頦',
'鞑':'韃',
'锒':'鋃',
'鸠':'鳩',
'骣':'驏',
'眦':'眥',
'袯':'襏',
'鲷':'鯛',
'喽':'嘍',
'錾':'鏨',
'迁':'遷',
'觅':'覓',
'杆':'桿',
'绋':'紼',
'飏':'颺',
'镒':'鎰',
'莸':'蕕',
'鲿':'鱨',
'鹠':'鶹',
'鸱':'鴟',
'铧':'鏵',
'迩':'邇',
'蕲':'蘄',
'驸':'駙',
'芈':'羋',
'鲌':'鮊',
'铯':'銫',
'缡':'縭',
'稣':'穌',
'赇':'賕',
'朱':'朱',
'肴':'餚',
'锽':'鍠',
'钼':'鉬',
'苈':'藶',
'鹋':'鶓',
'鳌':'鰲',
'睑':'瞼',
'盐':'鹽',
'痒':'癢',
'骥':'驥',
'槚':'檟',
'绠':'綆',
'诮':'誚',
'铼':'錸',
'谂':'諗',
'袅':'裊',
'馏':'餾',
'渖':'瀋',
'纡':'紆',
'颥':'顬',
'鹲':'鸏',
'鸶':'鷥',
'砺':'礪',
'钽':'鉭',
'锼':'鎪',
'诃':'訶',
'鳍':'鰭',
'荣':'榮',
'睐':'睞',
'呒':'嘸',
'绡':'綃',
'饤':'飣',
'俫':'倈',
'觯':'觶',
'蛱':'蛺',
'并':'並',
'铽':'鋱',
'辀':'輈',
'榄':'欖',
'缋':'繢',
'鹜':'鶩',
'窎':'窵',
'䴗':'鶪',
'鲢':'鰱',
'锧':'鑕',
'伫':'佇',
'碜':'磣',
'顼':'頊',
'哒':'噠',
'赗':'賵',
'诘':'詰',
'钤':'鈐',
'鹡':'鶺',
'铑':'銠',
'鳢':'鱧',
'啧':'嘖',
'轫':'軔',
'致':'致',
'絷':'縶',
'绶':'綬',
'闼':'闥',
'冁':'囅',
'垅':'壠',
'阄':'鬮',
'㶉':'鸂',
'缊':'縕',
'焖':'燜',
'碛':'磧',
'挢':'撟',
'枥':'櫪',
'刬':'剗',
'鸴':'鷽',
'脶':'腡',
'贾':'賈',
'鳡':'鱤',
'蛏':'蟶',
'觑':'覷',
'馇':'餷',
'兖':'兗',
'蓣':'蕷',
'轪':'軑',
'鹴':'鸘',
'橼':'櫞',
'炀':'煬',
'厂':'廠',
'鲈':'鱸',
'龊':'齪',
'殒':'殞',
'钘':'鈃',
'蕰':'薀',
'侪':'儕',
'缵':'纘',
'纴':'紝',
'蔹':'蘞',
'撸':'擼',
'秆':'稈',
'鳈':'鰁',
'苌':'萇',
'诒':'詒',
'镙':'鏍',
'铘':'鋣',
'埚':'堝',
'筝':'箏',
'鹟':'鶲',
'注':'註',
'俪':'儷',
'鲉':'鮋',
'咙':'嚨',
'锘':'鍩',
'阚':'闞',
'闫':'閆',
'羟':'羥',
'愠':'慍',
'讧':'訌',
'沩':'溈',
'猬':'蝟',
'鞯':'韉',
'娲':'媧',
'缴':'繳',
'郁':'鬱',
'鳉':'鱂',
'蟏':'蠨',
'哙':'噲',
'镘':'鏝',
'筜':'簹',
'胡':'胡',
'桦':'樺',
'凫':'鳧',
'埯':'垵',
'驲':'馹',
'罴':'羆',
'锃':'鋥',
'鲖':'鮦',
'舍':'舍',
'䴓':'鳾',
'辔':'轡',
'炖':'燉',
'锛':'錛',
'缟':'縞',
'鲞':'鯗',
'鞒':'鞽',
'氩':'氬',
'刭':'剄',
'䌷':'紬',
'镃':'鎡',
'魇':'魘',
'才':'才',
'觐':'覲',
'呙':'咼',
'铓':'鋩',
'铮':'錚',
'鱿':'魷',
'旸':'暘',
'诼':'諑',
'泾':'涇',
'龉':'齬',
'瘘':'瘺',
'骛':'騖',
'砜':'碸',
'鲟':'鱘',
'缞':'縗',
'稆':'穭',
'钯':'鈀',
'尴':'尷',
'蔺':'藺',
'玮':'瑋',
'莴':'萵',
'剀':'剴',
'酂':'酇',
'鹈':'鵜',
'苋':'莧',
'埙':'塤',
'镚':'鏰',
'鳟':'鱒',
'赪':'赬',
'偬':'傯',
'瓯':'甌',
'籴':'糴',
'轾':'輊',
'阃':'閫',
'缉':'緝',
'戋':'戔',
'脍':'膾',
'䴕':'鴷',
'䯄':'騧',
'讦':'訐',
'邬':'鄔',
'鲴':'鯝',
'莶':'薟',
'梼':'檮',
'铄':'鑠',
'赕':'賧',
'荡':'盪',
'桧':'檜',
'鹳':'鸛',
'钅':'釒',
'娆':'嬈',
'缈':'緲',
'锠':'錩',
'䴔':'鵁',
'缑':'緱',
'耢':'耮',
'谪':'謫',
'锉':'銼',
'鲵':'鯢',
'荟':'薈',
'讻':'訩',
'携':'攜',
'镄':'鐨',
'绉':'縐',
'届':'屆',
'浔':'潯',
'鹞':'鷂',
'荠':'薺',
'蓥':'鎣',
'嫱':'嬙',
'龈':'齦',
'鲊':'鮓',
'漓':'漓',
'谕':'諭',
'鲘':'鮜',
'阙':'闕',
'钚':'鈈',
'䜣':'訢',
'冬':'冬',
'黉':'黌',
'缳':'繯',
'蛲':'蟯',
'撺':'攛',
'鹉':'鵡',
'鳊':'鯿',
'聍':'聹',
'蛎':'蠣',
'诐':'詖',
'埘':'塒',
'铚':'銍',
'姜':'薑',
'俨':'儼',
'镯':'鐲',
'羁':'羈',
'厅':'廳',
'馉':'餶',
'骃':'駰',
'锖':'錆',
'馅':'餡',
'骟':'騸',
'钫':'鈁',
'垭':'埡',
'缲':'繰',
'娴':'嫻',
'坂':'阪',
'镖':'鏢',
'铥':'銩',
'鳛':'鰼',
'表':'表',
'铫':'銚',
'狯':'獪',
'鳁':'鰮',
'黩':'黷',
'恸':'慟',
'鲗':'鰂',
'诂':'詁',
'瘗':'瘞',
'疖':'癤',
'玚':'瑒',
'缝':'縫',
'讪':'訕',
'霭':'靄',
'鲰':'鯫',
'铈':'鈰',
'鹇':'鷳',
'轴':'軸',
'濒':'瀕',
'痖':'瘂',
'蓠':'蘺',
'荥':'滎',
'诪':'譸',
'龇':'齜',
'颉':'頡',
'焘':'燾',
'缜':'縝',
'眬':'矓',
'鲱':'鯡',
'鸲':'鴝',
'栾':'欒',
'旋':'旋',
'浐':'滻',
'蹒':'蹣',
'呖':'嚦',
'荤':'葷',
'嗫':'囁',
'跻':'躋',
'轼':'軾',
'诿':'諉',
'缇':'緹',
'鲆':'鮃',
'骊':'驪',
'茏':'蘢',
'谑':'謔',
'钖':'鍚',
'颞':'顳',
'伧':'傖',
'锫':'錇',
'邮':'郵',
'贻':'貽',
'颙':'顒',
'梾':'棶',
'驷':'駟',
'鳆':'鰒',
'诔':'誄',
'铖':'鋮',
'勚':'勩',
'鹝':'鷊',
'镫':'鐙',
'骦':'驦',
'韬':'韜',
'饳':'飿',
'绲':'緄',
'婵':'嬋',
'恹':'懨',
'锂':'鋰',
'鲇':'鯰',
'缆':'纜',
'娈':'孌',
'钗':'釵',
'颟':'顢',
'疭':'瘲',
'匮':'匱',
'鸰':'鴒',
'撷':'擷',
'荞':'蕎',
'梿':'槤',
'镂':'鏤',
'糇':'餱',
'骍':'騂',
'濑':'瀨',
'浒':'滸',
'叙':'敘',
'绛':'絳',
'钺':'鉞',
'诩':'詡',
'霁':'霽',
'龆':'齠',
'骈':'駢',
'馊':'餿',
'蒌':'蔞',
'鲙':'鱠',
'䴘':'鷈',
'粜':'糶',
'舣':'艤',
'谧':'謐',
'钬':'鈥',
'厮':'廝',
'缱':'繾',
'纰':'紕',
'䌹':'絅',
'芸':'芸',
'贽':'贄',
'魉':'魎',
'呗':'唄',
'鹛':'鶥',
'嵝':'嶁',
'鳜':'鱖',
'漤':'灠',
'俦':'儔',
'癫':'癲',
'啭':'囀',
'婳':'嫿',
'骉':'驫',
'殓':'殮',
'谒':'謁',
'阖':'闔',
'龛':'龕',
'粝':'糲',
'檩':'檁',
'瞆':'瞶',
'钭':'鈄',
'锬':'錟',
'刮':'刮',
'缰':'韁',
'䌸':'縳',
'鹆':'鵒',
'诓':'誆',
'鳝':'鱔',
'㧟':'擓',
'啬':'嗇',
'绱':'緔',
'饴':'飴',
'恺':'愷',
'猃':'獫',
'厘':'釐',
'缛':'縟',
'骞':'騫',
'疬':'癧',
'銮':'鑾',
'帱':'幬',
'鲲':'鯤',
'千':'千',
'苎':'苧',
'蹑':'躡',
'镗':'鏜',
'诨':'諢',
'闬':'閈',
'鹱':'鸌',
'黾':'黽',
'砀':'碭',
'鲃':'䰾',
'龅':'齙',
'合':'合',
'膑':'臏',
'嵘':'嶸',
'缚':'縛',
'锞':'錁',
'沣':'灃',
'愦':'憒',
'鹄':'鵠',
'懑':'懣',
'晔':'曄',
'㛟':'𡞵',
'镞':'鏃',
'桠':'椏',
'苧':'苎',
'绯':'緋',
'铳':'銃',
'跹':'躚',
'轺':'軺',
'颀':'頎',
'鼗':'鞀',
'㔉':'劚',
'岘':'峴',
'鲛':'鮫',
'㖞':'喎',
'伥':'倀',
'枪':'槍',
'闳':'閎',
'挽':'輓',
'奁':'奩',
'屃':'屓',
'准':'準',
'镉':'鎘',
'浍':'澮',
'鳘':'鰵',
'佥':'僉',
'执':'執',
'鹯':'鸇',
'珲':'琿',
'泸':'瀘',
'恻':'惻',
'虿':'蠆',
'缄':'緘',
'馀':'餘',
'阊':'閶',
'辏':'輳',
'斓':'斕',
'岙':'嶴',
'椠':'槧',
'妫':'媯',
'窭':'窶',
'讷':'訥',
'䌼':'綐',
'铉':'鉉',
'镈':'鎛',
'觋':'覡',
'藓':'蘚',
'硖':'硤',
'鳙':'鱅',
'鹚':'鶿',
'狝':'獮',
'䌽':'綵',
'㱮':'殨',
'嗳':'噯',
'囵':'圇',
'禀':'稟',
'崃':'崍',
'悦':'悅',
'赆':'贐',
'锳':'鍈',
'垴':'堖',
'趸':'躉',
'莼':'蒓',
'硁':'硜',
'诙':'詼',
'飖':'颻',
'铞':'銱',
'桡':'橈',
'槠':'櫧',
'跸':'蹕',
'钛':'鈦',
'狲':'猻',
'板':'板',
'缀':'綴',
'阈':'閾',
'锊':'鋝',
'栌':'櫨',
'缯':'繒',
'鲮':'鯪',
'殡':'殯',
'挦':'撏',
'阆':'閬',
'鲯':'鯕',
'缮':'繕',
'玱':'瑲',
'怼':'懟',
'铒':'鉺',
'饫':'飫',
'奂':'奐',
'巅':'巔',
'觍':'覥',
'飗':'飀',
'鹘':'鶻',
'嵚':'嶔',
'荦':'犖',
'掼':'摜',
'雳':'靂',
'闵':'閔',
'迹':'跡',
'松':'松',
'骀':'駘',
'布':'布',
'馂':'餕',
'鲄':'魺',
'历':'歷',
'㖊':'噚',
'浃':'浹',
'谏':'諫',
'辎':'輜',
'茑':'蔦',
'砗':'硨',
'缙':'縉',
'炜':'煒',
'耧':'耬',
'电':'電',
'钴':'鈷',
'亸':'嚲',
'舻':'艫',
'鳄':'鱷',
'缠':'纏',
'硗':'磽',
'杩':'榪',
'镵':'鑱',
'铴':'鐋',
'诶':'誒',
'轹':'轢',
'腽':'膃',
'骁':'驍',
'龃':'齟',
'鲅':'鮁',
'崄':'嶮',
'鲭':'鯖',
'吊':'弔',
'缘':'緣',
'炝':'熗',
'莳':'蒔',
'锴':'鍇',
'鳅':'鰍',
'采':'採',
'诋':'詆',
'荐':'薦',
'恒':'恆',
'䓕':'薳',
'姗':'姍',
'癞':'癩',
'俣':'俁',
'桢':'楨',
'郦':'酈',
'饬':'飭',
'巯':'巰',
'辒':'轀',
'铵':'銨',
'啴':'嘽',
'轸':'軫',
'腼':'靦',
'简':'簡',
'阗':'闐',
'钊':'釗',
'镅':'鎇',
'鹀':'鵐',
'骖':'驂',
'岚':'嵐',
'锟':'錕',
'讠':'訁',
'伣':'俔',
'谥':'謚',
'枨':'棖',
'镳':'鑣',
'累':'累',
'纮':'紘',
'疴':'痾',
'陉':'陘',
'铊':'鉈',
'觌':'覿',
'浏':'瀏',
'扑':'撲',
'鹙':'鶖',
'鳚':'䲁',
'镟':'鏇',
'回':'回',
'诠':'詮',
'裢':'褳',
'鸧':'鶬',
'绮':'綺',
'台':'台',
'泺':'濼',
'恽':'惲',
'颃':'頏',
'锆':'鋯',
'辍':'輟',
'渌':'淥',
'龁':'齕',
'咛':'嚀',
'谠':'讜',
'暧':'曖',
'鲫':'鯽',
'鸬':'鸕',
'疱':'皰',
'贶':'貺',
'黡':'黶',
'罂':'罌',
'镆':'鏌',
'绗':'絎',
'铛':'鐺',
'筚':'篳',
'噜':'嚕',
'裣':'襝',
'莺':'鶯',
'荪':'蓀',
'鹬':'鷸',
'闱':'闈',
'鉴':'鑒',
'柽':'檉',
'腾':'騰',
'鲀':'魨',
'龂':'齗',
'阇':'闍',
'蔑':'蔑',
'茕':'煢',
'缭':'繚',
'锱':'錙',
'钰':'鈺',
'垲':'塏',
'煴':'熅',
'觎':'覦',
'鹗':'鶚',
'赑':'贔',
'绬':'緓',
'镱':'鐿',
'跶':'躂',
'馃':'餜',
'骅':'驊',
'炉':'爐',
'栎':'櫟',
'鲂':'魴',
'茔':'塋',
'簖':'籪',
'馄':'餛',
'贠':'貟',
'欤':'歟',
'枧':'梘',
'萦':'縈',
'纭':'紜',
'缬':'纈',
'决':'決',
'谶':'讖',
'鼋':'黿',
'糁':'糝',
'幂':'冪',
'髅':'髏',
'呆':'獃',
'诏':'詔',
'志':'志',
'飙':'飆',
'骎':'駸',
'坜':'壢',
'扪':'捫',
'却':'卻',
'蝼':'螻',
'揿':'撳',
'娅':'婭',
'钆':'釓',
'辌':'輬',
'缗':'緡',
'岖':'嶇',
'唛':'嘜',
'谡':'謖',
'涠':'潿',
'䜧':'譅',
'皲':'皸',
'昽':'曨',
'籁':'籟',
'祃':'禡',
'绂':'紱',
'硙':'磑',
'镛':'鏞',
'珑':'瓏',
'滢':'瀅',
'橥':'櫫',
'诤':'諍',
'蓦':'驀',
'聩':'聵',
'鹭':'鷺',
'轷':'軤',
'泶':'澩',
'征':'徵',
'窃':'竊',
'崂':'嶗',
'禅':'禪',
'钇':'釔',
'厉':'厲',
'谌':'諶',
'编':'編',
'垱':'壋',
'锲':'鍥',
'铟':'銦',
'铇':'鉋',
'鳗':'鰻',
'桤':'榿',
'绫':'綾',
'邝':'鄺',
'镲':'鑔',
'泷':'瀧',
'轶':'軼',
'诹':'諏',
'缁':'緇',
'垆':'壚',
'骘':'騭',
'阛':'闤',
'唝':'嗊',
'钜':'鉅',
'借':'借',
'鸫':'鶇',
'鲬':'鯒',
'谷':'谷',
'怿':'懌',
'绀':'紺',
'㟆':'㠏',
'赍':'齎',
'诎':'詘',
'镝':'鏑',
'哜':'嚌',
'滠':'灄',
'荩':'藎',
'鹫':'鷲',
'困':'困',
'瓒':'瓚',
'蝾':'蠑',
'揾':'搵',
'瘆':'瘮',
'辋':'輞',
'脔':'臠',
'骙':'騤',
'砚':'硯',
'咝':'噝',
'锜':'錡',
'氢':'氫',
'椤':'欏',
'绁':'紲',
'症':'症',
'餍':'饜',
'觏':'覯',
'鹖':'鶡',
'哝':'噥',
'裥':'襇',
'镧':'鑭',
'荨':'蕁',
'跷':'蹺',
'龀':'齔',
'笃':'篤',
'锇':'鋨',
'䞐':'賰',
'颚':'顎',
'缫':'繅',
'钲':'鉦',
'鹁':'鵓',
'鳂':'鰃',
'潋':'瀲',
'懔':'懍',
'绖':'絰',
'飚':'飈',
'扩':'擴',
'胪':'臚',
'祯':'禎',
'橹':'櫓',
}

jdict = dict((k.decode('utf8'), v.decode('utf8')) for k,v in zh_dict.iteritems())
fdict = dict((v.decode('utf8'), k.decode('utf8')) for k,v in zh_dict.iteritems())

def utf8_ftoj(d):
    d=d.decode("utf-8", 'ignore')
    d=ftoj(d)
    d=d.encode("utf-8")
    return d


def ftoj(data):
    return u''.join(fdict.get(c,c) for c in data)

