# encoding:utf-8

import numpy as np
import os
import redis


def readfile(contentdir):
    result_user_temp = {}
    result_user_local = []
    # 读取用户文件
    listfile = os.listdir(contentdir)
    # 存放全部的用户
    line_list = []
    for filenames in listfile:
        for line in open(contentdir + "\\" + filenames):
            line_list.append(line)

    # 输出1000个用户的值
    for i in xrange(0, 1000):
        uid, fondTags, result_local = process_result_tag(line_list[i])
        result_user_temp[uid] = fondTags
        result_user_local.append(result_local)
    # print result_user_temp
    # print result_user_local
    local_path = "user_profile.txt"
    with open(local_path, "a") as f:
        # 方法一：
        f.write("\n".join(result_user_local))
        # 方法二：
        # for i in result_user_local:
        #     f.write(i + '\n')
        # np.save('tag_list_local.npy', result_user_local)
    return result_user_temp


# 最后得到一个用户的tag标签列表  1 * 85
def tagprocess(tags, user_tags):
    temp_list = [0] * len(tags)
    for i in xrange(0, len(tags)):
        # 判断用户哪些标签在list列表中
        for j in xrange(0, len(user_tags)):
            if (int(user_tags[j]) == tags[i]):
                temp_list[i] = int(user_tags[j])
            else:
                temp_list[i] == 0
    return temp_list


# 计算模型
def user_model_computation(user_tags, model):
    userprofile = np.array(user_tags)
    user_weights = userprofile.dot(model)
    # print "user_weights: ", user_weights
    category_list = [81, 20, 36, 42, 29, 18, 4, 22, 34, 101, 19, 5, 3, 21, 28, 44, 49, 57, 74, 75, 77, 82, 85, 103, 105]
    category_weights = []
    for i in xrange(len(category_list)):
        category_weights.append((category_list[i], user_weights[i]))
    ###排序###
    category_weights_sorted = sorted(category_weights, key=lambda x: x[1], reverse=True)
    return category_weights_sorted


# 处理单个标签
def process_result_tag(line):
    utag = line.replace("\'", "").replace("u", "").split(":")[-1][1:-2].split(",")
    # 用户uid
    uid = line.split(":")[1]
    # 用户喜欢的标签
    tags = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34,
            35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 0, 61, 60, 59, 57, 64, 63,
            65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 105, 142, 145, 148, 149,
            150, 155, 160, 162]

    fond_tags = tagprocess(tags, utag)
    # model * fond_tags
    result_model = user_model_computation(fond_tags, model)
    # print "uid:%s:fondTags:%s" % (uid, result_model)

    # 拼接结果
    key = "uid:%s:fondTags" % uid
    value = result_model

    # 保存本地的
    result_local = "uid:%s:fondTags:%s" % (uid, result_model)
    # print result_local
    # print type(result_local)
    # 建立临时文件
    return key, value, result_local


# 数据存入redis
def sava2Redis(redclient, result_user_profile, delaytime=60 * 60 * 24 * 30):
    # 遍历结果map，插入数据
    for key in result_user_profile:
        # print key + ":%s" % result_user_profile[key]
        redclient.setex(key, result_user_profile[key], delaytime)
        # redclient.setex(hkeystr + ":%s:%s" % (uid, snsid), json.dumps(datas), delaytime)  # datas外部参数，传入该函数保存到redis


if __name__ == '__main__':
    # 读取model
    model_path = "model_v6.npy"
    model = np.load(model_path)
    # 读取文件
    contentdir = 'E:\\MojieWork\\data'
    result_user_profile = readfile(contentdir)
    # print result_user_profile
    # 存入redis中
    redclient = redis.Redis(host='192.168.1.11', port=6381, db=3, password='mojichina')  # local test redis
    # sava2Redis(redclient, result_user_profile)
    # 查看数据
    # for key in result_user_profile:
    #     print redclient.get(key)
