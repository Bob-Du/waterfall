import pymysql

connection = pymysql.connect('db.bobdu.cc', 'root', '123456', 'waterfall', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

arr = [
    {'id': '1', 'title': '  小清新格子包臀裙     ', 'pic': '    ./images/3aa3744cf515f5c0b7fd8b21c4c6edaf.jpg    ', 'price': '  55   '},
    {'id': '2', 'title': '  呛口小辣椒刺绣吊带连衣裙     ', 'pic': '    ./images/b1faf31f316b3079a96a82169c426258.jpg    ', 'price': '  128  '},
    {'id': '3', 'title': '  立体花喇叭袖短裙雪纺衫  ', 'pic': '    ./images/689dd5eae077459af4a17e9f815bad50.jpg    ', 'price': '  118  '},
    {'id': '4', 'title': '  韩国新款 优雅名媛连衣裙     ', 'pic': '    ./images/604a6dad0be72b2426d63e0d8efaf917.jpg    ', 'price': '  79   '},
    {'id': '5', 'title': '  欧美单排扣高腰牛仔裙裤  ', 'pic': '    ./images/568309f2a4b2ee0c4ed1f1f9d6c69de3.jpg    ', 'price': '  42   '},
    {'id': '6', 'title': '  宽松短袖连衣裙  ', 'pic': '    ./images/f45c350eb2f192077c450164b8986716.jpg    ', 'price': '  70   '},
    {'id': '7', 'title': '  沙滩短裙欧根纱公主裙   ', 'pic': '    ./images/520330a46fdc687f8b325ee5a16a4832.jpg    ', 'price': '  69   '},
    {'id': '8', 'title': '  纯色荷叶边包臀裙     ', 'pic': '    ./images/27f7b404889169e12edabb23e8d80889.jpg    ', 'price': '  65   '},
    {'id': '9', 'title': '  欧根纱卡通印花无袖连衣裙     ', 'pic': '    ./images/0168e002115edc79a028117ec4b48bff.jpg    ', 'price': '  98   '},
    {'id': '10', 'title': ' 夏季美裙露肩印花连衣裙  ', 'pic': '    ./images/edb14f72deb2a2c5566d96beefab7d57.jpg    ', 'price': '  69   '},
    {'id': '11', 'title': ' 棉麻荷叶袖抽绳条纹连衣裙     ', 'pic': '    ./images/325b5c0e5c133cb61171d286d37c13d9.jpg    ', 'price': '  88   '},
    {'id': '12', 'title': ' 做旧插兜双口袋牛仔半身裙     ', 'pic': '    ./images/99034a47383ce8ead2ce3fe48bdead79.jpg    ', 'price': '  59   '},
    {'id': '13', 'title': ' 宽松大码喇叭袖连衣裙   ', 'pic': '    ./images/605190a25644c015ebada86c5e815310.jpg    ', 'price': '  59   '},
    {'id': '14', 'title': ' 荷叶领碎花雪纺吊带连衣裙     ', 'pic': '    ./images/2524bc9ecbbb687a18208f665c070c5e.jpg    ', 'price': '  88   '},
    {'id': '15', 'title': ' 原宿风破洞牛仔短裙    ', 'pic': '    ./images/a0c84c6248d7e6fe29fb86a44ddc35da.jpg    ', 'price': '  69   '},
    {'id': '16', 'title': ' 高腰修身包臀牛仔短裙   ', 'pic': '    ./images/4ec1e01c209a394e629c967f48c2ac19.jpg    ', 'price': '  67   '},
    {'id': '17', 'title': ' 韩版显瘦修身短裙连衣裙  ', 'pic': '    ./images/186a39f9111ae0db0d44ed2961f5da07.jpg    ', 'price': '  96   '},
    {'id': '18', 'title': ' 夏季韩版雪纺连衣裙包臀裙     ', 'pic': '    ./images/8c5c54152e0f269ccdb3a61f243cb3d1.jpg    ', 'price': '  69   '},
    {'id': '19', 'title': ' 韩版条纹假两件连衣裙   ', 'pic': '    ./images/9695d002e584ac1b1f0bbe7d5a226c7d.jpg    ', 'price': '  138  '},
    {'id': '20', 'title': ' 夏装收腰无袖连衣裙    ', 'pic': '    ./images/21236ef9bface4fef38410da83b60f78.jpg    ', 'price': '  89   '},
    {'id': '21', 'title': ' 套装蕾丝纯色镂空连衣裙夏     ', 'pic': '    ./images/13c2376b2bcf67abfd76e0c12ec6e079.jpg    ', 'price': '  109  '},
    {'id': '22', 'title': ' 条纹撞色拼接修身连衣裙  ', 'pic': '    ./images/383f45de0317e8073631d77c75e70c16.jpg    ', 'price': '  149  '},
    {'id': '23', 'title': ' 欧根纱水墨抽象印花连衣裙     ', 'pic': '    ./images/6ad0702c9d16cd51fcbc8320da4fb1df.jpg    ', 'price': '  138  '},
    {'id': '24', 'title': ' 夏装韩国宽松背心连衣裙  ', 'pic': '    ./images/629bd963864f67c05da6aae9a3505d3d.jpg    ', 'price': '  78   '},
    {'id': '25', 'title': ' 夏季新款学院风背带连衣裙     ', 'pic': '    ./images/617a7198b845a140bc8cb480d52b27b2.jpg    ', 'price': '  79   '},
    {'id': '26', 'title': ' 梭织麻料单排扣连衣裙   ', 'pic': '    ./images/b26e8021d45509ca538dd903287c1f77.jpg    ', 'price': '  86   '},
    {'id': '27', 'title': ' 波西米亚短裙印花背心裙  ', 'pic': '    ./images/90446c8a1d0dc0610824b3f9dc346b4c.jpg    ', 'price': '  75   '},
    {'id': '28', 'title': ' 欧美羽毛印花背心连衣裙  ', 'pic': '    ./images/c7957c6786b3b4497214dff536ffa853.jpg    ', 'price': '  118  '},
    {'id': '29', 'title': ' 气质V领纯色修身连衣裙  ', 'pic': '    ./images/ea63ccbe670ffd767517de6780b405b9.jpg    ', 'price': '  149  '},
    {'id': '30', 'title': ' 夏季新款名媛短裙连衣裙  ', 'pic': '    ./images/37ddbe295277bf81ae09a086218834de.jpg    ', 'price': '  79   '},
    {'id': '31', 'title': ' 新款修身无袖流苏连衣裙  ', 'pic': '    ./images/7e3825d89a5dff806f6ca36df4af4fb7.jpg    ', 'price': '  69   '},
    {'id': '32', 'title': ' 韩版青花瓷碎花背心连衣裙     ', 'pic': '    ./images/0cc6e9d321abc1332518eb6f23d8bbc8.jpg    ', 'price': '  69   '},
    {'id': '33', 'title': ' 夏季时尚性感露肩连衣裙  ', 'pic': '    ./images/33fdfa927e7f121b73dc5e7f245f3675.jpg    ', 'price': '  79   '},
    {'id': '34', 'title': ' 牛仔背带裙连衣裙短裙   ', 'pic': '    ./images/4bd9e05b224abeea1de56ecb62c94b24.jpg    ', 'price': '  68   '},
    {'id': '35', 'title': ' 无袖露背收腰雪纺连衣裙  ', 'pic': '    ./images/6c54af51a990500c86ecc19fdb29e4cd.jpg    ', 'price': '  79   '},
    {'id': '36', 'title': ' 韩版姐妹款连衣裙     ', 'pic': '    ./images/d7d26ff942fec41274ed43d688e694f8.jpg    ', 'price': '  87   '},
    {'id': '37', 'title': ' 衬衣+印花短裙套装    ', 'pic': '    ./images/36903020fe0619b5cc93e1801eb9190e.jpg    ', 'price': '  99   '},
    {'id': '38', 'title': ' 纯色修身气质网纱连衣裙  ', 'pic': '    ./images/ce831be19199a3feaa1f13b2927c67e9.jpg    ', 'price': '  138  '},
    {'id': '39', 'title': ' 韩版条纹无袖连衣裙    ', 'pic': '    ./images/e60173e3867f3192f59a53d85ae90146.jpg    ', 'price': '  89   '},
    {'id': '40', 'title': ' 夏新款时尚排扣牛仔包裙  ', 'pic': '    ./images/499ba1648b39a1514a3e743a3b65e715.jpg    ', 'price': '  70   '},
    {'id': '41', 'title': ' 重工钉珠百搭背带连衣裙  ', 'pic': '    ./images/2541e071aea98d21fb242fec8f297fe0.jpg    ', 'price': '  279  '},
    {'id': '42', 'title': ' 韩版高品质麻料连衣裙   ', 'pic': '    ./images/35f32c68a7c489f90ceeab0fec33e4f2.jpg    ', 'price': '  80   '},
    {'id': '43', 'title': ' 性感网纱拼接无袖背心裙  ', 'pic': '    ./images/544b37532d01aff51f98c7ceff68e73f.jpg    ', 'price': '  79   '},
    {'id': '44', 'title': ' 雪纺连衣裙露肩宽松A字裙     ', 'pic': '    ./images/7c4db20bfd3051542b8f050fdebb8fbb.jpg    ', 'price': '  69   '},
    {'id': '45', 'title': ' 复古牛仔A字伞状半身短裙     ', 'pic': '    ./images/32fa987c0abe0904339dbec4dc196ab0.jpg    ', 'price': '  69   '},
    {'id': '46', 'title': ' 钮扣双口袋牛仔半身裙   ', 'pic': '    ./images/a9db754e44f42afd91857cb2478ffb31.jpg    ', 'price': '  79   '},
    {'id': '47', 'title': ' 韩版修身气质OL半身裙  ', 'pic': '    ./images/f9e63e3fde0fa0072d26f8268b8b417b.jpg    ', 'price': '  39   '},
    {'id': '48', 'title': ' 韩版显瘦名媛短裙连衣裙  ', 'pic': '    ./images/2894def20d04b501d9dd913eb7853a2e.jpg    ', 'price': '  79   '},
    {'id': '49', 'title': ' 夏季雪纺碎花包臀半身裙  ', 'pic': '    ./images/85b1f1ed4c8125c08b0940c71c3193ce.jpg    ', 'price': '  38   '},
    {'id': '50', 'title': ' 百搭牛仔半身裙调节背带裙     ', 'pic': '    ./images/5d546cb1bf72f5f88958907c427f0706.jpg    ', 'price': '  77   '},
    {'id': '51', 'title': ' 印花短裙半身裙廓形蓬蓬裙     ', 'pic': '    ./images/bb70dc1ef15f1595cf4b59970eac8433.jpg    ', 'price': '  99   '},
    {'id': '52', 'title': ' 收腰显瘦蓬蓬短裙     ', 'pic': '    ./images/2cedf043b0667354b3eed99c3e0bd557.jpg    ', 'price': '  78   '},
    {'id': '53', 'title': ' 夏季韩版棉麻露肩连衣裙  ', 'pic': '    ./images/633c42ace82d4e51fec2d206917842c7.jpg    ', 'price': '  95   '},
    {'id': '54', 'title': ' 夏装名媛气质雪纺连衣裙  ', 'pic': '    ./images/2278e6388c25c10fbc3b7118ca6cbf21.jpg    ', 'price': '  89   '},
    {'id': '55', 'title': ' 条纹百褶圆领连衣裙    ', 'pic': '    ./images/d87b0074a2b887d0f2f8d38ca97bf2e7.jpg    ', 'price': '  89   '},
    {'id': '56', 'title': ' 小碎花收腰印花牛仔连衣裙     ', 'pic': '    ./images/5268844d1ad657b5156874f8e700f9da.jpg    ', 'price': '  88   '},
    {'id': '57', 'title': ' 韩版修身显瘦蕾丝连衣裙  ', 'pic': '    ./images/4facbf688567535eca937edc11c8c19d.jpg    ', 'price': '  99   '},
    {'id': '58', 'title': ' 新款韩版修身破洞半身裙  ', 'pic': '    ./images/6f1bff4a9eb74b96b7afbe859ec5776d.jpg    ', 'price': '  67   '},
    {'id': '59', 'title': ' 蝙蝠袖拼接蕾丝透视连衣裙     ', 'pic': '    ./images/8b16423f1f3f36cb5fd7769747b7f3d2.jpg    ', 'price': '  79   '},
    {'id': '60', 'title': ' 时尚简约学院风牛仔半身裙     ', 'pic': '    ./images/ca560738fc912e72853016062511738b.jpg    ', 'price': '  78   '},
    {'id': '61', 'title': ' 圆领碎花印花打底连衣裙  ', 'pic': '    ./images/3ed94db323d4290ad98ad9e9a6122463.jpg    ', 'price': '  78   '},
    {'id': '62', 'title': ' 真丝印花拼接收腰连衣裙  ', 'pic': '    ./images/d23baad586775a247f522ed3f7acba39.jpg    ', 'price': '  359  '},
    {'id': '63', 'title': ' 森女系棉麻连衣裙短裙   ', 'pic': '    ./images/392f77c1a5f6cc8b4639f83b36f456c8.jpg    ', 'price': '  68   '},
    {'id': '64', 'title': ' 花边字母短袖T恤连衣裙  ', 'pic': '    ./images/96962fc823a5b366d118f4b57de1eb59.jpg    ', 'price': '  79   '},
    {'id': '65', 'title': ' 露肩一字领简约显瘦连衣裙     ', 'pic': '    ./images/3e06eb6ddd2f1b5af9b6f243447e7dc8.jpg    ', 'price': '  149  '},
    {'id': '66', 'title': ' 韩版夏装喇叭袖连衣裙短裙     ', 'pic': '    ./images/f3838d05b3220ecd8975fd052d69f8ee.jpg    ', 'price': '  47   '},
    {'id': '67', 'title': ' HI夏季新款拼接连衣裙  ', 'pic': '    ./images/f4114207e0a91270f1c61455571c1504.jpg    ', 'price': '  218  '},
    {'id': '68', 'title': ' 碎花不规则半身裙短裙   ', 'pic': '    ./images/d3a4230d3a2270b0e550e1e9c4608df0.jpg    ', 'price': '  59   '},
    {'id': '69', 'title': ' 字母不规则荷叶摆边连衣裙     ', 'pic': '    ./images/1777dcf8a092b8b4dfd7965d9d605148.jpg    ', 'price': '  55   '},
    {'id': '70', 'title': ' 韩版显瘦高腰鱼尾半身裙  ', 'pic': '    ./images/07a693e19997c45f6e700ffa876d4d8b.jpg    ', 'price': '  65   '},
    {'id': '71', 'title': ' 森系花朵连衣裙  ', 'pic': '    ./images/59e3195fb4e8f7557debee48914ff22a.jpg    ', 'price': '  49   '},
    {'id': '72', 'title': ' 欧根纱绣花蕾丝短袖连衣裙     ', 'pic': '    ./images/04c79b9dde6c803faf3b2ddbadce76f7.jpg    ', 'price': '  68   '},
    {'id': '73', 'title': ' 性感镂空修身大摆连衣裙  ', 'pic': '    ./images/0442556551093e6b03b1eec64b1cea22.jpg    ', 'price': '  0    '},
    {'id': '74', 'title': ' 欧根纱拼接A字裙女短裙  ', 'pic': '    ./images/11cea80745732d1f011478b122f9bd7b.jpg    ', 'price': '  326  '},
    {'id': '75', 'title': ' 纯色双层网纱A字瘦腿短裙     ', 'pic': '    ./images/6cbe693689a9a831b9cd1d523085bde3.jpg    ', 'price': '  581  '},
    {'id': '76', 'title': ' 初夏新品韩版刺绣牛仔裙  ', 'pic': '    ./images/d5e76cf3f7cfa661acd0ac774fca2fe9.jpg    ', 'price': '  128  '},
    {'id': '77', 'title': ' 韩版显瘦高腰鱼尾半身裙  ', 'pic': '    ./images/07a693e19997c45f6e700ffa876d4d8b.jpg    ', 'price': '  65   '},
    {'id': '78', 'title': ' 新款碎花双层网纱半身裙  ', 'pic': '    ./images/24735a488a83e347370793bd1050bd80.jpg    ', 'price': '  58   '},
    {'id': '79', 'title': ' 韩版条纹拼接牛仔连衣裙  ', 'pic': '    ./images/0a2e815e62207be182acd6e54579d9dc.jpg    ', 'price': '  78   '},
    {'id': '80', 'title': ' 欧根纱绣花蕾丝短袖连衣裙     ', 'pic': '    ./images/04c79b9dde6c803faf3b2ddbadce76f7.jpg    ', 'price': '  68   '},
    {'id': '81', 'title': ' 韩版显瘦高腰鱼尾半身裙  ', 'pic': '    ./images/07a693e19997c45f6e700ffa876d4d8b.jpg    ', 'price': '  65   '},
    {'id': '82', 'title': ' 高腰包臀荷叶边半身裙短裙     ', 'pic': '    ./images/17b717b6674bd4c399d82a1047097693.jpg    ', 'price': '  49   '},
    {'id': '83', 'title': ' 韩国破洞牛仔包臀裙    ', 'pic': '    ./images/602ad5b243d724ea2c8e6ac27b80a85e.jpg    ', 'price': '  79   '},
    {'id': '84', 'title': ' 欧根纱拼接A字裙女短裙  ', 'pic': '    ./images/11cea80745732d1f011478b122f9bd7b.jpg    ', 'price': '  32   '},
    {'id': '85', 'title': ' 欧根纱绣花蕾丝短袖连衣裙     ', 'pic': '    ./images/04c79b9dde6c803faf3b2ddbadce76f7.jpg    ', 'price': '  68   '},
    {'id': '86', 'title': ' 蝴蝶结一字领连衣裙短裙  ', 'pic': '    ./images/660785975b1d1b02db37e8afdd1f7a81.jpg    ', 'price': '  89   '},
    {'id': '87', 'title': ' 百搭高腰半身百褶短裙   ', 'pic': '    ./images/0c0284bb404ac7213ef8cd1acdbfdc2f.jpg    ', 'price': '  70   '},
    {'id': '88', 'title': ' 初夏新品韩版刺绣牛仔裙  ', 'pic': '    ./images/d5e76cf3f7cfa661acd0ac774fca2fe9.jpg    ', 'price': '  128  '},
    {'id': '89', 'title': ' 流苏开叉包臀牛仔裙    ', 'pic': '    ./images/87c4aa8c0150ec4893ce737b6e5960a2.jpg    ', 'price': '  49   '},
    {'id': '90', 'title': ' 欧根纱拼接A字裙女短裙  ', 'pic': '    ./images/11cea80745732d1f011478b122f9bd7b.jpg    ', 'price': '  32   '},
    {'id': '91', 'title': ' 韩版高腰修身印花连衣裙  ', 'pic': '    ./images/063a9b05dbe192f16fbe4dc2e4159084.jpg    ', 'price': '  89   '},
    {'id': '92', 'title': ' 韩版条纹拼接牛仔连衣裙  ', 'pic': '    ./images/0a2e815e62207be182acd6e54579d9dc.jpg    ', 'price': '  78   '},
    {'id': '93', 'title': ' 初夏新品韩版刺绣牛仔裙  ', 'pic': '    ./images/d5e76cf3f7cfa661acd0ac774fca2fe9.jpg    ', 'price': '  128  '},
    {'id': '94', 'title': ' 学院风复古牛仔连衣裙   ', 'pic': '    ./images/0284457a7fe9eec89ec4023f60159993.jpg    ', 'price': '  88   '},
    {'id': '95', 'title': ' 高腰包臀荷叶边半身裙短裙     ', 'pic': '    ./images/17b717b6674bd4c399d82a1047097693.jpg    ', 'price': '  49   '},
    {'id': '96', 'title': ' HI夏季新款蝴蝶结百搭裙     ', 'pic': '    ./images/5e6a060e6343bdaf59e49a4dab669527.jpg    ', 'price': '  196  '},
    {'id': '97', 'title': ' 韩版条纹拼接牛仔连衣裙  ', 'pic': '    ./images/0a2e815e62207be182acd6e54579d9dc.jpg    ', 'price': '  78   '},
    {'id': '98', 'title': ' 格子短裙长袖蓬蓬连衣裙  ', 'pic': '    ./images/411088d37ec21fd2742a0cdf43b02130.jpg    ', 'price': '  88   '},
    {'id': '99', 'title': ' 蝴蝶结一字领连衣裙短裙  ', 'pic': '    ./images/660785975b1d1b02db37e8afdd1f7a81.jpg    ', 'price': '  89   '},
    {'id': '100', 'title': '气质印花无袖背心连衣裙  ', 'pic': '    ./images/72b404b5fba83af9cc9a9afd92188346.jpg    ', 'price': '  78   '},
    {'id': '101', 'title': '高腰包臀荷叶边半身裙短裙     ', 'pic': '    ./images/17b717b6674bd4c399d82a1047097693.jpg    ', 'price': '  49   '},
    {'id': '102', 'title': '流苏开叉包臀牛仔裙    ', 'pic': '    ./images/87c4aa8c0150ec4893ce737b6e5960a2.jpg    ', 'price': '  49   '},
    {'id': '103', 'title': '名嫒气质显瘦格纹连衣裙  ', 'pic': '    ./images/20f62810734e9efefde11466588baa45.jpg    ', 'price': '  99   '},
    {'id': '104', 'title': '蝴蝶结一字领连衣裙短裙  ', 'pic': '    ./images/660785975b1d1b02db37e8afdd1f7a81.jpg    ', 'price': '  89   '},
    {'id': '105', 'title': 'HI夏季新款蝴蝶结百搭裙     ', 'pic': '    ./images/5e6a060e6343bdaf59e49a4dab669527.jpg    ', 'price': '  196  '},
    {'id': '106', 'title': '流苏开叉包臀牛仔裙    ', 'pic': '    ./images/87c4aa8c0150ec4893ce737b6e5960a2.jpg    ', 'price': '  49   '},
    {'id': '107', 'title': '韩版夏日薄款碎花连衣裙  ', 'pic': '    ./images/05bb0203db64c3cfea040ffb05e2e73c.jpg    ', 'price': '  89   '},
    {'id': '108', 'title': '气质印花无袖背心连衣裙  ', 'pic': '    ./images/72b404b5fba83af9cc9a9afd92188346.jpg    ', 'price': '  78   '},
    {'id': '109', 'title': '荷叶边显瘦鱼尾裙连衣裙  ', 'pic': '    ./images/7e6a98acea6308b72e3053187c425777.jpg    ', 'price': '  89   '},
    {'id': '110', 'title': 'HI夏季新款蝴蝶结百搭裙     ', 'pic': '    ./images/5e6a060e6343bdaf59e49a4dab669527.jpg    ', 'price': '  196  '},
    {'id': '111', 'title': '名嫒气质显瘦格纹连衣裙  ', 'pic': '    ./images/20f62810734e9efefde11466588baa45.jpg    ', 'price': '  99   '},
    {'id': '112', 'title': '气质印花无袖背心连衣裙  ', 'pic': '    ./images/72b404b5fba83af9cc9a9afd92188346.jpg    ', 'price': '  78   '},
    {'id': '113', 'title': '假两件无袖棉麻连衣裙   ', 'pic': '    ./images/2a6ab27548bb2b2229b261b3bebecfc6.jpg    ', 'price': '  98   '},
    {'id': '114', 'title': '韩版夏日薄款碎花连衣裙  ', 'pic': '    ./images/05bb0203db64c3cfea040ffb05e2e73c.jpg    ', 'price': '  89   '},
    {'id': '115', 'title': '名嫒气质显瘦格纹连衣裙  ', 'pic': '    ./images/20f62810734e9efefde11466588baa45.jpg    ', 'price': '  99   '},
    {'id': '116', 'title': '做旧磨边百搭背带牛仔裙  ', 'pic': '    ./images/a7265b027fbd56b4b540bdd0c74709ae.jpg    ', 'price': '  69   '},
    {'id': '117', 'title': '荷叶边显瘦鱼尾裙连衣裙  ', 'pic': '    ./images/7e6a98acea6308b72e3053187c425777.jpg    ', 'price': '  89   '},
    {'id': '118', 'title': '韩版夏日薄款碎花连衣裙  ', 'pic': '    ./images/05bb0203db64c3cfea040ffb05e2e73c.jpg    ', 'price': '  89   '},
    {'id': '119', 'title': '简约 露背系带连衣裙   ', 'pic': '    ./images/7cb5252f11b7181865986e9b1c813563.jpg    ', 'price': '  69   '},
    {'id': '120', 'title': '假两件无袖棉麻连衣裙   ', 'pic': '    ./images/2a6ab27548bb2b2229b261b3bebecfc6.jpg    ', 'price': '  98   '},
    {'id': '121', 'title': '荷叶边显瘦鱼尾裙连衣裙  ', 'pic': '    ./images/7e6a98acea6308b72e3053187c425777.jpg    ', 'price': '  89   '},
    {'id': '122', 'title': '印花蕾丝无袖欧根纱连衣裙     ', 'pic': '    ./images/7fab916d7f5ef61f2640ede509f96090.jpg    ', 'price': '  105  '},
    {'id': '123', 'title': '做旧磨边百搭背带牛仔裙  ', 'pic': '    ./images/a7265b027fbd56b4b540bdd0c74709ae.jpg    ', 'price': '  69   '},
    {'id': '124', 'title': '假两件无袖棉麻连衣裙   ', 'pic': '    ./images/2a6ab27548bb2b2229b261b3bebecfc6.jpg    ', 'price': '  98   '},
    {'id': '125', 'title': '气质荷叶袖包臀裙连衣裙  ', 'pic': '    ./images/10de0fbefd1750dc5c81fad66b3636d9.jpg    ', 'price': '  70   '},
    {'id': '126', 'title': '简约 露背系带连衣裙   ', 'pic': '    ./images/7cb5252f11b7181865986e9b1c813563.jpg    ', 'price': '  69   '},
    {'id': '127', 'title': '做旧磨边百搭背带牛仔裙  ', 'pic': '    ./images/a7265b027fbd56b4b540bdd0c74709ae.jpg    ', 'price': '  69   '},
    {'id': '128', 'title': '雪纺波西米亚长裙半身裙  ', 'pic': '    ./images/cdeff333d4b50df78e19f9f8fe9e1f94.jpg    ', 'price': '  68   '},
    {'id': '129', 'title': '印花蕾丝无袖欧根纱连衣裙     ', 'pic': '    ./images/7fab916d7f5ef61f2640ede509f96090.jpg    ', 'price': '  105  '},
    {'id': '130', 'title': '简约 露背系带连衣裙   ', 'pic': '    ./images/7cb5252f11b7181865986e9b1c813563.jpg    ', 'price': '  69   '},
    {'id': '131', 'title': '气质荷叶袖包臀裙连衣裙  ', 'pic': '    ./images/10de0fbefd1750dc5c81fad66b3636d9.jpg    ', 'price': '  70   '},
    {'id': '132', 'title': '海军风T恤裙短裙连衣裙  ', 'pic': '    ./images/688afce2e4d490ce99f191f474083e81.jpg    ', 'price': '  57   '},
    {'id': '133', 'title': '印花蕾丝无袖欧根纱连衣裙     ', 'pic': '    ./images/7fab916d7f5ef61f2640ede509f96090.jpg    ', 'price': '  105  '},
    {'id': '134', 'title': '雪纺波西米亚长裙半身裙  ', 'pic': '    ./images/cdeff333d4b50df78e19f9f8fe9e1f94.jpg    ', 'price': '  68   '},
    {'id': '135', 'title': '气质荷叶袖包臀裙连衣裙  ', 'pic': '    ./images/10de0fbefd1750dc5c81fad66b3636d9.jpg    ', 'price': '  70   '},
    {'id': '136', 'title': '海军风T恤裙短裙连衣裙  ', 'pic': '    ./images/688afce2e4d490ce99f191f474083e81.jpg    ', 'price': '  57   '},
    {'id': '137', 'title': '雪纺波西米亚长裙半身裙  ', 'pic': '    ./images/cdeff333d4b50df78e19f9f8fe9e1f94.jpg    ', 'price': '  68   '},
    {'id': '138', 'title': '海军风T恤裙短裙连衣裙  ', 'pic': '    ./images/688afce2e4d490ce99f191f474083e81.jpg    ', 'price': '  57   '},
    {'id': '139', 'title': '韩版数字83号连衣裙   ', 'pic': '    ./images/24dd4dad34f6fd86527402fb3607de9a.jpg    ', 'price': '  48   '},
    {'id': '140', 'title': '短袖气质欧根纱连衣裙   ', 'pic': '    ./images/30827ae7fe308bbae7a546f70e50cb7e.jpg    ', 'price': '  95   '},
    {'id': '141', 'title': '字母T恤拼接牛仔裙连衣裙     ', 'pic': '    ./images/e041ac8e36a59388212d2870c3069688.jpg    ', 'price': '  88   '},
    {'id': '142', 'title': '百搭半身牛仔包臀短裙   ', 'pic': '    ./images/5039e7d0fd0cfb9af0981b3c485dc01b.jpg    ', 'price': '  89   '},
    {'id': '143', 'title': '2015超值百褶小短裙裤     ', 'pic': '    ./images/5371cf3470567d61127a9b9194e57e79.jpg    ', 'price': '  70   '},
    {'id': '144', 'title': '仙人掌印花宽松大码连衣裙     ', 'pic': '    ./images/fd07bb56695b332a326417ac8638a4f2.jpg    ', 'price': '  79   '},
    {'id': '145', 'title': '大牌无袖雪纺短裙连衣裙  ', 'pic': '    ./images/92f157fd6800eb3cd0258031a2a90c40.jpg    ', 'price': '  79   '},
    {'id': '146', 'title': '亮片短袖下摆拼纱连衣裙  ', 'pic': '    ./images/b0c737ee5c99eb09da88494408d09d85.jpg    ', 'price': '  79   '},
    {'id': '147', 'title': '韩版棉麻蝴蝶结腰带连衣裙     ', 'pic': '    ./images/d501a5566d135dbd6cdc144f3190cd52.jpg    ', 'price': '  79   '},
    {'id': '148', 'title': '韩版背心高腰圆领连衣裙  ', 'pic': '    ./images/4e46c4fe07ba36cf78ba03b4330a2291.jpg    ', 'price': '  69   '},
    {'id': '149', 'title': '韩版海军风露肩短裙连衣裙     ', 'pic': '    ./images/59eaf0d95e3e7335825bf8d62054bc1e.jpg    ', 'price': '  49   '},
    {'id': '150', 'title': '夏季不规则印花短裙半身裙     ', 'pic': '    ./images/3efe7262d88c3e74cfe0c0142d140537.jpg    ', 'price': '  60   '},
    {'id': '151', 'title': '初夏新品高腰雪纺显瘦短裙     ', 'pic': '    ./images/508643dd9359127eccc8c3313cdd3fcf.jpg    ', 'price': '  55   '},
    {'id': '152', 'title': '纯色包臀荷叶高腰半身裙  ', 'pic': '    ./images/6edcea4e40d931656049a536bf39402e.jpg    ', 'price': '  89   '},
    {'id': '153', 'title': '无袖条纹蕾丝拼接连衣裙  ', 'pic': '    ./images/2025fa1af657688c221f9e7333876641.jpg    ', 'price': '  89   '},
    {'id': '154', 'title': '大码弹力短裙糖果色20色     ', 'pic': '    ./images/1cf23b258b736de278f8f1ea4f49a9c5.jpg    ', 'price': '  30   '},
    {'id': '155', 'title': '初夏连衣裙    ', 'pic': '    ./images/339f7d0ad1b920495f81fdf9f541cb84.jpg    ', 'price': '  55   '},
    {'id': '156', 'title': 'PU高腰百褶短裙伞裙皮裙     ', 'pic': '    ./images/ed84dfcffccb67c0d41f795ccf8c3d43.jpg    ', 'price': '  35   '},
    {'id': '157', 'title': '纯色勾花镂空A字连衣裙  ', 'pic': '    ./images/952b43f4275984bea9c15f5efa0209eb.jpg    ', 'price': '  359  '},
    {'id': '158', 'title': '印花宽松T恤大摆短裙套装     ', 'pic': '    ./images/a85a51396cd287ab726b7d76e9743224.jpg    ', 'price': '  79   '},
    {'id': '159', 'title': '无袖潮流斗篷连衣裙    ', 'pic': '    ./images/024e31c9b94586bcb09d90eb4cf51e13.jpg    ', 'price': '  89   '},
    {'id': '160', 'title': '喇叭短袖印花雪纺裙连衣裙     ', 'pic': '    ./images/e1803a057a52a33075b35395657726b6.jpg    ', 'price': '  69   '},
    {'id': '161', 'title': '夏装印花连衣裙 送腰带  ', 'pic': '    ./images/7cc01988e8351940f072db93319f1bcd.jpg    ', 'price': '  128  '},
    {'id': '162', 'title': '初夏波西米亚露肩连衣裙  ', 'pic': '    ./images/2def2b6c64c406a1874e3a890df242f0.jpg    ', 'price': '  98   '},
    {'id': '163', 'title': '春夏新款雪纺吊带连衣裙  ', 'pic': '    ./images/44f28d3dbb2aabe3b86e254692993bb2.jpg    ', 'price': '  71   '},
    {'id': '164', 'title': '欧美范休闲短袖连衣裙   ', 'pic': '    ./images/4301a676952a1e16fcf7459995ccf650.jpg    ', 'price': '  69   '},
    {'id': '165', 'title': '气质纯色背带裙连衣裙   ', 'pic': '    ./images/99a76739515905f6004c8e32ab903206.jpg    ', 'price': '  79   '},
    {'id': '166', 'title': '夏季条纹网纱无袖连衣裙  ', 'pic': '    ./images/625aa837def4cad7c7c05f6fc88a8489.jpg    ', 'price': '  119  '},
    {'id': '167', 'title': '字母棉料接拼牛仔连衣裙  ', 'pic': '    ./images/4331c3b9def4ff975ff8952634143689.jpg    ', 'price': '  79   '},
    {'id': '168', 'title': '新款叶边鱼尾包臀半身裙  ', 'pic': '    ./images/1650fc37e0b7d04c65ced61942a4089a.jpg    ', 'price': '  68   '},
    {'id': '169', 'title': '欧美风高腰AA牛仔短裙  ', 'pic': '    ./images/499b51a15427fcfa403553fe97dd318e.jpg    ', 'price': '  70   '},
    {'id': '170', 'title': '夏季新款宽松印花连衣裙  ', 'pic': '    ./images/6db11a259f16264243e490276fe029a0.jpg    ', 'price': '  138  '},
    {'id': '171', 'title': '韩版背心连衣裙短裙蓬蓬裙     ', 'pic': '    ./images/4996c857b17d917a448c8ccaededd837.jpg    ', 'price': '  78   '},
    {'id': '172', 'title': '假两件针织T恤 牛仔裙  ', 'pic': '    ./images/b92edc5a8ae04e048dffb41e313adcd6.jpg    ', 'price': '  127  '},
    {'id': '173', 'title': '网纱短袖亮片印花连衣裙  ', 'pic': '    ./images/09f9a0ec8510367f1db415b25471abd5.jpg    ', 'price': '  59   '},
    {'id': '174', 'title': '夏季亚麻打底裙连衣裙短裙     ', 'pic': '    ./images/ec75246697d7b9565d080ec56ecdaf45.jpg    ', 'price': '  47   '},
    {'id': '175', 'title': '飞飞袖荷叶边包臀连衣裙  ', 'pic': '    ./images/9d59e3921141905b4ff1f71bd0ee479e.jpg    ', 'price': '  98   '},
    {'id': '176', 'title': '镂空领性感修身连衣裙短  ', 'pic': '    ./images/8e81a37991a0ea41e4bde9dd0a3c2db5.jpg    ', 'price': '  69   '},
    {'id': '177', 'title': '夏装印花撞色短袖连衣裙  ', 'pic': '    ./images/8a9250b0e0be9093cfa4a7b4d7c3474b.jpg    ', 'price': '  105  '},
    {'id': '178', 'title': 'HI夏季新款印花A字裙  ', 'pic': '    ./images/19a00fe319b37cd6f20ef6c810c3f96d.jpg    ', 'price': '  168  '},
    {'id': '179', 'title': '修身蕾丝牛仔印花连衣裙  ', 'pic': '    ./images/89978655633d84a7f946b9a1c069bc07.jpg    ', 'price': '  69   '},
    {'id': '180', 'title': '欧根纱拼接纯色蛋糕连衣裙     ', 'pic': '    ./images/cc515dac6f3b6f6176f04dd8cd24a75d.jpg    ', 'price': '  79   '},
    {'id': '181', 'title': '全棉针织运动连衣裙    ', 'pic': '    ./images/4fb0d684533f8b555d16d4fe713ff93a.jpg    ', 'price': '  48   '},
    {'id': '182', 'title': '破洞牛仔短裙   ', 'pic': '    ./images/f94dae82182ebd2e4d828a455afa12b6.jpg    ', 'price': '  89   '},
    {'id': '183', 'title': '卡通印花短袖T恤连衣裙  ', 'pic': '    ./images/cb27d980a61d73b11264a6b1e337554b.jpg    ', 'price': '  65   '},
    {'id': '184', 'title': '小清新印花雪纺裙短裙   ', 'pic': '    ./images/812a0465eb7644fbe1f974a8d79a2cc6.jpg    ', 'price': '  78   '},
    {'id': '185', 'title': '韩国气质褶皱显瘦短裙潮  ', 'pic': '    ./images/930c35f72a75ece04ecff322b75cbed2.jpg    ', 'price': '  55   '},
    {'id': '186', 'title': '韩国气质褶皱显瘦短裙潮  ', 'pic': '    ./images/930c35f72a75ece04ecff322b75cbed2.jpg    ', 'price': '  55   '},
    {'id': '187', 'title': '拼色宽松短款连衣裙    ', 'pic': '    ./images/01884e43a82f280c426e59612e02b0ed.jpg    ', 'price': '  78   '},
    {'id': '188', 'title': '韩国气质褶皱显瘦短裙潮  ', 'pic': '    ./images/930c35f72a75ece04ecff322b75cbed2.jpg    ', 'price': '  55   '},
    {'id': '189', 'title': '韩国气质褶皱显瘦短裙潮  ', 'pic': '    ./images/930c35f72a75ece04ecff322b75cbed2.jpg    ', 'price': '  55   '},
    {'id': '190', 'title': '圆领背心连衣裙背心短裙  ', 'pic': '    ./images/76aa8248f86cb7476693425b658c5f0e.jpg    ', 'price': '  66   '},
    {'id': '191', 'title': '蕾丝A字裙宽松打底连衣裙     ', 'pic': '    ./images/4b4a0bf39c9298e0f6484f9237220c11.jpg    ', 'price': '  68   '},
    {'id': '192', 'title': '蕾丝A字裙宽松打底连衣裙     ', 'pic': '    ./images/4b4a0bf39c9298e0f6484f9237220c11.jpg    ', 'price': '  68   '},
    {'id': '193', 'title': '韩版短裙A字牛仔半身裙  ', 'pic': '    ./images/df8a144f77f587afa468cecdbd068b2b.jpg    ', 'price': '  67   '},
    {'id': '194', 'title': '蕾丝A字裙宽松打底连衣裙     ', 'pic': '    ./images/4b4a0bf39c9298e0f6484f9237220c11.jpg    ', 'price': '  68   '},
    {'id': '195', 'title': '蕾丝A字裙宽松打底连衣裙     ', 'pic': '    ./images/4b4a0bf39c9298e0f6484f9237220c11.jpg    ', 'price': '  68   '},
    {'id': '196', 'title': '名媛V领吊带蓬蓬连衣裙  ', 'pic': '    ./images/913bdd9a78fe1e34eeeb58cbd1fbb633.jpg    ', 'price': '  85   '},
    {'id': '197', 'title': '螺纹小包裙    ', 'pic': '    ./images/fb2c3bc89e74371140d73333f62110a6.jpg    ', 'price': '  59   '},
    {'id': '198', 'title': '名媛V领吊带蓬蓬连衣裙  ', 'pic': '    ./images/913bdd9a78fe1e34eeeb58cbd1fbb633.jpg    ', 'price': '  85   '},
    {'id': '199', 'title': '名媛V领吊带蓬蓬连衣裙  ', 'pic': '    ./images/913bdd9a78fe1e34eeeb58cbd1fbb633.jpg    ', 'price': '  85   '},
    {'id': '200', 'title': '韩版修身漏背收腰连衣裙  ', 'pic': '    ./images/2be995e415ba3159d553fce1a34ace3e.jpg    ', 'price': '  88   '},
    {'id': '201', 'title': '前后V领连衣短裙B19  ', 'pic': '    ./images/8495bd7618608a45383917145911e796.jpg    ', 'price': '  49   '},
    {'id': '202', 'title': '名媛V领吊带蓬蓬连衣裙  ', 'pic': '    ./images/913bdd9a78fe1e34eeeb58cbd1fbb633.jpg    ', 'price': '  85   '},
    {'id': '203', 'title': '韩版修身漏背收腰连衣裙  ', 'pic': '    ./images/2be995e415ba3159d553fce1a34ace3e.jpg    ', 'price': '  88   '},
    {'id': '204', 'title': '2015新品牛仔包裙破洞     ', 'pic': '    ./images/f799cdc0f912f61349d93cc8bdf243ba.jpg    ', 'price': '  69   '},
    {'id': '205', 'title': '韩版修身漏背收腰连衣裙  ', 'pic': '    ./images/2be995e415ba3159d553fce1a34ace3e.jpg    ', 'price': '  88   '},
    {'id': '206', 'title': '波西米亚无袖印花雪纺裙  ', 'pic': '    ./images/78c3c268da2745410cf65aab17ecfd67.jpg    ', 'price': '  88   '},
    {'id': '207', 'title': '韩版修身漏背收腰连衣裙  ', 'pic': '    ./images/2be995e415ba3159d553fce1a34ace3e.jpg    ', 'price': '  88   '},
    {'id': '208', 'title': '2015新品牛仔包裙破洞     ', 'pic': '    ./images/f799cdc0f912f61349d93cc8bdf243ba.jpg    ', 'price': '  69   '},
    {'id': '209', 'title': '2015高腰牛仔包裙短裙     ', 'pic': '    ./images/8e0d550f28c3f8ad6fc6ebbe4f62ea7b.jpg    ', 'price': '  69   '},
    {'id': '210', 'title': '2015新品牛仔包裙破洞     ', 'pic': '    ./images/f799cdc0f912f61349d93cc8bdf243ba.jpg    ', 'price': '  69   '},
    {'id': '211', 'title': '夏装牛仔吊带半身裙    ', 'pic': '    ./images/2ddd49e027207b180847b408cd10bc5b.jpg    ', 'price': '  75   '},
    {'id': '212', 'title': '2015高腰牛仔包裙短裙     ', 'pic': '    ./images/8e0d550f28c3f8ad6fc6ebbe4f62ea7b.jpg    ', 'price': '  69   '},
    {'id': '213', 'title': '2015新品牛仔包裙破洞     ', 'pic': '    ./images/f799cdc0f912f61349d93cc8bdf243ba.jpg    ', 'price': '  69   '},
    {'id': '214', 'title': '春夏新款显瘦雪纺连衣裙  ', 'pic': '    ./images/47ce394385623a43d31d5ce4223fe210.jpg    ', 'price': '  128  '},
    {'id': '215', 'title': '2015高腰牛仔包裙短裙     ', 'pic': '    ./images/8e0d550f28c3f8ad6fc6ebbe4f62ea7b.jpg    ', 'price': '  69   '},
    {'id': '216', 'title': '修身圆领镂空短袖连衣裙  ', 'pic': '    ./images/9daa953293cd012ebe1d33573ecd7328.jpg    ', 'price': '  68   '},
    {'id': '217', 'title': '2015高腰牛仔包裙短裙     ', 'pic': '    ./images/8e0d550f28c3f8ad6fc6ebbe4f62ea7b.jpg    ', 'price': '  69   '},
    {'id': '218', 'title': '春夏新款显瘦雪纺连衣裙  ', 'pic': '    ./images/47ce394385623a43d31d5ce4223fe210.jpg    ', 'price': '  128  '},
    {'id': '219', 'title': '交叉肩带连衣裙  ', 'pic': '    ./images/03134213489fefcdf898719d50f0ccf7.jpg    ', 'price': '  79   '},
    {'id': '220', 'title': '春夏新款显瘦雪纺连衣裙  ', 'pic': '    ./images/47ce394385623a43d31d5ce4223fe210.jpg    ', 'price': '  128  '},
    {'id': '221', 'title': '夏季修身两件套连衣长裙  ', 'pic': '    ./images/8adaff7518165f53986f9bc3e6d82877.jpg    ', 'price': '  99   '},
    {'id': '222', 'title': '春夏新款显瘦雪纺连衣裙  ', 'pic': '    ./images/47ce394385623a43d31d5ce4223fe210.jpg    ', 'price': '  128  '},
    {'id': '223', 'title': '交叉肩带连衣裙  ', 'pic': '    ./images/03134213489fefcdf898719d50f0ccf7.jpg    ', 'price': '  79   '},
    {'id': '224', 'title': '韩版条纹梦幻连衣裙    ', 'pic': '    ./images/f17a6f45cc18673baf4dd125b35f25e8.jpg    ', 'price': '  69   '},
    {'id': '225', 'title': '交叉肩带连衣裙  ', 'pic': '    ./images/03134213489fefcdf898719d50f0ccf7.jpg    ', 'price': '  79   '},
    {'id': '226', 'title': '印花修身A字裙无袖连衣裙     ', 'pic': '    ./images/ee97bc70170e8c9b4b7f3a0d1b5366be.jpg    ', 'price': '  79   '},
    {'id': '227', 'title': '交叉肩带连衣裙  ', 'pic': '    ./images/03134213489fefcdf898719d50f0ccf7.jpg    ', 'price': '  79   '},
    {'id': '228', 'title': '夏季韩版针织包臀连衣裙  ', 'pic': '    ./images/b1daf44ac8846ba8b040208c68a9d5c2.jpg    ', 'price': '  79   '},
    {'id': '229', 'title': '韩版条纹梦幻连衣裙    ', 'pic': '    ./images/f17a6f45cc18673baf4dd125b35f25e8.jpg    ', 'price': '  69   '},
    {'id': '230', 'title': '韩版条纹梦幻连衣裙    ', 'pic': '    ./images/f17a6f45cc18673baf4dd125b35f25e8.jpg    ', 'price': '  69   '},
    {'id': '231', 'title': 'V领黑色名媛内搭短裙   ', 'pic': '    ./images/f3ec263f957cab7af116fa1ff4588a47.jpg    ', 'price': '  270  '},
    {'id': '232', 'title': '韩版条纹梦幻连衣裙    ', 'pic': '    ./images/f17a6f45cc18673baf4dd125b35f25e8.jpg    ', 'price': '  69   '},
    {'id': '233', 'title': '韩版显瘦雪纺连衣裙短裙  ', 'pic': '    ./images/3ab49bda748a06eea65a7a3446c23b7a.jpg    ', 'price': '  109  '},
    {'id': '234', 'title': '夏季韩版针织包臀连衣裙  ', 'pic': '    ./images/b1daf44ac8846ba8b040208c68a9d5c2.jpg    ', 'price': '  79   '},
    {'id': '235', 'title': '夏季韩版针织包臀连衣裙  ', 'pic': '    ./images/b1daf44ac8846ba8b040208c68a9d5c2.jpg    ', 'price': '  79   '},
    {'id': '236', 'title': '春夏新品性感露肩连衣裙  ', 'pic': '    ./images/3597b8d000ec2955702c830e81e04d5b.jpg    ', 'price': '  109  '},
    {'id': '237', 'title': '夏季韩版针织包臀连衣裙  ', 'pic': '    ./images/b1daf44ac8846ba8b040208c68a9d5c2.jpg    ', 'price': '  79   '},
    {'id': '238', 'title': '韩版复古显瘦牛仔背带裙  ', 'pic': '    ./images/34419efcf109566faf2c7a12107552e6.jpg    ', 'price': '  79   '},
    {'id': '239', 'title': '韩版显瘦雪纺连衣裙短裙  ', 'pic': '    ./images/3ab49bda748a06eea65a7a3446c23b7a.jpg    ', 'price': '  109  '},
    {'id': '240', 'title': '韩版显瘦雪纺连衣裙短裙  ', 'pic': '    ./images/3ab49bda748a06eea65a7a3446c23b7a.jpg    ', 'price': '  109  '},
    {'id': '241', 'title': '夏季韩版一字领印花连衣裙     ', 'pic': '    ./images/aba4c58be78ac44977e8f25be2dfe57a.jpg    ', 'price': '  69   '},
    {'id': '242', 'title': '韩版显瘦雪纺连衣裙短裙  ', 'pic': '    ./images/3ab49bda748a06eea65a7a3446c23b7a.jpg    ', 'price': '  109  '},
    {'id': '243', 'title': '韩版钩花镂空蕾丝连衣裙  ', 'pic': '    ./images/dd721fd414d819b1253caa462fd11c08.jpg    ', 'price': '  139  '},
    {'id': '244', 'title': '韩版复古显瘦牛仔背带裙  ', 'pic': '    ./images/34419efcf109566faf2c7a12107552e6.jpg    ', 'price': '  79   '},
    {'id': '245', 'title': '韩版复古显瘦牛仔背带裙  ', 'pic': '    ./images/34419efcf109566faf2c7a12107552e6.jpg    ', 'price': '  79   '},
    {'id': '246', 'title': '学院风宽松牛仔背带连衣裙     ', 'pic': '    ./images/8b1618d1baa9265c0195225dea7463fb.jpg    ', 'price': '  75   '},
    {'id': '247', 'title': '韩版复古显瘦牛仔背带裙  ', 'pic': '    ./images/34419efcf109566faf2c7a12107552e6.jpg    ', 'price': '  79   '},
    {'id': '248', 'title': '[预售]名族风刺绣深V领连衣裙  ', 'pic': '    ./images/f7ca4df5f1e716d33495c6bdf3603c87.jpg    ', 'price': '  109  '},
    {'id': '249', 'title': '韩版钩花镂空蕾丝连衣裙  ', 'pic': '    ./images/dd721fd414d819b1253caa462fd11c08.jpg    ', 'price': '  139  '},
    {'id': '250', 'title': '韩版钩花镂空蕾丝连衣裙  ', 'pic': '    ./images/dd721fd414d819b1253caa462fd11c08.jpg    ', 'price': '  139  '},
    {'id': '251', 'title': '韩版钩花镂空蕾丝连衣裙  ', 'pic': '    ./images/dd721fd414d819b1253caa462fd11c08.jpg    ', 'price': '  139  '},
    {'id': '252', 'title': '正版欧根纱披肩连衣裙   ', 'pic': '    ./images/a59d5380b9a67472faa4f783af3f941f.jpg    ', 'price': '  89   '},
    {'id': '253', 'title': '[预售]名族风刺绣深V领连衣裙  ', 'pic': '    ./images/f7ca4df5f1e716d33495c6bdf3603c87.jpg    ', 'price': '  109  '},
    {'id': '254', 'title': '[预售]名族风刺绣深V领连衣裙  ', 'pic': '    ./images/f7ca4df5f1e716d33495c6bdf3603c87.jpg    ', 'price': '  109  '},
    {'id': '255', 'title': '[预售]名族风刺绣深V领连衣裙  ', 'pic': '    ./images/f7ca4df5f1e716d33495c6bdf3603c87.jpg    ', 'price': '  109  '},
    {'id': '256', 'title': '灯笼袖网纱连衣裙     ', 'pic': '    ./images/ba47ea9c70aab0108e2ee8cd058ede18.jpg    ', 'price': '  89   '},
    {'id': '257', 'title': '正版欧根纱披肩连衣裙   ', 'pic': '    ./images/a59d5380b9a67472faa4f783af3f941f.jpg    ', 'price': '  89   '},
    {'id': '258', 'title': '正版欧根纱披肩连衣裙   ', 'pic': '    ./images/a59d5380b9a67472faa4f783af3f941f.jpg    ', 'price': '  89   '},
    {'id': '259', 'title': '正版欧根纱披肩连衣裙   ', 'pic': '    ./images/a59d5380b9a67472faa4f783af3f941f.jpg    ', 'price': '  89   '},
    {'id': '260', 'title': '破洞欧美风牛仔短裙    ', 'pic': '    ./images/ab573e563c271e98cafab9a36ffd6d36.jpg    ', 'price': '  49   '},
    {'id': '261', 'title': '灯笼袖网纱连衣裙     ', 'pic': '    ./images/ba47ea9c70aab0108e2ee8cd058ede18.jpg    ', 'price': '  89   '},
    {'id': '262', 'title': '灯笼袖网纱连衣裙     ', 'pic': '    ./images/ba47ea9c70aab0108e2ee8cd058ede18.jpg    ', 'price': '  89   '},
    {'id': '263', 'title': '灯笼袖网纱连衣裙     ', 'pic': '    ./images/ba47ea9c70aab0108e2ee8cd058ede18.jpg    ', 'price': '  89   '},
    {'id': '264', 'title': '夏刺绣A字裙欧根纱连衣裙     ', 'pic': '    ./images/2054540a06a0c46019660bca9d0850bd.jpg    ', 'price': '  88   '},
    {'id': '265', 'title': '破洞欧美风牛仔短裙    ', 'pic': '    ./images/ab573e563c271e98cafab9a36ffd6d36.jpg    ', 'price': '  49   '},
    {'id': '266', 'title': '破洞欧美风牛仔短裙    ', 'pic': '    ./images/ab573e563c271e98cafab9a36ffd6d36.jpg    ', 'price': '  49   '},
    {'id': '267', 'title': '破洞欧美风牛仔短裙    ', 'pic': '    ./images/ab573e563c271e98cafab9a36ffd6d36.jpg    ', 'price': '  49   '},
    {'id': '268', 'title': '韩版蕾丝短裙背心裙连衣裙     ', 'pic': '    ./images/f9526cafcc30994e90feaec0becd8c59.jpg    ', 'price': '  89   '},
    {'id': '269', 'title': '夏刺绣A字裙欧根纱连衣裙     ', 'pic': '    ./images/2054540a06a0c46019660bca9d0850bd.jpg    ', 'price': '  88   '},
    {'id': '270', 'title': '夏刺绣A字裙欧根纱连衣裙     ', 'pic': '    ./images/2054540a06a0c46019660bca9d0850bd.jpg    ', 'price': '  88   '},
    {'id': '271', 'title': '夏刺绣A字裙欧根纱连衣裙     ', 'pic': '    ./images/2054540a06a0c46019660bca9d0850bd.jpg    ', 'price': '  88   '},
    {'id': '272', 'title': '吊带露肩一字领连衣裙短裙     ', 'pic': '    ./images/3f4f9664d95771901014a2e95110970c.jpg    ', 'price': '  65   '},
    {'id': '273', 'title': '韩版蕾丝短裙背心裙连衣裙     ', 'pic': '    ./images/f9526cafcc30994e90feaec0becd8c59.jpg    ', 'price': '  89   '},
    {'id': '274', 'title': '韩版蕾丝短裙背心裙连衣裙     ', 'pic': '    ./images/f9526cafcc30994e90feaec0becd8c59.jpg    ', 'price': '  89   '},
    {'id': '275', 'title': '韩版蕾丝短裙背心裙连衣裙     ', 'pic': '    ./images/f9526cafcc30994e90feaec0becd8c59.jpg    ', 'price': '  89   '},
    {'id': '276', 'title': '吊带露肩一字领连衣裙短裙     ', 'pic': '    ./images/3f4f9664d95771901014a2e95110970c.jpg    ', 'price': '  65   '},
    {'id': '277', 'title': '吊带露肩一字领连衣裙短裙     ', 'pic': '    ./images/3f4f9664d95771901014a2e95110970c.jpg    ', 'price': '  65   '},
    {'id': '278', 'title': '吊带露肩一字领连衣裙短裙     ', 'pic': '    ./images/3f4f9664d95771901014a2e95110970c.jpg    ', 'price': '  65   '},
]

for a in arr:
    sql = 'insert into goods value ({id}, "{title}", "{pic}", {price})'.format(**a)
    print(sql)
    cursor.execute(sql)

connection.commit()






