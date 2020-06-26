import uiautomator2 as u2
d = u2.connect()
print(d.device_info)
ele = d(resourceId="com.sina.weibo:id/contentTextView")
print(d.info['currentPackageName'])