#函数名：dealFunc(com_map : ComVo,*args) ->[]:VoHash

#结构列表：
# import hashlib
# import re
# from lxml import etree as et
# # import xml.etree.ElementTree as et
# from enum import Enum
# from pathlib import Path
# from typing import List

# class RefType(Enum):
#     IMAGE = 0
#     URL = 1
#     FNT = 2


# class VoRef:
#     # 类型
#     type = 0
#     tree: et.ElementTree = None
#     node: et.Element = None
#     file: Path = None
#     uid = ''
#     pkg = ''


# class ComVo:
#     uid = ''
#     pkg_id = ''
#     com_id = ''
#     name = ''
#     pkg = ''
#     file_pkg: Path = None
#     md5 = ''
#     node: et.Element = None
#     tree: et.ElementTree = None
#     root: et.Element = None
#     fileName = ''
#     # 相对于assets文件夹的地址
#     rela_add = ''
#     # 排除
#     exclude = False
#     # 导出
#     exported = False
#     url = ''
#     refs: List[VoRef] = None

#     def __init__(self):
#         self.refs = []


# class VoHash:
#     key = ''
#     com_list: List[ComVo] = None
#     # 保留的uid
#     reserved_uid = ''

#     def __init__(self):
#         self.com_list = []

#     def get_name(self):
#         if len(self.com_list) > 0:
#             return self.com_list[0].name
#         else:
#             return '无'

class dealFuncType(Enum):
    HASHREP = 1, #哈希值重复

funcNameMap = {
    dealFuncType.HASHREP = "同资源文件"
}

def dealFunc(com_map,*args):
    funcType = args[0]
    if(funcType == dealFuncType.HASHREP):
        print("查询hash值重复的资源")
        return isHashRepeatition(com_map)
        
def isHashRepeatition(com_map) -> []:
    md5_map = {}
    comRep_list = []
    for k in com_map:
        com_vo = com_map[k]
        if com_vo.md5 not in md5_map :
            md5_map[com_vo.md5] = hash_vo = VoHash()
            hash_vo.key = com_vo.md5
        else:
            hash_vo = md5_map[com_vo.md5]
        hash_vo.com_list.append(com_vo)    
    
    for k in md5_map:
        if len(md5_map[k].com_list) > 1 :
            comRep_list.append(md5_map[k])

    return comRep_list


