# coding:utf8
class Date:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def tomorrow(self):
        self.z += 1
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.x,month=self.y,day=self.z)


    @staticmethod
    def str_format_date(str,delimiter):
        a, b, c = d.split(delimiter)
        return Date(int(a), int(b), int(c))  #Date为硬编码，不够灵活，用classmethod处理

    @classmethod
    def str_format(cls,str,delimiter):
        a, b, c = d.split(delimiter)
        return cls(int(a), int(b), int(c))

    # 当不需要调用本类时，statismethod就有了用武之地
    @staticmethod
    def valid_str(str,delimiter):
        year,month,day = tuple(str.split(delimiter))
        if int(year)>0 and (int(month)>0 and int(month)<13) and (int(day)>0 and int(day)<32):
            return True
        else:
            return False

if __name__ == '__main__':
    d = "2019-12-12"
    a,b,c = d.split("-")
    date = Date(int(a),int(b),int(c))
    print(date)

    #staticmethod调用
    print(Date.str_format_date(d,"-"))
    print(Date.valid_str(d,"-"))

    # classmethod调用
    print(Date.str_format(d,"-"))

