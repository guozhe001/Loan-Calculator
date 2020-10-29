nickname = input()
profession = input()

# 方法1：
# print(str.format("http://example.com/{}/desirable/{}/profile", nickname, profession))

# 方法2：
# print("http://example.com/%s/desirable/%s/profile" % (nickname, profession))

# 方法3：
# print(str.format("http://example.com/{0}/desirable/{1}/profile", nickname, profession))

# 方法4：
# print("http://example.com/{0}/desirable/{1}/profile".format(nickname, profession))

# 方法5：
# print("http://example.com/{nickname}/desirable/{profession}/profile".format(nickname=nickname, profession=profession))

# 方法6：
# print("http://example.com/{0}/desirable/{profession}/profile".format(nickname, profession=profession))

# 方法7：
print(f"http://example.com/{nickname}/desirable/{profession}/profile")
