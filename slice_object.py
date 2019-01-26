# coding:utf8
# 实现一个具有切片功能的对象
import numbers
class Group:
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.group_staffs = staffs

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.group_staffs[item])
        elif isinstance(item,(int)):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=[self.group_staffs[item]])
        else:
            raise IndexError


    # 可变列表
    def __setitem__(self, key, value):
        self.group_staffs[key] = value

    def __delitem__(self, key):
        del self.group_staffs[key]


    def  __reversed__(self):
        self.group_staffs.reverse()

    def __iter__(self):
        return iter(self.group_staffs)

    def __len__(self):
        return len(self.group_staffs)

    def __contains__(self, item):
        if item in self.group_staffs:
            return True
        else:
            return False

if __name__ == '__main__':
    staffs = ["lee1","lee2","lee3"]
    group = Group(group_name="个人云",company_name="金山",staffs=staffs)
    print(group.group_staffs[0])
    sub_group = group[0]
    print(sub_group)
    for g in group:
        print(g)
    # for g in group:
    #     print(g)



