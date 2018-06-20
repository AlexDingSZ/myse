def test_var_kwargs(farg, *args ,**dict_args):
    print("formal arg:"+ str(farg))
    for arg in args:
        print(arg)

    for i in dict_args:
        print(i)


def foo(arg,*args,**kwargs):
    print("arg:",arg)
    print("*args:", args)
    print("**kwargs:", kwargs)


if __name__ =="__main__":
    foo("ab")
    foo("ab","args1",2,"args3",4)
    foo("ab", "args1", 2, "args3", 4,a=1,b=2,c=3)
    foo("ab", a=1, b=2, c=3)




