##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

class ZH_S():
    '''
    Simplified Chinese Messages.
    '''

    '''
    returnValue_100: OK或成功
    returnValue_[101-199]: 固件基本情况
    returnValue_[401-449]: 固件服务器
    returnValue_[450-499]: 固件播放器

    returnValue_[1011-1099]: Python系统
    returnValue_[1201-1399]: 驱动装置
    returnValue_[1401-1499]: 服务
    returnValue_[1501-1599]: KBX参考类型
    returnValue_[1601-1699]: 共享管理
    returnValue_[1701-1799]: 数据库
    returnValue_[1801-1899]: 应用管理
    returnValue_[1901-1999]: 文件浏览模块
    
    returnValue_[2201-2299]: 虚拟远程控制
    returnValue_[2301-2399]: 通知管理
    
    returnValue_[5001-5999]:  物联王用户服务器
    '''

    returnMsg = {
           "100":"Ok",

           "101":"等待",
           "102":"繁忙",
           "103":"超时",
           "104":"错误",
           "105":"最大应用上限",
           "106":"应用已在运行",
           "107":"应用未启动",
           "108":"应用未安装",
           "109":"无效参数",
           "110":"无效密码",
           "111":"无效用户",
           "112":"数据库错误",
           "114":"沙盒错误",

           "401":"会话已过期",
           "402":"无效申诉",
           "403":"无效登录",
           "404":"达到最多用户量",
           "405":"无效的Cookie",
           "406":"多次登录失败\n请30分钟后再试",

           "450":"还未开始播放",
           
           "501":"报警器正在运行",
           "502":"报警器未运行",
           "503":"调光器或灯泡正在运行",
           "504":"X10安全地址没有复位",
           

           "0":"成功",
           "1001":"发生意外错误",
           "1002":"无效的参数",
           "1003":"网络错误",
           "1004":"设备不可用",
           
           "1010":"未找到模块",
           "1011":"未找到方法",
           
           "1030":"无法调用功能",
           "1031":"缺失功能",
           "1032":"未找到功能",
           "1033":"目标应用ID未注册",
           "1034":"事件已登记",
           "1035":"未找到事件",
           "1036":"事件不属于提供的应用ID",
           "1037":"持续连接寻找",
           "1038":"未知的源应用ID",
           "1040":"事先注册事件监听",
           "1041":"监听事件未找到",

           "1201":"未能配对设备",
           "1202":"设备已存在",
           "1203":"设备认证失败",
           "1204":"配对设备终止",
           "1205":"扫描设备已存在",
           "1206":"扫描设备失败",
           "1207":"扫描设备超时",
           "1208":"删除设备失败",
           "1209":"失败，请删除设备并重新配对.",
           
           "1221":"连接至另一个扬声器.",
           "1222":"正在连接到另一个扬声器.",
           "1223":"连接扬声器失败.",
           "1224":"未能断开扬声器.",
           "1225":"已转移到另一个扬声器",

           "1301":"协议存在",
           "1302":"协议不存在",
           "1303":"协议设备扫描开始",
           "1304":"协议设备扫描未开始",
           "1305":"协议设备正在配对",
           "1306":"协议设备配对未开始",
           "1307":"协议设备删除中",
           "1308":"未开始删除协议设备",
           
           "1351":"设备控制器已存在",
           "1352":"设备控制器不存在",
           "1353":"高级设备控制器已存在",
           "1354":"高级设备控制器不存在",
           
           "1370":"条件不满足d", # Generic automation condition response

          "1401":"服务注册失败",
           "1404":"无法找到对象",
           "1405":"程序失败",
           "1406":"无效的参数",
           "1407":"无法找到发送人",
           "1408":"同一时间内只有一个执行个体可以运行",
           "1409":"参数格式不当",
           "1410":"无法找到收件人对象",

           "1411":"无法找到位置",
           "1412":"无效的纬度",
           "1413":"无效的经度",
           "1414":"无效的温度单位",
           "1415":"没有找到匹配的位置",
           "1416":"单位不受支持",
           "1417":"坐标必须在类似地球边界里。 经度:-180 to 180, 纬度:-90 to 90",
           "1418":"无效的位置",
           "1419":"读取气象数据失败",

           "1420":"获取推特回调网址失败",
           "1421":"添加推特发送人失败",
           "1422":"发送推特讯息失败",
           "1423":"无效的回调网址",
           "1424":"未能获得跟随者列表",
           "1425":"未能获得跟随者Id列表",
           "1426":"服务器暂无法回应，请稍候再尝试",
           "1427":"您的推特户口已被暂停， 无法享用此功能",
           "1428":"未能获得接口调用限数列表",
           
           "1431":"服务无法使用，或已被其他用户禁用",
           "1432":"服务请求超时",
           "1433":"无效的回应",

           "1440":"获取新浪微博回调网址失败",
           "1441":"添加新浪微博发送人失败",
           "1442":"发送新浪微博讯息失败",
           "1443":"获取新浪微博用户状态失败",
           "1444":"更新状态失败",
           "1445":"添加评论失败",
           "1446":"获取最新讯息失败",
           "1447":"设定新浪微博私人令牌失败",

           "1501":"无效的数据类型",
           "1502":"无效的时间戳记",
           "1503":"无效的数值",
           "1504":"无效的数值范围",
           "1505":"无效的数值长度",
           "1506":"无效的物体对象大小",
           "1507":"无效的字符串格式",
           "1508":"字符串里有无效的字符",
           "1509":"索引指标超出范围",
           "1510":"禁止重复的索引指标",
           "1511":"数值是必须的",
           "1512":"程序失败",

           "1601":"函数已被删除",
           "1602":"函数已被禁用",
           "1603":"无效的参数",
           "1604":"无法连接系统",
           "1605":"未知错误",
           "1606":"没有权限",
           "1607":"附加参数格式不当",
           "1608":"无法找到函数",
           "1609":"无法找到函数组合",

           "1701":"储藏数据失败",
           "1702":"连接数据库失败",
           "1703":"版本升级失败",
           "1704":"创建列索引失败",
           "1705":"删除列索引失败",
           "1706":"创建数据库列表失败",
           "1707":"删除数据库列表失败",
           "1708":"查询失败",
           "1709":"更新数据失败",
           "1710":"获取数据失败",
           "1711":"删除数据失败",
           "1712":"列举数据库列表失败",
           "1713":"更新数据库设定失败",
           "1714":"程序失败。数据依存在或数值无效",
           "1715":"创建触发失败",
           "1716":"删除触发失败",
           "1717":"获取触发失败",
           "1718":"启动重复性触发失败",

           "1801":"无法找到该当的应用程序ID",
           "1802":"无法读取应用程序列表",

           "1901":"无效的路径",
           "1902":"无效的储存类型",
           "1903":"无法处理文件",
           "1904":"无法获取文件夹内容",
           "1905":"无法获取文件详情",
           "2001":"Insteon hub身份验证失败.",
           "2002":"Insteon hub登录超时.",
           "2003":"无法扫描Insteon设备.",
           
           "2100":"转换类型失败.",
           "2101":"部分/选项错误.",
           
           "2201":"重点记录程序正在运行，请稍后再试.",
           "2202":"无法添加关键项.",
           "2203":"无法启动记录.",
           
           "2301":"无效的注册码.",
           "2302":"关注已达上线，请稍后再试.",
           "2003":"无法获得 Insteon仪器列表",
           
           "2100":"未能进行类型转换",
           "2101":"部落/选项错误",
           
           "2201":"正在运行关键记录进程，请稍后再试.",
           "2202":"未能添加输入键.",
           "2203":"未能开始记录进程.",
           
           "2501":"密码错误",
           "2502":"取回密码的电子邮件已设置",
           "2503":"令牌错误",
           "2504":"此应用程序未授权",
           "2505":"超过API调用的限制",
           "2506":"取回密码的电子邮件未设置.",
           "2507":"提供的旧电子邮件地址不一样.",
           "2508":"密码已设置",
           "2509":"密码未设置",
           "2510":"应用程序ID错误",
           "2511":"此应用程序不允许访问此函数",
           "2512":"PIN错误",
           "2513":"尝试超过最大值, 请点击“忘記密碼？”",
           "2514":"更改令牌错误",
           "2515":"尝试超过最大值, 请稍候再尝试。",
           
           "2601":"此位置已经存在该区域",
           "2602":"此区域已经存在"
           }
