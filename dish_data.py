ingredients = {
    "Leek": 185, "Mushroom": 167, "Egg": 115, "Potato": 124, "Apple": 90,
    "Herb": 130, "Sausage": 103, "Milk": 98, "Honey": 101, "Oil": 121,
    "Ginger": 109, "Tomato": 110, "Cacao": 151, "Tail": 342, "Soybeans": 100
}
	
all_dishes = {
    "curries": {
        "Fancy Apple Curry": {
            "multiplier": 1.06, "power": [668, 681, 695, 708, 721, 728, 741, 755, 775, 788, 795, 808, 822, 828, 842, 855, 868, 875, 888, 902, 915, 935, 949, 969, 982, 1002, 1015, 1035, 1055, 1075, 1096, 1116, 1136, 1162, 1182, 1209, 1229, 1256, 1283, 1309, 1336, 1363, 1389, 1423, 1450, 1483, 1516, 1550, 1583, 1617], "amount": 7,
            "ingredients": {
                "Apple": 7
            }
        },
        "Simple Chowder": {
            "multiplier": 1.06, "power": [727, 742, 756, 771, 785, 792, 807, 822, 843, 858, 865, 880, 894, 901, 916, 931, 945, 952, 967, 981, 996, 1018, 1032, 1054, 1069, 1091, 1105, 1127, 1149, 1170, 1192, 1214, 1236, 1265, 1287, 1316, 1338, 1367, 1396, 1425, 1454, 1483, 1512, 1549, 1578, 1614, 1650, 1687, 1723, 1759], "amount": 7,
            "ingredients": {
                "Milk": 7
            }
        },
        "Beanburger Curry": {
            "multiplier": 1.06, "power": [764, 779, 795, 810, 825, 833, 848, 863, 886, 902, 909, 924, 940, 947, 963, 978, 993, 1001, 1016, 1031, 1047, 1070, 1085, 1108, 1123, 1146, 1161, 1184, 1207, 1230, 1253, 1276, 1299, 1329, 1352, 1383, 1406, 1436, 1467, 1497, 1528, 1559, 1589, 1627, 1658, 1696, 1734, 1772, 1811, 1849], "amount": 7,
            "ingredients": {
                "Sausage": 7
            }
        },
        "Mild Honey Curry": {
            "multiplier": 1.06, "power": [749, 764, 779, 794, 809, 816, 831, 846, 869, 884, 891, 906, 921, 929, 944, 959, 974, 981, 996, 1011, 1026, 1049, 1064, 1086, 1101, 1124, 1138, 1161, 1183, 1206, 1228, 1251, 1273, 1303, 1326, 1356, 1378, 1408, 1438, 1468, 1498, 1528, 1558, 1595, 1625, 1663, 1700, 1738, 1775, 1813], "amount": 7,
            "ingredients": {
                "Honey": 7
            }
        },
        "Solar Power Tomato Curry": {
            "multiplier": 1.11, "power": [1943, 1982, 2021, 2060, 2098, 2118, 2157, 2196, 2254, 2293, 2312, 2351, 2390, 2409, 2448, 2487, 2526, 2545, 2584, 2623, 2662, 2720, 2759, 2817, 2856, 2915, 2953, 3012, 3070, 3128, 3187, 3245, 3303, 3381, 3439, 3517, 3575, 3653, 3731, 3808, 3886, 3964, 4041, 4139, 4216, 4313, 4411, 4508, 4605, 4702], "amount": 15,
            "ingredients": {
                "Tomato": 10,
                "Herb": 5
            }
        },
        "Drought Katsu Curry": {
            "multiplier": 1.11, "power": [1815, 1851, 1888, 1924, 1960, 1978, 2015, 2051, 2105, 2142, 2160, 2196, 2232, 2251, 2287, 2323, 2360, 2378, 2414, 2450, 2487, 2541, 2577, 2632, 2668, 2723, 2759, 2813, 2868, 2922, 2977, 3031, 3086, 3158, 3213, 3285, 3340, 3412, 3485, 3557, 3630, 3703, 3775, 3866, 3939, 4029, 4120, 4211, 4302, 4392], "amount": 15,
            "ingredients": {
                "Sausage": 10,
                "Oil": 5
            }
        },
        "Hearty Cheeseburger Curry": {
            "multiplier": 1.11, "power": [1785, 1821, 1856, 1892, 1928, 1946, 1981, 2017, 2071, 2106, 2124, 2160, 2196, 2213, 2249, 2285, 2321, 2338, 2374, 2410, 2445, 2499, 2535, 2588, 2624, 2678, 2713, 2767, 2820, 2874, 2927, 2981, 3035, 3106, 3159, 3231, 3284, 3356, 3427, 3499, 3570, 3641, 3713, 3802, 3873, 3963, 4052, 4141, 4230, 4320], "amount": 16,
            "ingredients": {
                "Milk": 8,
                "Sausage": 8
            }
        },
        "Melty Omelette Curry": {
            "multiplier": 1.11, "power": [2009, 2049, 2089, 2130, 2170, 2190, 2230, 2270, 2330, 2371, 2391, 2431, 2471, 2491, 2531, 2572, 2612, 2632, 2672, 2712, 2752, 2813, 2853, 2913, 2953, 3014, 3054, 3114, 3174, 3234, 3295, 3355, 3415, 3496, 3556, 3636, 3697, 3777, 3857, 3938, 4018, 4098, 4179, 4279, 4360, 4460, 4560, 4661, 4761, 4862], "amount": 16,
            "ingredients": {
                "Tomato": 6,
                "Egg": 10
            }
        },
        "Soft Potato Chowder": {
            "multiplier": 1.17, "power": [3089, 3151, 3213, 3274, 3336, 3367, 3429, 3491, 3583, 3645, 3676, 3738, 3799, 3830, 3892, 3954, 4016, 4047, 4108, 4170, 4232, 4325, 4386, 4479, 4541, 4634, 4695, 4788, 4881, 4973, 5066, 5159, 5251, 5375, 5468, 5591, 5684, 5807, 5931, 6054, 6178, 6302, 6425, 6580, 6703, 6858, 7012, 7166, 7321, 7475], "amount": 22,
            "ingredients": {
                "Milk": 10,
                "Potato": 8,
                "Mushroom": 4
            }
        },
        "Spore Mushroom Curry": {
            "multiplier": 1.17, "power": [4041, 4122, 4203, 4283, 4364, 4405, 4486, 4566, 4688, 4768, 4809, 4890, 4970, 5011, 5092, 5172, 5253, 5294, 5375, 5455, 5536, 5657, 5738, 5859, 5940, 6062, 6142, 6264, 6385, 6506, 6627, 6748, 6870, 7031, 7153, 7314, 7435, 7597, 7759, 7920, 8082, 8244, 8405, 8607, 8769, 8971, 9173, 9375, 9577, 9779], "amount": 23,
            "ingredients": {
                "Potato": 9,
                "Mushroom": 14
            }
        },
        "Bulk Up Bean Curry": {
            "multiplier": 1.17, "power": [3274, 3339, 3405, 3470, 3536, 3569, 3634, 3700, 3798, 3863, 3896, 3962, 4027, 4060, 4125, 4191, 4256, 4289, 4354, 4420, 4485, 4584, 4649, 4747, 4813, 4911, 4976, 5075, 5173, 5271, 5369, 5468, 5566, 5697, 5795, 5926, 6024, 6155, 6286, 6417, 6548, 6679, 6810, 6974, 7105, 7268, 7432, 7596, 7759, 7923], "amount": 26,
            "ingredients": {
                "Soybeans": 12,
                "Sausage": 6,
                "Egg": 4,
                "Herb": 4
            }
        },
        "Spicy Leek Curry": {
            "multiplier": 1.25, "power": [5900, 6018, 6136, 6254, 6372, 6431, 6549, 6667, 6844, 6962, 7021, 7139, 7257, 7316, 7434, 7552, 7670, 7729, 7847, 7965, 8083, 8260, 8378, 8555, 8673, 8850, 8968, 9145, 9322, 9499, 9676, 9853, 10030, 10266, 10443, 10679, 10856, 11092, 11328, 11564, 11800, 12036, 12272, 12567, 12803, 13098, 13393, 13688, 13983, 14278], "amount": 32,
            "ingredients": {
                "Ginger": 10,
                "Herb": 8,
                "Leek": 14
            }
        },
        "Grilled Tail Curry": {
            "multiplier": 1.25, "power": [7483, 7633, 7782, 7932, 8082, 8156, 8306, 8456, 8680, 8830, 8905, 9054, 9204, 9279, 9429, 9578, 9728, 9803, 9952, 10102, 10252, 10476, 10626, 10850, 11000, 11225, 11374, 11599, 11823, 12048, 12272, 12497, 12721, 13020, 13245, 13544, 13769, 14068, 14367, 14667, 14966, 15265, 15565, 15939, 16238, 16612, 16986, 17361, 17735, 18109], "amount": 33,
            "ingredients": {
                "Herb": 25,
                "Tail": 8
            }
        },
        "Ninja Curry": {
            "multiplier": 1.25, "power": [6159, 6282, 6405, 6529, 6652, 6713, 6836, 6960, 7144, 7268, 7329, 7452, 7576, 7637, 7760, 7884, 8007, 8068, 8191, 8315, 8438, 8623, 8746, 8931, 9054, 9239, 9362, 9546, 9731, 9916, 10101, 10286, 10470, 10717, 10901, 11148, 11333, 11579, 11825, 12072, 12318, 12564, 12811, 13119, 13365, 13673, 13981, 14289, 14597, 14905], "amount": 38,
            "ingredients": {
                "Soybeans": 15,
                "Sausage": 9,
                "Mushroom": 5,
                "Leek": 9
            }
        },
        "Egg Bomb Curry": {
            "multiplier": 1.25, "power": [4523, 4613, 4704, 4794, 4885, 4930, 5021, 5111, 5247, 5337, 5382, 5473, 5563, 5609, 5699, 5789, 5880, 5925, 6016, 6106, 6197, 6332, 6423, 6558, 6649, 6785, 6875, 7011, 7146, 7282, 7418, 7553, 7689, 7870, 8006, 8187, 8322, 8503, 8684, 8865, 9046, 9227, 9408, 9634, 9815, 10041, 10267, 10493, 10720, 10946], "amount": 35,
            "ingredients": {
                "Apple": 11,
                "Honey": 12,
                "Egg": 8,
                "Potato": 4
            }
        },
        "Dream Eater Butter Curry": {
            "multiplier": 1.35, "power": [9010, 9190, 9370, 9551, 9731, 9821, 10001, 10181, 10452, 10632, 10722, 10902, 11082, 11172, 11353, 11533, 11713, 11803, 11983, 12164, 12344, 12614, 12794, 13065, 13245, 13515, 13695, 13966, 14236, 14506, 14776, 15047, 15317, 15677, 15948, 16308, 16578, 16939, 17299, 17660, 18020, 18380, 18741, 19191, 19552, 20002, 20453, 20903, 21354, 21804], "amount": 55,
            "ingredients": {
                "Milk": 10,
                "Tomato": 15,
                "Potato": 18,
                "Cacao": 12
            }
        }
    },
    "salads": {
        "Bean Ham Salad": {
            "multiplier": 1.06, "power": [873, 890, 908, 925, 943, 952, 969, 986, 1013, 1030, 1039, 1056, 1074, 1083, 1100, 1117, 1135, 1144, 1161, 1179, 1196, 1222, 1240, 1266, 1283, 1310, 1327, 1353, 1379, 1406, 1432, 1458, 1484, 1519, 1545, 1580, 1606, 1641, 1676, 1711, 1746, 1781, 1816, 1859, 1894, 1938, 1982, 2025, 2069, 2113], "amount": 8,
            "ingredients": {
                "Sausage": 8
            }
        },
        "Snoozy Tomato Salad": {
            "multiplier": 1.06, "power": [933, 952, 970, 989, 1008, 1017, 1036, 1054, 1082, 1101, 1110, 1129, 1148, 1157, 1176, 1194, 1213, 1222, 1241, 1260, 1278, 1306, 1325, 1353, 1372, 1400, 1418, 1446, 1474, 1502, 1530, 1558, 1586, 1623, 1651, 1689, 1717, 1754, 1791, 1829, 1866, 1903, 1941, 1987, 2025, 2071, 2118, 2165, 2211, 2258], "amount": 8,
            "ingredients": {
                "Tomato": 8
            }
        },
        "Fancy Apple Salad": {
            "multiplier": 1.06, "power": [763, 778, 794, 809, 824, 832, 847, 862, 885, 900, 908, 923, 938, 946, 961, 977, 992, 1000, 1015, 1030, 1045, 1068, 1083, 1106, 1122, 1145, 1160, 1183, 1206, 1228, 1251, 1274, 1297, 1328, 1351, 1381, 1404, 1434, 1465, 1495, 1526, 1557, 1587, 1625, 1656, 1694, 1732, 1770, 1808, 1846], "amount": 8,
            "ingredients": {
                "Apple": 8
            }
        },
        "Immunity Leek Salad": {
            "multiplier": 1.11, "power": [2658, 2711, 2764, 2817, 2871, 2897, 2950, 3004, 3083, 3136, 3163, 3216, 3269, 3296, 3349, 3402, 3455, 3482, 3535, 3588, 3641, 3721, 3774, 3854, 3907, 3987, 4040, 4120, 4200, 4279, 4359, 4439, 4519, 4625, 4705, 4811, 4891, 4997, 5103, 5210, 5316, 5422, 5529, 5662, 5768, 5901, 6034, 6167, 6299, 6432], "amount": 15,
            "ingredients": {
                "Ginger": 5,
                "Leek": 10
            }
        },
        "Snow Cloak Caesar Salad": {
            "multiplier": 1.11, "power": [1774, 1809, 1845, 1880, 1916, 1934, 1969, 2005, 2058, 2093, 2111, 2147, 2182, 2200, 2235, 2271, 2306, 2324, 2359, 2395, 2430, 2484, 2519, 2572, 2608, 2661, 2696, 2750, 2803, 2856, 2909, 2963, 3016, 3087, 3140, 3211, 3264, 3335, 3406, 3477, 3548, 3619, 3690, 3779, 3850, 3938, 4027, 4116, 4204, 4293], "amount": 16,
            "ingredients": {
                "Milk": 10,
                "Sausage": 6
            }
        },
        "Water Veil Tofu Salad": {
            "multiplier": 1.11, "power": [1843, 1880, 1917, 1954, 1990, 2009, 2046, 2083, 2138, 2175, 2193, 2230, 2267, 2285, 2322, 2359, 2396, 2414, 2451, 2488, 2525, 2580, 2617, 2672, 2709, 2765, 2801, 2857, 2912, 2967, 3023, 3078, 3133, 3207, 3262, 3336, 3391, 3465, 3539, 3612, 3686, 3760, 3833, 3926, 3999, 4091, 4184, 4276, 4368, 4460], "amount": 16,
            "ingredients": {
                "Soybeans": 10,
                "Tomato": 6
            }
        },
        "Heat Wave Tofu Salad": {
            "multiplier": 1.11, "power": [1976, 2016, 2055, 2095, 2134, 2154, 2193, 2233, 2292, 2332, 2351, 2391, 2430, 2450, 2490, 2529, 2569, 2589, 2628, 2668, 2707, 2766, 2806, 2865, 2905, 2964, 3004, 3063, 3122, 3181, 3241, 3300, 3359, 3438, 3498, 3577, 3636, 3715, 3794, 3873, 3952, 4031, 4110, 4209, 4288, 4387, 4486, 4584, 4683, 4782], "amount": 16,
            "ingredients": {
                "Soybeans": 10,
                "Herb": 6
            }
        },
        "Superpower Extreme Salad": {
            "multiplier": 1.17, "power": [2958, 3017, 3076, 3135, 3195, 3224, 3283, 3343, 3431, 3490, 3520, 3579, 3638, 3668, 3727, 3786, 3845, 3875, 3934, 3993, 4052, 4141, 4200, 4289, 4348, 4437, 4496, 4585, 4674, 4762, 4851, 4940, 5029, 5147, 5236, 5354, 5443, 5561, 5679, 5798, 5916, 6034, 6153, 6301, 6419, 6567, 6715, 6863, 7010, 7158], "amount": 23,
            "ingredients": {
                "Sausage": 9,
                "Ginger": 9,
                "Egg": 5,
                "Potato": 3
            }
        },
        "Moomoo Caprese Salad": {
            "multiplier": 1.17, "power": [2856, 2913, 2970, 3027, 3084, 3113, 3170, 3227, 3313, 3370, 3399, 3456, 3513, 3541, 3599, 3656, 3713, 3741, 3798, 3856, 3913, 3998, 4056, 4141, 4198, 4284, 4341, 4427, 4512, 4598, 4684, 4770, 4855, 4969, 5055, 5169, 5255, 5369, 5484, 5598, 5712, 5826, 5940, 6083, 6198, 6340, 6483, 6626, 6769, 6912], "amount": 23,
            "ingredients": {
                "Milk": 12,
                "Tomato": 6,
                "Oil": 5
            }
        },
        "Contrary Chocolate Meat Salad": {
            "multiplier": 1.17, "power": [3558, 3629, 3700, 3771, 3843, 3878, 3949, 4021, 4127, 4198, 4234, 4305, 4376, 4412, 4483, 4554, 4625, 4661, 4732, 4803, 4874, 4981, 5052, 5159, 5230, 5337, 5408, 5515, 5622, 5728, 5835, 5942, 6049, 6191, 6298, 6440, 6547, 6689, 6831, 6974, 7116, 7258, 7401, 7579, 7721, 7899, 8077, 8255, 8432, 8610], "amount": 23,
            "ingredients": {
                "Sausage": 9,
                "Cacao": 14
            }
        },
        "Dazzling Apple Cheese Salad": {
            "multiplier": 1.17, "power": [2578, 2630, 2681, 2733, 2784, 2810, 2862, 2913, 2990, 3042, 3068, 3119, 3171, 3197, 3248, 3300, 3351, 3377, 3429, 3480, 3532, 3609, 3661, 3738, 3790, 3867, 3919, 3996, 4073, 4151, 4228, 4305, 4383, 4486, 4563, 4666, 4744, 4847, 4950, 5053, 5156, 5259, 5362, 5491, 5594, 5723, 5852, 5981, 6110, 6239], "amount": 23,
            "ingredients": {
                "Apple": 15,
                "Milk": 5,
                "Oil": 3
            }
        },
        "Spore Mushroom Salad": {
            "multiplier": 1.25, "power": [5859, 5976, 6093, 6211, 6328, 6386, 6503, 6621, 6796, 6914, 6972, 7089, 7207, 7265, 7382, 7500, 7617, 7675, 7792, 7910, 8027, 8203, 8320, 8496, 8613, 8789, 8906, 9081, 9257, 9433, 9609, 9785, 9960, 10195, 10370, 10605, 10781, 11015, 11249, 11484, 11718, 11952, 12187, 12480, 12714, 13007, 13300, 13593, 13886, 14179], "amount": 33,
            "ingredients": {
                "Tomato":8,
                "Oil":8,
                "Mushroom": 17
            }
        },
        "Slowpoke Tail Pepper Salad": {
            "multiplier": 1.25, "power": [8169, 8332, 8496, 8659, 8823, 8904, 9068, 9231, 9476, 9639, 9721, 9884, 10048, 10130, 10293, 10456, 10620, 10701, 10865, 11028, 11192, 11437, 11600, 11845, 12008, 12254, 12417, 12662, 12907, 13152, 13397, 13642, 13887, 14214, 14459, 14786, 15031, 15358, 15684, 16011, 16338, 16665, 16992, 17400, 17727, 18135, 18544, 18952, 19361, 19769], "amount": 35,
            "ingredients": {
                "Oil": 15,
                "Herb": 10,
                "Tail": 10
            }
        },
        "Overheat Ginger Salad": {
            "multiplier": 1.25, "power": [5225, 5330, 5434, 5539, 5643, 5695, 5800, 5904, 6061, 6166, 6218, 6322, 6427, 6479, 6584, 6688, 6793, 6845, 6949, 7054, 7158, 7315, 7420, 7576, 7681, 7838, 7942, 8099, 8256, 8412, 8569, 8726, 8883, 9092, 9248, 9457, 9614, 9823, 10032, 10241, 10450, 10659, 10868, 11129, 11338, 11600, 11861, 12122, 12383, 12645], "amount": 35,
            "ingredients": {
                "Ginger": 10,
                "Tomato": 8,
                "Herb": 17
            }
        },
        "Gluttony Potato Salad": {
            "multiplier": 1.25, "power": [5040, 5141, 5242, 5342, 5443, 5494, 5594, 5695, 5846, 5947, 5998, 6098, 6199, 6250, 6350, 6451, 6552, 6602, 6703, 6804, 6905, 7056, 7157, 7308, 7409, 7560, 7661, 7812, 7963, 8114, 8266, 8417, 8568, 8770, 8921, 9122, 9274, 9475, 9677, 9878, 10080, 10282, 10483, 10735, 10937, 11189, 11441, 11693, 11945, 12197], "amount": 36,
            "ingredients": {
                "Apple": 6,
                "Sausage": 7,
                "Egg": 9,
                "Potato": 14
            }
        },
        "Ninja Salad": {
            "multiplier": 1.35, "power": [10095, 10297, 10499, 10701, 10903, 11004, 11205, 11407, 11710, 11912, 12013, 12215, 12417, 12518, 12720, 12922, 13124, 13224, 13426, 13628, 13830, 14133, 14335, 14638, 14840, 15143, 15344, 15647, 15950, 16253, 16556, 16859, 17162, 17565, 17868, 18272, 18575, 18979, 19382, 19786, 20190, 20594, 20998, 21502, 21906, 22411, 22916, 23420, 23925, 24430], "amount": 53,
            "ingredients": {
                "Soybeans": 15,
                "Ginger": 11,
                "Mushroom": 12,
                "Leek": 15
            }
        }
    },
    "desserts": {
        "Fancy Apple Juice": {
            "multiplier": 1.06, "power": [763, 778, 794, 809, 824, 832, 847, 862, 885, 900, 908, 923, 938, 946, 961, 977, 992, 1000, 1015, 1030, 1045, 1068, 1083, 1106, 1122, 1145, 1160, 1183, 1206, 1228, 1251, 1274, 1297, 1328, 1351, 1381, 1404, 1434, 1465, 1495, 1526, 1557, 1587, 1625, 1656, 1694, 1732, 1770, 1808, 1846], "amount": 8,
            "ingredients": {
                "Apple": 8
            }
        },
        "Craft Soda Pop": {
            "multiplier": 1.06, "power": [964, 983, 1003, 1022, 1041, 1051, 1070, 1089, 1118, 1138, 1147, 1166, 1186, 1195, 1215, 1234, 1253, 1263, 1282, 1301, 1321, 1350, 1369, 1398, 1417, 1446, 1465, 1494, 1523, 1552, 1581, 1610, 1639, 1677, 1706, 1745, 1774, 1812, 1851, 1889, 1928, 1967, 2005, 2053, 2092, 2140, 2188, 2236, 2285, 2333], "amount": 9,
            "ingredients": {
                "Honey": 9
            }
        },
        "Warm Moomoo Milk": {
            "multiplier": 1.06, "power": [727, 742, 756, 771, 785, 792, 807, 822, 843, 858, 865, 880, 894, 901, 916, 931, 945, 952, 967, 981, 996, 1018, 1032, 1054, 1069, 1091, 1105, 1127, 1149, 1170, 1192, 1214, 1236, 1265, 1287, 1316, 1338, 1367, 1396, 1425, 1454, 1483, 1512, 1549, 1578, 1614, 1650, 1687, 1723, 1759], "amount": 7,
            "ingredients": {
                "Milk": 7
            }
        },
        "Fluffy Sweet Potatoes": {
            "multiplier": 1.11, "power": [1783, 1819, 1854, 1890, 1926, 1943, 1979, 2015, 2068, 2104, 2122, 2157, 2193, 2211, 2247, 2282, 2318, 2336, 2371, 2407, 2443, 2496, 2532, 2585, 2621, 2675, 2710, 2764, 2817, 2871, 2924, 2978, 3031, 3102, 3156, 3227, 3281, 3352, 3423, 3495, 3566, 3637, 3709, 3798, 3869, 3958, 4047, 4137, 4226, 4315], "amount": 14,
            "ingredients": {
                "Milk": 5,
                "Potato": 9
            }
        },
        "Cloud Nine Soy Cake": {
            "multiplier": 1.11, "power": [1798, 1834, 1870, 1906, 1942, 1960, 1996, 2032, 2086, 2122, 2140, 2176, 2212, 2230, 2265, 2301, 2337, 2355, 2391, 2427, 2463, 2517, 2553, 2607, 2643, 2697, 2733, 2787, 2841, 2895, 2949, 3003, 3057, 3129, 3182, 3254, 3308, 3380, 3452, 3524, 3596, 3668, 3740, 3830, 3902, 3992, 4081, 4171, 4261, 4351], "amount": 15,
            "ingredients": {
                "Soybeans": 7,
                "Egg": 8
            }
        },
        "Ember Ginger Tea": {
            "multiplier": 1.11, "power": [1788, 1824, 1860, 1895, 1931, 1949, 1985, 2020, 2074, 2110, 2128, 2163, 2199, 2217, 2253, 2289, 2324, 2342, 2378, 2414, 2450, 2503, 2539, 2593, 2628, 2682, 2718, 2771, 2825, 2879, 2932, 2986, 3040, 3111, 3165, 3236, 3290, 3361, 3433, 3504, 3576, 3648, 3719, 3808, 3880, 3969, 4059, 4148, 4238, 4327], "amount": 16,
            "ingredients": {
                "Apple": 7,
                "Ginger": 9
            }
        },
        "Lucky Chant Apple Pie": {
            "multiplier": 1.11, "power": [1634, 1667, 1699, 1732, 1765, 1781, 1814, 1846, 1895, 1928, 1944, 1977, 2010, 2026, 2059, 2092, 2124, 2141, 2173, 2206, 2239, 2288, 2320, 2369, 2402, 2451, 2484, 2533, 2582, 2631, 2680, 2729, 2778, 2843, 2892, 2958, 3007, 3072, 3137, 3203, 3268, 3333, 3399, 3480, 3546, 3627, 3709, 3791, 3873, 3954], "amount": 16,
            "ingredients": {
                "Apple": 12,
                "Milk": 4
            }
        },
        "Stalwart Vegetable Juice": {
            "multiplier": 1.11, "power": [1798, 1834, 1870, 1906, 1942, 1960, 1996, 2032, 2086, 2122, 2140, 2176, 2212, 2230, 2265, 2301, 2337, 2355, 2391, 2427, 2463, 2517, 2553, 2607, 2643, 2697, 2733, 2787, 2841, 2895, 2949, 3003, 3057, 3129, 3182, 3254, 3308, 3380, 3452, 3524, 3596, 3668, 3740, 3830, 3902, 3992, 4081, 4171, 4261, 4351], "amount": 16,
            "ingredients": {
                "Apple": 7,
                "Tomato": 9
            }
        },
        "Huge Power Soy Donuts": {
            "multiplier": 1.17, "power": [3213, 3277, 3342, 3406, 3470, 3502, 3566, 3631, 3727, 3791, 3823, 3888, 3952, 3984, 4048, 4113, 4177, 4209, 4273, 4338, 4402, 4498, 4562, 4659, 4723, 4820, 4884, 4980, 5077, 5173, 5269, 5366, 5462, 5591, 5687, 5816, 5912, 6040, 6169, 6297, 6426, 6555, 6683, 6844, 6972, 7133, 7294, 7454, 7615, 7775], "amount": 22,
            "ingredients": {
                "Soybeans": 6,
                "Oil": 9,
                "Cacao": 7
            }
        },
        "Hustle Protein Smoothie": {
            "multiplier": 1.17, "power": [3168, 3231, 3295, 3358, 3421, 3453, 3516, 3580, 3675, 3738, 3770, 3833, 3897, 3928, 3992, 4055, 4118, 4150, 4213, 4277, 4340, 4435, 4499, 4594, 4657, 4752, 4815, 4910, 5005, 5100, 5196, 5291, 5386, 5512, 5607, 5734, 5829, 5956, 6083, 6209, 6336, 6463, 6589, 6748, 6875, 7033, 7191, 7350, 7508, 7667], "amount": 23,
            "ingredients": {
                "Soybeans": 15,
                "Cacao": 8
            }
        },
        "Big Malasada": {
            "multiplier": 1.17, "power": [2927, 2986, 3044, 3103, 3161, 3190, 3249, 3308, 3395, 3454, 3483, 3542, 3600, 3629, 3688, 3747, 3805, 3834, 3893, 3951, 4010, 4098, 4156, 4244, 4303, 4391, 4449, 4537, 4625, 4712, 4800, 4888, 4976, 5093, 5181, 5298, 5386, 5503, 5620, 5737, 5854, 5971, 6088, 6235, 6352, 6498, 6644, 6791, 6937, 7083], "amount": 23,
            "ingredients": {
                "Milk": 7,
                "Honey": 6,
                "Oil": 10
            }
        },
        "Sweet Scent Chocolate Cake": {
            "multiplier": 1.17, "power": [3280, 3346, 3411, 3477, 3542, 3575, 3641, 3706, 3805, 3870, 3903, 3969, 4034, 4067, 4133, 4198, 4264, 4297, 4362, 4428, 4494, 4592, 4658, 4756, 4822, 4920, 4986, 5084, 5182, 5281, 5379, 5478, 5576, 5707, 5806, 5937, 6035, 6166, 6298, 6429, 6560, 6691, 6822, 6986, 7118, 7282, 7446, 7610, 7774, 7938], "amount": 24,
            "ingredients": {
                "Milk": 7,
                "Honey": 9,
                "Cacao": 8
            }
        },
        "Steadfast Ginger Cookies": {
            "multiplier": 1.25, "power": [4921, 5019, 5118, 5216, 5315, 5364, 5462, 5561, 5708, 5807, 5856, 5954, 6053, 6102, 6200, 6299, 6397, 6447, 6545, 6643, 6742, 6889, 6988, 7135, 7234, 7382, 7480, 7628, 7775, 7923, 8070, 8218, 8366, 8563, 8710, 8907, 9055, 9251, 9448, 9645, 9842, 10039, 10236, 10482, 10679, 10925, 11171, 11417, 11663, 11909], "amount": 35,
            "ingredients": {
                "Honey": 14,
                "Ginger": 12,
                "Egg": 4,
                "Cacao": 5
            }
        },
        "Lovely Kiss Smoothie": {
            "multiplier": 1.25, "power": [4734, 4829, 4923, 5018, 5113, 5160, 5255, 5349, 5491, 5586, 5633, 5728, 5823, 5870, 5965, 6060, 6154, 6202, 6296, 6391, 6486, 6628, 6722, 6864, 6959, 7101, 7196, 7338, 7480, 7622, 7764, 7906, 8048, 8237, 8379, 8569, 8711, 8900, 9089, 9279, 9468, 9657, 9847, 10083, 10273, 10509, 10746, 10983, 11220, 11456], "amount": 35,
            "ingredients": {
                "Apple": 11,
                "Milk": 9,
                "Honey": 7,
                "Cacao": 8
            }
        },
        "Neroli's Restorative Tea": {
            "multiplier": 1.25, "power": [5065, 5166, 5268, 5369, 5470, 5521, 5622, 5723, 5875, 5977, 6027, 6129, 6230, 6281, 6382, 6483, 6585, 6635, 6736, 6838, 6939, 7091, 7192, 7344, 7446, 7598, 7699, 7851, 8003, 8155, 8307, 8459, 8611, 8813, 8965, 9168, 9320, 9522, 9725, 9927, 10130, 10333, 10535, 10788, 10991, 11244, 11498, 11751, 12004, 12257], "amount": 35,
            "ingredients": {
                "Apple": 15,
                "Ginger": 11,
                "Mushroom": 9
            }
        },
        "Jigglypuff's Fruity Flan": {
            "multiplier": 1.35, "power": [7594, 7746, 7898, 8050, 8202, 8277, 8429, 8581, 8809, 8961, 9037, 9189, 9341, 9417, 9568, 9720, 9872, 9948, 10100, 10252, 10404, 10632, 10783, 11011, 11163, 11391, 11543, 11771, 11999, 12226, 12454, 12682, 12910, 13214, 13441, 13745, 13973, 14277, 14580, 14884, 15188, 15492, 15796, 16175, 16479, 16859, 17238, 17618, 17998, 18377], "amount": 55,
            "ingredients": {
                "Apple": 10,
                "Milk": 10,
                "Honey": 20,
                "Egg": 15
            }
        }
    }
}
